from typing import Optional

from ..baseapi import BaseAPI, Response
from ..utils import (
    DisputeStatus,
    Resolution,
    add_to_payload,
    append_query_params,
    validate_amount,
)


class Dispute(BaseAPI):
    """Provides a wrapper for paystack Disputes API

    The Disputes API allows you manage transaction disputes on your integration.
    https://paystack.com/docs/api/#dispute
    """

    def get_disputes(
        self,
        start_date: str,
        end_date: str,
        pagination=50,
        page=1,
        transaction: Optional[str] = None,
        status: Optional[DisputeStatus] = None,
    ) -> Response:
        """Fetches disputes filed against you

        Parameters
        ----------
        start_date: str
            A timestamp from which to start listing dispute e.g. 2016-09-21
        end_date: str
            A timestamp at which to stop listing dispute e.g. 2016-09-21
        pagination : int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        page: int
            Specify exactly what dispute you want to page.
            If not specify we use a default value of 1.
        transaction: Optional[str]
            Transaction Id
        status: Optional[DisputeStatus]
            Any of DisputeStatus enum values.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/dispute?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_dispute(self, id: str) -> Response:
        """Get more details about a dispute.

        Parameters
        ----------
        id: str
            The dispute ID you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/dispute/{id}")
        return self._handle_request("GET", url)

    def get_transaction_disputes(self, id: str) -> Response:
        """This method retrieves disputes for a particular transaction

        Parameters
        ----------
        id: str
            The transaction ID you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/dispute/transaction/{id}")
        return self._handle_request("GET", url)

    def update_dispute(
        self, id: str, refund_amount: int, uploaded_filename: Optional[str]
    ) -> Response:
        """Update details of a dispute on your integration

        Parameters
        ----------
        id: str
            Dispute ID
        refund_amount: int
            the amount to refund, in kobo if currency is NGN, pesewas,
            if currency is GHS, and cents, if currency is ZAR
        uploaded_filename: Optional[str]
            filename of attachment returned via response from
            upload url(GET /dispute/:id/upload_url)

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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
    ) -> Response:
        """Provide evidence for a dispute

        Parameters
        ----------
        id: str
            Dispute ID
        customer_email: str
            Customer email
        customer_name: str
            Customer name
        customer_phone: str
            Customer phone
        service_details: str
            Details of service involved
        delivery_address: Optional[str]
            Delivery Address
        delivery_date: Optional[str]
            ISO 8601 representation of delivery date (YYYY-MM-DD)

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
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
        url = self._url(f"dispute/{id}/evidence")
        return self._handle_request("POST", url, payload)

    def get_upload_URL(self, id: str, upload_filename: str) -> Response:
        """Get URL to upload a dispute evidence.

        Parameters
        ----------
        id: str
            Dispute Id
        upload_filename: str
            The file name, with its extension, that you want to upload. e.g filename.pdf

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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
    ) -> Response:
        """Resolve a dispute on your integration

        Parameters
        ----------
        id: str
            Dispute ID
        resolution: Resolution
            Any of the Resolution enum value.
        message: str
            Reason for resolving
        refund_amount: int
            the amount to refund, in kobo if currency is NGN,
            pesewas, if currency is GHS, and cents, if currency is ZAR
        uploaded_filename: str
            filename of attachment returned via response from
            upload url(GET /dispute/:id/upload_url)
        evidence: Optional[int]
            Evidence Id for fraud claims

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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
    ) -> Response:
        """Export disputes available on your integration.

        Parameters
        ----------
        start_date: str
            A timestamp from which to start listing dispute e.g. 2016-09-21
        end_date: str
            A timestamp at which to stop listing dispute e.g. 2016-09-21
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        page: int
            Specify exactly what dispute you want to page.
            If not specify we use a default value of 1.
        transaction: Optional[str]
            Transaction Id
        status: Optional[DisputeStatus]
            Any value from the DisputeStatus enum

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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
