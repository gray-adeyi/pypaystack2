from typing import Any, Mapping, Optional

from ..baseapi import BaseAPI, Response
from ..utils import (
    Bearer,
    Currency,
    SplitType,
    add_to_payload,
    append_query_params,
    validate_amount,
)
from ..errors import InvalidDataError


class Split(BaseAPI):
    """Provides a wrapper for paystack Transaction Splits API

    The Transaction Splits API enables merchants split the settlement for a transaction
    across their payout account, and one or more Subaccounts.
    https://paystack.com/docs/api/#split
    """

    def create(
        self,
        name: str,
        type: SplitType,
        currency: Currency,
        subaccounts: list[dict[str, Any]],
        bearer_type: Bearer,
        bearer_subaccount: str,
    ) -> Response:
        """Create a split payment on your integration

        Parameters
        ----------
        name: str
            Name of the transaction split
        type: SplitType
            The type of transaction split you want to create.
            Any value from the ``SplitType`` enum
        currency: Currency
            Any value from the ``Currency`` enum
        subaccounts: list[dict[str,Any]]
            A list of dictionaries containing subaccount code and
            number of shares: ``[{subaccount: 'ACT_xxxxxxxxxx', share: xxx},{...}]``
        bearer_type: Bearer
            Any value from the ``Bearer`` enum
        bearer_subaccount: str
            Subaccount code

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/split")
        payload = {
            "name": name,
            "type": type,
            "currency": currency,
            "subaccounts": subaccounts,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount,
        }
        return self._handle_request("POST", url, payload)

    def get_splits(
        self,
        name: str,
        sort_by: Optional[str],
        page: Optional[int],
        start_date: Optional[str],
        end_date: Optional[str],
        active: bool = True,
        pagination=50,
    ) -> Response:
        """Get/search for the transaction splits available on your integration.

        Parameters
        ----------
        name: str
            The name of the split
        sort_by: Optional[str]
            Sort by name, defaults to createdAt date
        page: Optional[int]
            Page number to view. If not specify we use a default value of 1.
        start_date: Optional[str]
            A timestamp from which to start listing splits
            e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing splits
            e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
        active: bool
        pagination: int
            Number of splits per page.
            If not specify we use a default value of 50.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/split?perPage={pagination}")
        query_params = [
            ("name", name),
            ("sort_by", sort_by),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("active", active),
        ]
        url = append_query_params(query_params)

        return self._handle_request("GET", url)

    def get_split(self, id: str) -> Response:
        """Get details of a split on your integration.

        Parameters
        ----------
        id: str
            The id of the split

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/split/{id}/")
        return self._handle_request("GET", url)

    def update(
        self,
        id: str,
        name: str,
        active: bool,
        bearer_type: Optional[Bearer],
        bearer_subaccount: Optional[str],
    ) -> Response:
        """Update a transaction split details on your integration

        Parameters
        ----------
        id: str
            Split ID
        name: str
            Name of the transaction split
        active: bool
        bearer_type: Optional[Bearer]
            Any value from the Bearer enum
        bearer_subaccount: Optional[str]
            Subaccount code of a subaccount in the split group.
            This should be specified only if the bearer_type
            is ``Bearer.subaccount``

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        if bearer_subaccount:
            if bearer_type != Bearer.SUBACCOUNT:
                raise InvalidDataError(
                    "`bearer_subaccount` can only have a value if `bearer_type` is `Bearer.SUBACCOUNT`"
                )

        payload = {
            "name": name,
            "active": active,
        }
        optional_params = [
            ("bearer_type", bearer_type),
            ("bearer_subaccount", bearer_subaccount),
        ]
        payload = add_to_payload()
        url = self._url(f"/split/{id}/")
        return self._handle_request("PUT", url, payload)

    def add_or_update(self, id: str, subaccount: str, share: int) -> Response:
        """
        Add a Subaccount to a Transaction Split, or update
        the share of an existing Subaccount in a Transaction Split

        Parameters
        ----------
         id: str
            Split Id
         subaccount: str
            This is the sub account code
         share: int
            This is the transaction share for the subaccount

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        share = validate_amount(share)
        payload = {"subaccount": subaccount, "share": share}
        url = self._url(f"/split/{id}/subaccount/add")
        return self._handle_request("POST", url, payload)

    def remove(self, id: str, subaccount: str):
        """Remove a subaccount from a transaction split

        Parameters
        ----------
        id: str
            Split Id
        subaccount: str
            This is the sub account code

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"subaccount": subaccount}
        url = self._url(f"/split/{id}/subaccount/remove")
        return self._handle_request("POST", url, payload)
