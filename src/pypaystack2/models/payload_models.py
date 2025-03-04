from typing import Any, Optional, Literal, Self

from pydantic import BaseModel, model_validator

from pypaystack2.enums import RecipientType, Currency


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
