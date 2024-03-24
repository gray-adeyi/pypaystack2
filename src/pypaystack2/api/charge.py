from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import validate_amount, add_to_payload, HTTPMethod, Response


class Charge(BaseAPI):
    """Provides a wrapper for paystack Charge API

    The Charge API allows you to configure a payment channel of your choice when initiating a payment.
    https://paystack.com/docs/api/charge/

    """

    def charge(
        self,
        email: str,
        amount: int,
        bank: Optional[dict] = None,
        bank_transfer: Optional[dict] = None,
        auth_code: Optional[str] = None,
        pin: Optional[str] = None,
        metadata: Optional[dict] = None,
        reference: Optional[str] = None,
        ussd: Optional[dict] = None,
        mobile_money: Optional[dict] = None,
        device_id: Optional[str] = None,
    ) -> Response:
        """Initiate a payment by integrating the payment channel of your choice.

        Args:
            email: Customer's email address
            amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS,
                and cents, if currency is ZAR
            bank: Bank account to charge (don't send if charging an authorization code)
            bank_transfer: Takes the settings for the Pay with Transfer (PwT) channel. Pass in the
                account_expires_at param to set the expiry time.
            auth_code: An authorization code to charge (don't send if charging a bank account)
            pin: 4-digit PIN (send with a non-reusable authorization code)
            metadata: A dictionary of data.
            reference: Unique transaction reference. Only -, .\\`, = and alphanumeric characters allowed.
            ussd: USSD type to charge (don't send if charging an authorization code, bank or card)
            mobile_money: Mobile details (don't send if charging an authorization code, bank or card)
            device_id: This is the unique identifier of the device a user uses in making payment. Only -, .\\`,
                = and alphanumeric characters allowed.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)
        payload = {"email": email, "amount": amount}
        optional_params = [
            ("bank", bank),
            ("bank_transfer", bank_transfer),
            ("authorization_code", auth_code),
            ("pin", pin),
            ("metadata", metadata),
            ("reference", reference),
            ("ussd", ussd),
            ("mobile_money", mobile_money),
            ("device_id", device_id),
        ]
        payload = add_to_payload(optional_params, payload)
        url = self._parse_url("/charge")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def submit_pin(self, pin: str, reference: str) -> Response:
        """Submit PIN to continue a charge

        Args:
            pin: PIN submitted by user
            reference: Reference for transaction that requested pin

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"pin": pin, "reference": reference}
        url = self._parse_url("/charge/submit_pin")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def submit_otp(self, otp: str, reference: str) -> Response:
        """Submit OTP to complete a charge

        Args:
            otp: OTP submitted by user
            reference: Reference for ongoing transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"otp": otp, "reference": reference}
        url = self._parse_url("/charge/submit_otp")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def submit_phone(self, phone: str, reference: str) -> Response:
        """Submit Phone when requested

        Args:
            phone: Phone submitted by user
            reference: Reference for ongoing transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"phone": phone, "reference": reference}
        url = self._parse_url("/charge/submit_phone")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def submit_birthday(self, birthday: str, reference: str) -> Response:
        """Submit Birthday when requested

        Args:
            birthday: Birthday submitted by user. ISO Format e.g. 2016-09-21
            reference: Reference for ongoing transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"birthday": birthday, "reference": reference}
        url = self._parse_url("/charge/submit_birthday")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def set_address(
        self,
        address: str,
        reference: str,
        city: str,
        state: str,
        zipcode: str,
    ) -> Response:
        """Submit address to continue a charge

        Args:
            address: Address submitted by user
            reference: Reference for ongoing transaction
            city: City submitted by user
            state: State submitted by user
            zipcode: sZipcode submitted by user

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {
            "address": address,
            "reference": reference,
            "city": city,
            "state": state,
            "zip_code": zipcode,
        }
        url = self._parse_url("/charge/submit_address")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def check_pending_charge(self, reference: str) -> Response:
        """
        When you get "pending" as a charge status or if there was an
        exception when calling any of the /charge endpoints, wait 10
        seconds or more, then make a check to see if its status has changed.
        Don't call too early as you may get a lot more pending than you should.

        Args:
            reference: The reference to check

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/charge/{reference}")
        return self._handle_request(HTTPMethod.GET, url)


class AsyncCharge(BaseAsyncAPI):
    """Provides a wrapper for paystack Charge API

    The Charge API allows you to configure a payment channel of your choice when initiating a payment.
    https://paystack.com/docs/api/charge/

    """

    async def charge(
        self,
        email: str,
        amount: int,
        bank: Optional[dict] = None,
        bank_transfer: Optional[dict] = None,
        auth_code: Optional[str] = None,
        pin: Optional[str] = None,
        metadata: Optional[dict] = None,
        reference: Optional[str] = None,
        ussd: Optional[dict] = None,
        mobile_money: Optional[dict] = None,
        device_id: Optional[str] = None,
    ) -> Response:
        """Initiate a payment by integrating the payment channel of your choice.

        Args:
            email: Customer's email address
            amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS,
                and cents, if currency is ZAR
            bank: Bank account to charge (don't send if charging an authorization code)
            bank_transfer: Takes the settings for the Pay with Transfer (PwT) channel. Pass in the
                account_expires_at param to set the expiry time.
            auth_code: An authorization code to charge (don't send if charging a bank account)
            pin: 4-digit PIN (send with a non-reusable authorization code)
            metadata: A dictionary of data.
            reference: Unique transaction reference. Only -, .\\`, = and alphanumeric characters allowed.
            ussd: USSD type to charge (don't send if charging an authorization code, bank or card)
            mobile_money: Mobile details (don't send if charging an authorization code, bank or card)
            device_id: This is the unique identifier of the device a user uses in making payment. Only -, .\\`,
                = and alphanumeric characters allowed.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)
        payload = {"email": email, "amount": amount}
        optional_params = [
            ("bank", bank),
            ("bank_transfer", bank_transfer),
            ("authorization_code", auth_code),
            ("pin", pin),
            ("metadata", metadata),
            ("reference", reference),
            ("ussd", ussd),
            ("mobile_money", mobile_money),
            ("device_id", device_id),
        ]
        payload = add_to_payload(optional_params, payload)
        url = self._parse_url("/charge")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def submit_pin(self, pin: str, reference: str) -> Response:
        """Submit PIN to continue a charge

        Args:
            pin: PIN submitted by user
            reference: Reference for transaction that requested pin

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"pin": pin, "reference": reference}
        url = self._parse_url("/charge/submit_pin")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def submit_otp(self, otp: str, reference: str) -> Response:
        """Submit OTP to complete a charge

        Args:
            otp: OTP submitted by user
            reference: Reference for ongoing transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"otp": otp, "reference": reference}
        url = self._parse_url("/charge/submit_otp")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def submit_phone(self, phone: str, reference: str) -> Response:
        """Submit Phone when requested

        Args:
            phone: Phone submitted by user
            reference: Reference for ongoing transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"phone": phone, "reference": reference}
        url = self._parse_url("/charge/submit_phone")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def submit_birthday(self, birthday: str, reference: str) -> Response:
        """Submit Birthday when requested

        Args:
            birthday: Birthday submitted by user. ISO Format e.g. 2016-09-21
            reference: Reference for ongoing transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"birthday": birthday, "reference": reference}
        url = self._parse_url("/charge/submit_birthday")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def set_address(
        self,
        address: str,
        reference: str,
        city: str,
        state: str,
        zipcode: str,
    ) -> Response:
        """Submit address to continue a charge

        Args:
            address: Address submitted by user
            reference: Reference for ongoing transaction
            city: City submitted by user
            state: State submitted by user
            zipcode: sZipcode submitted by user

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {
            "address": address,
            "reference": reference,
            "city": city,
            "state": state,
            "zip_code": zipcode,
        }
        url = self._parse_url("/charge/submit_address")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def check_pending_charge(self, reference: str) -> Response:
        """
        When you get "pending" as a charge status or if there was an
        exception when calling any of the /charge endpoints, wait 10
        seconds or more, then make a check to see if its status has changed.
        Don't call too early as you may get a lot more pending than you should.

        Args:
            reference: The reference to check

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/charge/{reference}")
        return await self._handle_request(HTTPMethod.GET, url)
