from typing import Any, Mapping, Optional

from ..baseapi import BaseAPI, Response
from ..utils import (
    Currency,
    InvoiceStatus,
    add_to_payload,
    append_query_params,
    validate_amount,
)


class Invoice(BaseAPI):
    """Provides a wrapper for paystack Invoices API

    The Invoices API allows you issue out and manage payment requests.
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

        Parameters
        ----------
        customer: str
            Customer id or code
        amount: int
            Payment request amount. It should be used when line items and
            tax values aren't specified.
        due_date: Optional[str]
            ISO 8601 representation of request due date
        description: Optional[str]
            A short description of the payment request
        line_items: Optional[list[dict[str,Any]]]
            List of line items int the format [{"name":"item 1", "amount":2000, "quantity": 1}]
        tax: Optional[list[dict[str,Any]]]
            List of taxes to be charged in the format [{"name":"VAT", "amount":2000}]
        currency: Optional[Currency]
            Any value from Currency enum. default ``Currency.NGN``
        send_notification: Optional[bool]
            Indicates whether Paystack sends an email notification to customer. Defaults to ``True``
        draft: Optional[bool]
            Indicate if request should be saved as draft. Defaults to ``False`` and overrides
            send_notification
        has_invoice: Optional[bool]
            Set to ``True`` to create a draft invoice (adds an auto incrementing invoice number
            if none is provided) even if there are no line_items or tax passed
        invoice_number: Optional[int]
            Numeric value of invoice. Invoice will start from 1 and auto increment from there.
            This field is to help override whatever value Paystack decides. Auto increment for
            subsequent invoices continue from this point.
        split_code: Optional[str]
            The split code of the transaction split. e.g. SPL_98WF13Eb3w

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/paymentrequest")

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
        return self._handle_request("POST", url, payload)

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

        Parameters
        ----------
        customer: str
            Filter by customer ID
        status: InvoiceStatus
            Filter by invoice status. Any value from enum of ``InvoiceStatus``
        currency: Currency
            Filter by currency. Any value from enum of ``Currency``
        include_archive: bool
            Show archived invoices.
        page: int
            Specify exactly what invoice you want to page. If not specify we use a
            default value of 1.
        pagination: int
            Specify how many records you want to retrieve per page. If not specify
            we use a default value of 50.
        start_date: Optional[str]
            A timestamp from which to start listing invoice
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing invoice
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/paymentrequest?perPage={pagination}")
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
        return self._handle_request("GET", url)

    def get_invoice(self, id_or_code: str) -> Response:
        """Get details of an invoice on your integration.

        Parameters
        ----------
        id_or_code: str
            The invoice ID or code you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/paymentrequest/{id_or_code}")
        return self._handle_request("GET", url)

    def verify_invoice(self, code: str) -> Response:
        """Verify details of an invoice on your integration.

        Parameters
        ----------
        code: str
            Invoice code

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/paymentrequest/verify/{code}")
        return self._handle_request("GET", url)

    def send_notification(self, code: str) -> Response:
        """Send notification of an invoice to your customers

        Parameters
        ----------
        code: str
            Invoice code

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/paymentrequest/notify/{code}")
        return self._handle_request("POST", url)

    def get_total(self) -> Response:
        """Get invoice metrics for dashboard

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/paymentrequest/totals")
        return self._handle_request("GET", url)

    def finalize_invoice(self, code: str) -> Response:
        """Finalize a Draft Invoice

        Parameters
        ----------
        code: str
            Invoice Code

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/paymentrequest/finalize/{code}")
        return self._handle_request("POST", url)

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
    ):
        """Update an invoice details on your integration

        Parameters
        ----------
        id_or_code: str
            Invoice ID or slug
        customer: str
            Customer id or code
        amount: int
            Payment request amount. Only useful if line items and tax values are ignored.
            method will throw a friendly warning in the response if neither is available.
        due_date: Optional[str]
            ISO 8601 representation of request due date
        description: Optional[str]
            A short description of the payment request
        line_items: Optional[list[dict[str,Any]]]
            List of line items in the format [{"name":"item 1", "amount":2000}]
        tax: Optional[list[dict[str,Any]]]
            List of taxes to be charged in the format [{"name":"VAT", "amount":2000}]
        currency: Optional[Currency]
            Specify the currency of the invoice. Any value from the ``Currency`` enum
        send_notification: Optional[bool]
            Indicates whether Paystack sends an email notification to customer. Defaults to ``True``
        draft: Optional[bool]
            Indicate if request should be saved as draft. Defaults to false and overrides
            send_notification
        invoice_number: Optional[int]
            Numeric value of invoice. Invoice will start from 1 and auto increment from there.
            This field is to help override whatever value Paystack decides. Auto increment for
            subsequent invoices continue from this point.
        split_code: Optional[str]
            The split code of the transaction split. e.g. SPL_98WF13Eb3w

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)

        url = self._url(f"/paymentrequest/{id_or_code}")
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
        return self._handle_request("PUT", url, payload)

    def archive_invoice(self, code: str):
        """Used to archive an invoice. Invoice will no longer be fetched
        on list or returned on verify.

        Parameters
        ----------
        code: str
            Invoice ID

         Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/paymentrequest/archive/{code}")
        return self._handle_request("POST", url)
