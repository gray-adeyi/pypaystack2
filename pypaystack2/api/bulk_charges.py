from typing import Any, Optional

from ..baseapi import BaseAPI, Response
from ..utils import ChargeStatus, append_query_params


class BulkCharge(BaseAPI):
    """Provides a wrapper for paystack Bulk Charge API

    The Bulk Charges API allows you create and manage multiple recurring payments from your customers.
    https://paystack.com/docs/api/#bulk-charge
    """

    def initiate(self, body: list[dict[str, Any]]) -> Response:
        """
        Send a list of dictionaries with authorization ``codes`` and ``amount``
        (in kobo if currency is NGN, pesewas, if currency is GHS, and cents,
        if currency is ZAR ) so paystack can process transactions as a batch.

        Parameters
        ----------
        body: list
            A list of dictionaries with authorization codes and amount.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/bulkcharge")
        payload = body
        return self._handle_request("POST", url, payload)

    def get_batches(
        self,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """This gets all bulk charge batches created by the integration.

        Parameters
        ----------
        page:int
            Specify exactly what transfer you want to page.
            If not specify we use a default value of 1.
        pagination:int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        start_date: Optional[str]
            A timestamp from which to start listing batches
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing batches
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/bulkcharge?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_batch(self, id_or_code: str) -> Response:
        """
        This method retrieves a specific batch code. It also returns
        useful information on its progress by way of the total_charges
        and pending_charges attributes in the Response.

        Parameters
        ----------
        id_or_code:str
            An ID or code for the charge whose batches you want to retrieve.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/bulkcharge/{id_or_code}")
        return self._handle_request("GET", url)

    def get_charges_in_batch(
        self,
        id_or_code: str,
        status: ChargeStatus,
        pagination=50,
        page=1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """
        This method retrieves the charges associated with a specified
        batch code. Pagination parameters are available. You can also
        filter by status. Charge statuses can be `ChargeStatus.PENDING`,
        `ChargeStatus.SUCCESS` or `ChargeStatus.FAILED`.

        Parameters
        ----------
        id_or_code: str
            An ID or code for the batch whose charges you want to retrieve.
        status: ChargeStatus
            Any of the values from the ChargeStatus enum.
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        page: int
            Specify exactly what transfer you want to page.
            If not specify we use a default value of 1.
        start_date: Optional[str]
            A timestamp from which to start listing batches
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing batches
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/bulkcharge/{id_or_code}/charges?perPage={pagination}")
        query_params = [
            ("status", status),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def pause_batch(self, batch_code: str) -> Response:
        """Use this method to pause processing a batch

        Parameters
        ----------
        batch_code: str
            The batch code for the bulk charge you want to pause.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/bulkcharge/pause/{batch_code}")
        return self._handle_request("GET", url)

    def resume_batch(self, batch_code: str) -> Response:
        """Use this method to resume processing a batch

        Parameters
        ----------
        batch_code: str
            The batch code for the bulk charge you want to resume.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/bulkcharge/resume/{batch_code}")
        return self._handle_request("GET", url)
