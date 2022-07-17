from typing import Mapping, Optional

from pkg_resources import split_sections

from pypaystack2.errors import InvalidDataError
from .baseapi import BaseAPI
from . import utils
from .utils import (
    Currency,
    InvoiceStatus,
    add_to_payload,
    append_query_params,
    validate_amount,
)


class Invoice(BaseAPI):
    """
    The Invoices API allows you
    issue out and manage payment requests
    """

    def create(
        self,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        line_items: Optional[list[Mapping]] = None,
        tax: Optional[list[Mapping]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        has_invoice: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ):
        """ """

        url = self._url("/paymentrequest")

        payload = {"customer": customer, "amount": amount}
        optional_params = [
            ("due_date", due_date),
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
    ):
        """ """
        if include_archive:
            _include_archive = "true"
        else:
            _include_archive = "false"

        url = self._url(f"/paymentrequest?perPage={pagination}")
        query_params = [
            ("customer", customer),
            ("status", status),
            ("currency", currency),
            ("include_archive", _include_archive),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_invoice(self, id_or_code: str):
        """ """
        url = self._url(f"/paymentrequest/{id_or_code}")
        return self._handle_request("GET", url)

    def verify_invoice(self, code: str):
        """ """
        url = self._url(f"/paymentrequest/verify/{code}")
        return self._handle_request("GET", url)

    def send_notification(self, code: str):
        """ """
        url = self._url(f"/paymentrequest/notify/{code}")
        return self._handle_request("POST", url)

    def get_total(self):
        """ """
        url = self._url(f"/paymentrequest/totals")
        return self._handle_request("GET", url)

    def finalize_invoice(self, code: str):
        """ """
        url = self._url(f"/paymentrequest/finalize/{code}")
        return self._handle_request("POST", url)

    def update_invoice(
        self,
        id_or_code: str,
        customer: str,
        amount: int,
        due_date: Optional[str] = None,
        description: Optional[str] = None,
        line_items: Optional[list[Mapping]] = None,
        tax: Optional[list[Mapping]] = None,
        currency: Optional[Currency] = None,
        send_notification: Optional[bool] = None,
        draft: Optional[bool] = None,
        invoice_number: Optional[int] = None,
        split_code: Optional[str] = None,
    ):
        """ """
        amount = validate_amount(amount)

        url = self._url(f"/paymentrequest/{id_or_code}")
        payload = {
            "customer": customer,
            "amount": amount,
        }
        optional_params = [
            ("due_date", amount),
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
        """ """
        url = self._url(f"/paymentrequest/archive/{code}")
        return self._handle_request("POST", url)
