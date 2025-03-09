from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import BaseAsyncAPIClient, add_to_payload
from pypaystack2.models import Response
from pypaystack2.models.response_models import Transaction
from pypaystack2.types import PaystackDataModel


class AsyncChargeClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Charge API

    The Charge API allows you to configure a payment channel of your choice when initiating a payment.
    https://paystack.com/docs/api/charge/

    """

    async def charge(
        self,
        email: str,
        amount: int,
        bank: dict[str, Any] | None = None,
        bank_transfer: dict[str, Any] | None = None,
        auth_code: str | None = None,
        pin: str | None = None,
        metadata: dict[str, Any] | None = None,
        reference: str | None = None,
        ussd: dict[str, Any] | None = None,
        mobile_money: dict[str, Any] | None = None,
        device_id: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
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
        url = self._full_url("/charge")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def submit_pin(
        self,
        pin: str,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """Submit PIN to continue a charge

        Args:
            pin: PIN submitted by user
            reference: Reference for transaction that requested pin
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

        payload = {"pin": pin, "reference": reference}
        url = self._full_url("/charge/submit_pin")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def submit_otp(
        self,
        otp: str,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """Submit OTP to complete a charge

        Args:
            otp: OTP submitted by user
            reference: Reference for ongoing transaction
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

        payload = {"otp": otp, "reference": reference}
        url = self._full_url("/charge/submit_otp")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def submit_phone(
        self,
        phone: str,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """Submit Phone when requested

        Args:
            phone: Phone submitted by user
            reference: Reference for ongoing transaction
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

        payload = {"phone": phone, "reference": reference}
        url = self._full_url("/charge/submit_phone")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def submit_birthday(
        self,
        birthday: str,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """Submit Birthday when requested

        Args:
            birthday: Birthday submitted by user. ISO Format e.g. 2016-09-21
            reference: Reference for ongoing transaction
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

        payload = {"birthday": birthday, "reference": reference}
        url = self._full_url("/charge/submit_birthday")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def set_address(
        self,
        address: str,
        reference: str,
        city: str,
        state: str,
        zipcode: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """Submit address to continue a charge

        Args:
            address: Address submitted by user
            reference: Reference for ongoing transaction
            city: City submitted by user
            state: State submitted by user
            zipcode: Zipcode submitted by user
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
            "address": address,
            "reference": reference,
            "city": city,
            "state": state,
            "zip_code": zipcode,
        }
        url = self._full_url("/charge/submit_address")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def check_pending_charge(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """
        When you get "pending" as a charge status or if there was an
        exception when calling any of the /charge endpoints, wait 10
        seconds or more, then make a check to see if its status has changed.
        Don't call too early as you may get a lot more pending than you should.

        Args:
            reference: The reference to check
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

        url = self._full_url(f"/charge/{reference}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transaction,
        )
