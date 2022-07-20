from typing import Optional

from ..baseapi import BaseAPI
from ..utils import (
    add_to_payload,
    append_query_params,
)


class SubAccount(BaseAPI):
    """
    The Subaccounts API allows you create
    and manage subaccounts on your integration.
    Subaccounts can be used to split payment
    between two accounts
    (your main account and a sub account)
    """

    def create(
        self,
        business_name: str,
        settlement_bank: str,
        account_number: str,
        percentage_charge: float,
        description: str,
        primary_contact_email: Optional[str] = None,
        primary_contact_name: Optional[str] = None,
        primary_contact_phone: Optional[str] = None,
        metadata: Optional[str] = None,
    ):
        """
        Create a subacount on your integration.
        """
        url = self._url("/subaccount")
        payload = {
            "business_name": business_name,
            "settlement_bank": settlement_bank,
            "account_number": account_number,
            "percentage_charge": percentage_charge,
            "description": description,
        }
        optional_params = [
            ("primary_contact_email", primary_contact_email),
            ("primary_contact_name", primary_contact_name),
            ("primary_contact_phone", primary_contact_phone),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def list_subaccounts(self, start_date: str, end_date: str, page=1, pagination=50):
        """
        List subaccounts available on your integration.
        """
        url = self._url(f"/subaccount?perPage={pagination}")
        query_params = [
            ("from", start_date),
            ("to", end_date),
            ("page", page),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_subaccount(self, id_or_code: str):
        """Get details of a subaccount on your integration."""
        url = self._url(f"/subaccount/{id_or_code}")
        return self._handle_request("GET", url)

    def update_subaccount(
        self,
        id_or_code: str,
        business_name: str,
        settlement_bank: str,
        account_number: Optional[str] = None,
        active: Optional[bool] = None,
        percentage_charge: Optional[float] = None,
        description: Optional[str] = None,
        primary_contact_email: Optional[str] = None,
        primary_contact_name: Optional[str] = None,
        primary_contact_phone: Optional[str] = None,
        settlement_schedule: Optional[str] = None,
        metadata: Optional[str] = None,
    ):
        """
        Update a subaccount details on your integration
        """
        payload = {
            "id_or_code": id_or_code,
            "business_name": business_name,
            "settlement_bank": settlement_bank,
        }
        optional_params = [
            ("account_number", account_number),
            ("active", active),
            ("percentage_charge", percentage_charge),
            ("description", description),
            ("primary_contact_email", primary_contact_email),
            ("primary_contact_name", primary_contact_name),
            ("primary_contact_phone", primary_contact_phone),
            ("settlement_schedule", settlement_schedule),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        url = self._url(f"/subaccount/{id_or_code}")
        return self._handle_request("PUT", url, payload)
