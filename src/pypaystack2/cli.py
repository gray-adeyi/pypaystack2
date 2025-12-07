from pypaystack2.utils import (
    WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE,
    try_import_module,
)
from pypaystack2.webhook.cli import webhook_cli_app

# for now only the webhook feature needs the cli from a consumer standpoint so the error message is sufficient
typer_module = try_import_module(
    "typer",
    error_msg=WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE.format(
        package_name="typer"
    ),
)


cli_app = typer_module.Typer()
cli_app.add_typer(
    webhook_cli_app,
    name="webhook",
    help="Webhook CLI app for working with paystack webhooks. Try `pypaystack2 webhook --help`",
)
