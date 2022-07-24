from typing import Optional


from ..baseapi import BaseAPI, Response
from ..utils import (
    Currency,
    add_to_payload,
    append_query_params,
    validate_amount,
)


class Refund(BaseAPI):
    """Provides a wrapper for paystack Refunds API

    The Refunds API allows you create and manage transaction refunds.
    https://paystack.com/docs/api/#refund
    """

    def create(
        self,
        transaction: str,
        amount: Optional[int] = None,
        currency: Optional[Currency] = None,
        customer_note: Optional[str] = None,
        merchant_note: Optional[str] = None,
    ) -> Response:
        """Initiate a refund on your integration

        Parameters
        ----------
        transaction: str
            Transaction reference or id
        amount: Optional[int]
            Amount ( in kobo if currency is NGN, pesewas, if currency is
            GHS, and cents, if currency is ZAR ) to be refunded to the
            customer. Amount is optional(defaults to original
            transaction amount) and cannot be more than the original
            transaction amount
        currency: Optional[Currency]
            Any value from the ``Currency`` enum
        customer_note: Optional[str]
            Customer reason
        merchant_note: Optional[str]
            Merchant reason

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        if amount is not None:
            amount = validate_amount(amount)
        url = self._url("/refund")
        payload = {"transaction": transaction}
        optional_params = [
            ("amount", amount),
            ("currency", currency),
            ("customer_note", customer_note),
            ("merchant_note", merchant_note),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def get_refunds(
        self,
        reference: str,
        currency: Currency,
        pagination=50,
        page=1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch refunds available on your integration.

        Parameters
        ----------
        reference: str
            Identifier for transaction to be refunded
        currency: Currency
            Any value from the ``Currency`` enum
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        page: int
            Specify exactly what refund you want to page.
            If not specify we use a default value of 1.
        start_date: Optional[str]
            A timestamp from which to start listing refund e.g. 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing refund e.g. 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/refund?perPage={pagination}")
        query_params = [
            ("reference", reference),
            ("currency", currency),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_refund(self, reference: str) -> Response:
        """Get details of a refund on your integration.

        Parameters
        ----------
        reference: str
            Identifier for transaction to be refunded

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/refund/{reference}")
        return self._handle_request("GET", url)
