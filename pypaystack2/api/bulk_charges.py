from typing import Optional

from ..baseapi import BaseAPI
from ..utils import ChargeStatus, append_query_params


class BulkCharge(BaseAPI):
    """
    The Bulk Charges API allows you
    create and manage multiple recurring
    payments from your customers
    """

    def initiate(self, body: list):
        """ """
        url = self._url("/bulkcharge")
        payload = body
        return self._handle_request("POST", url, payload)

    def get_batches(
        self,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        """ """
        url = self._url(f"/bulkcharge?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_batch(self, id_or_code: str):
        """ """
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
    ):
        """ """
        url = self._url(f"/bulkcharge/{id_or_code}/charges?perPage={pagination}")
        query_params = [
            ("status", status),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def pause_batch(self, batch_code: str):
        """ """
        url = self._url(f"/bulkcharge/pause/{batch_code}")
        return self._handle_request("GET", url)

    def resume_batch(self, batch_code: str):
        """ """
        url = self._url(f"/bulkcharge/resume/{batch_code}")
        return self._handle_request("GET", url)
