from typing import Mapping, Optional

from ..baseapi import BaseAPI
from ..utils import add_to_payload, validate_amount


class Charge(BaseAPI):
    """
    The Charge API allows you to configure
    payment channel of your choice when
    initiating a payment.
    """

    def charge(
        self,
        email: str,
        amount: int,
        bank: Optional[Mapping] = None,
        auth_code: Optional[str] = None,
        pin: Optional[str] = None,
        metadata: Optional[Mapping] = None,
        reference: Optional[str] = None,
        ussd: Optional[Mapping] = None,
        mobile_money: Optional[Mapping] = None,
        device_id: Optional[str] = None,
    ):
        """ """
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

    def submit_pin(self, pin: int, reference: str):
        """ """
        payload = {"pin": pin, "reference": reference}
        url = self._url("/charge/submit_pin")
        return self._handle_request("POST", url, payload)

    def submit_OTP(self, otp: str, reference: str):
        """ """
        payload = {"otp": otp, "reference": reference}
        url = self._url("/charge/submit_otp")
        return self._handle_request("POST", url, payload)

    def submit_phone(self, phone: str, reference: str):
        """ """
        payload = {"phone": phone, "reference": reference}
        url = self._url("/charge/submit_phone")
        return self._handle_request("POST", url, payload)

    def submit_birthday(self, date: str, reference: str):
        """ """
        payload = {"date": date, "reference": reference}
        url = self._url("/charge/submit_birthday")
        return self._handle_request("POST", url, payload)

    def submit_address(
        self,
        address: str,
        reference: str,
        city: str,
        state: str,
        zipcode: str,
    ):
        """ """
        payload = {
            "address": address,
            "reference": reference,
            "city": city,
            "state": state,
            "zipcode": zipcode,
        }
        url = self._url("/charge/submit_address")
        return self._handle_request("POST", url, payload)

    def check_pending_charge(self, reference: str):
        url = self._url(f"/charge/{reference}")
        return self._handle_request("GET", url)
