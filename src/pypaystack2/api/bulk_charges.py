from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    HTTPMethod,
    append_query_params,
    Response,
    Status,
    BulkChargeInstruction,
)


class BulkCharge(BaseAPI):
    """Provides a wrapper for paystack Bulk Charge API

    The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.
    https://paystack.com/docs/api/bulk-charge/
    """

    def initiate(self, body: list[BulkChargeInstruction]) -> Response:
        """
        Send a list of dictionaries with authorization ``codes`` and ``amount``
        (in kobo if currency is NGN, pesewas, if currency is GHS, and cents,
        if currency is ZAR ) so paystack can process transactions as a batch.

        Args:
            body: A list of BulkChargeInstruction.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/bulkcharge")
        payload = [item.dict for item in body]
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_batches(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """This gets all bulk charge batches created by the integration.

        Args:
            page: Specify exactly what transfer you want to page. If not specified, we use a default value of 1.
            pagination: Specify how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_batch(self, id_or_code: str) -> Response:
        """
        This method retrieves a specific batch code. It also returns
        useful information on its progress by way of the total_charges
        and pending_charges attributes in the Response.

        Args:
            id_or_code: An ID or code for the charge whose batches you want to retrieve.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/{id_or_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def get_charges_in_batch(
        self,
        id_or_code: str,
        status: Status,
        pagination: int = 50,
        page: int = 1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/{id_or_code}/charges?perPage={pagination}")
        query_params = [
            ("status", status),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def pause_batch(self, batch_code: str) -> Response:
        """Use this method to pause processing a batch.

        Args:
            batch_code: The batch code for the bulk charge you want to pause.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/pause/{batch_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def resume_batch(self, batch_code: str) -> Response:
        """Use this method to resume processing a batch

        Args:
            batch_code: The batch code for the bulk charge you want to resume.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/resume/{batch_code}")
        return self._handle_request(HTTPMethod.GET, url)


class AsyncBulkCharge(BaseAsyncAPI):
    """Provides a wrapper for paystack Bulk Charge API

    The Bulk Charges API allows you to create and manage multiple recurring payments from your customers.
    https://paystack.com/docs/api/bulk-charge/
    """

    async def initiate(self, body: list[BulkChargeInstruction]) -> Response:
        """
        Send a list of dictionaries with authorization ``codes`` and ``amount``
        (in kobo if currency is NGN, pesewas, if currency is GHS, and cents,
        if currency is ZAR ) so paystack can process transactions as a batch.

        Args:
            body: A list of BulkChargeInstruction.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/bulkcharge")
        payload = [item.dict for item in body]
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_batches(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """This gets all bulk charge batches created by the integration.

        Args:
            page: Specify exactly what transfer you want to page. If not specified, we use a default value of 1.
            pagination: Specify how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_batch(self, id_or_code: str) -> Response:
        """
        This method retrieves a specific batch code. It also returns
        useful information on its progress by way of the total_charges
        and pending_charges attributes in the Response.

        Args:
            id_or_code: An ID or code for the charge whose batches you want to retrieve.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/{id_or_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_charges_in_batch(
        self,
        id_or_code: str,
        status: Status,
        pagination: int = 50,
        page: int = 1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/{id_or_code}/charges?perPage={pagination}")
        query_params = [
            ("status", status),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def pause_batch(self, batch_code: str) -> Response:
        """Use this method to pause processing a batch.

        Args:
            batch_code: The batch code for the bulk charge you want to pause.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/pause/{batch_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def resume_batch(self, batch_code: str) -> Response:
        """Use this method to resume processing a batch

        Args:
            batch_code: The batch code for the bulk charge you want to resume.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bulkcharge/resume/{batch_code}")
        return await self._handle_request(HTTPMethod.GET, url)
