from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import Reason, HTTPMethod, Response


class TransferControl(BaseAPI):
    """Provides a wrapper for paystack Transfers Control API

    The Transfer Control API allows you to manage settings of your transfers.
    https://paystack.com/docs/api/transfer-control/
    """

    def check_balance(self) -> Response:
        """Fetch the available balance on your integration

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/balance")
        return self._handle_request(HTTPMethod.GET, url)

    def get_balance_ledger(self) -> Response:
        """Fetch all pay-ins and pay-outs that occured on your integration

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/balance/ledger")
        print(url)
        return self._handle_request(HTTPMethod.GET, url)

    def resend_otp(self, transfer_code: str, reason: Reason) -> Response:
        """
        Generates a new OTP and sends to customer in the event they are having trouble receiving one.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
            transfer_code: Transfer code
            reason: Any value from the ``Reason`` enum

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        payload = {"transfer_code": transfer_code, "reason": reason}
        url = self._parse_url("/transfer/resend_otp")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def disable_otp(self) -> Response:
        """
        This is used in the event that you want to be able to complete transfers
        programmatically without use of OTPs. No arguments required. You will get
        an OTP to complete the request

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/transfer/disable_otp")
        return self._handle_request(HTTPMethod.POST, url)

    def finalize_disable_otp(self, otp: str) -> Response:
        """Finalize the request to disable OTP on your transfers.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
            otp: One time password

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        payload = {"otp": otp}
        url = self._parse_url("/transfer/disable_otp_finalize")
        return self._handle_request(HTTPMethod.POST, url, payload)

    def enable_otp(self) -> Response:
        """
        In the event that a customer wants to stop being able to complete transfers
        programmatically, this endpoint helps turn OTP requirement back on. No
        arguments required.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/transfer/enable_otp")
        return self._handle_request(HTTPMethod.POST, url)


class AsyncTransferControl(BaseAsyncAPI):
    """Provides a wrapper for paystack Transfers Control API

    The Transfer Control API allows you to manage settings of your transfers.
    https://paystack.com/docs/api/transfer-control/
    """

    async def check_balance(self) -> Response:
        """Fetch the available balance on your integration

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/balance")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_balance_ledger(self) -> Response:
        """Fetch all pay-ins and pay-outs that occured on your integration

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("balance/ledger")
        return await self._handle_request(HTTPMethod.GET, url)

    async def resend_otp(self, transfer_code: str, reason: Reason) -> Response:
        """
        Generates a new OTP and sends to customer in the event they are having trouble receiving one.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
            transfer_code: Transfer code
            reason: Any value from the ``Reason`` enum

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        payload = {"transfer_code": transfer_code, "reason": reason}
        url = self._parse_url("/transfer/resend_otp")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def disable_otp(self) -> Response:
        """
        This is used in the event that you want to be able to complete transfers
        programmatically without use of OTPs. No arguments required. You will get
        an OTP to complete the request

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/transfer/disable_otp")
        return await self._handle_request(HTTPMethod.POST, url)

    async def finalize_disable_otp(self, otp: str) -> Response:
        """Finalize the request to disable OTP on your transfers.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Args:
            otp: One time password

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        payload = {"otp": otp}
        url = self._parse_url("/transfer/disable_otp_finalize")
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def enable_otp(self) -> Response:
        """
        In the event that a customer wants to stop being able to complete transfers
        programmatically, this endpoint helps turn OTP requirement back on. No
        arguments required.

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria and Ghana.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/transfer/enable_otp")
        return await self._handle_request(HTTPMethod.POST, url)
