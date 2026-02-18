import httpx
from http import HTTPMethod
from typing import Any, Literal

from pypaystack2.base_clients import BaseAPIClient, add_to_payload, append_query_params
from pypaystack2.enums import Currency
from pypaystack2.types import PaystackDataModel


class VirtualTerminalClient(BaseAPIClient):
    """This client provides API for interacting with Paystack's Virtual Terminal API

    he Virtual Terminal API allows you to accept in-person payments without a POS device.
    """

    def create(
        self,
        name: str,
        destinations: list[dict[str, Any]],
        currency: Currency | None = None,
        custom_fields: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """Create a Virtual Terminal on your integration

        Args:
            name: The name of the Virtual Terminal
            destinations: A list of dictionaries containing the notificaiton recipients for
                payments to the Virtual Terminal. Each dictionary includes a `target` key,
                value pair for the Whatsapp phone number to send notifications to, and a
                `name` key, value pair for a descriptive label.
            metadata: Additional metadata.
            currency: The transaction currency for the Virtual Terminal. Defaults to your
                integration currency.
            custom_fields: A list of dictionaries representing custom fields to display on
                the form. each dictionary should contain a `display_name` key, value pair
                for representing what will be displayed on the Virtual Terminal page, and
                `variable_name` key, value pair for referenceing the custom field
                programmatically.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.


        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url("/virtual_terminal")
        payload = {
            "name": name,
            "destinations": destinations,
        }

        optional_params = [
            ("currency", currency),
            ("custom_fields", custom_fields),
        ]
        payload = add_to_payload(optional_params, payload)

        return self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def all(
        self,
        status: Literal["active", "inactive"] | None = None,
        pagination: int = 50,
        next_: str | None = None,
        search: str | None = None,
        previous: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        List virtual terminals on your integration.

        Args:
            status: Filter the terminals to retrieve by their statuses.
            pagination: How much terminals to retrieve in a call.
            search: Filter by search.
            next_: The next page cursor.
            previous: The previous page cursor.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/?perPage={pagination}")
        query_params = [
            ("status", status),
            ("search", search),
            ("next", next_),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    def get(
        self,
        code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        Retrieve a virtual terminal on your integration by it's code.

        Args:
            code: The code of the virtual terminal to retrieve.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/{code}")
        return self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    def update(
        self,
        code: str,
        name: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        Update a virtual terminal on your integration.

        Args:
            code: The code of the virtual terminal to update.
            name: The new name to assign to the virtual terminal.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/{code}")
        payload = {"name": name}
        return self._handle_request(
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def deactivate(
        self,
        code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        Deactivate a virtual terminal on your integration.

        Args:
            code: The code of the virtual terminal to update.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/{code}/deactivate")
        return self._handle_request(
            HTTPMethod.PUT,
            url,
            response_data_model_class=alternate_model_class,
        )

    def assign_destination(
        self,
        code: str,
        destinations: list[dict[str, Any]],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        Assign destinations (Whatsapp number) to a virtual terminal on your integration.

        Args:
            code: The code of the virtual terminal to update.
            destinations: A list of dictionaries containing the recipients for payments
                to the Virtual Terminal. Each dictionary must include a `target` key,
                value pair for the Wahtsapp phone number to send notifications to, and
                a `name` key, value pair for a descriptive label.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/{code}")
        payload = {"destinations": destinations}
        return self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def unassign_destination(
        self,
        code: str,
        targets: list[str],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        Unassign destinations (Whatsapp number) to a virtual terminal on your integration.

        Args:
            code: The code of the virtual terminal to update.
            targets: A list of phone numbers to unassign.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/{code}/destination/unassign")
        payload = {"targets": targets}
        return self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def add_split_code(
        self,
        code: str,
        split_code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        Add a split code to a virtual terminal on your integration.

        Args:
            code: The code of the virtual terminal to update.
            split_code: split code to be added to the virtual terminal

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/{code}/split_code")
        payload = {"split_code": split_code}
        return self._handle_request(
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def remove_split_code(
        self,
        code: str,
        split_code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """
        Remove a split code to a virtual terminal on your integration.

        Args:
            code: The code of the virtual terminal to update.
            split_code: split code to be removed to the virtual terminal

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/virtual_terminal/{code}/split_code")
        payload = {
            "split_code": split_code,
        }
        raw_response = httpx.request(
            HTTPMethod.DELETE, url, json=payload, headers=self._headers
        )
        return self._deserialize_response(
            raw_response,
            response_data_model_class=alternate_model_class,
        )
