from typing import Mapping, Optional

from ..baseapi import BaseAPI
from ..utils import (
    Bearer,
    Channel,
    Currency,
    SplitType,
    TransactionStatus,
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
        subaccounts: list[Mapping],
        bearer_type: Bearer,
        bearer_subaccount: str,
    ):
        """
        Create a split payment on your integration
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
    ):
        """
        List/search for the transaction splits available on your integration.
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

    def get_split(self, id: str):
        """
        Get details of a split on your integration.
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
    ):
        """
        Update a transaction split details on your integration
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

    def add_or_update(self, id: str, subaccount: str, share: int):
        """
        Add a Subaccount to a Transaction Split, or update
        the share of an existing Subaccount in a Transaction Split
        """
        share = validate_amount(share)
        payload = {"subaccount": subaccount, "share": share}
        url = self._url(f"/split/{id}/subaccount/add")
        return self._handle_request("POST", url, payload)

    def remove(self, id: str, subaccount: str):
        """
        Remove a subaccount from a transaction split
        """
        payload = {"subaccount": subaccount}
        url = self._url(f"/split/{id}/subaccount/remove")
        return self._handle_request("POST", url, payload)
