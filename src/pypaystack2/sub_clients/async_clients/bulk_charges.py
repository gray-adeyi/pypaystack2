from http import HTTPMethod

from pypaystack2.base_clients import BaseAsyncAPIClient, append_query_params
from pypaystack2.enums import Status
from pypaystack2.models import Response
from pypaystack2.models.payload_models import BulkChargeInstruction
from pypaystack2.models.response_models import BulkCharge, BulkChargeUnitCharge
from pypaystack2.types import PaystackDataModel


class AsyncBulkChargeClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Bulk Charge API

    The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.
    https://paystack.com/docs/api/bulk-charge/
    """

    async def initiate(
        self,
        body: list[BulkChargeInstruction],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[BulkCharge] | Response[PaystackDataModel]:
        """
        Send a list of dictionaries with authorization ``codes`` and ``amount``
        (in kobo if currency is NGN, pesewas, if currency is GHS, and cents,
        if currency is ZAR ) so paystack can process transactions as a batch.

        Args:
            body: A list of BulkChargeInstruction.
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
                by paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url("/bulkcharge")
        payload = [item.model_dump() for item in body]
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or BulkCharge,
        )

    async def get_batches(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[BulkCharge]] | Response[PaystackDataModel]:
        """This gets all bulk charge batches created by the integration.

        Args:
            page: Specify exactly what transfer you want to page. If not specified, we use a default value of 1.
            pagination: Specify how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
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

        url = self._full_url(f"/bulkcharge?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or BulkCharge,
        )

    async def get_batch(
        self,
        id_or_code: str | int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[BulkCharge] | Response[PaystackDataModel]:
        """
        This method retrieves a specific batch code. It also returns
        useful information on its progress by way of the total_charges
        and pending_charges attributes in the Response.

        Args:
            id_or_code: An ID or code for the charge whose batches you want to retrieve.
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

        url = self._full_url(f"/bulkcharge/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or BulkCharge,
        )

    async def get_charges_in_batch(
        self,
        id_or_code: str | int,
        status: Status,
        pagination: int = 50,
        page: int = 1,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[BulkChargeUnitCharge]] | Response[PaystackDataModel]:
        """
        This method retrieves the charges associated with a specified
        batch code. Pagination parameters are available. You can also
        filter by status. Charge statuses can be `Status.PENDING`,
        `Status.SUCCESS` or `Status.FAILED`.

        Args:
            id_or_code: An ID or code for the batch whose charges you want to retrieve.
            status: Any of the values from the Status enum.
            pagination: Specify how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specify exactly what transfer you want to page. If not specified we use a default value of 1.
            start_date: A timestamp from which to start listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
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

        url = self._full_url(f"/bulkcharge/{id_or_code}/charges?perPage={pagination}")
        query_params = [
            ("status", status),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or BulkChargeUnitCharge,
        )

    async def pause_batch(
        self,
        batch_code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Use this method to pause processing a batch.

        Args:
            batch_code: The batch code for the bulk charge you want to pause.
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

        url = self._full_url(f"/bulkcharge/pause/{batch_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def resume_batch(
        self,
        batch_code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Use this method to resume processing a batch

        Args:
            batch_code: The batch code for the bulk charge you want to resume.
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

        url = self._full_url(f"/bulkcharge/resume/{batch_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )
