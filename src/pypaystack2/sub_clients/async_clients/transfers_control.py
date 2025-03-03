from http import HTTPMethod
from typing import Type

from pypaystack2.base_api_client import BaseAsyncAPIClient
from pypaystack2.utils.enums import Reason
from pypaystack2.utils.models import PaystackDataModel, Response
from pypaystack2.utils.response_models import BalanceLedgerItem, IntegrationBalance


class AsyncTransferControlClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Transfers Control API

    The Transfer Control API allows you to manage settings of your transfers.
    https://paystack.com/docs/api/transfer-control/
    """

    async def check_balance(
        self,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[list[IntegrationBalance]] | Response[PaystackDataModel]:
        """Fetch the available balance on your integration

        Args:
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
        url = self._full_url("/balance")
        return await self._handle_request(
            HTTPMethod.GET,
            url,  # type: ignore
            response_data_model_class=alternate_model_class or IntegrationBalance,
        )

    async def get_balance_ledger(
        self,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[list[BalanceLedgerItem]] | Response[PaystackDataModel]:
        """Fetch all pay-ins and pay-outs that occured on your integration

        Args:
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
        url = self._full_url("balance/ledger")
        return await self._handle_request(
            HTTPMethod.GET,
            url,  # type: ignore
            response_data_model_class=alternate_model_class or BalanceLedgerItem,
        )

    async def resend_otp(
        self,
        transfer_code: str,
        reason: Reason,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """
        Generates a new OTP and sends to customer in the event they are having trouble receiving one.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
            transfer_code: Transfer code
            reason: Any value from the ``Reason`` enum
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
        payload = {"transfer_code": transfer_code, "reason": reason}
        url = self._full_url("/transfer/resend_otp")
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,  # type: ignore
            response_data_model_class=alternate_model_class,
        )

    async def disable_otp(
        self,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """
        This is used in the event that you want to be able to complete transfers
        programmatically without use of OTPs. No arguments required. You will get
        an OTP to complete the request

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
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
        url = self._full_url("/transfer/disable_otp")
        return await self._handle_request(
            HTTPMethod.POST,
            url,  # type: ignore
            response_data_model_class=alternate_model_class,
        )

    async def finalize_disable_otp(
        self,
        otp: str,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Finalize the request to disable OTP on your transfers.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
            otp: One time password
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
        payload = {"otp": otp}
        url = self._full_url("/transfer/disable_otp_finalize")
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,  # type: ignore
            response_data_model_class=alternate_model_class,
        )

    async def enable_otp(
        self,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """
        In the event that a customer wants to stop being able to complete transfers
        programmatically, this endpoint helps turn OTP requirement back on. No
        arguments required.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
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
        url = self._full_url("/transfer/enable_otp")
        return await self._handle_request(
            HTTPMethod.POST,
            url,  # type: ignore
            response_data_model_class=alternate_model_class,
        )
