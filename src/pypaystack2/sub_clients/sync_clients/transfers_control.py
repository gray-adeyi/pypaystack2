from http import HTTPMethod

from pypaystack2.base_clients import BaseAPIClient
from pypaystack2.enums import Reason
from pypaystack2.models import Response
from pypaystack2.models.response_models import IntegrationBalance, BalanceLedgerItem
from pypaystack2.types import PaystackDataModel


class TransferControlClient(BaseAPIClient):
    """Provides a wrapper for paystack Transfers Control API

    The Transfer Control API allows you to manage settings of your transfers.
    https://paystack.com/docs/api/transfer-control/
    """

    def check_balance(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
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
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or IntegrationBalance,
        )

    def get_balance_ledger(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[BalanceLedgerItem]] | Response[PaystackDataModel]:
        """Fetch all pay-ins and pay-outs that occurred on your integration

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
        url = self._full_url("/balance/ledger")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or BalanceLedgerItem,
        )

    def resend_otp(
        self,
        transfer_code: str,
        reason: Reason,
        alternate_model_class: type[PaystackDataModel] | None = None,
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
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def disable_otp(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
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
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )

    def finalize_disable_otp(
        self,
        otp: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
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
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def enable_otp(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
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
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )
