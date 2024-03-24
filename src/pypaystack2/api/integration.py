from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import HTTPMethod, Response


class Integration(BaseAPI):
    """Provides a wrapper for paystack Integration API

    The Integration API allows you to manage some settings on your integration.
    https://paystack.com/docs/api/integration/
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


class AsyncIntegration(BaseAsyncAPI):
    """Provides a wrapper for paystack Integration API

    The Integration API allows you to manage some settings on your integration.
    https://paystack.com/docs/api/integration/
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
