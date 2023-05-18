from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import HTTPMethod, Response


class ApplePay(BaseAPI):
    """Provides a wrapper for paystack Apple Pay API

    The Apple Pay API allows you register your application's top-level domain or subdomain.
    [Visit paystack api doc](https://paystack.com/docs/api/apple-pay/)
    """

    def register_domain(self, domain_name: str) -> Response:
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
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_domains(self) -> Response:
        """Fetches all registered domains on your integration.

        Returns an empty array if no domains have been added.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        return self._handle_request(HTTPMethod.GET, url)

    def unregister_domain(self, domain_name: str) -> Response:
        """Unregister a top-level domain or subdomain previously used for your Apple Pay integration.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        # return self._handle_request(HTTPMethod.DELETE, url, payload)
        raise NotImplementedError(
            "The package `httpx` which PyPaystack uses to make REST "
            "API calls does not allow HTTPMethod.DELETE have a body"
        )


class AsyncApplePay(BaseAsyncAPI):
    """Provides a wrapper for paystack Apple Pay API

    The Apple Pay API allows you register your application's top-level domain or subdomain.
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

    async def get_domains(self) -> Response:
        """Fetches all registered domains on your integration.

        Returns an empty array if no domains have been added.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        return await self._handle_request(HTTPMethod.GET, url)

    async def unregister_domain(self, domain_name: str) -> Response:
        """Unregister a top-level domain or subdomain previously used for your Apple Pay integration.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        # return await self._handle_request(HTTPMethod.DELETE, url, payload)
        raise NotImplementedError(
            "The package `httpx` which PyPaystack uses to make REST "
            "API calls does not allow HTTPMethod.DELETE have a body"
        )
