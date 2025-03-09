from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Currency
from pypaystack2.models import Response, TransferInstruction
from pypaystack2.models.response_models import Transfer, BulkTransferItem
from pypaystack2.types import PaystackDataModel


class AsyncTransferClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Transfers API

    The Transfers API allows you to automate sending money on your integration
    https://paystack.com/docs/api/transfer/

    Note
    ----
    This feature is only available to businesses in Nigeria and Ghana.
    """

    async def initiate(
        self,
        amount: int,
        recipient: str,
        reason: str | None = None,
        currency: Currency | None = None,
        reference: str | None = None,
        source: str = "balance",
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transfer] | Response[PaystackDataModel]:
        """Initiate transfer

        Args:
            amount: amount to transfer
            recipient: the beneficiary of the transfer
            reason: narration of the transfer
            currency: transfer currency
            reference: reference id
            source: transfer source
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

        url = self._full_url("/transfer")

        payload = {
            "amount": amount,
            "recipient": recipient,
            "source": source,
        }
        optional_params = [
            ("reason", reason),
            ("reference", reference),
            ("currency", currency),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,  # type: ignore
            response_data_model_class=alternate_model_class or Transfer,
        )

    async def finalize(
        self,
        transfer_code: str,
        otp: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transfer] | Response[PaystackDataModel]:
        """Finalize transfer

        Args:
            transfer_code: The code for transfer.
            otp: One time password.
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

        url = self._full_url("/transfer/finalize_transfer")

        payload = {
            "transfer_code": transfer_code,
            "otp": otp,
        }
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,  # type: ignore
            response_data_model_class=alternate_model_class or Transfer,
        )

    async def bulk_transfer(
        self,
        transfers: list[TransferInstruction],
        source: str = "balance",
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[BulkTransferItem]] | Response[PaystackDataModel]:
        """Transfer in bulk

        Args:
            transfers: list of transfer instructions
            source: source of the funds to transfer
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

        url = self._full_url("/transfer/bulk")

        payload = {
            "transfers": [tx.model_dump() for tx in transfers],
            "source": source,
        }
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,  # type: ignore
            response_data_model_class=alternate_model_class or BulkTransferItem,
        )

    async def get_transfers(
        self,
        page: int = 1,
        pagination: int = 50,
        customer: str | int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transfer] | Response[PaystackDataModel]:
        """Retrieve transfers made to a customer

        Args:
            customer: customer id
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing refund e.g. 2016-09-21
            end_date: A timestamp at which to stop listing refund e.g. 2016-09-21
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
        url = self._full_url(f"/transfer?perPage={pagination}")
        query_params = [
            ("customer", customer),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transfer,
        )

    async def get_transfer(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transfer] | Response[PaystackDataModel]:
        """Retrieve a transfer

        Args:
            id_or_code: transfer ID or code
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
        url = self._full_url(f"/transfer/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transfer,
        )

    async def verify(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transfer] | Response[PaystackDataModel]:
        """Verify a transfer

        Args:
            reference: str
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
        url = self._full_url(f"/transfer/verify/{reference}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transfer,
        )
