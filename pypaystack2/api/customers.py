from typing import Any, Optional

from ..baseapi import BaseAPI, Response
from ..errors import InvalidDataError
from ..utils import (
    add_to_payload,
    append_query_params,
    Identification,
    Country,
    RiskAction,
)


class Customer(BaseAPI):
    """Provides a wrapper for paystack Customer API

    The Customers API allows you create and manage customers on your integration.
    https://paystack.com/docs/api/#customer
    """

    def create(
        self,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> Response:
        """Create a customer on your integration

        Parameters
        ----------
        email: str
            Customer's email address
        first_name: Optional[str]
            Customer's first name
        last_name: Optional[str]
            Customer's last name
        phone: Optional[str]
            Customer's phone number
        metadata: Optional[dict[str,Any]]
            A dictionary that you can attach to the customer. It can be used
            to store additional information in a structured format.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        The `first_name`, `last_name` and `phone` are optional parameters. However,
        when creating a customer that would be assigned a Dedicated Virtual
        Account and your business catgeory falls under Betting, Financial
        services, and General Service, then these parameters become compulsory.
        """

        url = self._url("/customer/")
        payload = {
            "email": email,
        }
        optional_params = (
            ("first_name", first_name),
            ("last_name", last_name),
            (
                "phone",
                phone,
            ),
            ("metadata", metadata),
        )
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def get_customers(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page=1,
        pagination: int = 50,
    ) -> Response:
        """Fetches customers available on your integration.

        Parameters
        ----------
        start_date: Optional[str]
            A timestamp from which to start listing customers
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing customers
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        page: int
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = self._url(f"/customer/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_customer(self, email_or_code: str) -> Response:
        """Get details of a customer on your integration.

        Parameters
        ----------
        email_or_code: str
            An email or customer code for the customer you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/customer/{email_or_code}/")
        return self._handle_request("GET", url)

    def update(
        self,
        code: str,
        first_name: str,
        last_name: str,
        phone: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> Response:
        """Update a customer's details on your integration

        Parameters
        ----------
        code: str
            Customer's code
        first_name: str
            Customer's first name
        last_name: str
            Customer's last name
        phone: Optional[str]
            Customer's phone number
        metadata: Optional[dict[str, Any]]
            A dictionary that you can attach to the customer. It can be used
            to store additional information in a structured format.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/customer/{code}/")
        payload = {
            "first_name": first_name,
            "last_name": last_name,
        }

        optional_params = [
            (
                "phone",
                phone,
            ),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("PUT", url, payload)

    def validate(
        self,
        code: str,
        first_name: str,
        last_name: str,
        identification_type: Identification,
        identification_number: str,
        country: Country,
        bvn: str,
        bank_code: Optional[str] = None,
        account_number: Optional[str] = None,
        middle_name: Optional[str] = None,
    ) -> Response:
        """Validate a customer's identity

        Parameters
        ----------
        code: str
            Customer's code
        first_name: str
            Customer's first name
        last_name: str
            Customer's last name
        identification_type: Identification
            Enum of Identification e.g `Identification.BVN`
        identification_number: str
        country: Country
            Enum of Country e.g `Country.NIGERIA`
        bvn: str
            Customer's Bank Verification Number
        bank_code: Optional[str]
            You can get the list of Bank Codes by calling the
            Miscellaneous API `get_banks` method. (required if type is bank_account)
        account_number: Optional[str]
            Customer's bank account number. (required if type is bank_account)
        middle_name: Optional[str]
            Customer's middle name

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        if identification_type == Identification.BANK_ACCOUNT:
            if bank_code is None:
                raise InvalidDataError(
                    "`bank_code` is required if identification type is `Identification.BANK_ACCOUNT`"
                )
            if account_number is None:
                raise InvalidDataError(
                    "`account_number` is required if identification type is `Identification.BANK_ACCOUNT`"
                )

        url = self._url(f"/customer/{code}/identification")
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "type": identification_type,
            "value": identification_number,
            "country": country,
            "bvn": bvn,
        }
        optional_params = (
            ("bank_code", bank_code),
            ("account_number", account_number),
            ("middle_name", middle_name),
        )
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def flag(
        self,
        customer: str,
        risk_action: Optional[RiskAction] = None,
    ) -> Response:
        """Whitelist or blacklist a customer on your integration

        Parameters
        ----------
        customer: str
            Customer's code, or email address
        risk_action: Optional[RiskAction]
            One of the possible risk actions from the
            RiskAction enum e.g `RiskAction.DEFAULT`

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/customer/set_risk_action")
        payload = {
            "customer": customer,
        }
        optional_params = (("risk_action", risk_action),)
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def deactivate(
        self,
        auth_code: str,
    ) -> Response:
        """Deactivate an authorization when the card needs to be forgotten

        Parameters
        ----------
        auth_code: str
            Authorization code to be deactivated

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/customer/deactivate_authorization")
        payload = {
            "authorization_code": auth_code,
        }
        return self._handle_request("POST", url, payload)
