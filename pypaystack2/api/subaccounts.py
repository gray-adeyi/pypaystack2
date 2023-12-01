from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    Schedule,
    add_to_payload,
    append_query_params,
    HTTPMethod,
    Response,
)


class SubAccount(BaseAPI):
    """Provides a wrapper for paystack Subaccounts API

    The Subaccounts API allows you to create and manage subaccounts on your integration.
    Subaccounts can be used to split payment between two accounts
    (your main account and a sub account).
    https://paystack.com/docs/api/subaccount/
    """

    def create(
        self,
        business_name: str,
        settlement_bank: str,
        account_number: str,
        percentage_charge: float,
        description: Optional[str] = None,
        primary_contact_email: Optional[str] = None,
        primary_contact_name: Optional[str] = None,
        primary_contact_phone: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """Create a subacount on your integration.

        Args:
            business_name: Name of business for subaccount
            settlement_bank: Bank Code for the bank. You can get the
                list of Bank Codes by calling the ``.get_banks``
                method from the Miscellaneous API wrapper
            account_number: Bank Account Number
            percentage_charge: The default percentage charged when receiving on behalf of this subaccount
            description: A description for this subaccount
            primary_contact_email: A contact email for the subaccount
            primary_contact_name: A name for the contact person for this subaccount
            primary_contact_phone: A phone number to call for this subaccount
            metadata: Add a custom_fields attribute which has a list of dictionaries if
                you would like the fields to be added to your transaction when
                displayed on the dashboard.
                Sample: ``{"custom_fields":[{"display_name":"Cart ID",
                "variable_name": "cart_id","value": "8393"}]}``

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subaccount")
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
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_subaccounts(
        self, start_date: str, end_date: str, page: int = 1, pagination: int = 50
    ) -> Response:
        """Fetch subaccounts available on your integration.

        Args:
            start_date: A timestamp from which to start listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            page: Specifies exactly what page you want to retrieve. If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/subaccount?perPage={pagination}")
        query_params = [
            ("from", start_date),
            ("to", end_date),
            ("page", page),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_subaccount(self, id_or_code: str) -> Response:
        """Get details of a subaccount on your integration.

        Args:
            id_or_code: The subaccount ``ID`` or ``code`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subaccount/{id_or_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def update(
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
        settlement_schedule: Optional[Schedule] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """Update a subaccount details on your integration.

        Args:
            id_or_code: Subaccount's ID or code
            business_name: Name of business for subaccount
            settlement_bank: Bank Code for the bank. You can get the
                list of Bank Codes by calling the ``.get_banks``
                method from the Miscellaneous API wrapper
            account_number: Bank Account Number
            active: Activate or deactivate a subaccount.
            percentage_charge: The default percentage charged when
                receiving on behalf of this subaccount
            description: A description for this subaccount
            primary_contact_email: A contact email for the subaccount
            primary_contact_name: A name for the contact person for this subaccount
            primary_contact_phone: A phone number to call for this subaccount
            settlement_schedule: ``Schedule.AUTO`` means payout is T+1 and manual means payout to the
                subaccount should only be made when requested.
                Defaults to ``Schedule.AUTO``
            metadata: Add a custom_fields attribute which has a list of dictionaries if you would
                like the fields to be added to your transaction when displayed on the
                dashboard. Sample: ``{"custom_fields":[{"display_name":"Cart ID",
                "variable_name": "cart_id","value": "8393"}]}``

        Returns:
            A named tuple containing the response gotten from paystack's server.
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
        url = self._parse_url(f"/subaccount/{id_or_code}")
        return self._handle_request(HTTPMethod.PUT, url, payload)


class AsyncSubAccount(BaseAsyncAPI):
    """Provides a wrapper for paystack Subaccounts API

    The Subaccounts API allows you to create and manage subaccounts on your integration.
    Subaccounts can be used to split payment between two accounts
    (your main account and a sub account).
    https://paystack.com/docs/api/subaccount/
    """

    async def create(
        self,
        business_name: str,
        settlement_bank: str,
        account_number: str,
        percentage_charge: float,
        description: str,
        primary_contact_email: Optional[str] = None,
        primary_contact_name: Optional[str] = None,
        primary_contact_phone: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """Create a subacount on your integration.

        Args:
            business_name: Name of business for subaccount
            settlement_bank: Bank Code for the bank. You can get the
                list of Bank Codes by calling the ``.get_banks``
                method from the Miscellaneous API wrapper
            account_number: Bank Account Number
            percentage_charge: The default percentage charged when receiving on behalf of this subaccount
            description: A description for this subaccount
            primary_contact_email: A contact email for the subaccount
            primary_contact_name: A name for the contact person for this subaccount
            primary_contact_phone: A phone number to call for this subaccount
            metadata: Add a custom_fields attribute which has a list of dictionaries if
                you would like the fields to be added to your transaction when
                displayed on the dashboard.
                Sample: ``{"custom_fields":[{"display_name":"Cart ID",
                "variable_name": "cart_id","value": "8393"}]}``

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/subaccount")
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
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_subaccounts(
        self, start_date: str, end_date: str, page: int = 1, pagination: int = 50
    ) -> Response:
        """Fetch subaccounts available on your integration.

        Args:
            start_date: A timestamp from which to start listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            page: Specifies exactly what page you want to retrieve. If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/subaccount?perPage={pagination}")
        query_params = [
            ("from", start_date),
            ("to", end_date),
            ("page", page),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    async def get_subaccount(self, id_or_code: str) -> Response:
        """Get details of a subaccount on your integration.

        Args:
            id_or_code: The subaccount ``ID`` or ``code`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/subaccount/{id_or_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update(
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
        settlement_schedule: Optional[Schedule] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """Update a subaccount details on your integration.

        Args:
            id_or_code: Subaccount's ID or code
            business_name: Name of business for subaccount
            settlement_bank: Bank Code for the bank. You can get the
                list of Bank Codes by calling the ``.get_banks``
                method from the Miscellaneous API wrapper
            account_number: Bank Account Number
            active: Activate or deactivate a subaccount.
            percentage_charge: The default percentage charged when
                receiving on behalf of this subaccount
            description: A description for this subaccount
            primary_contact_email: A contact email for the subaccount
            primary_contact_name: A name for the contact person for this subaccount
            primary_contact_phone: A phone number to call for this subaccount
            settlement_schedule: ``Schedule.AUTO`` means payout is T+1 and manual means payout to the
                subaccount should only be made when requested.
                Defaults to ``Schedule.AUTO``
            metadata: Add a custom_fields attribute which has a list of dictionaries if you would
                like the fields to be added to your transaction when displayed on the
                dashboard. Sample: ``{"custom_fields":[{"display_name":"Cart ID",
                "variable_name": "cart_id","value": "8393"}]}``

        Returns:
            A named tuple containing the response gotten from paystack's server.
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
        url = self._parse_url(f"/subaccount/{id_or_code}")
        return await self._handle_request(HTTPMethod.PUT, url, payload)
