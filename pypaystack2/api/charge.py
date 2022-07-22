from typing import Any, Mapping, Optional

from ..baseapi import BaseAPI, Response
from ..utils import add_to_payload, validate_amount


class Charge(BaseAPI):
    """Provides a wrapper for paystack Charge API

    The Charge API allows you to configure payment channel of your choice when initiating a payment.
    https://paystack.com/docs/api/#charge

    """

    def charge(
        self,
        email: str,
        amount: int,
        bank: Optional[dict[str, Any]] = None,
        auth_code: Optional[str] = None,
        pin: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        reference: Optional[str] = None,
        ussd: Optional[dict[str, Any]] = None,
        mobile_money: Optional[dict[str, Any]] = None,
        device_id: Optional[str] = None,
    ) -> Response:
        """Initiate a payment by integrating the payment channel of your choice.

        Parameters
        ----------
        email: str
            Customer's email address
        amount: int
            Amount should be in kobo if currency is NGN, pesewas, if currency is GHS,
            and cents, if currency is ZAR
        bank: Optional[dict[str,Any]]
            Bank account to charge (don't send if charging an authorization code)
        auth_code: Optional[str]
            An authorization code to charge (don't send if charging a bank account)
        pin: Optional[str]
            4-digit PIN (send with a non-reusable authorization code)
        metadata: Optional[dict[str, Any]]
            A dictionary of data.
        reference: Optional[str]
            Unique transaction reference. Only -, .\`, = and alphanumeric characters allowed.
        ussd: Optional[dict[str, Any]]
            USSD type to charge (don't send if charging an authorization code, bank or card)
        mobile_money: Optional[dict[str, Any]]
            Mobile details (don't send if charging an authorization code, bank or card)
        device_id: str
            This is the unique identifier of the device a user uses in making payment. Only -, .\`,
            = and alphanumeric characters allowed.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)
        payload = {"email": email, "amount": amount}
        optional_params = [
            ("bank", bank),
            ("authorization_code", auth_code),
            ("pin", pin),
            ("metadata", metadata),
            ("reference", reference),
            ("ussd", ussd),
            ("mobile_money", mobile_money),
            ("device_id", device_id),
        ]
        payload = add_to_payload(optional_params, payload)
        url = self._url("/charge")
        return self._handle_request("POST", url, payload)

    def submit_pin(self, pin: str, reference: str) -> Response:
        """Submit PIN to continue a charge

        Parameters
        ----------
        pin: str
            PIN submitted by user
        reference: str
            Reference for transaction that requested pin

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"pin": pin, "reference": reference}
        url = self._url("/charge/submit_pin")
        return self._handle_request("POST", url, payload)

    def submit_OTP(self, otp: str, reference: str) -> Response:
        """Submit OTP to complete a charge

        Parameters
        ----------
        otp: str
            OTP submitted by user
        reference: str
            Reference for ongoing transaction

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"otp": otp, "reference": reference}
        url = self._url("/charge/submit_otp")
        return self._handle_request("POST", url, payload)

    def submit_phone(self, phone: str, reference: str) -> Response:
        """Submit Phone when requested

        Parameters
        ----------
        phone: str
            Phone submitted by user
        reference:str
            Reference for ongoing transaction

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"phone": phone, "reference": reference}
        url = self._url("/charge/submit_phone")
        return self._handle_request("POST", url, payload)

    def submit_birthday(self, date: str, reference: str) -> Response:
        """Submit Birthday when requested

        Parameters
        ----------
        date: str
            Birthday submitted by user. ISO Format e.g. 2016-09-21
        reference: str
            Reference for ongoing transaction

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"date": date, "reference": reference}
        url = self._url("/charge/submit_birthday")
        return self._handle_request("POST", url, payload)

    def set_address(
        self,
        address: str,
        reference: str,
        city: str,
        state: str,
        zipcode: str,
    ) -> Response:
        """Submit address to continue a charge

        Parameters
        ----------
        address: str
            Address submitted by user
        reference: str
            Reference for ongoing transaction
        city: str
            City submitted by user
        state: str
            State submitted by user
        zipcode: str
            Zipcode submitted by user

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {
            "address": address,
            "reference": reference,
            "city": city,
            "state": state,
            "zipcode": zipcode,
        }
        url = self._url("/charge/submit_address")
        return self._handle_request("POST", url, payload)

    def check_pending_charge(self, reference: str) -> Response:
        """
        When you get "pending" as a charge status or if there was an
        exception when calling any of the /charge endpoints, wait 10
        seconds or more, then make a check to see if its status has changed.
        Don't call too early as you may get a lot more pending than you should.

        Parameters
        ----------
        reference: str
            The reference to check

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/charge/{reference}")
        return self._handle_request("GET", url)
