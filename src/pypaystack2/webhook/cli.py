import logging
import os
import threading
from enum import IntEnum
from multiprocessing import Process
from typing import Annotated, Literal

from pypaystack2._metadata import __version__ as pypaystack2_version
from pypaystack2.utils import (
    WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE,
    parse_address,
    try_import_module,
)
from pypaystack2.webhook.logging_config import WEBHOOK_CLI_LOGGING_NAME
from pypaystack2.webhook.webhook_proxy_server import run_webhook_proxy_server

typer_module = try_import_module(
    "typer",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="typer"
    ),
)

rich_module = try_import_module(
    "rich",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="rich"
    ),
)

ngrok_module = try_import_module(
    "ngrok",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="ngrok"
    ),
)

dotenv_module = try_import_module(
    "dotenv",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="dotenv"
    ),
)

logger = logging.getLogger(WEBHOOK_CLI_LOGGING_NAME)
webhook_cli_app = typer_module.Typer()


class CLIExitCode(IntEnum):
    SUCCESS = 0
    NGROK_TOKEN_NOT_SET = 401
    PROXY_CLIENTS_NOT_SET = 402


ADDR_FLAG_HELP = """The port or address (formatted as host:port) where the tunnel server should forward
webhook payloads when running in `--mode direct` (i.e., paystack -> tunnel server -> localhost).
In `--mode proxy`, this specifies the address where the proxy server will start.

Note: Do NOT include a scheme when using `--addr`. The value must be in the form host:port
(e.g., `localhost:8080`), not `https://localhost:8080`.

This can also be configured using the PAYSTACK_WEBHOOK_ADDRESS environment variable.
If both the flag and the environment variable are set, the environment variable takes precedence.
"""

NGROK_AUTH_TOKEN_FLAG_HELP = """Flag to enable entering your ngrok auth token through an interactive prompt.
An auth token provided this way takes precedence over the value set in the
PAYSTACK_WEBHOOK_NGROK_AUTH_TOKEN environment variable.
"""

MODE_FLAG_HELP = """The mode in which the tunnel server should operate. In `--mode direct`, the webhook
payload received by the tunnel server is forwarded directly to your local app via
the specified `--addr` (i.e., paystack -> tunnel server -> localhost).

In `--mode proxy`, the tunnel server forwards the webhook payload to the proxy
server running at `--addr`, which then forwards the payload to the clients defined
via `--proxy-clients` (i.e., paystack -> tunnel server -> proxy server -> proxy clients).

This can also be set using the PAYSTACK_WEBHOOK_MODE environment variable. If both
the flag and the environment variable are provided, the flag value takes precedence.
"""

PROXY_CLIENTS_FLAG_HELP = """The clients that a proxy server should forward webhook payloads to when operating in
`--mode proxy`. This is a comma-separated list of URLs, e.g.
`http://localhost:5173,http://127.0.0.1:8000/webhooks/paystack`.

Note: the scheme must be included (e.g., `http://localhost:5173`, not `localhost:5173`).

This can also be configured using the PAYSTACK_WEBHOOK_PROXY_CLIENTS environment variable.
If both the flag and the environment variable are set, the environment variable takes precedence.
"""

PROXY_SERVER_LOG_PAYLOAD_FLAG_HELP = """This flag enables the proxy server to log the webhook payload it receives from the
tunnel server before forwarding it to the proxy clients.

It can also be configured using the PAYSTACK_WEBHOOK_PROXY_SERVER_LOG_PAYLOAD
environment variable. If both the flag and the environment variable are set,
the flag value takes precedence.
"""

DOTENV_PATH_FLAG = """This flag is used to set a custom dotenv file path, by default, this cli will look for your
environmental variables in a `.env` file"""

PACKAGE_CAMPAIGN_MESSAGE = f"""
💪🏽 Paystack Integration powered by [blue bold]PyPaystack2 v{pypaystack2_version}[/] 🔥

Need more guide on how to use this package?
See documentation at https://gray-adeyi.github.io/pypaystack2/v3.1/

Found a bug?
Create an issue for it at https://github.com/gray-adeyi/pypaystack2/issues

If this project is useful to you or your company, please consider sponsoring the project by

- 🧑🏻‍🤝‍🧑 Sharing it with your developer friends
- ✨ Starring it on github at https://github.com/gray-adeyi/pypaystack2
- 💻 Contribute to it at https://github.com/gray-adeyi/pypaystack2
- ☕ Buy me a coffee at https://buymeacoffee.com/jigani
"""


@webhook_cli_app.command()
def start_tunnel_server(
    addr: Annotated[str, typer_module.Option(help=ADDR_FLAG_HELP)] = "4044",
    ngrok_auth_token: Annotated[
        bool, typer_module.Option(help=NGROK_AUTH_TOKEN_FLAG_HELP)
    ] = False,
    mode: Annotated[
        Literal["direct", "proxy"], typer_module.Option(help=MODE_FLAG_HELP)
    ] = "direct",
    proxy_clients: Annotated[
        list[str] | None, typer_module.Option(help=PROXY_CLIENTS_FLAG_HELP)
    ] = None,
    proxy_server_log_payload: Annotated[
        bool, typer_module.Option(help=PROXY_SERVER_LOG_PAYLOAD_FLAG_HELP)
    ] = True,
    dotenv_path: Annotated[
        str | None, typer_module.Option(help=DOTENV_PATH_FLAG)
    ] = None,
) -> None:
    """Start a tunnel server for receiving webhook events on localhost over the internet.

    This utility makes working with webhooks during local development easy by leveraging
    ngrok, which provides HTTP tunneling capabilities.

    Note: You must sign up for ngrok to obtain an auth token, which can be provided via
    the `--ngrok-auth-token` flag or the `PAYSTACK_WEBHOOK_NGROK_AUTH_TOKEN`
    environment variable.

    The main challenge when working with webhooks locally is that external servers cannot
    directly send webhook payloads to your local development endpoint. A tunnel server solves
    this by acting as an intermediary between your local app and the webhook event producer.
    You start the tunnel server and provide the port on your localhost where incoming webhook
    events should be forwarded. The tunnel server then provides a URL that you can register
    with the webhook event producer (i.e., Paystack).

    Example flows:
    paystack -> tunnel server -> localhost
    paystack -> tunnel server -> proxy server -> proxy clients

    The tunnel server supports two modes: `direct` and `proxy`.

    In `direct` mode, the tunnel server forwards webhook events directly to your local app
    (`localhost`). The port or `host:port` address is supplied via the `--addr` flag.
    If your local webhook handler is `http://127.0.0.1:8000/webhooks/paystack` and the tunnel
    URL is `https://338742e1646f.ngrok-free.app`, you should register:
    `https://338742e1646f.ngrok-free.app/webhooks/paystack` as your webhook callback URL.

    In `proxy` mode, an intermediate proxy server is started locally at the port specified via
    `--addr` (the environment variable value takes precedence over the flag if both are set).
    This proxy server then forwards webhook events to the URLs provided in the
    `--proxy-clients` flag as a comma-separated list.
    """
    dotenv_module.load_dotenv(dotenv_path=dotenv_path)
    tunnel_server_listener: ngrok_module.Listener | None = None
    proxy_server_process: Process | None = None
    tunnel_server_listener_options = {}
    err_console = rich_module.console.Console(stderr=True)

    addr = os.environ.get("PAYSTACK_WEBHOOK_ADDRESS") or addr
    mode = mode or os.environ.get("PAYSTACK_WEBHOOK_MODE")
    proxy_clients = os.environ.get("PAYSTACK_WEBHOOK_PROXY_CLIENTS") or proxy_clients
    proxy_server_log_payload = proxy_server_log_payload or os.environ.get(
        "PAYSTACK_WEBHOOK_PROXY_SERVER_LOG_PAYLOAD"
    )

    try:
        _ngrok_auth_token = ""
        if ngrok_auth_token:
            _ngrok_auth_token = typer_module.prompt(
                "Please enter or paste you NGROK auth token [input is hidden, press enter when done]",
                hide_input=True,
            )
        if not ngrok_auth_token and not os.environ.get(
            "PAYSTACK_WEBHOOK_NGROK_AUTH_TOKEN"
        ):
            err_console.print(
                "[red]ngrok auth token not provided in flags or environment variable[/red]"
            )
            raise typer_module.Exit(CLIExitCode.NGROK_TOKEN_NOT_SET)
        tunnel_server_listener_options["authtoken"] = (
            _ngrok_auth_token or os.environ.get("PAYSTACK_WEBHOOK_NGROK_AUTH_TOKEN")
        )

        if mode == "proxy":
            if not proxy_clients:
                err_console.print(
                    "[red]proxy clients not provided in --proxy-clients flag and --mode flag is proxy[/red]"
                )
                raise typer_module.Exit(CLIExitCode.PROXY_CLIENTS_NOT_SET)
            _addr = parse_address(addr)
            # TODO: Validate proxy clients
            proxy_server_process = Process(
                target=run_webhook_proxy_server,
                name="pypaystack2 proxy server",
                kwargs={
                    "addr": _addr,
                    "proxy_clients": proxy_clients,
                    "proxy_server_log_payload": proxy_server_log_payload,
                },
            )
            proxy_server_process.start()

        endpoint_address = parse_address(addr)
        endpoint = f"http://{endpoint_address.host if endpoint_address.host else '0.0.0.0'}:{endpoint_address.port if endpoint_address.port else 4044}"
        tunnel_server_listener = ngrok_module.forward(
            endpoint, **tunnel_server_listener_options
        )

        # Output ngrok url to console
        logger.info(
            f"Tunnel Server is listening to requests at {tunnel_server_listener.url()}"
        )

        if mode == "direct":
            logger.info(
                f"Register {tunnel_server_listener.url()}/<your-app-webhook-endpoint> as your webhook endpoint in your paystack dashboard"
            )

        if mode == "proxy":
            logger.info(
                f"Register {tunnel_server_listener.url()}/webhook as your webhook endpoint in your paystack dashboard"
            )

        # TODO: Figure out if it's okay to block like this
        # Keep the tunnel server alive
        stop_event = threading.Event()
        stop_event.wait()
        # while True:
        #     time.sleep(1)
    except KeyboardInterrupt:
        # Gracefully shutdown the tunnel server and proxy server
        if proxy_server_process:
            proxy_server_process.terminate()
            proxy_server_process.join()
            logger.info("PyPaystack2 Webhook Proxy Server shutdown successful")
        if tunnel_server_listener:
            # TODO: Figure out how to close ngrok in synchronous mode
            # tunnel_server_listener.close()
            logger.info("PyPaystack2 Webhook Tunnel Server shutdown successful")
        rich_module.print(PACKAGE_CAMPAIGN_MESSAGE)
        logger.info("Ìrè ó!")
        raise typer_module.Exit(CLIExitCode.SUCCESS)


if __name__ == "__main__":
    webhook_cli_app()
