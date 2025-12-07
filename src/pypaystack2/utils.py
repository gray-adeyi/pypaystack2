import importlib
from types import ModuleType

from pypaystack2.webhook.models import EndpointAddress

WEBHOOK_DEPENDENCY_IMPORT_ERROR_MESSAGE_TEMPLATE = "Package {package_name} not found. Please run `pip install pypaystack2[webhook]` or `uv add pypaystack2[webhook]`"


def try_import_module(name: str, error_msg: str | None = None) -> ModuleType:
    try:
        return importlib.import_module(name)
    except ImportError as exc:
        raise ImportError(
            error_msg or 'Could not import module "{}"'.format(name)
        ) from exc


def parse_address(address: str) -> EndpointAddress:
    if not address:
        return EndpointAddress()
    if address.isdigit():
        return EndpointAddress(host=None, port=int(address))
    parts = address.split(":")
    if len(parts) == 2:
        return EndpointAddress(
            host=parts[0] if parts[0] else None,
            port=int(parts[1]) if parts[1].isdigit() else None,
        )
    if parts[0].isdigit():
        return EndpointAddress(host=None, port=int(parts[0]))
    if parts[0]:
        return EndpointAddress(host=parts[0], port=None)
