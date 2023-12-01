from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import add_to_payload, append_query_params, HTTPMethod, Response


class Subscription(BaseAPI):
    """Provides a wrapper for paystack Subscriptions API

    The Subscriptions API allows you to create and manage recurring
    payment on your integration.
    https://paystack.com/docs/api/subscription/
    """

    def create(
        self,
        customer: str,
        plan: str,
        authorization: Optional[str] = None,
        start_date: Optional[str] = None,
    ) -> Response:
        """Create a subscription on your integration

        Note:
            Email Token
                paystack creates an email token on each subscription to allow customers
                cancel their subscriptions from within the invoices sent to their mailboxes.
                Since they are not authorized, the email tokens are what we use to authenticate
                the requests over the API.

        Args:
            customer: Customer's email address or customer code
            plan: Plan code
            authorization: If customer has multiple authorizations, you can set
                the desired authorization you wish to use for this
                subscription here. If this is not supplied, the
                customer's most recent authorization would be used
            start_date: Set the date for the first debit. (ISO 8601 format) e.g. 2017-05-16T00:30:13+01:00


        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subscription")

        payload = {"customer": customer, "plan": plan}
        optional_params = [
            ("start_date", start_date),
            ("authorization", authorization),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_subscriptions(
        self,
        page: int = 1,
        pagination: int = 50,
        customer: Optional[int] = None,
        plan: Optional[str] = None,
    ) -> Response:
        """Fetch subscriptions available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            customer: Filter by Customer ID
            plan: Filter by Plan ID

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subscription/?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("customer", customer),
            ("plan", plan),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_subscription(self, id_or_code: str) -> Response:
        """Fetch details of a subscription on your integration.

        Args:
            id_or_code: The subscription ``ID`` or ``code`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subscription/{id_or_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def enable(self, code: str, token: str) -> Response:
        """Enable a subscription on your integration

        Args:
            code: Subscription code
            token: Email token

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subscription/enable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def disable(self, code: str, token: str) -> Response:
        """Disable a subscription on your integration

        Args:
            code: Subscription code
            token: Email token

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/subscription/disable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_update_link(self, code: str) -> Response:
        """Generate a link for updating the card on a subscription

        Args:
            code: Subscription code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subscription/{code}/manage/link/")
        return self._handle_request(HTTPMethod.GET, url)

    def send_update_link(self, code: str) -> Response:
        """Email a customer a link for updating the card on their subscription

        Args:
            code: Subscription code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subscription/{code}/manage/email/")
        payload = {"code": "code"}
        return self._handle_request(HTTPMethod.POST, url, payload)


class AsyncSubscription(BaseAsyncAPI):
    """Provides a wrapper for paystack Subscriptions API

    The Subscriptions API allows you to create and manage recurring
    payment on your integration.
    https://paystack.com/docs/api/subscription/
    """

    async def create(
        self,
        customer: str,
        plan: str,
        authorization: Optional[str] = None,
        start_date: Optional[str] = None,
    ) -> Response:
        """Create a subscription on your integration

        Note:
            Email Token
                paystack creates an email token on each subscription to allow customers
                cancel their subscriptions from within the invoices sent to their mailboxes.
                Since they are not authorized, the email tokens are what we use to authenticate
                the requests over the API.

        Args:
            customer: Customer's email address or customer code
            plan: Plan code
            authorization: If customer has multiple authorizations, you can set
                the desired authorization you wish to use for this
                subscription here. If this is not supplied, the
                customer's most recent authorization would be used
            start_date: Set the date for the first debit. (ISO 8601 format) e.g. 2017-05-16T00:30:13+01:00


        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subscription")

        payload = {"customer": customer, "plan": plan}
        optional_params = [
            ("start_date", start_date),
            ("authorization", authorization),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_subscriptions(
        self,
        page: int = 1,
        pagination: int = 50,
        customer: Optional[int] = None,
        plan: Optional[str] = None,
    ) -> Response:
        """Fetch subscriptions available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            customer: Filter by Customer ID
            plan: Filter by Plan ID

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subscription/?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("customer", customer),
            ("plan", plan),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_subscription(self, id_or_code: str) -> Response:
        """Fetch details of a subscription on your integration.

        Args:
            id_or_code: The subscription ``ID`` or ``code`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subscription/{id_or_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def enable(self, code: str, token: str) -> Response:
        """Enable a subscription on your integration

        Args:
            code: Subscription code
            token: Email token

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subscription/enable")
        payload = {
            "code": code,
            "token": token,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def disable(self, code: str, token: str) -> Response:
        """Disable a subscription on your integration

        Args:
            code: Subscription code
            token: Email token

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/subscription/disable")
        payload = {
            "code": code,
            "token": token,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_update_link(self, code: str) -> Response:
        """Generate a link for updating the card on a subscription

        Args:
            code: Subscription code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subscription/{code}/manage/link/")
        return await self._handle_request(HTTPMethod.GET, url)

    async def send_update_link(self, code: str) -> Response:
        """Email a customer a link for updating the card on their subscription

        Args:
            code: Subscription code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subscription/{code}/manage/email/")
        payload = {"code": "code"}
        return await self._handle_request(HTTPMethod.POST, url, payload)
