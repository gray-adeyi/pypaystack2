from pypaystack2.utils import Reason
from ..baseapi import BaseAPI, Response


class TransferControl(BaseAPI):
    """Provides a wrapper for paystack Transfers Control API

    The Transfers Control API allows you manage settings of your transfers.
    https://paystack.com/docs/api/#transfer-control
    """

    def check_balance(self) -> Response:
        """Fetch the available balance on your integration

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url("/balance")
        return self._handle_request("GET", url)

    def get_balance_ledger(self) -> Response:
        """Fetch all pay-ins and pay-outs that occured on your integration

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url("balance/ledger")
        return self._handle_request("GET", url)

    def resend_OTP(self, transfer_code: str, reason: Reason) -> Response:
        """
        Generates a new OTP and sends to customer in the event they are having trouble receiving one.

        Parameters
        ----------
        transfer_code: str
            Transfer code
        reason: Reason
            Any value from the ``Reason`` enum

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Feature Availability
            This feature is only available to businesses in Nigeria and Ghana.
        """
        payload = {"transfer_code": transfer_code, "reason": reason}
        url = self._url("/transfer/resend_otp")
        return self._handle_request("POST", url, payload)

    def disable_OTP(self) -> Response:
        """
        This is used in the event that you want to be able to complete transfers
        programmatically without use of OTPs. No arguments required. You will get
        an OTP to complete the request

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Feature Availability
            This feature is only available to businesses in Nigeria and Ghana.
        """
        url = self._url("/transfer/disable_otp")
        return self._handle_request("POST", url)

    def finalize_disable_OTP(self, otp: str) -> Response:
        """Finalize the request to disable OTP on your transfers.

        Parameters
        ----------
        otp: str

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Feature Availability
            This feature is only available to businesses in Nigeria and Ghana.
        """
        payload = {"otp": otp}
        url = self._url("/transfer/disable_otp_finalize")
        return self._handle_request("POST", url, payload)

    def enable_OTP(self) -> Response:
        """
        In the event that a customer wants to stop being able to complete transfers
        programmatically, this endpoint helps turn OTP requirement back on. No
        arguments required.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Feature Availability
            This feature is only available to businesses in Nigeria and Ghana.
        """
        url = self._url("/transfer/enable_otp")
        return self._handle_request("POST", url)
