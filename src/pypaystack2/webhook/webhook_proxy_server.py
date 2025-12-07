import asyncio
import json
import logging
from typing import Annotated, Any

from pypaystack2._metadata import __version__
from pypaystack2.utils import (
    WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE,
    try_import_module,
)
from pypaystack2.webhook.logging_config import LOGGING_CONFIG, SERVER_LOGGING_NAME
from pypaystack2.webhook.models import EndpointAddress

fastapi_module = try_import_module(
    "fastapi",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="fastapi"
    ),
)

uvicorn_module = try_import_module(
    "uvicorn",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="uvicorn"
    ),
)

httpx_module = try_import_module(
    "httpx",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="httpx"
    ),
)

MAX_CONCURRENT_WEBHOOK_SEND = 50
GLOBAL_VARS = {  # server global shared variables
    "proxy_clients": [],
    "proxy_server_log_payload": True,
}
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(SERVER_LOGGING_NAME)

app = fastapi_module.FastAPI(
    title="PyPaystack2 Webhook Proxy Server",
    version=__version__,
    description="""this server serves as an intermediary between the tunnel server and all proxy clients.
If forwards the webhook payload it receives from the tunnel server to all the proxy clients registered with it""",
)


def extract_signature(
    x_paystack_signature: Annotated[str | None, fastapi_module.Header()] = None,
) -> str:
    return x_paystack_signature


@app.post("/webhook")
async def webhook(
    signature: Annotated[str, fastapi_module.Depends(extract_signature)],
    request: fastapi_module.Request,
    background_tasks: fastapi_module.BackgroundTasks,
):
    body = await request.json()
    if GLOBAL_VARS["proxy_server_log_payload"]:
        logger.info("New webhook event received")
        logger.info(f"{json.dumps(body)}")
    background_tasks.add_task(broadcast_webhook, signature=signature, body=body)
    return None


async def broadcast_webhook(signature: str, body: Any):
    sem = asyncio.Semaphore(MAX_CONCURRENT_WEBHOOK_SEND)
    tasks = [
        send_webhook(endpoint, signature, body, sem)
        for endpoint in GLOBAL_VARS["proxy_clients"]
    ]
    results = await asyncio.gather(*tasks)
    log_broadcast_results(results)


async def send_webhook(
    endpoint: str, signature: str, body: Any, sem: asyncio.Semaphore
) -> tuple[str, int]:
    async with httpx_module.AsyncClient() as client, sem:
        try:
            response = await client.post(
                endpoint, json=body, headers={"X-Paystack-Signature": signature}
            )
            return endpoint, response.status_code
        except httpx_module.NetworkError:
            return endpoint, -1


def log_broadcast_results(results: list[tuple[str, int]]) -> None:
    for result in results:
        if result[1] == 200:
            logger.info(
                f"Webhook payload sent to proxy client {result[0]} was well received"
            )
        elif result[1] == -1:
            logger.error(
                f"Webhook payload sent to proxy client {result[0]} failed to deliver. client was unreachable due to network error. is client alive?"
            )
        else:
            logger.error(
                f"Webhook payload to sent to proxy client {result[0]} failed to deliver, failed with http status {result[1]}"
            )


def run_webhook_proxy_server(
    proxy_clients: list[str], addr: EndpointAddress, proxy_server_log_payload: bool
):
    GLOBAL_VARS["proxy_clients"] = proxy_clients
    GLOBAL_VARS["proxy_server_log_payload"] = proxy_server_log_payload

    host = addr.host or "localhost"
    port = addr.port or 4044

    async def run():
        config = uvicorn_module.Config(
            app, host=host, port=port, log_config=LOGGING_CONFIG
        )
        logger.info(
            f"Starting PyPaystack2 Webhook Proxy Server at http://{host}:{port} ..."
        )
        server = uvicorn_module.Server(config)
        await server.serve()

    asyncio.run(run())
