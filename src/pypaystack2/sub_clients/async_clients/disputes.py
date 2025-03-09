from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import DisputeStatus, Resolution
from pypaystack2.models import Response
from pypaystack2.models.response_models import (
    Dispute,
    DisputeEvidence,
    DisputeExportInfo,
    DisputeUploadInfo,
)
from pypaystack2.types import PaystackDataModel


class AsyncDisputeClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Disputes API

    The Disputes API allows you manage transaction disputes on your integration.
    https://paystack.com/docs/api/dispute/
    """

    async def get_disputes(
        self,
        start_date: str,
        end_date: str,
        pagination: int = 50,
        page: int = 1,
        transaction: str | None = None,
        status: DisputeStatus | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Dispute]] | Response[PaystackDataModel]:
        """Fetches disputes filed against you

        Args:
            start_date: A timestamp from which to start listing dispute e.g. 2016-09-21
            end_date: A timestamp at which to stop listing dispute e.g. 2016-09-21
            pagination : Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specifies exactly what dispute you want to page.
                If not specified we use a default value of 1.
            transaction: Transaction ID
            status: Any of DisputeStatus enum values.
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

        url = self._full_url(f"/dispute?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Dispute,
        )

    async def get_dispute(
        self,
        id_: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Dispute] | Response[PaystackDataModel]:
        """Get more details about a dispute.

        Args:
            id_: The dispute ID you want to fetch
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

        url = self._full_url(f"/dispute/{id_}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Dispute,
        )

    async def get_transaction_disputes(
        self,
        id_: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Dispute]] | Response[PaystackDataModel]:
        """This method retrieves disputes for a particular transaction

        Args:
            id_: The transaction ID you want to fetch
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

        url = self._full_url(f"/dispute/transaction/{id_}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Dispute,
        )

    async def update_dispute(
        self,
        id_: int | str,
        refund_amount: int,
        uploaded_filename: str | None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Dispute] | Response[PaystackDataModel]:
        """Update details of a dispute on your integration

        Args:
            id_: Dispute ID
            refund_amount: the amount to refund, in kobo if currency is NGN, pesewas,
                if currency is GHS, and cents, if currency is ZAR
            uploaded_filename: filename of attachment returned via response from upload url(GET /dispute/:id/upload_url)
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

        payload = {"refund_amount": refund_amount}
        payload = add_to_payload([("uploaded_filename", uploaded_filename)], payload)
        url = self._full_url(f"/dispute/{id_}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or Dispute,
        )

    async def add_evidence(
        self,
        id_: int | str,
        customer_email: str,
        customer_name: str,
        customer_phone: str,
        service_details: str,
        delivery_address: str | None = None,
        delivery_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DisputeEvidence] | Response[PaystackDataModel]:
        """Provide evidence for a dispute

        Args:
            id_: Dispute ID
            customer_email: Customer email
            customer_name: Customer name
            customer_phone: Customer phone
            service_details: Details of service involved
            delivery_address: Delivery Address
            delivery_date: ISO 8601 representation of delivery date (YYYY-MM-DD)
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
            "customer_email": customer_email,
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "service_details": service_details,
        }
        optional_params = [
            ("delivery_address", delivery_address),
            ("delivery_date", delivery_date),
        ]
        payload = add_to_payload(optional_params, payload)
        url = self._full_url(f"dispute/{id_}/evidence")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or DisputeEvidence,
        )

    async def get_upload_url(
        self,
        id_: int | str,
        upload_filename: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DisputeUploadInfo] | Response[PaystackDataModel]:
        """Get URL to upload a dispute evidence.

        Args:
            id_: Dispute ID
            upload_filename: The file name, with its extension, that you want to upload. e.g. filename.pdf
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
            f"/dispute/{id_}/upload_url?upload_filename={upload_filename}"
        )
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or DisputeUploadInfo,
        )

    async def resolve_dispute(
        self,
        id_: int | str,
        resolution: Resolution,
        message: str,
        refund_amount: int,
        uploaded_filename: str,
        evidence: int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Dispute] | Response[PaystackDataModel]:
        """Resolve a dispute on your integration

        Args:
            id_: Dispute ID
            resolution: Any of the Resolution enum value.
            message: Reason for resolving
            refund_amount: the amount to refund, in kobo if currency is NGN,
                pesewas, if currency is GHS, and cents, if currency is ZAR
            uploaded_filename: filename of attachment returned via response from
                upload url(GET /dispute/:id/upload_url)
            evidence: Evidence ID for fraud claims
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
            "resolution": resolution,
            "message": message,
            "refund_amount": refund_amount,
            "uploaded_filename": uploaded_filename,
        }
        payload = add_to_payload([("evidence", evidence)], payload)
        url = self._full_url(f"/dispute/{id_}/resolve")
        return await self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or Dispute,
        )

    async def export_disputes(
        self,
        start_date: str,
        end_date: str,
        pagination: int = 50,
        page: int = 1,
        transaction: str | None = None,
        status: DisputeStatus | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DisputeExportInfo] | Response[PaystackDataModel]:
        """Export disputes available on your integration.

        Args:
            start_date: A timestamp from which to start listing dispute e.g. 2016-09-21
            end_date: A timestamp at which to stop listing dispute e.g. 2016-09-21
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specifies exactly what dispute you want to page. If not specified we use a default value of 1.
            transaction: Transaction ID
            status: Any value from the DisputeStatus enum
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

        url = self._full_url(f"/dispute/export?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or DisputeExportInfo,
        )
