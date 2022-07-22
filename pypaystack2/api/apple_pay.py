from ..baseapi import BaseAPI, Response


class ApplePay(BaseAPI):
    """Provides a wrapper for paystack Apple Pay API

    The Apple Pay API allows you register your application's top-level domain or subdomain.
    https://paystack.com/docs/api/#apple-pay
    """

    def register_domain(self, domain_name: str) -> Response:
        """Register a top-level domain or subdomain
        for your Apple Pay integration.

        Parameters
        ----------
        domain_name: str
            Domain name to be registered

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        This method can only be called with one domain or subdomain at a time.
        """

        url = self._url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return self._handle_request("POST", url, payload)

    def get_domains(self) -> Response:
        """Fetches all registered domains on your integration.
        Returns an empty array if no domains have been added.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/apple-pay/domain")
        return self._handle_request("GET", url)

    def unregister_domain(self, domain_name: str) -> Response:
        """Unregister a top-level domain or
        subdomain previously used for your
        Apple Pay integration.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return self._handle_request("DELETE", url, payload)
