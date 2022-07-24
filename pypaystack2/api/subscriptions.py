from typing import Optional

from ..baseapi import BaseAPI, Response
from ..utils import add_to_payload, append_query_params


class Subscription(BaseAPI):
    """Provides a wrapper for paystack Subscriptions API

    The Subscriptions API allows you create and manage recurring
    payment on your integration.
    https://paystack.com/docs/api/#subscription
    """

    def create(
        self,
        customer: str,
        plan: str,
        authorization: str,
        start_date: Optional[str] = None,
    ) -> Response:
        """Create a subscription on your integration

        Parameters
        ----------
        customer: str
            Customer's email address or customer code
        plan: str
            Plan code
        authorization: str
            If customer has multiple authorizations, you can set
            the desired authorization you wish to use for this
            subscription here. If this is not supplied, the
            customer's most recent authorization would be used
        start_date: Optional[str]
            Set the date for the first debit. (ISO 8601 format) e.g. 2017-05-16T00:30:13+01:00


        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Email Token
            paystack creates an email token on each subscription to allow customers
            cancel their subscriptions from within the invoices sent to their mailboxes.
            Since they are not authorized, the email tokens are what we use to authenticate
            the requests over the API.
        """

        url = self._url("/subscription")

        payload = {"customer": customer, "plan": plan, "authorization": authorization}
        optional_params = [
            ("start_date", start_date),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def get_subscriptions(
        self,
        page=1,
        pagination=50,
        customer: Optional[int] = None,
        plan: Optional[int] = None,
    ) -> Response:
        """Fetch subscriptions available on your integration.

        Parameters
        ----------
        page: int
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        customer: Optional[int]
            Filter by Customer ID
        plan: Optional[int]
            Filter by Plan ID

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/plan/?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("customer", customer),
            ("plan", plan),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_subscription(self, id_or_code: str) -> Response:
        """Fetch details of a subscription on your integration.

        Parameters
        ----------
        id_or_code: str
            The subscription ``ID`` or ``code`` you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/subscription/{id_or_code}")
        return self._handle_request("GET", url)

    def enable(self, code: str, token: str) -> Response:
        """Enable a subscription on your integration

        Parameters
        ----------
        code: str
            Subscription code
        token: str
            Email token

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/subscription/enable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request("POST", url, payload)

    def disable(self, code: str, token: str) -> Response:
        """Disable a subscription on your integration

        Parameters
        ----------
        code: str
            Subscription code
        token: str
            Email token

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url("/subscription/disable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request("POST", url, payload)

    def get_update_link(self, code: str) -> Response:
        """Generate a link for updating the card on a subscription

        Parameters
        ----------
        code: str
            Subscription code

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/subscription/{code}/manage/link/")
        return self._handle_request("GET", url)

    def send_update_link(self, code: str) -> Response:
        """Email a customer a link for updating the card on their subscription

        Parameters
        ----------
        code: str
            Subscription code

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/subscription/{code}/manage/email/")
        payload = {"code": "code"}
        return self._handle_request("POST", url, payload)
