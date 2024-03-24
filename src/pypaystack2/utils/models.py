from dataclasses import dataclass
from typing import Any, Optional, Union, NamedTuple

from pypaystack2.utils.enums import RecipientType


@dataclass
class BulkChargeInstruction:
    """A dataclass for bulk charge instruction.

    Attributes:
        authorization: The authorization code of the customer you want to charge.
        amount: The amount you want to charge.
        reference: The transaction reference.
    """

    authorization: str
    amount: int
    reference: str

    @property
    def dict(self) -> dict:
        """Converts a BulkChargeInstruction to a dictionary"""
        return {
            "authorization": self.authorization,
            "amount": self.amount,
            "reference": self.reference,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "BulkChargeInstruction":
        """Creates a BulkChargeInstruction from a dictionary.

        The dictionary has to have the following keys: `authorization`, `amount`, `reference`
        """
        return cls(
            authorization=value["authorization"],
            amount=value["amount"],
            reference=value["reference"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["BulkChargeInstruction"]:
        """Creates a list of BulkChargeInstruction from a list of dictionaries.

        The dictionaries must have the following keys: `authorization`, `amount`, `reference`
        """
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
    """A dataclass for LineItem.

    Attributes:
        name: The name of the product.
        amount: The price of the product.
        quantity: The quantity.
    """

    name: str
    amount: int
    quantity: int

    @property
    def dict(self) -> dict:
        """Converts a LineItem to a dictionary"""
        return {
            "name": self.name,
            "amount": self.amount,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "LineItem":
        """Creates a LineItem from a dictionary.

        The dictionary has to have the following keys: `name`, `amount`, `quantity`
        """
        return cls(
            name=value["authorization"],
            amount=value["amount"],
            quantity=value["quantity"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["LineItem"]:
        """Creates a list of LineItem from a list of dictionaries.

        The dictionary has to have the following keys: `name`, `amount`, `quantity`
        """
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
    """A dataclass for Tax.

    Attributes:
        name: The name of the tax.
        amount: The price of the tax.
    """

    name: str
    amount: int

    @property
    def dict(self) -> dict:
        """Converts a Tax to a dictionary"""
        return {
            "name": self.name,
            "amount": self.amount,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "Tax":
        """Creates a Tax from a dictionary.

        The dictionary has to have the following keys: `name`, `amount`
        """
        return cls(
            name=value["name"],
            amount=value["amount"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["Tax"]:
        """Creates a list of Tax from a list of dictionaries.

        The dictionary has to have the following keys: `name`, `amount`
        """
        return [
            cls(
                name=item["name"],
                amount=item["amount"],
            )
            for item in values
        ]


@dataclass
class SplitAccount:
    """A dataclass for SplitAccount.

    Attributes:
        subaccount: The id of the sub account.
        share: The share of the split account the sub account should have.
    """

    subaccount: str
    share: Union[int, float]

    @property
    def dict(self) -> dict:
        """Converts a SplitAccount to a dictionary"""
        return {
            "subaccount": self.subaccount,
            "share": self.share,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "SplitAccount":
        """Creates a SplitAccount from a dictionary.

        The dictionary has to have the following keys: `subaccount`, `share`
        """
        return cls(
            subaccount=value["subaccount"],
            share=value["share"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["SplitAccount"]:
        """Creates a list of SplitAccount from a list of dictionaries.

        The dictionary has to have the following keys: `subaccount`, `share`
        """
        return [
            cls(
                subaccount=item["subaccount"],
                share=item["share"],
            )
            for item in values
        ]


@dataclass
class Recipient:
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

    @property
    def dict(self) -> dict:
        """Converts a Recipient to a dictionary"""
        return {
            "type": self.type,
            "name": self.name,
            "bank_code": self.bank_code,
            "account_number": self.account_number,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "Recipient":
        """Creates a Recipient from a dictionary.

        The dictionary has to have the following keys: `type`, `name`, `bank_code`, `account_number`
        """
        return cls(
            type=value["type"],
            name=value["name"],
            bank_code=value["bank_code"],
            account_number=value["account_number"],
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["Recipient"]:
        """Creates a list of SplitAccount from a list of dictionaries.

        The dictionary has to have the following keys: `type`, `name`, `bank_code`, `account_number`
        """
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

    @property
    def dict(self) -> dict:
        """Converts a TransferInstruction to a dictionary"""
        return {
            "amount": self.amount,
            "reference": self.reference,
            "recipient": self.recipient,
            "reason": self.reason,
        }

    @classmethod
    def from_dict(cls, value: dict) -> "TransferInstruction":
        """Creates a TransferInstruction from a dictionary.

        The dictionary has to have the following keys: `amount`, `reference`, `recipient`, `reason`
        """
        return cls(
            amount=value["amount"],
            reference=value.get("reference"),
            recipient=value["recipient"],
            reason=value.get("reason"),
        )

    @classmethod
    def from_dict_many(cls, values: list[dict]) -> list["TransferInstruction"]:
        """Creates a list of TransferInstruction from a list of dictionaries.

        The dictionary has to have the following keys: `amount`, `reference`, `recipient`, `reason`
        """
        return [
            cls(
                amount=item["amount"],
                reference=item.get("reference"),
                recipient=item["recipient"],
                reason=item.get("reason"),
            )
            for item in values
        ]


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
