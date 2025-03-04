from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import (
    BaseAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Country, RiskAction, Identification
from pypaystack2.models import Response
from pypaystack2.models.response_models import Customer
from pypaystack2.types import PaystackDataModel


class CustomerClient(BaseAPIClient):
    """Provides a wrapper for paystack Customer API

    The Customers API allows you to create and manage customers in your integration.
    https://paystack.com/docs/api/customer/
    """

    def create(
        self,
        email: str,
        first_name: str | None = None,
        last_name: str | None = None,
        phone: str | None = None,
        metadata: dict[str, Any] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Customer] | Response[PaystackDataModel]:
        """Create a customer on your integration.

        Note:
            The `first_name`, `last_name` and `phone` are optional parameters. However,
            when creating a customer that would be assigned a Dedicated Virtual
            Account and your business category falls under Betting, Financial
            services, and General Service, then these parameters become compulsory.

        Args:
            email: Customer's email address
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number
            metadata: A dictionary that you can attach to the customer. It can be used
                to store additional information in a structured format.
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

        url = self._full_url("/customer/")
        payload = {
            "email": email,
        }
        optional_params = [
            ("first_name", first_name),
            ("last_name", last_name),
            ("phone", phone),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Customer,
        )

    def get_customers(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Customer]] | Response[PaystackDataModel]:
        """Fetches customers available on your integration.

        Args:
            start_date: A timestamp from which to start listing customers e.g., 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing customers e.g., 2016-09-24T00:00:05.000Z, 2016-09-21
            page: Specify exactly what page you want to retrieve. If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
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

        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = self._full_url(f"/customer/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Customer,
        )

    def get_customer(
        self,
        email_or_code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Customer] | Response[PaystackDataModel]:
        """Get details of a customer on your integration.

        Args:
            email_or_code: An email or customer code for the customer you want to fetch
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

        url = self._full_url(f"/customer/{email_or_code}/")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Customer,
        )

    def update(
        self,
        code: str,
        first_name: str | None = None,
        last_name: str | None = None,
        phone: str | None = None,
        metadata: dict[str, Any] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Customer] | Response[PaystackDataModel]:
        """Update a customer's details on your integration

        Args:
            code: Customer's code
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number
            metadata: A dictionary that you can attach to the customer. It can be used to store additional
                information in a structured format.
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

        url = self._full_url(f"/customer/{code}/")
        payload: dict[str, Any] = {}
        optional_params = [
            ("first_name", first_name),
            ("last_name", last_name),
            ("phone", phone),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or Customer,
        )

    def validate(
        self,
        email_or_code: str,
        first_name: str,
        last_name: str,
        identification_type: Identification,
        country: Country,
        bvn: str,
        identification_number: str | None = None,
        bank_code: str | None = None,
        account_number: str | None = None,
        middle_name: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Validate a customer's identity

        Args:
            email_or_code: Customer's email or code
            first_name: Customer's first name
            last_name: Customer's last name
            identification_type: Enum of Identification e.g `Identification.BVN`
            identification_number: An identification number based on the `identification_type`
            country: Customer's Country e.g `Country.NIGERIA`
            bvn: Customer's Bank Verification Number
            bank_code: You can get the list of Bank Codes by calling the
                Miscellaneous API `get_banks` method. (required if type is bank_account)
            account_number: Customer's bank account number. (required if type is bank_account)
            middle_name: Customer's middle name
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

        if identification_type == Identification.BANK_ACCOUNT:
            if bank_code is None:
                raise ValueError(
                    "`bank_code` is required if identification type is `Identification.BANK_ACCOUNT`"
                )
            if account_number is None:
                raise ValueError(
                    "`account_number` is required if identification type is `Identification.BANK_ACCOUNT`"
                )

        url = self._full_url(f"/customer/{email_or_code}/identification")
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "type": identification_type,
            "country": country,
            "bvn": bvn,
        }
        optional_params = [
            ("bank_code", bank_code),
            ("account_number", account_number),
            ("middle_name", middle_name),
            ("value", identification_number),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def flag(
        self,
        customer: str,
        risk_action: RiskAction | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Customer] | Response[PaystackDataModel]:
        """Whitelist or blacklist a customer on your integration

        Args:
            customer: Customer's code, or email address
            risk_action: One of the possible risk actions from the RiskAction enum e.g `RiskAction.DEFAULT`
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

        url = self._full_url("/customer/set_risk_action")
        payload = {
            "customer": customer,
        }
        optional_params = [
            ("risk_action", risk_action),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Customer,
        )

    def deactivate(
        self,
        auth_code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Deactivate an authorization when the card needs to be forgotten

        Args:
            auth_code: Authorization code to be deactivated
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

        url = self._full_url("/customer/deactivate_authorization")
        payload = {
            "authorization_code": auth_code,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )
