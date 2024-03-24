from typing import Optional

import httpx
from httpx import codes

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import HTTPMethod, Response, append_query_params


class ApplePay(BaseAPI):
    """Provides a wrapper for paystack Apple Pay API

    The Apple Pay API allows you to register your application's top-level domain or subdomain.
    see https://paystack.com/docs/api/apple-pay/

    Note
      This feature is available to businesses in all markets except South Africa.
    """

    def register_domain(self, domain_name: str) -> Response:
        """Register a top-level domain or subdomain for your Apple Pay integration.

        Note
            * This method can only be called with one domain or subdomain at a time.
            * This feature is available to businesses in all markets except South Africa.


        Args:
            domain_name: Domain name to be registered.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_domains(
        self,
        use_cursor: bool = False,
        next: Optional[str] = None,
        previous: Optional[str] = None,
    ) -> Response:
        """Fetches all registered domains on your integration.

        Note
            * This feature is available to businesses in all markets except South Africa.

        Returns:
            A named tuple containing the response gotten from paystack's server.
            An empty list in the data if no domains have been added.
        """

        url = self._parse_url("/apple-pay/domain")
        query_params = [
            ("use_cursor", use_cursor),
            ("next", next),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def unregister_domain(self, domain_name: str) -> Response:
        """Unregister a top-level domain or subdomain previously used for your Apple Pay integration.

        Note
            * This feature is available to businesses in all markets except South Africa.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        raw_response = httpx.request(
            HTTPMethod.DELETE, url, json=payload, headers=self._headers
        )
        return (
            self._parse_response(raw_response)
            if codes.is_success(raw_response.status_code)
            else self._parse_response(raw_response, as_error=True)
        )


class AsyncApplePay(BaseAsyncAPI):
    """Provides a wrapper for paystack Apple Pay API

    The Apple Pay API allows you to register your application's top-level domain or subdomain.
    [Visit paystack api doc](https://paystack.com/docs/api/apple-pay/)
    """

    async def register_domain(self, domain_name: str) -> Response:
        """Register a top-level domain or subdomain for your Apple Pay integration.

        This method can only be called with one domain or subdomain at a time.

        Args:
            domain_name: Domain name to be registered.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_domains(
        self,
        use_cursor: bool = False,
        next: Optional[str] = None,
        previous: Optional[str] = None,
    ) -> Response:
        """Fetches all registered domains on your integration.

        Note
            * This feature is available to businesses in all markets except South Africa.

        Returns:
            A named tuple containing the response gotten from paystack's server.
            An empty list in the data if no domains have been added.
        """

        url = self._parse_url("/apple-pay/domain")
        query_params = [
            ("use_cursor", use_cursor),
            ("next", next),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def unregister_domain(self, domain_name: str) -> Response:
        """Unregister a top-level domain or subdomain previously used for your Apple Pay integration.

        Note
            * This feature is available to businesses in all markets except South Africa.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        async with httpx.AsyncClient() as client:
            raw_response = await client.request(
                HTTPMethod.DELETE, url, json=payload, headers=self._headers
            )
        return (
            self._parse_response(raw_response)
            if codes.is_success(raw_response.status_code)
            else self._parse_response(raw_response, as_error=True)
        )
