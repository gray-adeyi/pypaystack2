from ..baseapi import BaseAPI


class TransferControl(BaseAPI):
    """
    The Transfers API allows you
    automate sending money on
    your integration
    """

    def check_balance(self):
        """ """
        url = self._url("/balance")
        return self._handle_request("GET", url)

    def get_balance_ledger(self):
        """ """
        url = self._url("balance/ledger")
        return self._handle_request("GET", url)

    def resend_otp(self, transfer_code: str, reason: str):
        """ """
        payload = {"transfer_code": transfer_code, "reason": reason}
        url = self._url("/transfer/resend_otp")
        return self._handle_request("POST", url, payload)

    def disable_otp(self):
        """ """
        url = self._url("/transfer/disable_otp")
        return self._handle_request("POST", url)

    def finalize_disable_otp(self, otp: str):
        """ """
        payload = {"otp": otp}
        url = self._url("/transfer/disable_otp_finalize")
        return self._handle_request("POST", url, payload)

    def enable_otp(self):
        """ """
        url = self._url("/transfer/enable_otp")
        return self._handle_request("POST", url)
