from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    BankType,
    Country,
    Currency,
    Gateway,
    append_query_params,
    HTTPMethod, Response,
)


class Miscellaneous(BaseAPI):
    """Provides a wrapper for paystack Miscellaneous API

    The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.
    https://paystack.com/docs/api/#miscellaneous
    """

    def get_banks(
        self,
        country: Country,
        use_cursor: bool = False,
        next: Optional[str] = None,
        previous: Optional[str] = None,
        gateway: Optional[Gateway] = None,
        type: Optional[BankType] = None,
        currency: Optional[Currency] = None,
        pagination=50,
    ) -> Response:
        """Get a list of all supported banks and their properties

        Args:
            country: The country from which to obtain the list of supported banks. any value from the ``Country`` enum.
            use_cursor: Flag to enable cursor pagination.
            next: A cursor that indicates your place in the list. It can be used to fetch the next page of the list
            previous: A cursor that indicates your place in the list. It should be used
                to fetch the previous page of the list after an intial next request
            gateway: The gateway type of the bank. Any value from the ``Gateway`` enum.
            type: Type of financial channel. For Ghanaian channels, please use either
                mobile_money for mobile money channels OR ghipps for bank channels
            currency: Any value from the Currency enum.
            pagination: The number of objects to return per page. Defaults to 50, and limited to 100 records per page.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        country = Country.get_full(country)
        url = self._parse_url(f"/bank?perPage={pagination}")
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
        return self._handle_request(HTTPMethod.GET, url)

    def get_providers(
        self,
        pay_with_bank_transfer: bool = False,
    ) -> Response:
        """Get a list of all providers for Dedicated Virtual Account

        Args:
        pay_with_bank_transfer: A flag to filter for available providers

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bank?pay_with_bank_transfer={pay_with_bank_transfer}")
        return self._handle_request(HTTPMethod.GET, url)

    def get_countries(self) -> Response:
        """Gets a list of Countries that Paystack currently supports

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/country")
        return self._handle_request(HTTPMethod.GET, url)

    def get_states(self, country: Country):
        """Get a list of states for a country for address verification.

        Args:
        country: Any value from the country enum.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/address_verification/states?country={country}")
        return self._handle_request(HTTPMethod.GET, url)


class AsyncMiscellaneous(BaseAsyncAPI):
    """Provides a wrapper for paystack Miscellaneous API

    The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.
    https://paystack.com/docs/api/#miscellaneous
    """

    async def get_banks(
        self,
        country: Country,
        use_cursor: bool = False,
        next: Optional[str] = None,
        previous: Optional[str] = None,
        gateway: Optional[Gateway] = None,
        type: Optional[BankType] = None,
        currency: Optional[Currency] = None,
        pagination=50,
    ) -> Response:
        """Get a list of all supported banks and their properties

        Args:
            country: The country from which to obtain the list of supported banks. any value from the ``Country`` enum.
            use_cursor: Flag to enable cursor pagination.
            next: A cursor that indicates your place in the list. It can be used to fetch the next page of the list
            previous: A cursor that indicates your place in the list. It should be used
                to fetch the previous page of the list after an intial next request
            gateway: The gateway type of the bank. Any value from the ``Gateway`` enum.
            type: Type of financial channel. For Ghanaian channels, please use either
                mobile_money for mobile money channels OR ghipps for bank channels
            currency: Any value from the Currency enum.
            pagination: The number of objects to return per page. Defaults to 50, and limited to 100 records per page.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        country = Country.get_full(country)
        url = self._parse_url(f"/bank?perPage={pagination}")
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
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_providers(
        self,
        pay_with_bank_transfer: bool = False,
    ) -> Response:
        """Get a list of all providers for Dedicated Virtual Account

        Args:
        pay_with_bank_transfer: A flag to filter for available providers

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/bank?pay_with_bank_transfer={pay_with_bank_transfer}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_countries(self) -> Response:
        """Gets a list of Countries that Paystack currently supports

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/country")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_states(self, country: Country):
        """Get a list of states for a country for address verification.

        Args:
        country: Any value from the country enum.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/address_verification/states?country={country}")
        return await self._handle_request(HTTPMethod.GET, url)
