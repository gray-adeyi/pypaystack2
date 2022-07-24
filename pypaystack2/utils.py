from functools import reduce
from typing import Any, Optional, Union
from unittest.mock import DEFAULT
from .errors import InvalidDataError
from enum import Enum
from operator import add


class Currency(str, Enum):
    """Enum of currencies supported by paystack."""

    NGN = "NGN"
    GHS = "GHS"
    ZAR = "ZAR"
    USD = "USD"


class Interval(str, Enum):
    """Enum of intervals supported by paystack."""

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ANNUALLY = "annually"


class Channel(str, Enum):
    """Enum of payment channels supported by paystack"""

    CARD = "card"
    BANK = "bank"
    USSD = "ussd"
    QR = "qr"
    MOBILE_MONEY = "mobile_money"
    BANK_TRANSFER = "bank_transfer"


class Bearer(str, Enum):
    """Enum for who bears paystack charges"""

    ACCOUNT = "account"
    SUBACCOUNT = "subaccount"
    ALL_PROPOTIONAL = "all-proportional"
    ALL = "all"


class TransactionStatus(str, Enum):
    """Enum of transaction status"""

    FAILED = "failed"
    SUCCESS = "success"
    ABANDONED = "abandoned"


class SplitType(str, Enum):
    """Enum of split types"""

    PERCENTAGE = "percentage"
    FLAT = "flat"


class Country(str, Enum):
    """Enum of countries supported by paystack"""

    NIGERIA = "ng"
    GHANA = "gh"

    @staticmethod
    def get_full(val: str) -> Optional[str]:
        """Returns paystack supported country name in full lowercase

        Parameters
        ----------
        val : str
            The two digit iso name of the country.
        Returns
        -------
        str,optinal
            The name of the country in lowercase if it is supported by
            paystack or none.
        """
        val = val.lower()
        if val == "ng":
            return "nigeria"
        elif val == "gh":
            return "ghana"
        return None


class RiskAction(str, Enum):
    """Enum of RiskActions supported by paystack"""

    DEFAULT = "default"
    WHITELIST = "allow"
    BLACKLIST = "deny"


class Identification(str, Enum):
    """Enum of Identification methods supported by paystack"""

    BVN = "bvn"
    BANK_ACCOUNT = "bank_account"


class TRType(str, Enum):
    """Enum of Transfer Recipient types"""

    # FIXME: Find a better name for this class to reduce confusion.

    NUBAN = "nuban"
    MOBILE_MONEY = "mobile_money"
    BASA = "basa"


class DocumentType(str, Enum):
    """Enum of Document types supported by paystack"""

    IDENTITY_NUMBER = "identityNumber"
    PASSPORT_NUMBER = "passportNumber"
    BUSINESS_REGISTRATION_NUMBER = "businessRegistrationNumber"


# FIXME: Unify status codes with similarities
# InvoiceStatus and ChargeStatus is redundant
class InvoiceStatus(str, Enum):
    """Enum of invoice status supported by paystack"""

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class ChargeStatus(str, Enum):
    """Enum of charge status supported by paystack"""

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class PlanStatus(str, Enum):
    """Enum of plan status supported by paystack"""

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class Schedule(str, Enum):
    """Enum of settlement schedules supported by paystack"""

    AUTO = "auto"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    MANUAL = "manual"


class Reason(str, Enum):
    """Enum of Reset OTP options"""

    RESEND_OTP = "resend_otp"
    TRANSFER = "transfer"


class Gateway(str, Enum):
    """Enum of bank gateways supported by paystack"""

    EMANDATE = "emandate"
    DIGITALBANKMANDATE = "digitalbankmandate"


class AccountType(str, Enum):
    """Enum of Account types supported by paystack"""

    PERSONAL = "personal"
    BUSINESS = "business"


class Resolution(str, Enum):
    """Enum of Resolutions supported by paystack"""

    MERCHANT_ACCEPTED = "merchant-accepted"
    DECLINED = "declined"


class BankType(str, Enum):
    """Enum of bank types"""

    GHIPPS = "ghipps"
    MOBILE_MONEY = "mobile_money"


class DisputeStatus(str, Enum):
    """Enum of dispute status supported by paystack"""

    PENDING = "pending"
    RESOLVED = "resolved"
    AWAITING_BANK_FEEDBACK = "awaiting-bank-feedback"
    AWAITING_MERCHANT_FEEDBACK = "awaiting-merchant-feedback"


def validate_amount(amount: Union[int, float]) -> Union[int, float]:
    """Helps to validate money amount.

    Helps to ensure that a valid amount of money
    is supplied as an input, to prevent cases where
    negative or zero value is provided as an amount.

    Parameters
    ----------
    amount: int,float
        The money to be validated.

    Returns
    -------
    int,float
        The money supplied if it is valid.

    Raises
    ------
    InvalidDataError
        With the cause of the validation error
    """

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


def validate_interval(interval: str) -> str:
    """Validates that the interval supplied is supported by paystack

    Parameters
    ----------
    interval:str
        any of the intervals supported by paystack i.e hourly,daily
        weekly,monthly,annually

    Returns
    -------
    str
        returns the interval if it is a valid paystack interval

    Raises
    ------
    InvalidDataError
        to provide feedback that an invalid interval was provided.
    """

    interval = (
        interval
        if interval.lower() in ["hourly", "daily", "weekly", "monthly", "annually"]
        else None
    )
    if not interval:
        raise InvalidDataError("Please provide a valid plan interval")
    return interval


def add_to_payload(
    optional_params: list[tuple[str, Any]], payload: dict[str, Any]
) -> dict[str, Any]:
    """Adds more parameters to an existing payload.

    This is a utility is used in the generation of payloads
    for a request body. It helps to add more parameters to
    a payload if it is not None.
    e.g say you want to send a payload which is currently
    ``{"amount": 20000}`` and you want to include an additional
    data such as ``currency`` if provided in the ``optional_params``
    to send this ``{"amount": 20000,"currency":"ngn"}`` if only
    the currency is available otherwise send the intial payload.
    This functions takes a list of optional parameters
    which is added to the payload is they are available and
    returns the payload.

    Parameters
    ----------
    optional_params: list[tuple[str,Any]]
        A list of additional data to be added to the payload if it is
        available. It follows the format ``[("name-on-payload","value")].``
        e.g ``[("currency","ngn"),("amount",2000)]``
    payload: dict[str,Any]
        A dictionary containing the data to be sent in the request body.

    Returns
    -------
    dict[str,Any]
        A dictionary of the payload updated with addtional data in the
        optional_params that are not ``None``.
    """
    [
        payload.update({item[0]: item[1]})
        for item in optional_params
        if item[1] is not None
    ]
    return payload


def append_query_params(query_params: list[tuple[str, Any]], url: str) -> str:
    """Adds more queries to a url that already has query parameters in its suffix

    This function should only be used with urls that already have a
    query parameter suffixed to it because it makes that assumption
    that the url supplied is of the state ``http://example-url.com?firstQuery=1``
    and it adds more query parameters delimited by & to the end of the provided
    url ``http://example-url.com?firstQuery=1&otherQuery=2&...``

    Parameters
    ----------
    query_params: list[tuple[str,Any]]
        A list of other query parameters that should be appended to the url
        if it is not None. e.g ``[("page",2),("pagination",50),("currency",None)]`` ->
        ``url&page=2&pagination=50``
    url: str
        The url to which additional query parameters is added.

    Returns
    -------
    str
        The new url with padded query parameters.
    """
    params = [
        f"&{param[0]}={param[1]}" for param in query_params if param[1] is not None
    ]
    if len(params) == 0:
        return url
    return url + reduce(add, params)
