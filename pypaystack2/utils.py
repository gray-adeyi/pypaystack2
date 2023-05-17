from dataclasses import dataclass
from enum import Enum
from functools import reduce
from operator import add
from typing import Any, Optional, Union, NamedTuple

from pypaystack2.errors import InvalidDataError


@dataclass
class BulkChargeInstruction:
    authorization: str
    amount: int
    reference: str

    @property
    def dict(self) -> dict:
        return {
            "authorization": self.authorization,
            "amount": self.amount,
            "reference": self.reference,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "BulkChargeInstruction":
        return cls(
            authorization=value["authorization"],
            amount=value["amount"],
            reference=value["reference"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["BulkChargeInstruction"]:
        return [
            cls(
                authorization=item["authorization"],
                amount=item["amount"],
                reference=item["reference"],
            )
            for item in values
        ]


@dataclass
class LineItem:
    name: str
    amount: int
    quantity: int

    @property
    def dict(self) -> dict:
        return {
            "name": self.name,
            "amount": self.amount,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "LineItem":
        return cls(
            name=value["authorization"],
            amount=value["amount"],
            quantity=value["quantity"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["LineItem"]:
        return [
            cls(
                name=item["name"],
                amount=item["amount"],
                quantity=item["quantity"],
            )
            for item in values
        ]


@dataclass
class Tax:
    name: str
    amount: int

    @property
    def dict(self) -> dict:
        return {
            "name": self.name,
            "amount": self.amount,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "Tax":
        return cls(
            name=value["authorization"],
            amount=value["amount"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["Tax"]:
        return [
            cls(
                name=item["name"],
                amount=item["amount"],
            )
            for item in values
        ]


@dataclass
class SplitAccount:
    subaccount: str
    share: Union[int, float]

    @property
    def dict(self) -> dict:
        return {
            "subaccount": self.subaccount,
            "share": self.share,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "SplitAccount":
        return cls(
            subaccount=value["subaccount"],
            share=value["share"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["SplitAccount"]:
        return [
            cls(
                subaccount=item["subaccount"],
                share=item["share"],
            )
            for item in values
        ]


@dataclass
class Recipient:
    type: "RecipientType"
    name: str
    bank_code: str
    account_number: str

    @property
    def dict(self) -> dict:
        return {
            "type": self.type,
            "name": self.name,
            "bank_code": self.bank_code,
            "account_number": self.account_number,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "Recipient":
        return cls(
            type=value["type"],
            name=value["name"],
            bank_code=value["bank_code"],
            account_number=value["account_number"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["Recipient"]:
        return [
            cls(
                type=item["type"],
                name=item["name"],
                bank_code=item["bank_code"],
                account_number=item["account_number"],
            )
            for item in values
        ]


@dataclass
class TransferInstruction:
    amount: int
    recipient: str
    reference: Optional[str]
    reason: Optional[str]

    @property
    def dict(self) -> dict:
        return {
            "amount": self.amount,
            "reference": self.reference,
            "recipient": self.recipient,
            "reason": self.reason,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "TransferInstruction":
        return cls(
            amount=value["amount"],
            reference=value.get("reference"),
            recipient=value["recipient"],
            reason=value.get("reason"),
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["TransferInstruction"]:
        return [
            cls(
                amount=item["amount"],
                reference=item.get("reference"),
                recipient=item["recipient"],
                reason=item.get("reason"),
            )
            for item in values
        ]


class HTTPMethod(str, Enum):
    """An enum of supported http methods"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class TerminalEvent(str, Enum):
    """Enum of the types of events supported by Terminal API"""

    TRANSACTION = "transaction"
    INVOICE = "invoice"


class TerminalEventAction(str, Enum):
    PROCESS = "process"
    VIEW = "view"
    PRINT = "print"


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
    SUB_ACCOUNT = "subaccount"
    ALL_PROPORTIONAL = "all-proportional"
    ALL = "all"


class TransactionStatus(str, Enum):
    """Enum of transaction status"""

    FAILED = "failed"
    SUCCESS = "success"
    ABANDONED = "abandoned"


class Split(str, Enum):
    """Enum of split types"""

    PERCENTAGE = "percentage"
    FLAT = "flat"


class Country(str, Enum):
    """Enum of countries supported by paystack"""

    NIGERIA = "NG"
    GHANA = "GH"
    SOUTH_AFRICA = "ZA"

    @staticmethod
    def get_full(value: str) -> Optional[str]:
        """Returns paystack supported country name in full lowercase

        Args:
            value: The two-digit iso name of the country.

        Returns:
            The name of the country in lowercase if it is supported by
            paystack or none.
        """
        value = value.lower()
        return {"ng": "nigeria", "gh": "ghana", "za": "south africa"}.get(value)


class RiskAction(str, Enum):
    """Enum of RiskActions supported by paystack"""

    DEFAULT = "default"
    WHITELIST = "allow"
    BLACKLIST = "deny"


class Identification(str, Enum):
    """Enum of Identification methods supported by paystack"""

    BVN = "bvn"
    BANK_ACCOUNT = "bank_account"


class RecipientType(str, Enum):
    """Enum of Transfer Recipient types"""

    NUBAN = "nuban"
    MOBILE_MONEY = "mobile_money"
    BASA = "basa"


class Document(str, Enum):
    """Enum of Document types supported by paystack"""

    IDENTITY_NUMBER = "identityNumber"
    PASSPORT_NUMBER = "passportNumber"
    BUSINESS_REGISTRATION_NUMBER = "businessRegistrationNumber"


# FIXME: Unify status codes with similarities
# InvoiceStatus and ChargeStatus is redundant


class Status(str, Enum):
    """Enum of statuses supported by paystack, used by Invoice, Charge & Plan"""

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
    DISABLE_OTP = "disable_otp"


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

    Args:
        amount: The money to be validated.

    Returns:
        The money supplied if it is valid.

    Raises:
        InvalidDataError: With the cause of the validation error
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

    Args:
        interval: any of the intervals supported by paystack i.e. hourly, daily
            weekly,monthly,annually

    Returns:
        The interval if it is a valid paystack interval

    Raises:
        InvalidDataError: to provide feedback that an invalid interval was provided.
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
    e.g. say you want to send a payload which is currently
    ``{"amount": 20000}`` and you want to include an additional
    data such as ``currency`` if provided in the ``optional_params``
    to send this ``{"amount": 20000,"currency":"ngn"}`` if only
    the currency is available otherwise send the initial payload.
    This functions takes a list of optional parameters
    which is added to the payload is they are available and
    returns the payload.

    Args:
        optional_params: A list of additional data to be added to the payload if it is
            available. It follows the format ``[("name-on-payload","value")].``
            e.g ``[("currency","ngn"),("amount",2000)]``
        payload: A dictionary containing the data to be sent in the request body.

    Returns:
        A dictionary of the payload updated with additional data in the
            optional_params that are not `None`.
    """
    [
        payload.update({item[0]: item[1]})
        for item in optional_params
        if item[1] is not None
    ]
    return payload


def append_query_params(query_params: list[tuple[str, Any]], url: str) -> str:
    """Adds more queries to url that already have query parameters in its suffix

    This function should only be used with urls that already have a
    query parameter suffixed to it because it makes that assumption
    that the url supplied is of the state ``http://example-url.com?firstQuery=1``
    and it adds more query parameters delimited by & to the end of the provided
    url ``http://example-url.com?firstQuery=1&otherQuery=2&...``

    Args:
        query_params: A list of other query parameters that should be appended to the url
            if it is not None. e.g ``[("page",2),("pagination",50),("currency",None)]`` ->
            ``url&page=2&pagination=50``
        url: The url to which additional query parameters are added.

    Returns:
        The new url with padded query parameters.
    """
    params = [
        f"&{param[0]}={param[1]}" for param in query_params if param[1] is not None
    ]
    if len(params) == 0:
        return url
    return url + reduce(add, params)


class Response(NamedTuple):
    """
    A namedtuple containing the data gotten from making a request to paystack's API endpoints.

    All wrapper methods returns an instance of `Response` which can be used as a tuple following
    this format `(status_code, status, message, data)`. Accessing by attributes is also possible
    say for example `response` is an instance of `Response`, we can access the data in the
    response like so `response.data`

    Attributes:
        status_code: The response status code
        status: A flag for the response status
        message: Paystack response message
        data: Data sent from paystack's server if any.
    """

    status_code: int
    status: bool
    message: str
    data: Optional[Union[dict[str, Any], list[dict[str, Any]]]]
