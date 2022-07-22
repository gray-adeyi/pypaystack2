from ..baseapi import BaseAPI, Response


class ControlPanel(BaseAPI):
    """Provides a wrapper for paystack Control Panel API

    The Control Panel API allows you manage some settings on your integration.
    https://paystack.com/docs/api/#control-panel
    """

    def get_payment_session_timeout(self) -> Response:
        """Fetch the payment session timeout on your integration

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/integration/payment_session_timeout")
        return self._handle_request("GET", url)

    def update_payment_session_timeout(self, timeout: int) -> Response:
        """Update the payment session timeout on your integration

        Parameters
        ----------
        timeout: int
            Time before stopping session (in seconds). Set to 0 to cancel session timeouts

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"timeout": timeout}
        url = self._url("/integration/payment_session_timeout")
        return self._handle_request("PUT", url, payload)
