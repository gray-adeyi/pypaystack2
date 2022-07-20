from ..baseapi import BaseAPI


class ControlPanel(BaseAPI):
    """
    The Control Panel API allows
    you manage some settings on
    your integration
    """

    def get_payment_session_timeout(self):
        """ """
        url = self._url("/integration/payment_session_timeout")
        return self._handle_request("GET", url)

    def update_payment_session_timeout(self, timeout: int):
        """ """
        payload = {"timeout": timeout}
        url = self._url("/integration/payment_session_timeout")
        return self._handle_request("PUT", url, payload)
