from http import HTTPStatus
from typing import Any, Optional, Literal, TypedDict, Self, TypeVar, Generic

from pydantic import BaseModel, model_validator

from pypaystack2.utils.enums import RecipientType

PaystackDataModel = TypeVar("PaystackDataModel")


class BulkChargeInstruction(BaseModel):
    """A dataclass for bulk charge instruction.

    Attributes:
        authorization: The authorization code of the customer you want to charge.
        amount: The amount you want to charge.
        reference: The transaction reference.
    """

    authorization: str
    amount: int
    reference: str


class LineItem(BaseModel):
    """A dataclass for LineItem.

    Attributes:
        name: The name of the product.
        amount: The price of the product.
        quantity: The quantity.
    """

    name: str
    amount: int
    quantity: int


class Tax(BaseModel):
    """A dataclass for Tax.

    Attributes:
        name: The name of the tax.
        amount: The price of the tax.
    """

    name: str
    amount: int


class SplitAccount(BaseModel):
    """A dataclass for SplitAccount.

    Attributes:
        subaccount: The id of the sub account.
        share: The share of the split account the sub account should have.
    """

    subaccount: str
    share: int | float


class Recipient(BaseModel):
    """A dataclass for Recipient.

    Attributes:
        type: The type of recipient e.g., RecipientType.NUBAN, RecipientType.BASA.
        name: The name.
        bank_code: The bank code.
        account_number: The account number of recipient.
    """

    type: RecipientType
    name: str
    bank_code: str
    account_number: str


class TransferInstruction(BaseModel):
    """A dataclass for TransferInstruction.

    Attributes:
        amount: The amount to be transferred.
        recipient: The beneficiary of the transaction.
        reference: The reference for the transaction.
        reason: The narration of the transaction.
    """

    amount: int
    recipient: str
    reference: Optional[str]
    reason: Optional[str]


class Response(BaseModel, Generic[PaystackDataModel]):
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
        meta: Additional information about the response.
        type: In cases where the response has a status of `False` or the status code
            is an error status code. the `type` field indicates the type of error e.g. `api_error`
        code: In cases where the response has a status of `False` or the status code
            is an error status code. the `type` field indicates the type of error e.g. `api_error`
    """

    status_code: HTTPStatus
    status: bool
    message: str
    data: PaystackDataModel | None
    meta: dict | None
    type: str | None
    code: str | None
    raw: dict[str, Any] | list[dict[str, Any]] | bytes | None


class ServiceFeeOptions(TypedDict):
    is_international: bool | None
    service: str
    is_eft: bool | None
    card: str | None


class BaseServiceFeeOptions(BaseModel):
    is_international: bool = False


class NigeriaServiceFeeOptions(BaseServiceFeeOptions):
    service: Literal[
        "transactions",
        "transfers",
        "virtual_account_transactions",
        "virtual_terminal_transfers",
        "virtual_terminal_ussd_transactions",
        "virtual_terminal_local_card_transactions",
        "virtual_terminal_international_card_transactions",
        "physical_terminal_live_smartpeak_p1000",
        "physical_terminal_test_smartpeak_p1000",
        "physical_terminal_card_transactions",
        "physical_terminal_ussd_transactions",
        "physical_terminal_bank_transfers",
    ] = "transactions"
    card: Literal["mastercard", "visa", "verve", "american_express"] | None = None

    @model_validator(mode="after")
    def validate_model(self) -> Self:  # type: ignore
        if self.is_international and self.service != "transactions":
            raise ValueError(
                'only service="transactions" is supported when is_international=True'
            )
        if self.is_international and self.card is None:
            raise ValueError("card is required when is_international=True")
        if (
            self.service == "virtual_terminal_international_card_transactions"
            and self.card is None
        ):
            raise ValueError(
                "card is required for service=virtual_terminal_international_card_transactions"
            )
        return self


class CoteDIvoreServiceFeeOptions(BaseServiceFeeOptions):
    service: Literal["mobile_money_transactions", "card_transactions"] = (
        "mobile_money_transactions"
    )


class GhanaServiceFeeOptions(BaseServiceFeeOptions):
    service: Literal[
        "transactions", "transfers_to_mobile_money", "transfers_to_bank_accounts"
    ] = "transactions"


class KenyaServiceFeeOptions(BaseServiceFeeOptions):
    service: Literal[
        "mpesa_transactions",
        "card_transactions",
        "transfers_to_mpesa_wallet",
        "transfers_to_mpesa_paybill",
        "transfers_to_bank_account",
    ] = "mpesa_transactions"


class SouthAfricaServiceFeeOptions(BaseServiceFeeOptions):
    service: Literal["transactions", "transfers"]
    is_eft: bool | None = None

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        if self.service == "transfers":
            self.is_eft = None
        if self.service == "transactions" and self.is_eft is None:
            self.is_eft = False
        return self


class RwandaServiceFeeOptions(BaseServiceFeeOptions):
    service: str = "transactions"


class EgyptServiceFeeOptions(BaseServiceFeeOptions):
    service: str = "transactions"
    card: Literal["meeza", "others"] = "others"
