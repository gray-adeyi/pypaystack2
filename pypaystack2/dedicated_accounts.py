from optparse import Option
from typing import Optional
from .baseapi import BaseAPI
from .errors import InvalidDataError
from .utils import (
    Currency,
    add_to_payload,
    append_query_params,
    Identification,
    Country,
    RiskAction,
)


class DedicatedAccount(BaseAPI):
    """
    The Dedicated Virtual Account API enables
    Nigerian merchants to manage unique payment
    accounts of their customers.

    Note: This feature is only available to businesses in Nigeria.
    """

    def create(
        self,
        customer: str,
        preferred_bank: Optional[str] = None,
        subaccount: Optional[str] = None,
        split_code: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
    ):
        """
        Create a dedicated virtual account and assign to a customer
        """
        url = self._url("/dedicated_account")
        payload = {
            "customer": customer,
        }
        optional_params = (
            ("preferred_bank", preferred_bank),
            ("subaccount", subaccount),
            ("split_code", split_code),
            ("first_name", first_name),
            ("last_name", last_name),
            ("phone", phone),
        )
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def getall(
        self,
        active=True,
        currency=Currency.NGN,
        provider_slug: Optional[str] = None,
        bank_id: Optional[str] = None,
        customer: Optional[str] = None,
    ):
        """
        Gets all the customers we have at paystack in steps of (default) 50 records per page.
        We can provide an optional pagination to indicate how many customer records we want to fetch per time

        args:
        pagination -- Count of data to return per call
        """
        if active:
            _active = "true"
        else:
            _active = "false"
        query_params = [
            ("currency", currency),
            ("provider_slug", provider_slug),
            ("bank_id", bank_id),
            ("customer", customer),
        ]
        url = self._url(f"/dedicated_account?active={_active}")
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def getone(self, dedicated_account_id: int):
        """
        Get details of a dedicated virtual account on your integration.
        """
        url = self._url(f"/dedicated_account/{dedicated_account_id}")
        return self._handle_request("GET", url)

    def requery(self, account_number: str, provider_slug: str, date: Optional[str]):
        """
        Get details of a dedicated virtual account on your integration.
        """
        url = self._url(f"/dedicated_account?account_number={account_number}")
        query_params = [
            ("provider_slug", provider_slug),
            ("date", date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def deactivate(self, account_number: str, provider_slug: str, date: Optional[str]):
        """
        Deactivate a dedicated virtual account on your integration.
        """
        url = self._url(f"/dedicated_account/dedicated_account_id")
        return self._handle_request("DELETE", url)

    def split(
        self,
        customer: str,
        subaccount: Optional[str] = None,
        split_code: Optional[str] = None,
        preferred_bank: Optional[str] = None,
    ):
        """Split a dedicated virtual account transaction with one or more accounts"""
        url = self._url(f"/dedicated_account/split")
        payload = {"customer": customer}

        optional_params = [
            ("subaccount", subaccount),
            ("split_code", split_code),
            ("preferred_bank", preferred_bank),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def remove_split(self, account_number: str):
        """
        If you've previously set up split payment
        for transactions on a dedicated virtual
        account, you can remove it with this endpoint
        """
        url = self._url(f"/dedicated_account/split")
        payload = {
            "account_number": account_number,
        }
        return self._handle_request("DELETE", url, payload)

    def get_providers(self):
        """
        Get available bank providers for a dedicated virtual account
        """
        url = self._url(f"/dedicated_account/available_providers")
        return self._handle_request("GET", url)
