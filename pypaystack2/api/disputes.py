from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    DisputeStatus,
    append_query_params,
    HTTPMethod,
    validate_amount,
    add_to_payload,
    Resolution,
    Response,
)


class Dispute(BaseAPI):
    """Provides a wrapper for paystack Disputes API

    The Disputes API allows you to manage transaction disputes on your integration.
    https://paystack.com/docs/api/dispute/
    """

    def get_disputes(
        self,
        start_date: str,
        end_date: str,
        pagination: int = 50,
        page: int = 1,
        transaction: Optional[str] = None,
        status: Optional[DisputeStatus] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_dispute(self, id: str) -> Response:
        """Get more details about a dispute.

        Args:
            id: The dispute ID you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute/{id}")
        return self._handle_request(HTTPMethod.GET, url)

    def get_transaction_disputes(self, id: str) -> Response:
        """This method retrieves disputes for a particular transaction

        Args:
            id: The transaction ID you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute/transaction/{id}")
        return self._handle_request(HTTPMethod.GET, url)

    def update_dispute(
        self, id: str, refund_amount: int, uploaded_filename: Optional[str]
    ) -> Response:
        """Update details of a dispute on your integration

        Args:
            id: Dispute ID
            refund_amount: the amount to refund, in kobo if currency is NGN, pesewas,
                if currency is GHS, and cents, if currency is ZAR
            uploaded_filename: filename of attachment returned via response from upload url(GET /dispute/:id/upload_url)

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        refund_amount = validate_amount(refund_amount)
        payload = {"refund_amount": refund_amount}
        payload = add_to_payload([("uploaded_filename", uploaded_filename)], payload)
        url = self._parse_url(f"/dispute/{id}")
        return self._handle_request(HTTPMethod.PUT, url, payload)

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

        Args:
            id: Dispute ID
            customer_email: Customer email
            customer_name: Customer name
            customer_phone: Customer phone
            service_details: Details of service involved
            delivery_address: Delivery Address
            delivery_date: ISO 8601 representation of delivery date (YYYY-MM-DD)

        Returns:
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
        url = self._parse_url(f"dispute/{id}/evidence")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_upload_url(self, id: str, upload_filename: str) -> Response:
        """Get URL to upload a dispute evidence.

        Args:
            id: Dispute ID
            upload_filename: The file name, with its extension, that you want to upload. e.g. filename.pdf

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(
            f"/dispute/{id}/upload_url?upload_filename={upload_filename}"
        )
        return self._handle_request(HTTPMethod.GET, url)

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

        Args:
            id: Dispute ID
            resolution: Any of the Resolution enum value.
            message: Reason for resolving
            refund_amount: the amount to refund, in kobo if currency is NGN,
                pesewas, if currency is GHS, and cents, if currency is ZAR
            uploaded_filename: filename of attachment returned via response from
                upload url(GET /dispute/:id/upload_url)
            evidence: Evidence ID for fraud claims

        Returns:
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
        url = self._parse_url(f"/dispute/{id}/resolve")
        return self._handle_request(HTTPMethod.PUT, url, payload)

    def export_disputes(
        self,
        start_date: str,
        end_date: str,
        pagination: int = 50,
        page: int = 1,
        transaction: Optional[str] = None,
        status: Optional[DisputeStatus] = None,
    ) -> Response:
        """Export disputes available on your integration.

        Args:
            start_date: A timestamp from which to start listing dispute e.g. 2016-09-21
            end_date: A timestamp at which to stop listing dispute e.g. 2016-09-21
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specifies exactly what dispute you want to page. If not specified we use a default value of 1.
            transaction: Transaction ID
            status: Any value from the DisputeStatus enum

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute/export?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)


class AsyncDispute(BaseAsyncAPI):
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
        transaction: Optional[str] = None,
        status: Optional[DisputeStatus] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_dispute(self, id: str) -> Response:
        """Get more details about a dispute.

        Args:
            id: The dispute ID you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute/{id}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_transaction_disputes(self, id: str) -> Response:
        """This method retrieves disputes for a particular transaction

        Args:
            id: The transaction ID you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute/transaction/{id}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update_dispute(
        self, id: str, refund_amount: int, uploaded_filename: Optional[str]
    ) -> Response:
        """Update details of a dispute on your integration

        Args:
            id: Dispute ID
            refund_amount: the amount to refund, in kobo if currency is NGN, pesewas,
                if currency is GHS, and cents, if currency is ZAR
            uploaded_filename: filename of attachment returned via response from upload url(GET /dispute/:id/upload_url)

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        refund_amount = validate_amount(refund_amount)
        payload = {"refund_amount": refund_amount}
        payload = add_to_payload([("uploaded_filename", uploaded_filename)], payload)
        url = self._parse_url(f"/dispute/{id}")
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def add_evidence(
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

        Args:
            id: Dispute ID
            customer_email: Customer email
            customer_name: Customer name
            customer_phone: Customer phone
            service_details: Details of service involved
            delivery_address: Delivery Address
            delivery_date: ISO 8601 representation of delivery date (YYYY-MM-DD)

        Returns:
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
        url = self._parse_url(f"dispute/{id}/evidence")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_upload_url(self, id: str, upload_filename: str) -> Response:
        """Get URL to upload a dispute evidence.

        Args:
            id: Dispute ID
            upload_filename: The file name, with its extension, that you want to upload. e.g. filename.pdf

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(
            f"/dispute/{id}/upload_url?upload_filename={upload_filename}"
        )
        return await self._handle_request(HTTPMethod.GET, url)

    async def resolve_dispute(
        self,
        id: str,
        resolution: Resolution,
        message: str,
        refund_amount: int,
        uploaded_filename: str,
        evidence: Optional[int] = None,
    ) -> Response:
        """Resolve a dispute on your integration

        Args:
            id: Dispute ID
            resolution: Any of the Resolution enum value.
            message: Reason for resolving
            refund_amount: the amount to refund, in kobo if currency is NGN,
                pesewas, if currency is GHS, and cents, if currency is ZAR
            uploaded_filename: filename of attachment returned via response from
                upload url(GET /dispute/:id/upload_url)
            evidence: Evidence ID for fraud claims

        Returns:
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
        url = self._parse_url(f"/dispute/{id}/resolve")
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def export_disputes(
        self,
        start_date: str,
        end_date: str,
        pagination: int = 50,
        page: int = 1,
        transaction: Optional[str] = None,
        status: Optional[DisputeStatus] = None,
    ) -> Response:
        """Export disputes available on your integration.

        Args:
            start_date: A timestamp from which to start listing dispute e.g. 2016-09-21
            end_date: A timestamp at which to stop listing dispute e.g. 2016-09-21
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specifies exactly what dispute you want to page. If not specified we use a default value of 1.
            transaction: Transaction ID
            status: Any value from the DisputeStatus enum

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dispute/export?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("transaction", transaction),
            ("status", status),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)
