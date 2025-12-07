import logging
import os
import threading
from enum import IntEnum
from multiprocessing import Process
from typing import Annotated, Literal

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


ADDR_FLAG_HELP = """The port or address in the form host:port where the tunnel server should forward the webhook payload
to when in `--mode direct` i.e. you app running locally. Otherwise, it is the address where the proxy server is started
when in `--mode proxy`. Note: the scheme should not be included when using --addr in the form host:port e.g.
localhost:8080 and not https://localhost:8080"""

NGROK_AUTH_TOKEN_FLAG_HELP = """Flag to enable passing your ngrok auth token via an input prompt. auth token accepted
this way takes precedence over the value set in the environmental variable as `PAYSTACK_WEBHOOK_NGROK_AUTH_TOKEN`"""

MODE_FLAG_HELP = """The mode in which the tunnel server should operate in, when in `--mode direct`, the webook payload
received by the tunnel server is forwarded directly to your local app via the specified --addr i.e.
paystack -> tunnel server -> localhost. When in `--mode proxy`, the tunnel server forwards the webhook payload to
the proxy server setup at --addr which then forward the payload to the clients specified via --proxy-clients i.e.
paystack -> tunnel server -> proxy server -> proxy clients"""

PROXY_CLIENTS_FLAG_HELP = """The clients that a proxy server should forward webhook payloads to when operating in
`--mode proxy`. This is a comma separated value of urls e.g. http://localhost:5173,http://127.0.0.1:8000/webhooks/paystack
Note: the scheme must be included. http://localhost:5173 not localhost:5173"""

PROXY_SERVER_LOG_PAYLOAD_FLAG_HELP = """This flag is used to enable the proxy server to log the webhook payload it
receives from the tunnel server while forwarding it to the proxy clients."""

DOTENV_PATH_FLAG = """This flag is used to set a custom dotenv file path, by default, this cli will look for your
environmental variables in a `.env` file"""


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

    This utility makes working with webhooks locally while developing easy by leveraging ngrok
    which provides http tunneling functionality.

    (note you'll need to sign up to ngrok to obtain your ngrok auth token that can be set via
    --ngrok-auth-token flag or `PAYSTACK_NGROK_AUTH_TOKEN` environment variable.)

    The real issue with working with webhooks while working locally is that the servers emitting
    the webhook events cannot directly send the event payload to your local development endpoint
    that's where a tunnel server comes into the picture and makes this possible by serving as an
    intermediary between your local app and the webhook event producer server. The flow is that
    you'd start the tunnel server while providing it with the port on your localhost you want
    it to forward your incoming webhook events to. As a result of this, the tunnel server
    provides you with a url that you can register with the webhook event producer (Paystack)

    paystack -> tunnel server -> localhost

    paystack -> tunnel server -> proxy server -> proxy clients

    As you can see based on the diagram above, this tunnel server can work in two modes, i.e,
    direct and proxy. In the direct mode, the tunnel server forwards the webhook events directly
    to your local development app (localhost). There may be cases where you want the webhook
    events forwarded to multiple local clients, you can use the proxy mode. In direct mode,
    the port provided via the --addr flag or `PAYSTACK_WEBHOOK_PORT` environment variable,
    is the port of your application running locally. If you have a custom endpoint in your
    local app for handling webhook events like `http://127.0.0.1:8000/webhooks/paystack`,
    and you obtained a tunnel url like ``, you should register `` with paystack as your
    webhook event listening endpoint. In the proxy mode, an intermediate proxy server is set up
    locally with its port at the value of --addr flag or `PAYSTACK_WEBHOOK_ADDRESS` environment variable.
    (the --addr flag take precedence over the environment variable if both are set).
    This proxy server running locally is then responsible for forwarding the webhook events directly
    to a list of urls provided via the --proxy-clients flag.
    """
    dotenv_module.load_dotenv(dotenv_path=dotenv_path)
    tunnel_server_listener: ngrok_module.Listener | None = None
    proxy_server_process: Process | None = None
    tunnel_server_listener_options = {}

    try:
        _ngrok_auth_token = ""
        if ngrok_auth_token:
            _ngrok_auth_token = typer_module.prompt(
                "Please enter or paste you NGROK auth token [input is hidden, press enter when done]",
                hide_input=True,
            )
        if not ngrok_auth_token and not os.environ.get("PAYSTACK_NGROK_AUTH_TOKEN"):
            print("ngrok auth token not provided in flags or environment variable")
            raise typer_module.Exit(CLIExitCode.NGROK_TOKEN_NOT_SET)
        tunnel_server_listener_options["authtoken"] = (
            _ngrok_auth_token or os.environ.get("PAYSTACK_NGROK_AUTH_TOKEN")
        )

        if mode == "proxy":
            if not proxy_clients:
                print(
                    "proxy clients not provided in --proxy-clients flag and --mode flag is proxy"
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

        tunnel_server_listener = ngrok_module.forward(
            addr, **tunnel_server_listener_options
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
            ...
            # TODO: Figure out how to close ngrok in synchronous mode
            # tunnel_server_listener.close()
            logger.info("PyPaystack2 Webhook Tunnel Server shutdown successful")
        logger.info("Ìrè ó!")
        raise typer_module.Exit(CLIExitCode.SUCCESS)


if __name__ == "__main__":
    webhook_cli_app()
