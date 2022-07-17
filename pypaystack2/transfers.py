from typing import Mapping, Optional

from pypaystack2.errors import InvalidDataError
from .baseapi import BaseAPI
from . import utils
from .utils import TRType, add_to_payload, append_query_params


class Transfer(BaseAPI):
    """
    The Transfers API allows you
    automate sending money on
    your integration
    """

    def initiate(
        self,
        amount: int,
        recipient: str,
        reason: Optional[str] = None,
        currency: Optional[utils.Currency] = None,
        reference: Optional[str] = None,
        source="balance",
    ):
        """ """
        amount = utils.validate_amount(amount)

        url = self._url("/transfer")

        payload = {
            "amount": amount,
            "recipient": recipient,
            "source": source,
        }
        optional_params = [
            ("reason", reason),
            ("reference", reference),
            ("currency", currency),
        ]
        payload = add_to_payload(optional_params, payload)
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
