from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    Currency,
    HTTPMethod,
    add_to_payload,
    append_query_params,
    validate_amount,
    Response,
    Status,
    LineItem,
    Tax,
)


class PaymentRequest(BaseAPI):
    """Provides a wrapper for paystack Payment Requests API

    The Payment Requests API allows you to manage requests for payment of goods and services.
    https://paystack.com/docs/api/payment-request/
    """

    def create(
        self,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[LineItem]] = None,
        tax: Optional[list[Tax]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        has_invoice: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
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
            has_invoice: Set to ``True`` to create a draft invoice (adds an auto-incrementing invoice number
                if none is provided) even if there are no line_items or tax passed
            invoice_number: Numeric value of invoice. Invoice will start from 1 and auto increment from there.
                This field is to help override whatever value Paystack decides. Auto increment for
                subsequent invoices continue from this point.
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if line_items:
            line_items = [item.dict for item in line_items]
        if tax:
            tax = [unit_tax.dict for unit_tax in tax]

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

    def get_payment_requests(
        self,
        customer: Optional[str] = None,
        status: Optional[Status] = None,
        currency: Optional[Currency] = None,
        include_archive: bool = False,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetches the payment requests available on your integration.

        Args:
            customer: Filter by customer ID
            status: Filter by payment request status. Any value from enum of ``Status``
            currency: Filter by currency. Any value from enum of ``Currency``
            include_archive: Show archived payment requests.
            page: Specify exactly what payment request you want to page. If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page. If not specified,
                we use a default value of 50.
            start_date: A timestamp from which to start listing payment requests
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing payment requests e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

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

    def get_payment_request(self, id_or_code: str) -> Response:
        """Get details of a payment request on your integration

        Args:
            id_or_code: The payment request ID or code you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/{id_or_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def verify(self, code: str) -> Response:
        """Verify details of a payment request on your integration.

        Args:
            code: Payment Request id or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/verify/{code}")
        return self._handle_request(HTTPMethod.GET, url)

    def send_notification(self, id_or_code: str) -> Response:
        """Send notification of a payment request to your customers

        Args:
            id_or_code: Payment Request id or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/notify/{id_or_code}")
        return self._handle_request(HTTPMethod.POST, url)

    def get_total(self) -> Response:
        """Get payment requests metric

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/paymentrequest/totals")
        return self._handle_request(HTTPMethod.GET, url)

    def finalize(self, id_or_code: str) -> Response:
        """Finalize a draft payment request

        Args:
            id_or_code: Payment Request id or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/finalize/{id_or_code}")
        return self._handle_request(HTTPMethod.POST, url)

    def update(
        self,
        id_or_code: str,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[dict]] = None,
        tax: Optional[list[dict]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
        """Update the payment request details on your integration

        Args:
            id_or_code: Payment Request id or code
            customer: Customer id or code
            amount: Payment request amount. Only useful if line items and tax values are ignored.
                method will throw a friendly warning in the response if neither is available.
            due_date: ISO 8601 representation of request due date
            description: A short description of the payment request
            line_items: List of line items in the format [{"name":"item 1", "amount":2000}]
            tax: List of taxes to be charged in the format [{"name":"VAT", "amount":2000}]
            currency: Specify the currency of the Payment Request id or code. Any value from the ``Currency`` enum
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

    def archive(self, id_or_code: str) -> Response:
        """Used to archive a payment request. A payment request will no longer be fetched on list or returned on verify.

        Args:
            id_or_code: Payment Request id or code

         Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/archive/{id_or_code}")
        return self._handle_request(HTTPMethod.POST, url)


class AsyncPaymentRequest(BaseAsyncAPI):
    """Provides a wrapper for paystack Payment Requests API

    The Payment Requests API allows you to manage requests for payment of goods and services.
    https://paystack.com/docs/api/payment-request/
    """

    async def create(
        self,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[LineItem]] = None,
        tax: Optional[list[Tax]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        has_invoice: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        if line_items:
            line_items = [item.dict for item in line_items]
        if tax:
            tax = [unit_tax.dict for unit_tax in tax]

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

    async def get_payment_requests(
        self,
        customer: Optional[str] = None,
        status: Optional[Status] = None,
        currency: Optional[Currency] = None,
        include_archive: bool = False,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
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

    async def get_payment_request(self, id_or_code: str) -> Response:
        """Get details of a payment request on your integration.

        Args:
            id_or_code: Payment Request id or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/{id_or_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def verify(self, code: str) -> Response:
        """Verify details of a payment request on your integration.

        Args:
            code: Payment Request id or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/verify/{code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def send_notification(self, id_or_code: str) -> Response:
        """Send notification of a payment request to your customers

        Args:
            id_or_code: Payment Request id or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/notify/{id_or_code}")
        return await self._handle_request(HTTPMethod.POST, url)

    async def get_total(self) -> Response:
        """Get payment requests metric

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/paymentrequest/totals")
        return await self._handle_request(HTTPMethod.GET, url)

    async def finalize(self, id_or_code: str) -> Response:
        """Finalize a draft payment request

        Args:
            id_or_code: Payment Request id or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/finalize/{id_or_code}")
        return await self._handle_request(HTTPMethod.POST, url)

    async def update(
        self,
        id_or_code: str,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[dict]] = None,
        tax: Optional[list[dict]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ) -> Response:
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

    async def archive(self, id_or_code: str) -> Response:
        """Used to archive a payment request. A payment request will no longer be fetched on list or returned on verify.

        Args:
            id_or_code: Payment Request id or code

         Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/paymentrequest/archive/{id_or_code}")
        return await self._handle_request(HTTPMethod.POST, url)
