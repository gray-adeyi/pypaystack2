from typing import Optional

from ..baseapi import BaseAPI, Response
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
    ) -> Response:
        """Fetch settlements made to your settlement accounts.

        page: int
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        start_date: Optional[str]
            A timestamp from which to start listing settlements
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing settlements
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        subaccount: Optional[str]
            Provide a subaccount ID to export only settlements for that subaccount.
            Set to ``none`` to export only transactions for the account.


        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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
        id: int,
        pagination=50,
        page=1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Get the transactions that make up a particular settlement

        Parameters
        ----------
        id: int
            The settlement ID in which you want to fetch its transactions
        pagination: int
            Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        page: int
            Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        start_date: Optional[str]
            A timestamp from which to start listing settlement transactions
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing settlement transactions
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/settlement/{id}/transactions?perPage={pagination}")
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)
