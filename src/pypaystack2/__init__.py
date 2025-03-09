"""
This is the package-level documentation for the `pypaystack2` package.

The ``pypaystack2`` package provides clients for interacting with Paystack's API in your python project
it provides ``PaystackClient`` and ``AsyncPaystackClient``. The former for working in synchronous contexts
and the latter for working in asynchronous contexts. These two classes are considered the main clients
and provide bindings to other sub-clients as class attributes. E.g. ``PaystackClient.apple_pay``

Subpackages:
    - `pypaystack2.sub_clients`: A package containing clients for interacting with specific Paystack's API
    - `pypaystack2.models`: A package containing pydantic model representations of payload and response data
    the individual models may also be referred to as generic type called `PaystackDataModel` which serves
    as a placeholder for the models.

Module:
    - `pypaystack2.enum`: A module containing enums used package wide.


Example usage:

    from pypaystack2 import PaystackClient
    from pypaystack2.enums import Country

    client = PaystackClient() # Assumes your secret key is set in your environmental variables
    # as PAYSTACK_SECRET_KEY. you may also choose to pass the secret key explicitly on instantiation
    # of the client. `client = PaystackClient(secret_key='<your-secret-key>')`

    # Initializing a transaction
    response = client.transactions.initialize(amount=10_000,email="johndoe@example.com")
    print(repr(response))

    # Get banks
    response = client.miscellaneous.get_banks(country=Country.NIGERIA)
    print(repr(response))

For more details, refer to the documentation.
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
