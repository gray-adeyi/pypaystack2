from typing import Optional

from ..baseapi import BaseAPI
from ..utils import (
    append_query_params,
)


class Settlement(BaseAPI):
    """Provides a wrapper for paystack Settlement API

    The Settlements API allows you gain insights into payouts made by Paystack to your bank account.
    https://paystack.com/docs/api/#settlement
    """

    def get_settlements(
        self,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        subaccount: Optional[str] = None,
    ):
        """ """

        url = self._url(f"/settlement?perPage={pagination}")
        query_params = [
            ("subaccount", subaccount),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_settlement_transactions(
        self,
        id=int,
        pagination=50,
        page=1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        """ """

        url = self._url(f"/settlement/{id}/transactions?perPage={pagination}")
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)
