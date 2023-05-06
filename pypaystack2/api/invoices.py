from typing import Any, Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    Currency,
    HTTPMethod,
    add_to_payload,
    InvoiceStatus,
    append_query_params,
    validate_amount, Response,
)


class Invoice(BaseAPI):
    """Provides a wrapper for paystack Invoices API

    The Invoices API allows you to issue out and manage payment requests.
    https://paystack.com/docs/api/#invoice
    """

    def create(
        self,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[dict[str, Any]]] = None,
        tax: Optional[list[dict[str, Any]]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        has_invoice: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
        """Create an invoice for payment on your integration

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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/paymentrequest")

        payload = {"customer": customer, "amount": amount}
        optional_params = [
            ("due_date", due_date),
            ("description", description),
            ("line_items", line_items),
            ("tax", tax),
            ("currency", currency),
            ("send_notification", send_notification),
            ("draft", draft),
            ("has_invoice", has_invoice),
            ("invoice_number", invoice_number),
            ("split_code", split_code),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_invoices(
        self,
        customer: str,
        status: InvoiceStatus,
        currency: Currency,
        include_archive=False,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetches the invoice available on your integration.

        Args:
            customer: Filter by customer ID
            status: Filter by invoice status. Any value from enum of ``InvoiceStatus``
            currency: Filter by currency. Any value from enum of ``Currency``
            include_archive: Show archived invoices.
            page: Specify exactly what invoice you want to page. If not specify we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page. If not specified
                we use a default value of 50.
            start_date: A timestamp from which to start listing invoice e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing invoice e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest?perPage={pagination}")
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
        return self._handle_request(HTTPMethod.GET, url)

    def get_invoice(self, id_or_code: str) -> Response:
        """Get details of an invoice on your integration.

        Args:
            id_or_code: The invoice ID or code you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/{id_or_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def verify_invoice(self, code: str) -> Response:
        """Verify details of an invoice on your integration.

        Args:
            code: Invoice code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/verify/{code}")
        return self._handle_request(HTTPMethod.GET, url)

    def send_notification(self, code: str) -> Response:
        """Send notification of an invoice to your customers

        Args:
            code: Invoice code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/notify/{code}")
        return self._handle_request(HTTPMethod.POST, url)

    def get_total(self) -> Response:
        """Get invoice metrics for dashboard

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/paymentrequest/totals")
        return self._handle_request(HTTPMethod.GET, url)

    def finalize_invoice(self, code: str) -> Response:
        """Finalize a Draft Invoice

        Args:
            code: Invoice Code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/finalize/{code}")
        return self._handle_request(HTTPMethod.POST, url)

    def update_invoice(
        self,
        id_or_code: str,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[dict[str, Any]]] = None,
        tax: Optional[list[dict[str, Any]]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
        """Update an invoice details on your integration

        Args:
            id_or_code: Invoice ID or slug
            customer: Customer id or code
            amount: Payment request amount. Only useful if line items and tax values are ignored.
                method will throw a friendly warning in the response if neither is available.
            due_date: ISO 8601 representation of request due date
            description: A short description of the payment request
            line_items: List of line items in the format [{"name":"item 1", "amount":2000}]
            tax: List of taxes to be charged in the format [{"name":"VAT", "amount":2000}]
            currency: Specify the currency of the invoice. Any value from the ``Currency`` enum
            send_notification: Indicates whether Paystack sends an email notification to customer. Defaults to ``True``
            draft: Indicate if request should be saved as draft. Defaults to false and overrides send_notification
            invoice_number: Numeric value of invoice. Invoice will start from 1 and auto increment from there.
                This field is to help override whatever value Paystack decides. Auto increment for
                subsequent invoices continue from this point.
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)

        url = self._parse_url(f"/paymentrequest/{id_or_code}")
        payload = {
            "customer": customer,
            "amount": amount,
        }
        optional_params = [
            ("due_date", due_date),
            ("description", description),
            ("line_items", line_items),
            ("tax", tax),
            ("currency", currency),
            ("send_notification", send_notification),
            ("draft", draft),
            ("invoice_number", invoice_number),
            ("split_code", split_code),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.PUT, url, payload)

    def archive_invoice(self, code: str) -> Response:
        """Used to archive an invoice. Invoice will no longer be fetched
        on list or returned on verify.

        Args:
        code: Invoice ID

         Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/archive/{code}")
        return self._handle_request(HTTPMethod.POST, url)


class AsyncInvoice(BaseAsyncAPI):
    """Provides a wrapper for paystack Invoices API

    The Invoices API allows you to issue out and manage payment requests.
    https://paystack.com/docs/api/#invoice
    """

    async def create(
        self,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[dict[str, Any]]] = None,
        tax: Optional[list[dict[str, Any]]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        has_invoice: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
        """Create an invoice for payment on your integration

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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/paymentrequest")

        payload = {"customer": customer, "amount": amount}
        optional_params = [
            ("due_date", due_date),
            ("description", description),
            ("line_items", line_items),
            ("tax", tax),
            ("currency", currency),
            ("send_notification", send_notification),
            ("draft", draft),
            ("has_invoice", has_invoice),
            ("invoice_number", invoice_number),
            ("split_code", split_code),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_invoices(
        self,
        customer: str,
        status: InvoiceStatus,
        currency: Currency,
        include_archive=False,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetches the invoice available on your integration.

        Args:
            customer: Filter by customer ID
            status: Filter by invoice status. Any value from enum of ``InvoiceStatus``
            currency: Filter by currency. Any value from enum of ``Currency``
            include_archive: Show archived invoices.
            page: Specify exactly what invoice you want to page. If not specify we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page. If not specified
                we use a default value of 50.
            start_date: A timestamp from which to start listing invoice e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing invoice e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest?perPage={pagination}")
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
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_invoice(self, id_or_code: str) -> Response:
        """Get details of an invoice on your integration.

        Args:
            id_or_code: The invoice ID or code you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/{id_or_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def verify_invoice(self, code: str) -> Response:
        """Verify details of an invoice on your integration.

        Args:
            code: Invoice code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/verify/{code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def send_notification(self, code: str) -> Response:
        """Send notification of an invoice to your customers

        Args:
            code: Invoice code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/notify/{code}")
        return await self._handle_request(HTTPMethod.POST, url)

    async def get_total(self) -> Response:
        """Get invoice metrics for dashboard

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/paymentrequest/totals")
        return await self._handle_request(HTTPMethod.GET, url)

    async def finalize_invoice(self, code: str) -> Response:
        """Finalize a Draft Invoice

        Args:
            code: Invoice Code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/finalize/{code}")
        return await self._handle_request(HTTPMethod.POST, url)

    async def update_invoice(
        self,
        id_or_code: str,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[dict[str, Any]]] = None,
        tax: Optional[list[dict[str, Any]]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
        """Update an invoice details on your integration

        Args:
            id_or_code: Invoice ID or slug
            customer: Customer id or code
            amount: Payment request amount. Only useful if line items and tax values are ignored.
                method will throw a friendly warning in the response if neither is available.
            due_date: ISO 8601 representation of request due date
            description: A short description of the payment request
            line_items: List of line items in the format [{"name":"item 1", "amount":2000}]
            tax: List of taxes to be charged in the format [{"name":"VAT", "amount":2000}]
            currency: Specify the currency of the invoice. Any value from the ``Currency`` enum
            send_notification: Indicates whether Paystack sends an email notification to customer. Defaults to ``True``
            draft: Indicate if request should be saved as draft. Defaults to false and overrides send_notification
            invoice_number: Numeric value of invoice. Invoice will start from 1 and auto increment from there.
                This field is to help override whatever value Paystack decides. Auto increment for
                subsequent invoices continue from this point.
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)

        url = self._parse_url(f"/paymentrequest/{id_or_code}")
        payload = {
            "customer": customer,
            "amount": amount,
        }
        optional_params = [
            ("due_date", due_date),
            ("description", description),
            ("line_items", line_items),
            ("tax", tax),
            ("currency", currency),
            ("send_notification", send_notification),
            ("draft", draft),
            ("invoice_number", invoice_number),
            ("split_code", split_code),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def archive_invoice(self, code: str) -> Response:
        """Used to archive an invoice. Invoice will no longer be fetched
        on list or returned on verify.

        Args:
        code: Invoice ID

         Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/archive/{code}")
        return await self._handle_request(HTTPMethod.POST, url)
