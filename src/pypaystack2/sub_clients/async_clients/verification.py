from http import HTTPMethod

from pypaystack2.base_clients import BaseAsyncAPIClient
from pypaystack2.enums import AccountType, Country, Document
from pypaystack2.models import Response
from pypaystack2.models.response_models import (
    BankAccountInfo,
    AccountVerificationInfo,
    CardBin,
)
from pypaystack2.types import PaystackDataModel


class AsyncVerificationClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Verification API

    The Verification API allows you to perform KYC processes.
    https://paystack.com/docs/api/verification/

    Note:
        This feature is only available to businesses in Nigeria.
    """

    async def resolve_account_number(
        self,
        account_number: str,
        bank_code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[BankAccountInfo] | Response[PaystackDataModel]:
        """Confirm an account belongs to the right customer

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria.

        Args:
            account_number: Account Number
            bank_code: You can get the list of bank codes by calling
                `PaystackClient.miscellaneous.get_banks` method.
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(
            f"/bank/resolve?account_number={account_number}&bank_code={bank_code}"
        )
        return await self._handle_request(
            HTTPMethod.GET,
            url,  # type: ignore
            response_data_model_class=alternate_model_class or BankAccountInfo,
        )

    async def validate_account(
        self,
        account_name: str,
        account_number: str,
        account_type: AccountType,
        bank_code: str,
        country_code: Country,
        document_type: Document,
        document_number: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[AccountVerificationInfo] | Response[PaystackDataModel]:
        """Confirm the authenticity of a customer's account number before sending money

        Args:
            account_name: Customer's first and last name registered with their bank
            account_number: Customer's account number
            account_type: bank_code: The bank code of the customer’s bank. You can fetch the bank codes by
                using `PaystackClient.miscellaneous.get_banks` method.
            bank_code: The bank code of the customer’s bank
            country_code: Any value from the ``Country`` enum
            document_type: Customer’s mode of identity. any value from the
                ``Document`` enum.
            document_number: Customer’s mode of identity number
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        payload = {
            "account_name": account_name,
            "account_number": account_number,
            "account_type": account_type,
            "bank_code": bank_code,
            "country_code": country_code,
            "document_type": document_type,
            "document_number": document_number,
        }
        url = self._full_url("/bank/validate")

        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,  # type: ignore
            response_data_model_class=alternate_model_class or AccountVerificationInfo,
        )

    async def resolve_card_bin(
        self,
        bin_: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[CardBin] | Response[PaystackDataModel]:
        """Get more information about a customer's card

        Args:
            bin_: First 6 characters of card
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.


        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/decision/bin/{bin_}")
        return await self._handle_request(
            HTTPMethod.GET,
            url,  # type: ignore
            response_data_model_class=alternate_model_class or CardBin,
        )
