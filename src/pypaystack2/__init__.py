"""Pypaystack2 is a developer-friendly client library for Paystack.

It is a fork of [Pypaystack](https://github.com/edwardpopoola/pypaystack)
That has transformed into its own thing over the years

Modules and packages exported by this package:
   - `sub_clients`: A package containing several clients for Paystack API, like apple pay sub_clients,
    bulk charges sub_clients e.t.c.
   - `models`: A module containing useful utilities and enums
   - `errors`: A module containing error types for pypaystack2
"""

# ruff: noqa: F401
from pypaystack2._metadata import (
    __title__,
    __version__,
    __author__,
    __license__,
    __copyright__,
)

from pypaystack2.main_clients import PaystackClient, AsyncPaystackClient

__all__ = [
    "__title__",
    "__version__",
    "__author__",
    "__license__",
    "__copyright__",
    "PaystackClient",
    "AsyncPaystackClient",
]
