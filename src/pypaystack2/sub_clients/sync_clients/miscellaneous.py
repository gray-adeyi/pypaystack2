from http import HTTPMethod
from typing import Type

from pypaystack2.base_api_client import BaseAPIClient
from pypaystack2.utils import (
    BankType,
    Country,
    Currency,
    Gateway,
    append_query_params,
    Response,
)
from pypaystack2.utils.models import PaystackDataModel
from pypaystack2.utils.response_models import Bank, PaystackSupportedCountry, State


class MiscellaneousClient(BaseAPIClient):
    """Provides a wrapper for paystack Miscellaneous API

    The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.
    https://paystack.com/docs/api/miscellaneous/
    """

    def get_banks(
        self,
        country: Country,
        use_cursor: bool = False,
        next: str | None = None,
        previous: str | None = None,
        gateway: Gateway | None = None,
        type: BankType | None = None,
        currency: Currency | None = None,
        pay_with_bank_transfer: bool | None = None,
        pay_with_bank: bool | None = None,
        include_nip_sort_code: bool | None = None,
        pagination: int = 50,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[list[Bank]]:
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
            pay_with_bank_transfer: A flag to filter for available banks a customer can make a transfer to
                complete a payment
            pay_with_bank: A flag to filter for banks a customer can pay directly from
            pagination: The number of objects to return per page. Defaults to 50, and limited to 100 records per page.
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.
            include_nip_sort_code: A flag that returns Nigerian banks with their nip institution code.
                The returned value can be used in identifying institutions on NIP.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        country = Country.get_full(country)
        url = self._full_url(f"/bank?perPage={pagination}")
        query_params = [
            ("country", country),
            ("use_cursor", use_cursor),
            ("next", next),
            ("previous", previous),
            ("gateway", gateway),
            ("type", type),
            ("currency", currency),
            ("pay_with_bank_transfer", pay_with_bank_transfer),
            ("pay_with_bank", pay_with_bank),
            ("include_nip_sort_code", include_nip_sort_code),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Bank,
        )

    def get_countries(
        self,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[list[PaystackSupportedCountry]]:
        """Gets a list of Countries that Paystack currently supports

        Args:
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url("/country")
        return self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaystackSupportedCountry,
        )

    def get_states(
        self,
        country: Country | str,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[State]:
        """Get a list of states for a country for address verification.

        Args:
            country: Any value from the country enum.
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/address_verification/states?country={country}")
        return self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or State,
        )
