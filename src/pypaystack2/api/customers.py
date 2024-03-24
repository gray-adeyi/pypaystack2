from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.exceptions import InvalidDataException
from pypaystack2.utils import (
    add_to_payload,
    HTTPMethod,
    append_query_params,
    Identification,
    Country,
    RiskAction,
    Response,
)


class Customer(BaseAPI):
    """Provides a wrapper for paystack Customer API

    The Customers API allows you to create and manage customers in your integration.
    https://paystack.com/docs/api/customer/
    """

    def create(
        self,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/customer/")
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
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_customers(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page: int = 1,
        pagination: int = 50,
    ) -> Response:
        """Fetches customers available on your integration.

        Args:
            start_date: A timestamp from which to start listing customers e.g., 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing customers e.g., 2016-09-24T00:00:05.000Z, 2016-09-21
            page: Specify exactly what page you want to retrieve. If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = self._parse_url(f"/customer/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_customer(self, email_or_code: str) -> Response:
        """Get details of a customer on your integration.

        Args:
            email_or_code: An email or customer code for the customer you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/customer/{email_or_code}/")
        return self._handle_request(HTTPMethod.GET, url)

    def update(
        self,
        code: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """Update a customer's details on your integration

        Args:
            code: Customer's code
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number
            metadata: A dictionary that you can attach to the customer. It can be used to store additional
                information in a structured format.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/customer/{code}/")
        payload = {}

        optional_params = [
            ("first_name", first_name),
            ("last_name", last_name),
            ("phone", phone),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.PUT, url, payload)

    def validate(
        self,
        email_or_code: str,
        first_name: str,
        last_name: str,
        identification_type: Identification,
        country: Country,
        bvn: str,
        identification_number: Optional[str] = None,
        bank_code: Optional[str] = None,
        account_number: Optional[str] = None,
        middle_name: Optional[str] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if identification_type == Identification.BANK_ACCOUNT:
            if bank_code is None:
                raise InvalidDataException(
                    "`bank_code` is required if identification type is `Identification.BANK_ACCOUNT`"
                )
            if account_number is None:
                raise InvalidDataException(
                    "`account_number` is required if identification type is `Identification.BANK_ACCOUNT`"
                )

        url = self._parse_url(f"/customer/{email_or_code}/identification")
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
        return self._handle_request(HTTPMethod.POST, url, payload)

    def flag(
        self,
        customer: str,
        risk_action: Optional[RiskAction] = None,
    ) -> Response:
        """Whitelist or blacklist a customer on your integration

        Args:
            customer: Customer's code, or email address
            risk_action: One of the possible risk actions from the RiskAction enum e.g `RiskAction.DEFAULT`

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/customer/set_risk_action")
        payload = {
            "customer": customer,
        }
        optional_params = [
            ("risk_action", risk_action),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def deactivate(
        self,
        auth_code: str,
    ) -> Response:
        """Deactivate an authorization when the card needs to be forgotten

        Args:
            auth_code: Authorization code to be deactivated

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/customer/deactivate_authorization")
        payload = {
            "authorization_code": auth_code,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)


class AsyncCustomer(BaseAsyncAPI):
    """Provides a wrapper for paystack Customer API

    The Customers API allows you to create and manage customers in your integration.
    https://paystack.com/docs/api/customer/
    """

    async def create(
        self,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/customer/")
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
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_customers(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page: int = 1,
        pagination: int = 50,
    ) -> Response:
        """Fetches customers available on your integration.

        Args:
            start_date: A timestamp from which to start listing customers e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing customers e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            page: Specify exactly what page you want to retrieve. If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = self._parse_url(f"/customer/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_customer(self, email_or_code: str) -> Response:
        """Get details of a customer on your integration.

        Args:
            email_or_code: An email or customer code for the customer you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/customer/{email_or_code}/")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update(
        self,
        code: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """Update a customer's details on your integration

        Args:
            code: Customer's code
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number
            metadata: A dictionary that you can attach to the customer. It can be used to store additional
                information in a structured format.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/customer/{code}/")
        payload = {}

        optional_params = [
            ("first_name", first_name),
            ("last_name", last_name),
            ("phone", phone),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def validate(
        self,
        email_or_code: str,
        first_name: str,
        last_name: str,
        identification_type: Identification,
        country: Country,
        bvn: str,
        identification_number: Optional[str] = None,
        bank_code: Optional[str] = None,
        account_number: Optional[str] = None,
        middle_name: Optional[str] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if identification_type == Identification.BANK_ACCOUNT:
            if bank_code is None:
                raise InvalidDataException(
                    "`bank_code` is required if identification type is `Identification.BANK_ACCOUNT`"
                )
            if account_number is None:
                raise InvalidDataException(
                    "`account_number` is required if identification type is `Identification.BANK_ACCOUNT`"
                )

        url = self._parse_url(f"/customer/{email_or_code}/identification")
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
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def flag(
        self,
        customer: str,
        risk_action: Optional[RiskAction] = None,
    ) -> Response:
        """Whitelist or blacklist a customer on your integration

        Args:
            customer: Customer's code, or email address
            risk_action: One of the possible risk actions from the RiskAction enum e.g `RiskAction.DEFAULT`

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/customer/set_risk_action")
        payload = {
            "customer": customer,
        }
        optional_params = [
            ("risk_action", risk_action),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def deactivate(
        self,
        auth_code: str,
    ) -> Response:
        """Deactivate an authorization when the card needs to be forgotten

        Args:
            auth_code: Authorization code to be deactivated

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/customer/deactivate_authorization")
        payload = {
            "authorization_code": auth_code,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)
