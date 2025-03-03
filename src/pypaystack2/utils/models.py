from http import HTTPStatus
from typing import Any, Optional, Literal, TypedDict, Self, TypeVar, Generic

from pydantic import BaseModel, model_validator

from pypaystack2.utils.enums import RecipientType, Currency

PaystackDataModel = TypeVar("PaystackDataModel", bound=BaseModel)

# FIXME: I was having issues constraining this generic type to the types
#   `PaystackDataModel`, `list[PaystackDataModel]` or `None`. it's why it's left as is.
PaystackResponseData = TypeVar("PaystackResponseData")


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
    """A model for representing Transfer Recipients.

    Attributes:
        type: Recipient Type. any value from the `RecipientType` enum
        name: A name for the recipient
        account_number: Required if `type` is `RecipientType.NUBAN` or `RecipientType.BASA`
        bank_code: Required if `type` is `RecipientType.NUBAN` or `RecipientType.BASA`.
            You can get the list of Bank Codes by calling the `PaystackClient.get_banks`.
        description: description
        currency: currency
        auth_code: auth code
        metadata: metadata
    """

    type: RecipientType
    name: str
    account_number: str
    bank_code: str | None = None
    description: str | None = None
    currency: Currency | None = None
    auth_code: str | None = None
    metadata: dict[str, Any] | None = None


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


class Response(BaseModel, Generic[PaystackResponseData]):
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
        data: Data sent from paystack's server if any. This data is of a generic type called `PaystackDataModel`
            indicating that data can either be a pydantic model instance, a list of pydantic model instances or
            `None`. The exact type of the data can be determined by looking at the return type of the client method
            that you called that returns a `Response`. E.g. `PaystackClient.bulk_charges.get_batches` method has
            its return type as `Response[list[BulkCharge]]`, hence, if you called this method and got a `Response`,
            even though `Response.data` is type hinted as `PaystackDataModel`, you should expect `Response.data` to
            be `list[BulkCharge]` which is a list of `BulkCharge` pydantic model instances which is a valid
            `PaystackDataModel`. A client method with a return type of `Response[None]` indicates that no data is
            expected to be returned from paystack by calling that method, hence, `Response.data` is `None`. If
            `Response.data` is `None` when the client method does not explicitly specify that the return type of
            the method at `Response[None]`, this is an indicator that the library has failed to serialize the
            data returned from paystack into the `PaystackDataModel` (pydantic model) defined by the library.
            The data that failed to be serialized is still available via `Response.raw`. You may choose to override
            the type of `Response.data` by specifying a custom pydantic model class implemented by you or inheriting
            the model from the library and overriding the faulty fields and passing the custom class via the
            `alternate_response_model` parameter of the client methods that return a Response.
            As a result of this, they type of data is either an instance  or a list of instances of the custom
            pydantic model depending on if the client method is supposed to return a list or a single resource.
        meta: Additional information about the response.
        type: In cases where the response has a status of `False` or the status code
            is an error status code. the `type` field indicates the type of error e.g. `api_error`
        code: In cases where the response has a status of `False` or the status code
            is an error status code. the `type` field indicates the type of error e.g. `api_error`
        raw: The original data returned by paystack in native python types i.e. the JSON data returned
            from paystack REST APIs have only been converted to dicts or list. This is the same data
            that is further extracted into individual fields such as `status`, `message`, `data` e.t.c
            and also serialized to pydantic models in the case of `Response.data`.
    """

    status_code: HTTPStatus
    status: bool
    message: str
    data: PaystackResponseData
    meta: dict[str, Any] | None
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
    def validate_model(self) -> Self:  # type: ignore[unused-ignore]
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
