from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Country, Currency
from pypaystack2.models import Response
from pypaystack2.models.response_models import (
    DedicatedAccount,
    DedicatedAccountProvider,
)
from pypaystack2.types import PaystackDataModel


class DedicatedAccountClient(BaseAPIClient):
    """Provides a wrapper for paystack Dedicated Virtual Account API

    The Dedicated Virtual Account API enables Nigerian merchants to manage
    unique payment accounts of their customers.
    https://paystack.com/docs/api/dedicated-virtual-account/


    Note:
        This feature is only available to businesses in Nigeria.
    """

    def create(
        self,
        customer: str,
        preferred_bank: str | None = None,
        subaccount: str | None = None,
        split_code: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        phone: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DedicatedAccount] | Response[PaystackDataModel]:
        """Create a dedicated virtual account for an existing customer

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Wema Bank and Titan Paystack.

        Args:
            customer: Customer ID or code
            preferred_bank: The bank slug for a preferred bank. To get a list of available banks, use the
                Miscellaneous API ``.get_providers`` method.
            subaccount: Subaccount code of the account you want to split the transaction with
            split_code: Split code consisting of the lists of accounts you want to split the transaction with
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number
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

        url = self._full_url("/dedicated_account")
        payload = {
            "customer": customer,
        }
        optional_params = [
            ("preferred_bank", preferred_bank),
            ("subaccount", subaccount),
            ("split_code", split_code),
            ("first_name", first_name),
            ("last_name", last_name),
            ("phone", phone),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or DedicatedAccount,
        )

    def assign(
        self,
        email: str,
        first_name: str,
        last_name: str,
        phone: str,
        preferred_bank: str,
        country: Country = Country.NIGERIA,
        account_number: str | None = None,
        bvn: str | None = None,
        bank_code: str | None = None,
        subaccount: str | None = None,
        split_code: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Create a customer, validate the customer, and assign a DVA to the customer.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Wema Bank and Titan Paystack.

        Args:
            email: Customer email address
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number
            preferred_bank: The bank slug for preferred bank. To get a list of available banks, use the
                Paystack.miscellaneous.get_banks, AsyncPaystack.miscellaneous.get_banks, Miscellaneous.get_banks
                or AsyncMiscellaneous.get_banks, with `pay_with_bank_transfer=true`
            country: Currently accepts `Country.NIGERIA` only
            account_number: Customer's account number
            bvn: Customer's Bank Verification Number
            bank_code: Customer's bank code
            subaccount: Subaccount code of the account you want to split the transaction with
            split_code: Split code consisting of the lists of accounts you want to split the transaction with
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

        url = self._full_url("/dedicated_account/assign")
        payload = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "preferred_bank": preferred_bank,
            "country": country,
        }
        optional_params = [
            ("account_number", account_number),
            ("bvn", bvn),
            ("bank_code", bank_code),
            ("subaccount", subaccount),
            ("split_code", split_code),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def get_dedicated_accounts(
        self,
        active: bool = True,
        currency: Currency = Currency.NGN,
        provider_slug: str | None = None,
        bank_id: str | int | None = None,
        customer: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[DedicatedAccount]] | Response[PaystackDataModel]:
        """Fetches dedicated virtual accounts available on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Wema Bank and Titan Paystack.

        Args:
            active: Status of the dedicated virtual account
            currency: The currency of the dedicated virtual account. Only ``Currency.NGN`` is currently allowed
            provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank. call the `.get_providers`
                method of this class to see available providers.
            bank_id: The bank's ID e.g., 035
            customer: The customer's ID
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

        query_params = [
            ("currency", currency),
            ("provider_slug", provider_slug),
            ("bank_id", bank_id),
            ("customer", customer),
        ]
        url = self._full_url(f"/dedicated_account?active={active}")
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or DedicatedAccount,
        )

    def get_dedicated_account(
        self,
        dedicated_account_id: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DedicatedAccount] | Response[PaystackDataModel]:
        """Get details of a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Wema Bank and Titan Paystack.

        Args:
            dedicated_account_id: ID of dedicated virtual account
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

        url = self._full_url(f"/dedicated_account/{dedicated_account_id}")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or DedicatedAccount,
        )

    def requery(
        self,
        account_number: str,
        provider_slug: str,
        date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Get details of a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Wema Bank and Titan Paystack.

        Args:
            account_number: Virtual account number to requery
            provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank
            date: The day the transfer was made in YYYY-MM-DD ISO format
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

        url = self._full_url(f"/dedicated_account?account_number={account_number}")
        query_params = [
            ("provider_slug", provider_slug),
            ("date", date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET, url, response_data_model_class=alternate_model_class
        )

    def deactivate(
        self,
        dedicated_account_id: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DedicatedAccount] | Response[PaystackDataModel]:
        """Deactivate a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.

        Args:
            dedicated_account_id: ID of dedicated virtual account
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

        url = self._full_url(f"/dedicated_account/{dedicated_account_id}")
        return self._handle_request(  # type: ignore
            HTTPMethod.DELETE, url, response_data_model_class=alternate_model_class
        )

    def split(
        self,
        customer: int | str,
        subaccount: str | None = None,
        split_code: str | None = None,
        preferred_bank: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DedicatedAccount] | Response[PaystackDataModel]:
        """Split a dedicated virtual account transaction with one or more accounts

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.

        Args:
            customer: Customer ID or code
            subaccount: Subaccount code of the account you want to split the transaction with
            split_code: Split code consisting of the lists of accounts you want to split the transaction with
            preferred_bank: The bank slug for a preferred bank. To get a list of available banks,
                use the Miscellaneous API ``.get_providers`` method
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

        url = self._full_url("/dedicated_account/split")
        payload = {"customer": customer}

        optional_params = [
            ("subaccount", subaccount),
            ("split_code", split_code),
            ("preferred_bank", preferred_bank),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or DedicatedAccount,
        )

    def remove_split(
        self,
        account_number: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[DedicatedAccount] | Response[PaystackDataModel]:
        """Removes a split.

        If you've previously set up split payment for transactions on a dedicated virtual
        account, you can remove it with this method.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.

        Args:
            account_number: Dedicated virtual account number
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

        url = self._full_url("/dedicated_account/split")
        payload = {
            "account_number": account_number,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.DELETE,
            url,
            payload,
            response_data_model_class=alternate_model_class or DedicatedAccount,
        )

    def get_providers(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[DedicatedAccountProvider]] | Response[PaystackDataModel]:
        """Get available bank providers for a dedicated virtual account

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.

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

        url = self._full_url("/dedicated_account/available_providers")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or DedicatedAccountProvider,
        )
