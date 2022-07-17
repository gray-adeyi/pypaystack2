from typing import Mapping, Optional

from pypaystack2.errors import InvalidDataError
from .baseapi import BaseAPI
from . import utils
from .utils import TRType, add_to_payload, append_query_params


class TransferControl(BaseAPI):
    """
    The Transfers API allows you
    automate sending money on
    your integration
    """

    def check_balance(self):
        """ """
        url = self._url("/balance")
        return self._handle_request("GET", url)

    def get_balance_ledger(self):
        """ """
        url = self._url("balance/ledger")
        return self._handle_request("GET", url)

    def resend_otp(self, transfer_code: str, reason: str):
        """ """
        payload = {"transfer_code": transfer_code, "reason": reason}
        url = self._url("/transfer/resend_otp")
        return self._handle_request("POST", url, payload)

    def disable_otp(self):
        """ """
        url = self._url("/transfer/disable_otp")
        return self._handle_request("POST", url)

    def finalize_disable_otp(self, otp: str):
        """ """
        payload = {"otp": otp}
        url = self._url("/transfer/disable_otp_finalize")
        return self._handle_request("POST", url, payload)

    def finalize(
        self,
        transfer_code: str,
        otp: str,
    ):
        """ """
        amount = utils.validate_amount(amount)

        url = self._url("/transfer/finalize_transfer")

        payload = {
            "transfer_code": transfer_code,
            "otp": otp,
        }
        return self._handle_request("POST", url, payload)

    def bulk_transfer(self, transfers: list, source="balance"):
        """ """

        url = self._url("/transfer/bulk")

        payload = {
            "transfers": transfers,
            "source": source,
        }
        return self._handle_request("POST", url, payload)

    def get_transfers(
        self,
        customer: str,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        """ """
        url = self._url(f"/transfer?perPage={pagination}")
        query_params = [
            ("customer", customer),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_transfer(
        self,
        id_or_code: str,
    ):
        """ """
        url = self._url(f"/transfer/{id_or_code}")
        return self._handle_request("GET", url)

    def verify(
        self,
        reference: str,
    ):
        """ """
        url = self._url(f"/transfer/verify/{reference}")
        return self._handle_request("GET", url)
