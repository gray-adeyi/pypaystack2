from enum import StrEnum


class TerminalEvent(StrEnum):
    """Enum of the types of events supported by Terminal API"""

    TRANSACTION = "transaction"
    INVOICE = "invoice"


class TerminalEventAction(StrEnum):
    PROCESS = "process"
    VIEW = "view"
    PRINT = "print"


class Currency(StrEnum):
    """Enum of currencies supported by paystack."""

    NGN = "NGN"
    GHS = "GHS"
    ZAR = "ZAR"
    USD = "USD"
    KES = "KES"
    XOF = "XOF"
    EGP = "EGP"
    RWF = "RWF"


class Interval(StrEnum):
    """Enum of intervals supported by paystack."""

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
    ANNUALLY = "annually"


class Channel(StrEnum):
    """Enum of payment channels supported by paystack"""

    CARD = "card"
    BANK = "bank"
    APPLE_PAY = "apple_pay"
    USSD = "ussd"
    QR = "qr"
    MOBILE_MONEY = "mobile_money"
    BANK_TRANSFER = "bank_transfer"
    EFT = "eft"
    PAYATTITUDE = "payattitude"


class Bearer(StrEnum):
    """Enum for who bears paystack charges"""

    ACCOUNT = "account"
    SUB_ACCOUNT = "subaccount"
    ALL_PROPORTIONAL = "all-proportional"
    ALL = "all"


class TransactionStatus(StrEnum):
    """Enum of transaction status"""

    FAILED = "failed"
    SUCCESS = "success"
    ABANDONED = "abandoned"


class Split(StrEnum):
    """Enum of split types"""

    PERCENTAGE = "percentage"
    FLAT = "flat"


class Country(StrEnum):
    """Enum of countries supported by paystack"""

    NIGERIA = "NG"
    GHANA = "GH"
    SOUTH_AFRICA = "ZA"
    KENYA = "KE"
    COTE_D_IVOIRE = "CI"
    EGYPT = "EG"
    RWANDA = "RW"

    @staticmethod
    def get_full(value: str) -> str | None:
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
            "rw": "rwanda",
        }.get(value)


class RiskAction(StrEnum):
    """Enum of RiskActions supported by paystack"""

    DEFAULT = "default"
    WHITELIST = "allow"
    BLACKLIST = "deny"


class Identification(StrEnum):
    """Enum of Identification methods supported by paystack"""

    BVN = "bvn"
    BANK_ACCOUNT = "bank_account"


class RecipientType(StrEnum):
    """Enum of Transfer Recipient types"""

    NUBAN = "nuban"
    MOBILE_MONEY = "mobile_money"
    BASA = "basa"


class Document(StrEnum):
    """Enum of Document types supported by paystack"""

    IDENTITY_NUMBER = "identityNumber"
    PASSPORT_NUMBER = "passportNumber"
    BUSINESS_REGISTRATION_NUMBER = "businessRegistrationNumber"


class Status(StrEnum):
    """Enum of statuses supported by paystack, used by Invoice, Charge & Plan"""

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class Schedule(StrEnum):
    """Enum of settlement schedules supported by paystack"""

    AUTO = "auto"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    MANUAL = "manual"


class Reason(StrEnum):
    """Enum of Reset OTP options"""

    RESEND_OTP = "resend_otp"
    TRANSFER = "transfer"
    DISABLE_OTP = "disable_otp"


class Gateway(StrEnum):
    """Enum of bank gateways supported by paystack"""

    EMANDATE = "emandate"
    DIGITALBANKMANDATE = "digitalbankmandate"


class AccountType(StrEnum):
    """Enum of Account types supported by paystack"""

    PERSONAL = "personal"
    BUSINESS = "business"


class Resolution(StrEnum):
    """Enum of Resolutions supported by paystack"""

    MERCHANT_ACCEPTED = "merchant-accepted"
    DECLINED = "declined"


class BankType(StrEnum):
    """Enum of bank types"""

    GHIPPS = "ghipps"
    MOBILE_MONEY = "mobile_money"


class DisputeStatus(StrEnum):
    """Enum of dispute status supported by paystack"""

    PENDING = "pending"
    RESOLVED = "resolved"
    AWAITING_BANK_FEEDBACK = "awaiting-bank-feedback"
    AWAITING_MERCHANT_FEEDBACK = "awaiting-merchant-feedback"
    ARCHIVED = "archived"


class Domain(StrEnum):
    LIVE = "live"
    TEST = "test"


class BulkChargeStatus(StrEnum):
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETE = "complete"


class SupportedCountryRelationshipType(StrEnum):
    CURRENCY = "currency"
    INTEGRATION_FEATURE = "integration_feature"
    INTEGRATION_TYPE = "integration_type"
    PAYMENT_METHOD = "payment_method"


class WebhookEventType(StrEnum):
    CHARGE_DISPUTE_CREATE = "charge.dispute.create"
    CHARGE_DISPUTE_REMIND = "charge.dispute.remind"
    CHARGE_DISPUTE_RESOLVE = "charge.dispute.resolve"
    CHARGE_SUCCESS = "charge.success"
    CUSTOMER_IDENTIFICATION_FAILED = "customeridentification.failed"
    CUSTOMER_IDENTIFICATION_SUCCESS = "customeridentification.success"
    DEDICATED_ACCOUNT_ASSIGN_FAILED = "dedicatedaccount.assign.failed"
    DEDICATED_ACCOUNT_ASSIGN_SUCCESS = "dedicatedaccount.assign.success"
    INVOICE_CREATE = "invoice.create"
    INVOICE_PAYMENT_FAILED = "invoice.payment_failed"
    INVOICE_UPDATE = "invoice.update"
    PAYMENT_REQUEST_PENDING = "paymentrequest.pending"
    PAYMENT_REQUEST_SUCCESS = "paymentrequet.success"
    REFUND_FAILED = "refund.failed"
    REFUND_PENDING = "refund.pending"
    REFUND_PROCESSED = "refund.processed"
    REFUND_PROCESSING = "refund.processing"
    SUBSCRIPTION_CREATE = "subscription.create"
    SUBSCRIPTION_DISABLE = "subscription.disable"
    SUBSCRIPTION_EXPIRING_CARDS = "subscription.expiring_cards"
    SUBSCRIPTION_NOT_RENEW = "subscription.not_renew"
    TRANSFER_FAILED = "transfer.failed"
    TRANSFER_SUCCESS = "transfer.success"
    TRANSFER_REVERSED = "transfer.reversed"


class WebhookDeliveryStatus(StrEnum):
    DELIVERED = "Delivered"
    PENDING = "Pending"
    FAILED = "Failed"
