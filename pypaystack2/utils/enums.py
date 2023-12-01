from enum import Enum
from typing import Optional


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
    KES = "KES"
    XOF = "XOF"
    EGP = "EGP"


class Interval(str, Enum):
    """Enum of intervals supported by paystack."""

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
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
    KENYA = "KE"
    COTE_D_IVOIRE = "CI"
    EGYPT = "EG"

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
        return {
            "ng": "nigeria",
            "gh": "ghana",
            "za": "south africa",
            "ke": "kenya",
            "ci": "côte d'ivoire",
            "eg": "egypt",
        }.get(value)


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
