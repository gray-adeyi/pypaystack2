from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import HTTPMethod, Response


class ControlPanel(BaseAPI):
    """Provides a wrapper for paystack Control Panel API

    The Control Panel API allows you manage some settings on your integration.
    https://paystack.com/docs/api/#control-panel
    """

    def get_payment_session_timeout(self) -> Response:
        """Fetch the payment session timeout on your integration

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/integration/payment_session_timeout")
        return self._handle_request(HTTPMethod.GET, url)

    def update_payment_session_timeout(self, timeout: int) -> Response:
        """Update the payment session timeout on your integration

        Args:
            timeout: Time before stopping session (in seconds). Set to 0 to cancel session timeouts

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"timeout": timeout}
        url = self._parse_url("/integration/payment_session_timeout")
        return self._handle_request(HTTPMethod.PUT, url, payload)


class AsyncControlPanel(BaseAsyncAPI):
    """Provides a wrapper for paystack Control Panel API

    The Control Panel API allows you manage some settings on your integration.
    https://paystack.com/docs/api/#control-panel
    """

    async def get_payment_session_timeout(self) -> Response:
        """Fetch the payment session timeout on your integration

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/integration/payment_session_timeout")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update_payment_session_timeout(self, timeout: int) -> Response:
        """Update the payment session timeout on your integration

        Args:
            timeout: Time before stopping session (in seconds). Set to 0 to cancel session timeouts

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {"timeout": timeout}
        url = self._parse_url("/integration/payment_session_timeout")
        return await self._handle_request(HTTPMethod.PUT, url, payload)
