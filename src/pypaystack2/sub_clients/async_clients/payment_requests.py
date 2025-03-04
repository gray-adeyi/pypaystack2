from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Currency, Status
from pypaystack2.models import Response
from pypaystack2.models.payload_models import LineItem, Tax
from pypaystack2.models.response_models import PaymentRequest, PaymentRequestStat
from pypaystack2.types import PaystackDataModel


class AsyncPaymentRequestClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Payment Requests API

    The Payment Requests API allows you to manage requests for payment of goods and services.
    https://paystack.com/docs/api/payment-request/
    """

    async def create(
        self,
        customer: int | str,
        amount: int,
        due_date: str | None = None,
        description: str | None = None,
        line_items: list[LineItem] | None = None,
        tax: list[Tax] | None = None,
        currency: Currency | None = None,
        send_notification: bool | None = None,
        draft: bool | None = None,
        has_invoice: bool | None = None,
        invoice_number: int | None = None,
        split_code: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentRequest] | Response[PaystackDataModel]:
        """Create a payment request for a transaction on your integration

        Args:
            customer: Customer id or code
            amount: Payment request amount. It should be used when line items and tax values aren't specified.
            due_date: ISO 8601 representation of request due date
            description: A short description of the payment request
            line_items: List of line items int the format [{"name":"item 1", "amount":2000, "quantity": 1}]
            tax: List of taxes to be charged in the format [{"name":"VAT", "amount":2000}]
            currency: Any value from Currency enum. default ``Currency.NGN``
            send_notification: Indicates whether Paystack sends an email notification to customer. Defaults to ``True``
            draft: Indicate if request should be saved as draft. Defaults to ``False`` and overrides send_notification
            has_invoice: Set to ``True`` to create a draft invoice (adds an auto incrementing invoice number
                if none is provided) even if there are no line_items or tax passed
            invoice_number: Numeric value of invoice. Invoice will start from 1 and auto increment from there.
                This field is to help override whatever value Paystack decides. Auto increment for
                subsequent invoices continue from this point.
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w
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
        _line_items: list[dict[str, Any]] | None = None
        _tax: list[dict[str, Any]] | None = None
        if line_items:
            _line_items = [item.model_dump() for item in line_items]
        if tax:
            _tax = [unit_tax.model_dump() for unit_tax in tax]

        url = self._full_url("/paymentrequest")

        payload = {"customer": customer, "amount": amount}
        optional_params = [
            ("due_date", due_date),
            ("description", description),
            ("line_items", _line_items),
            ("tax", _tax),
            ("currency", currency),
            ("send_notification", send_notification),
            ("draft", draft),
            ("has_invoice", has_invoice),
            ("invoice_number", invoice_number),
            ("split_code", split_code),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or PaymentRequest,
        )

    async def get_payment_requests(
        self,
        customer: str | int | None = None,
        status: Status | None = None,
        currency: Currency | None = None,
        include_archive: bool = False,
        page: int = 1,
        pagination: int = 50,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[PaymentRequest]] | Response[PaystackDataModel]:
        """Fetches the payment requests available on your integration.

        Args:
            customer: Filter by customer ID
            status: Filter by payment request status. Any value from enum of ``Status``
            currency: Filter by currency. Any value from enum of ``Currency``
            include_archive: Show archived payment requests.
            page: Specify exactly what payment request you want to page. If not specify we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page. If not specified
                we use a default value of 50.
            start_date: A timestamp from which to start listing payment request
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing payment request e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
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

        url = self._full_url(f"/paymentrequest?perPage={pagination}")
        query_params = [
            ("customer", customer),
            ("status", status),
            ("currency", currency),
            ("include_archive", include_archive),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaymentRequest,
        )

    async def get_payment_request(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentRequest] | Response[PaystackDataModel]:
        """Get details of a payment request on your integration.

        Args:
            id_or_code: Payment Request id or code
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

        url = self._full_url(f"/paymentrequest/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaymentRequest,
        )

    async def verify(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentRequest] | Response[PaystackDataModel]:
        """Verify details of a payment request on your integration.

        Args:
            id_or_code: Payment Request id or code
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

        url = self._full_url(f"/paymentrequest/verify/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaymentRequest,
        )

    async def send_notification(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Send notification of a payment request to your customers

        Args:
            id_or_code: Payment Request id or code
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

        url = self._full_url(f"/paymentrequest/notify/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def get_total(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentRequestStat] | Response[PaystackDataModel]:
        """Get payment requests metric

        Args:
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

        url = self._full_url("/paymentrequest/totals")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaymentRequestStat,
        )

    async def finalize(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentRequest] | Response[PaystackDataModel]:
        """Finalize a draft payment request

        Args:
            id_or_code: Payment Request id or code
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

        url = self._full_url(f"/paymentrequest/finalize/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class or PaymentRequest,
        )

    async def update(
        self,
        id_or_code: int | str,
        customer: int | str,
        amount: int,
        due_date: str | None = None,
        description: str | None = None,
        line_items: list[LineItem] | None = None,
        tax: list[Tax] | None = None,
        currency: Currency | None = None,
        send_notification: bool | None = None,
        draft: bool | None = None,
        invoice_number: int | None = None,
        split_code: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentRequest] | Response[PaystackDataModel]:
        """Update a payment request details on your integration

        Args:
            id_or_code: Payment Request id or code
            customer: Customer id or code
            amount: Payment request amount. Only useful if line items and tax values are ignored.
                method will throw a friendly warning in the response if neither is available.
            due_date: ISO 8601 representation of request due date
            description: A short description of the payment request
            line_items: List of line items in the format [{"name":"item 1", "amount":2000}]
            tax: List of taxes to be charged in the format [{"name":"VAT", "amount":2000}]
            currency: Specify the currency of the payment request. Any value from the ``Currency`` enum
            send_notification: Indicates whether Paystack sends an email notification to customer. Defaults to ``True``
            draft: Indicate if request should be saved as draft. Defaults to false and overrides send_notification
            invoice_number: Numeric value of invoice. Invoice will start from 1 and auto increment from there.
                This field is to help override whatever value Paystack decides. Auto increment for
                subsequent invoices continue from this point.
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w
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
        _line_items: list[dict[str, Any]] | None = None
        _tax: list[dict[str, Any]] | None = None

        if line_items:
            _line_items = [item.model_dump() for item in line_items]
        if tax:
            _tax = [unit_tax.model_dump() for unit_tax in tax]

        url = self._full_url(f"/paymentrequest/{id_or_code}")
        payload = {
            "customer": customer,
            "amount": amount,
        }
        optional_params = [
            ("due_date", due_date),
            ("description", description),
            ("line_items", _line_items),
            ("tax", _tax),
            ("currency", currency),
            ("send_notification", send_notification),
            ("draft", draft),
            ("invoice_number", invoice_number),
            ("split_code", split_code),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or PaymentRequest,
        )

    async def archive(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Used to archive a payment request. A payment request will no longer be fetched on list or returned on verify.

        Args:
            id_or_code: Payment Request id or code
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

        url = self._full_url(f"/paymentrequest/archive/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )
