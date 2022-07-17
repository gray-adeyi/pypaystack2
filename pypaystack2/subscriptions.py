from typing import Optional
from .baseapi import BaseAPI
from . import utils
from .utils import add_to_payload, append_query_params


class Plan(BaseAPI):
    """
    The Subscriptions API allows
    you create and manage recurring
    payment on your integration
    """

    def create(
        self,
        customer: str,
        plan: str,
        authorization: str,
        start_data: Optional[str] = None,
    ):
        """
        Create a subscription on your integration

        """

        url = self._url("/subscription")

        payload = {"customer": customer, "plan": plan, "authorization": authorization}
        optional_params = [
            ("start_data", start_data),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def get_subscriptions(
        self,
        page=1,
        pagination=50,
        customer: Optional[int] = None,
        plan: Optional[int] = None,
    ):
        """
        List subscriptions available on your integration.
        """
        url = self._url(f"/plan/?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("customer", customer),
            ("plan", plan),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_subscription(self, id_or_code: str):
        """
        Get details of a subscription on your integration.
        """
        url = self._url(f"/subscription/{id_or_code}")
        return self._handle_request("GET", url)

    def enable(self, code: str, token: str):
        """ """
        url = self._url("/subscription/enable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request("POST", url, payload)

    def disable(self, code: str, token: str):
        """ """
        url = self._url("/subscription/disable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request("POST", url, payload)

    def get_update_link(self, code: str):
        """ """
        url = self._url(f"/subscription/{code}/manage/link/")
        return self._handle_request("GET", url)

    def send_update_link(self, code: str):
        url = self._url(f"/subscription/{code}/manage/email/")
        payload = {"code": "code"}
        return self._handle_request("POST", url, payload)
