from typing import Optional

from ..baseapi import BaseAPI
from ..errors import InvalidDataError
from ..utils import (
    add_to_payload,
    append_query_params,
    Identification,
    Country,
    RiskAction,
)


class Customer(BaseAPI):
    def create(
        self,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        metadata: Optional[str] = None,
    ):
        """
        Creates a new paystack customer account

        args:
        email -- Customer's email address
        first_name-- Customer's first name (Optional)
        last_name-- Customer's last name (Optional)
        phone -- optional
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
    ):
        """
        Gets all the customers we have at paystack in steps of (default) 50 records per page.
        We can provide an optional pagination to indicate how many customer records we want to fetch per time

        args:
        pagination -- Count of data to return per call
        """
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = self._url(f"/customer/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_customer(self, email_or_code: str):
        """
        Gets the customer with the given user id

        args:
        customer_code -- The customer's code
        """
        url = self._url(f"/customer/{email_or_code}/")
        return self._handle_request("GET", url)

    def update(
        self,
        user_id: str,
        first_name: str,
        last_name: str,
        phone: Optional[str] = None,
        metadata: Optional[str] = None,
    ):
        """
        Update a customer account given the user id

        args:
        user_id -- id of the customer
        email -- Customer's email address
        first_name-- Customer's first name (Optional)
        last_name-- Customer's last name (Optional)
        phone -- optional
        """
        url = self._url(f"/customer/{user_id}/")
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
        customer_code: str,
        first_name: str,
        last_name: str,
        identification_type: Identification,
        identification_number: str,
        country: Country,
        bvn: str,
        bank_code: Optional[str] = None,
        account_number: Optional[str] = None,
        middle_name: Optional[str] = None,
    ):
        """
        Validate a customer's identity
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

        url = self._url(f"/customer/{customer_code}/identification")
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
    ):
        """
        Whitelist or blacklist a customer on your integration
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
    ):
        """
        Deactivate an authorization when the card needs to be forgotten
        """

        url = self._url("/customer/deactivate_authorization")
        payload = {
            "authorization_code": auth_code,
        }
        return self._handle_request("POST", url, payload)
