from typing import Optional

from ..baseapi import BaseAPI, Response
from ..utils import Currency, add_to_payload, append_query_params, validate_amount


class Transfer(BaseAPI):
    """Provides a wrapper for paystack Transfers API

    The Transfers API allows you automate sending money on your integration
    https://paystack.com/docs/api/#transfer

    Note
    ----
    This feature is only available to businesses in Nigeria and Ghana.
    """

    def initiate(
        self,
        amount: int,
        recipient: str,
        reason: Optional[str] = None,
        currency: Optional[Currency] = None,
        reference: Optional[str] = None,
        source="balance",
    ) -> Response:
        """
        amount: int
        recipient: str
        reason: Optional[str]
        currency: Optional[Currency]
        reference: Optional[str]
        source: str

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        amount = validate_amount(amount)

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
    ) -> Response:
        """
        Parameters
        ----------
        transfer_code: str
        otp: str

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        amount = validate_amount(amount)

        url = self._url("/transfer/finalize_transfer")

        payload = {
            "transfer_code": transfer_code,
            "otp": otp,
        }
        return self._handle_request("POST", url, payload)

    def bulk_transfer(self, transfers: list, source="balance") -> Response:
        """

        Parameters
        ----------
        transfers: list
        source: str

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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
    ) -> Response:
        """

        Parameters
        ----------
        customer: str
        page: int
        pagination: int
        start_date: Optional[str]
        end_date: Optional[str]

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
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
    ) -> Response:
        """

        Parameters
        ----------
        id_or_code: str

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/transfer/{id_or_code}")
        return self._handle_request("GET", url)

    def verify(
        self,
        reference: str,
    ) -> Response:
        """

        Parameters
        ----------
        reference: str

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/transfer/verify/{reference}")
        return self._handle_request("GET", url)
