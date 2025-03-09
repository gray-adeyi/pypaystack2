from http import HTTPMethod

from pypaystack2.base_clients import BaseAsyncAPIClient, append_query_params
from pypaystack2.enums import Country, Gateway, BankType, Currency
from pypaystack2.models import Response
from pypaystack2.models.response_models import Bank, PaystackSupportedCountry, State
from pypaystack2.types import PaystackDataModel


class AsyncMiscellaneousClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Miscellaneous API

    The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs.
    https://paystack.com/docs/api/miscellaneous/
    """

    async def get_banks(
        self,
        country: Country,
        use_cursor: bool = False,
        next_: str | None = None,
        previous: str | None = None,
        gateway: Gateway | None = None,
        type_: BankType | None = None,
        currency: Currency | None = None,
        pay_with_bank_transfer: bool | None = None,
        pay_with_bank: bool | None = None,
        include_nip_sort_code: bool | None = None,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Bank]] | Response[PaystackDataModel]:
        """Get a list of all supported banks and their properties

        Args:
            country: The country from which to obtain the list of supported banks. any value from the ``Country`` enum.
            use_cursor: Flag to enable cursor pagination.
            next_: A cursor that indicates your place in the list. It can be used to fetch the next page of the list
            previous: A cursor that indicates your place in the list. It should be used
                to fetch the previous page of the list after an intial next request
            gateway: The gateway type of the bank. Any value from the ``Gateway`` enum.
            type_: Type of financial channel. For Ghanaian channels, please use either
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

        country_full = Country.get_full(country)
        url = self._full_url(f"/bank?perPage={pagination}")
        query_params = [
            ("country", country_full),
            ("use_cursor", use_cursor),
            ("next", next_),
            ("previous", previous),
            ("gateway", gateway),
            ("type", type_),
            ("currency", currency),
            ("pay_with_bank_transfer", pay_with_bank_transfer),
            ("pay_with_bank", pay_with_bank),
            ("include_nip_sort_code", include_nip_sort_code),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Bank,
        )

    async def get_countries(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[PaystackSupportedCountry]] | Response[PaystackDataModel]:
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
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaystackSupportedCountry,
        )

    async def get_states(
        self,
        country: Country | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[State]] | Response[PaystackDataModel]:
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
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or State,
        )
