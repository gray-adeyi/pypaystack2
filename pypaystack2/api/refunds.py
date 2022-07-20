from typing import Optional


from ..baseapi import BaseAPI
from ..utils import (
    Currency,
    add_to_payload,
    append_query_params,
    validate_amount,
)


class Refund(BaseAPI):
    """
    The Refunds API allows you
    create and manage transaction
    refunds
    """

    def create(
        self,
        transaction: str,
        amount: Optional[int] = None,
        currency: Optional[Currency] = None,
        customer_note: Optional[str] = None,
        merchant_note: Optional[str] = None,
    ):
        """ """
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
    ):
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

    def get_refund(self, reference: str):
        url = self._url(f"/refund/{reference}")
        return self._handle_request("GET", url)
