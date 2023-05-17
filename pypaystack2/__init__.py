"""Pypaystack2 is a simple python wrapper for Paystack API.

it is a fork of the original project [Pypaystack](https://github.com/edwardpopoola/pypaystack)
Modules and packages exported by this package:
   - `api`: A package containing several wrappers for Paystack API, like apple pay api, bulk charges api e.t.c.
   - `utils`: A module containing useful utilities and enums
   - `errors`: A module containing error types for pypaystack2
"""
from pypaystack2.paystack import Paystack, AsyncPaystack
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

# prevent removal of unused import
Paystack
AsyncPaystack
__title__
__version__
__author__
__license__
__copyright__
[
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
]
