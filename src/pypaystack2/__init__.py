"""Pypaystack2 is a developer-friendly client library for Paystack.

It is a fork of [Pypaystack](https://github.com/edwardpopoola/pypaystack)
That has transformed into its own thing over the years

Modules and packages exported by this package:
   - `sub_clients`: A package containing several clients for Paystack API, like apple pay sub_clients,
    bulk charges sub_clients e.t.c.
   - `utils`: A module containing useful utilities and enums
   - `errors`: A module containing error types for pypaystack2
"""

# ruff: noqa: F401
from pypaystack2.paystack import PaystackClient, AsyncPaystackClient
from pypaystack2._metadata import (
    __title__,
    __version__,
    __author__,
    __license__,
    __copyright__,
)
from pypaystack2.utils import (
    BulkChargeInstruction,
    LineItem,
    Tax,
    SplitAccount,
    Recipient,
    TransferInstruction,
    TerminalEvent,
    TerminalEventAction,
    Currency,
    Interval,
    Channel,
    Bearer,
    TransactionStatus,
    Split,
    Country,
    RiskAction,
    Identification,
    RecipientType,
    Document,
    Status,
    Schedule,
    Reason,
    Gateway,
    AccountType,
    Resolution,
    BankType,
    DisputeStatus,
    validate_amount,
    validate_interval,
    Response,
)
