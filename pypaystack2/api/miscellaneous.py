from typing import Optional

from ..baseapi import BaseAPI
from . import utils
from ..utils import (
    BankType,
    Country,
    append_query_params,
)


class Miscellaneous(BaseAPI):
    """
    The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs
    """

    def get_banks(
        self,
        country: Country,
        use_cursor: bool,
        next: Optional[str] = None,
        previous: Optional[str] = None,
        gateway: Optional[str] = None,
        type: Optional[BankType] = None,
        currency: Optional[Currency] = None,
        pagination=50,
    ):
        """ """
        country = Country.get_full(country)
        url = self._url(f"/bank?perPage={pagination}")
        query_params = [
            ("country", country),
            ("use_cursor", use_cursor),
            ("next", next),
            ("previous", previous),
            ("gateway", gateway),
            ("type", type),
            ("currency", currency),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_providers(
        self,
        pay_with_bank_transfer: bool,
    ):
        """ """
        country = Country.get_full(country)
        url = self._url(f"/bank?pay_with_bank_transfer={pay_with_bank_transfer}")
        return self._handle_request("GET", url)

    def get_countries(self):
        """ """
        url = self._url(f"/country")
        return self._handle_request("GET", url)

    def get_states(self, country: Country):
        """ """
        url = self._url(f"/address_verification/states?country={country}")
        return self._handle_request("GET", url)
