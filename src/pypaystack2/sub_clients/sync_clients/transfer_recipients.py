from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import (
    BaseAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import (
    Currency,
    RecipientType,
)
from pypaystack2.models import Response
from pypaystack2.models.payload_models import Recipient
from pypaystack2.models.response_models import (
    TransferRecipient,
    TransferRecipientBulkCreateData,
)
from pypaystack2.types import PaystackDataModel


class TransferRecipientClient(BaseAPIClient):
    """Provides a wrapper for paystack Transfer Receipts API

    The Transfer Recipients API allows you to create and manage beneficiaries that you send money to.
    https://paystack.com/docs/api/transfer-recipient/

    Note:
        Feature Availability
            This feature is only available to businesses in Nigeria and Ghana.
    """

    def create(
        self,
        type_: RecipientType,
        name: str,
        account_number: str,
        bank_code: str | None = None,
        description: str | None = None,
        currency: Currency | None = None,
        auth_code: str | None = None,
        metadata: dict[str, Any] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransferRecipient] | Response[PaystackDataModel]:
        """
        Creates a new recipient. A duplicate account number will lead to the
        retrieval of the existing record.

        Args:
            type_: Recipient Type. any value from the `RecipientType` enum
            name: A name for the recipient
            account_number: Required if `type` is `RecipientType.NUBAN` or `RecipientType.BASA`
            bank_code: Required if `type` is `RecipientType.NUBAN` or `RecipientType.BASA`.
                You can get the list of Bank Codes by calling the `PaystackClient.get_banks`.
            description: description
            currency: currency
            auth_code: auth code
            metadata: metadata
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
        if type_ == RecipientType.NUBAN or type_ == RecipientType.BASA:
            if bank_code is None:
                raise ValueError(
                    "`bank_code` is required if type is `RecipientType.NUBAN` or `RecipientType.BASA`"
                )

        url = self._full_url("/transferrecipient")

        payload = {
            "type": type_,
            "name": name,
            "account_number": account_number,
        }
        optional_params = [
            ("bank_code", bank_code),
            ("description", description),
            ("currency", currency),
            ("authorization_code", auth_code),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or TransferRecipient,
        )

    def bulk_create(
        self,
        batch: list[Recipient],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransferRecipientBulkCreateData] | Response[PaystackDataModel]:
        """
        Create multiple transfer recipients in batches. A duplicate account
        number will lead to the retrieval of the existing record.

        Args:
            batch: recipients to be created.
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
        batch_data = [item.model_dump() for item in batch]

        url = self._full_url("/transferrecipient/bulk")

        payload = {
            "batch": batch_data,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class
            or TransferRecipientBulkCreateData,
        )

    def get_transfer_recipients(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[TransferRecipient]] | Response[PaystackDataModel]:
        """Fetch transfer recipients available on your integration

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing transfer recipients
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
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
        url = self._full_url(f"/transferrecipient?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TransferRecipient,
        )

    def get_transfer_recipient(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransferRecipient] | Response[PaystackDataModel]:
        """Fetch the details of a transfer recipient

        Args:
            id_or_code: An ID or code for the recipient whose details you want to receive.
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
        url = self._full_url(f"/transferrecipient/{id_or_code}")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TransferRecipient,
        )

    def update(
        self,
        id_or_code: int | str,
        name: str,
        email: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """
        Update an existing recipient. A duplicate account number will lead
        to the retrieval of the existing record.

        Args:
            id_or_code: Transfer Recipient's ID or code
            name: A name for the recipient
            email: Email address of the recipient
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

        url = self._full_url(f"/transferrecipient/{id_or_code}")
        payload = {"name": name}
        optional_params = [("email", email)]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def delete(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Deletes a transfer recipient (sets the transfer recipient to inactive)

        Args:
            id_or_code: An ID or code for the recipient who you want to delete.
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

        url = self._full_url(f"/transferrecipient/{id_or_code}")
        return self._handle_request(  # type: ignore
            HTTPMethod.DELETE,
            url,
            response_data_model_class=alternate_model_class,
        )
