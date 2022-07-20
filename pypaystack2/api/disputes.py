from typing import Optional

from ..baseapi import BaseAPI
from ..utils import (
    DisputeStatus,
    Resolution,
    add_to_payload,
    append_query_params,
    validate_amount,
)


class Dispute(BaseAPI):
    """
    The Disputes API allows you manage
     transaction disputes on your integration
    """

    def get_disputes(
        self,
        start_date: str,
        end_date: int,
        pagination=50,
        page=1,
        status: Optional[DisputeStatus] = None,
    ):
        """ """
        url = self._url(f"/dispute?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_dispute(self, id: str):
        url = self._url(f"/dispute/{id}")
        return self._handle_request("GET", url)

    def get_transaction_disputes(self, id: str):
        url = self._url(f"/dispute/transaction/{id}")
        return self._handle_request("GET", url)

    def update_dispute(
        self, id: str, refund_amount: int, uploaded_filename: Optional[str]
    ):
        refund_amount = validate_amount(refund_amount)
        payload = {"refund_amount": refund_amount}
        payload = add_to_payload([("uploaded_filename", uploaded_filename)], payload)
        url = self._url(f"/dispute/{id}")
        return self._handle_request("PUT", url, payload)

    def add_evidence(
        self,
        id: str,
        customer_email: str,
        customer_name: str,
        customer_phone: str,
        service_details: str,
        delivery_address: Optional[str] = None,
        delivery_date: Optional[str] = None,
    ):
        """ """
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
        url = self._url(f"dispute/{id}/evidence")
        return self._handle_request("POST", url, payload)

    def get_upload_URL(self, id: str, upload_filename: str):
        """ """
        url = self._url(f"/dispute/{id}/upload_url?upload_filename={upload_filename}")
        return self._handle_request("GET", url)

    def resolve_dispute(
        self,
        id: str,
        resolution: Resolution,
        message: str,
        refund_amount: int,
        uploaded_filename: str,
        evidence: Optional[int] = None,
    ):
        """ """
        refund_amount = validate_amount(refund_amount)
        payload = {
            "resolution": resolution,
            "message": message,
            "refund_amount": refund_amount,
            "uploaded_filename": uploaded_filename,
        }
        payload = add_to_payload([("evidence", evidence)], payload)
        url = self._url(f"/dispute/{id}/resolve")
        return self._handle_request("PUT", url, payload)

    def export_disputes(
        self,
        start_date: str,
        end_date: str,
        pagination=50,
        page=1,
        transaction: Optional[str] = None,
        status: Optional[DisputeStatus] = None,
    ):
        """ """

        url = self._url(f"/dispute/export?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)
