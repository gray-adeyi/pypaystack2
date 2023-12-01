from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.exceptions import InvalidDataException
from pypaystack2.utils import (
    Bearer,
    Currency,
    Split,
    add_to_payload,
    append_query_params,
    validate_amount,
    HTTPMethod,
    Response,
    SplitAccount,
)


class TransactionSplit(BaseAPI):
    """Provides a wrapper for paystack Transaction Splits API

    The Transaction Splits API enables merchants split the settlement for a transaction
    across their payout account, and one or more Subaccounts.
    https://paystack.com/docs/api/split/
    """

    def create(
        self,
        name: str,
        type: Split,
        currency: Currency,
        subaccounts: list[SplitAccount],
        bearer_type: Bearer,
        bearer_subaccount: str,
    ) -> Response:
        """Create a split payment on your integration

        Args:
            name: Name of the transaction split
            type: The type of transaction split you want to create.
                Any value from the ``SplitType`` enum
            currency: Any value from the ``Currency`` enum
            subaccounts: A list of dictionaries containing subaccount code and
                number of shares: ``[{subaccount: 'ACT_xxxxxxxxxx', share: xxx},{...}]``
            bearer_type: Any value from the ``Bearer`` enum
            bearer_subaccount: Subaccount code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        subaccounts = [account.dict for account in subaccounts]

        url = self._parse_url("/split")
        payload = {
            "name": name,
            "type": type,
            "currency": currency,
            "subaccounts": subaccounts,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_splits(
        self,
        name: str,
        sort_by: Optional[str],
        page: Optional[int],
        start_date: Optional[str],
        end_date: Optional[str],
        active: bool = True,
        pagination: int = 50,
    ) -> Response:
        """Get/search for the transaction splits available on your integration.

        Args:
            name: The name of the split
            sort_by: Sort by name, defaults to createdAt date
            page: Page number to view. If not specify we use a default value of 1.
            start_date: A timestamp from which to start listing splits e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
            end_date: A timestamp at which to stop listing splits e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
            active: Flag to filter by active
            pagination: Number of splits per page. If not specified we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/split?perPage={pagination}")
        query_params = [
            ("name", name),
            ("sort_by", sort_by),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("active", active),
        ]
        url = append_query_params(query_params, url)

        return self._handle_request(HTTPMethod.GET, url)

    def get_split(self, id: str) -> Response:
        """Get details of a split on your integration.

        Args:
            id: The id of the split

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/split/{id}/")
        return self._handle_request(HTTPMethod.GET, url)

    def update(
        self,
        id: str,
        name: str,
        active: bool,
        bearer_type: Optional[Bearer],
        bearer_subaccount: Optional[str],
    ) -> Response:
        """Update a transaction split details on your integration

        Args:
            id: Split ID
            name: Name of the transaction split
            active: Flag for active
            bearer_type: Any value from the Bearer enum
            bearer_subaccount: Subaccount code of a subaccount in the split group.
                This should be specified only if the bearer_type
                is ``Bearer.subaccount``

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if bearer_subaccount:
            if bearer_type != Bearer.SUB_ACCOUNT:
                raise InvalidDataException(
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
        payload = add_to_payload(optional_params, payload)
        url = self._parse_url(f"/split/{id}/")
        return self._handle_request(HTTPMethod.PUT, url, payload)

    def add_or_update(self, id: str, subaccount: str, share: int) -> Response:
        """
        Add a Subaccount to a Transaction Split, or update
        the share of an existing Subaccount in a Transaction Split

        Args:
         id: Split ID
         subaccount: This is the subaccount code
         share: This is the transaction share for the subaccount

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        share = validate_amount(share)
        payload = {"subaccount": subaccount, "share": share}
        url = self._parse_url(f"/split/{id}/subaccount/add")
        return self._handle_request("POST", url, payload)

    def remove(self, id: str, subaccount: str) -> Response:
        """Remove a subaccount from a transaction split

        Args:
            id: Split ID
            subaccount: This is the subaccount code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"subaccount": subaccount}
        url = self._parse_url(f"/split/{id}/subaccount/remove")
        return self._handle_request(HTTPMethod.POST, url, payload)


class AsyncTransactionSplit(BaseAsyncAPI):
    """Provides a wrapper for paystack Transaction Splits API

    The Transaction Splits API enables merchants split the settlement for a transaction
    across their payout account, and one or more Subaccounts.
    https://paystack.com/docs/api/split/
    """

    async def create(
        self,
        name: str,
        type: TransactionSplit,
        currency: Currency,
        subaccounts: list[SplitAccount],
        bearer_type: Bearer,
        bearer_subaccount: str,
    ) -> Response:
        """Create a split payment on your integration

        Args:
            name: Name of the transaction split
            type: The type of transaction split you want to create.
                Any value from the ``SplitType`` enum
            currency: Any value from the ``Currency`` enum
            subaccounts: A list of dictionaries containing subaccount code and
                number of shares: ``[{subaccount: 'ACT_xxxxxxxxxx', share: xxx},{...}]``
            bearer_type: Any value from the ``Bearer`` enum
            bearer_subaccount: Subaccount code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        subaccounts = [account.dict for account in subaccounts]

        url = self._parse_url("/split")
        payload = {
            "name": name,
            "type": type,
            "currency": currency,
            "subaccounts": subaccounts,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_splits(
        self,
        name: str,
        sort_by: Optional[str],
        page: Optional[int],
        start_date: Optional[str],
        end_date: Optional[str],
        active: bool = True,
        pagination: int = 50,
    ) -> Response:
        """Get/search for the transaction splits available on your integration.

        Args:
            name: The name of the split
            sort_by: Sort by name, defaults to createdAt date
            page: Page number to view. If not specify we use a default value of 1.
            start_date: A timestamp from which to start listing splits e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
            end_date: A timestamp at which to stop listing splits e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
            active: Flag to filter by active
            pagination: Number of splits per page. If not specified we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/split?perPage={pagination}")
        query_params = [
            ("name", name),
            ("sort_by", sort_by),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("active", active),
        ]
        url = append_query_params(query_params, url)

        return await self._handle_request(HTTPMethod.GET, url)

    async def get_split(self, id: str) -> Response:
        """Get details of a split on your integration.

        Args:
            id: The id of the split

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/split/{id}/")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update(
        self,
        id: str,
        name: str,
        active: bool,
        bearer_type: Optional[Bearer],
        bearer_subaccount: Optional[str],
    ) -> Response:
        """Update a transaction split details on your integration

        Args:
            id: Split ID
            name: Name of the transaction split
            active: Flag for active
            bearer_type: Any value from the Bearer enum
            bearer_subaccount: Subaccount code of a subaccount in the split group.
                This should be specified only if the bearer_type
                is ``Bearer.subaccount``

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if bearer_subaccount:
            if bearer_type != Bearer.SUB_ACCOUNT:
                raise InvalidDataException(
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
        payload = add_to_payload(optional_params, payload)
        url = self._parse_url(f"/split/{id}/")
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def add_or_update(self, id: str, subaccount: str, share: int) -> Response:
        """
        Add a Subaccount to a Transaction Split, or update
        the share of an existing Subaccount in a Transaction Split

        Args:
         id: Split ID
         subaccount: This is the subaccount code
         share: This is the transaction share for the subaccount

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        share = validate_amount(share)
        payload = {"subaccount": subaccount, "share": share}
        url = self._parse_url(f"/split/{id}/subaccount/add")
        return await self._handle_request("POST", url, payload)

    async def remove(self, id: str, subaccount: str) -> Response:
        """Remove a subaccount from a transaction split

        Args:
            id: Split ID
            subaccount: This is the subaccount code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"subaccount": subaccount}
        url = self._parse_url(f"/split/{id}/subaccount/remove")
        return await self._handle_request(HTTPMethod.POST, url, payload)
