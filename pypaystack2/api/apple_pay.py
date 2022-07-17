from typing import Optional
from .baseapi import BaseAPI
from .errors import InvalidDataError
from .utils import (
    add_to_payload,
    append_query_params,
    Identification,
    Country,
    RiskAction,
)


class ApplePay(BaseAPI):
    """
    The Apple Pay API allows you register
    your application's top-level domain
    or subdomain.
    """

    def register_domain(self, domain_name: str):
        """
        Register a top-level domain or subdomain
        for your Apple Pay integration.
        """
        url = self._url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return self._handle_request("POST", url, payload)

    def list_domains(self):
        """
        Lists all registered domains on your integration.
        Returns an empty array if no domains have been added.
        """
        url = self._url("/apple-pay/domain")
        return self._handle_request("GET", url)

    def unregister_domain(self, domain_name: str):
        """
        Unregister a top-level domain or
        subdomain previously used for your
        Apple Pay integration.
        """
        url = self._url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return self._handle_request("DELETE", url, payload)
