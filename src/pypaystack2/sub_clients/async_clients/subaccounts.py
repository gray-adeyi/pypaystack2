from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Schedule
from pypaystack2.models import Response
from pypaystack2.models.response_models import SubAccount
from pypaystack2.types import PaystackDataModel


class AsyncSubAccountClient(BaseAsyncAPIClient):
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
        percentage_charge: float | int,
        description: str | None = None,
        primary_contact_email: str | None = None,
        primary_contact_name: str | None = None,
        primary_contact_phone: str | None = None,
        metadata: dict[str, Any] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[SubAccount] | Response[PaystackDataModel]:
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
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url("/subaccount")
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
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or SubAccount,
        )

    async def get_subaccounts(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[SubAccount]] | Response[PaystackDataModel]:
        """Fetch subaccounts available on your integration.

        Args:
            start_date: A timestamp from which to start listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            page: Specifies exactly what page you want to retrieve. If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/subaccount?perPage={pagination}")
        query_params = [
            ("from", start_date),
            ("to", end_date),
            ("page", page),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or SubAccount,
        )

    async def get_subaccount(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[SubAccount] | Response[PaystackDataModel]:
        """Get details of a subaccount on your integration.

        Args:
            id_or_code: The subaccount ``ID`` or ``code`` you want to fetch
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/subaccount/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or SubAccount,
        )

    async def update(
        self,
        id_or_code: int | str,
        business_name: str | None = None,
        settlement_bank: str | None = None,
        account_number: str | None = None,
        active: bool | None = None,
        percentage_charge: float | int | None = None,
        description: str | None = None,
        primary_contact_email: str | None = None,
        primary_contact_name: str | None = None,
        primary_contact_phone: str | None = None,
        settlement_schedule: Schedule | None = None,
        metadata: dict[str, Any] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[SubAccount] | Response[PaystackDataModel]:
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
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
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
        url = self._full_url(f"/subaccount/{id_or_code}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or SubAccount,
        )
