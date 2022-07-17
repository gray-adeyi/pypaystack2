from functools import reduce
from lib2to3.pgen2.token import PERCENT
from typing import Any, Mapping, Optional
from unittest.mock import DEFAULT
from .errors import InvalidDataError
from enum import Enum
from operator import add


class Currency(str, Enum):
    """
    Provides an enum of currencies
    supported by paystack.
    """

    NGN = "NGN"
    GHS = "GHS"
    ZAR = "ZAR"
    USD = "USD"


class Interval(str, Enum):
    """
    Provides an enum of intervals
    supported by paystack.
    """

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ANNUALLY = "annually"


class Channel(str, Enum):
    """
    Provides an enum of payment
    channels supported by paystack,
    """

    CARD = "card"
    BANK = "bank"
    USSD = "ussd"
    QR = "qr"
    MOBILE_MONEY = "mobile_money"
    BANK_TRANSFER = "bank_transfer"


class Bearer(str, Enum):
    """
    Enum for who bears Paystack charges
    """

    ACCOUNT = "account"
    SUBACCOUNT = "subaccount"
    ALL_PROPOTIONAL = "all-proportional"
    ALL = "all"


class TransactionStatus(str, Enum):
    FAILED = "failed"
    SUCCESS = "success"
    ABANDONED = "abandoned"


class SplitType(str, Enum):
    PERCENTAGE = "percentage"
    FLAT = "flat"


class Country(str, Enum):
    NIGERIA = "ng"
    GHANA = "gh"

    @staticmethod
    def get_full(val: str) -> Optional[str]:
        """returns country name lowercase full"""
        val = val.lower()
        if val == "ng":
            return "nigeria"
        elif val == "gh":
            return "ghana"
        return None


class RiskAction(str, Enum):
    DEFAULT = "default"
    WHITELIST = "allow"
    BLACKLIST = "deny"


class Identification(str, Enum):
    BVN = "bvn"
    BANK_ACCOUNT = "bank_account"


class TRType(str, Enum):
    NUBAN = "nuban"
    MOBILE_MONEY = "mobile_money"
    BASA = "basa"


class DocumentType(str, Enum):
    IDENTITY_NUMBER = "identityNumber"
    PASSPORT_NUMBER = "passportNumber"
    BUSINESS_REGISTRATION_NUMBER = "businessRegistrationNumber"


class InvoiceStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class ChargeStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class AccountType(str, Enum):
    PERSONAL = "personal"
    BUSINESS = "business"


class Resolution(str, Enum):
    MERCHANT_ACCEPTED = "merchant-accepted"
    DECLINED = "declined"


class BankType(str, Enum):
    GHIPPS = "ghipps"
    MOBILE_MONEY = "mobile_money"


class DisputeStatus(str, Enum):
    PENDING = "pending"
    RESOLVED = "resolved"
    AWAITING_BANK_FEEDBACK = "awaiting-bank-feedback"
    AWAITING_MERCHANT_FEEDBACK = "awaiting-merchant-feedback"


def validate_amount(amount):

    if not amount:
        raise InvalidDataError("Amount to be charged is required")

    if isinstance(amount, int) or isinstance(
        amount, float
    ):  # Save the sever some headaches
        if amount < 0:
            raise InvalidDataError("Negative amount is not allowed")
        return amount
    else:
        raise InvalidDataError("Amount should be a number")


def validate_interval(interval):

    interval = (
        interval
        if interval.lower() in ["hourly", "daily", "weekly", "monthly", "annually"]
        else None
    )
    if not interval:
        raise InvalidDataError("Please provide a valid plan interval")
    return interval


def add_to_payload(optional_params: list[tuple[str, Any]], payload: Mapping) -> Mapping:
    """
    checks each element in the params and ensure
    it's not None and add it to the param.
    """
    [
        payload.update({item[0]: item[1]})
        for item in optional_params
        if item[1] is not None
    ]
    return payload


def append_query_params(query_params: list[tuple[str, Any]], url) -> str:
    """
    adds other query parameters that are available
    to the url which has the first query parameter.
    """
    params = [
        f"&{param[0]}={param[1]}" for param in query_params if param[1] is not None
    ]
    if len(params) == 0:
        return url
    return url + reduce(add, params)
