from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    Currency,
    add_to_payload,
    append_query_params,
    HTTPMethod,
    Response,
)


class DedicatedAccount(BaseAPI):
    """Provides a wrapper for paystack Dedicated Virtual Account API

    The Dedicated Virtual Account API enables Nigerian merchants to manage
    unique payment accounts of their customers.
    https://paystack.com/docs/api/#dedicated-virtual-account


    Note:
        This feature is only available to businesses in Nigeria.
    """

    def create(
        self,
        customer: str,
        preferred_bank: Optional[str] = None,
        subaccount: Optional[str] = None,
        split_code: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> Response:
        """Create a dedicated virtual account and assign to a customer

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            customer: Customer ID or code
            preferred_bank: The bank slug for preferred bank. To get a list of available banks, use the
                Miscellaneous API ``.get_providers`` method.
            subaccount: Subaccount code of the account you want to split the transaction with
            split_code: Split code consisting of the lists of accounts you want to split the transaction with
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account")
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
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_dedicated_accounts(
        self,
        active: bool = True,
        currency: Currency = Currency.NGN,
        provider_slug: Optional[str] = None,
        bank_id: Optional[str] = None,
        customer: Optional[str] = None,
    ) -> Response:
        """Fetches dedicated virtual accounts available on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            active: Status of the dedicated virtual account
            currency: The currency of the dedicated virtual account. Only ``Currency.NGN`` is currently allowed
            provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank
            bank_id: The bank's ID e.g. 035
            customer: The customer's ID

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        query_params = [
            ("currency", currency),
            ("provider_slug", provider_slug),
            ("bank_id", bank_id),
            ("customer", customer),
        ]
        url = self._parse_url(f"/dedicated_account?active={active}")
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_dedicated_account(self, dedicated_account_id: int) -> Response:
        """Get details of a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            dedicated_account_id: ID of dedicated virtual account

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dedicated_account/{dedicated_account_id}")
        return self._handle_request(HTTPMethod.GET, url)

    def requery(
        self, account_number: str, provider_slug: str, date: Optional[str]
    ) -> Response:
        """Get details of a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            account_number: Virtual account number to requery
            provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank
            date: The day the transfer was made in YYYY-MM-DD ISO format

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dedicated_account?account_number={account_number}")
        query_params = [
            ("provider_slug", provider_slug),
            ("date", date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def deactivate(self, dedicated_account_id: int) -> Response:
        """Deactivate a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            dedicated_account_id: ID of dedicated virtual account

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dedicated_account/{dedicated_account_id}")
        return self._handle_request(HTTPMethod.DELETE, url)

    def split(
        self,
        customer: str,
        subaccount: Optional[str] = None,
        split_code: Optional[str] = None,
        preferred_bank: Optional[str] = None,
    ) -> Response:
        """Split a dedicated virtual account transaction with one or more accounts

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            customer: Customer ID or code
            subaccount: Subaccount code of the account you want to split the transaction with
            split_code: Split code consisting of the lists of accounts you want to split the transaction with
            preferred_bank: The bank slug for preferred bank. To get a list of available banks,
                use the Miscellaneous API ``.get_providers`` method

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account/split")
        payload = {"customer": customer}

        optional_params = [
            ("subaccount", subaccount),
            ("split_code", split_code),
            ("preferred_bank", preferred_bank),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def remove_split(self, account_number: str) -> Response:
        """Removes a split.

        If you've previously set up split payment for transactions on a dedicated virtual
        account, you can remove it with this method.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            account_number: Dedicated virtual account number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account/split")
        payload = {
            "account_number": account_number,
        }
        return self._handle_request(HTTPMethod.DELETE, url, payload)

    def get_providers(self) -> Response:
        """Get available bank providers for a dedicated virtual account

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account/available_providers")
        return self._handle_request(HTTPMethod.GET, url)


class AsyncDedicatedAccount(BaseAsyncAPI):
    """Provides a wrapper for paystack Dedicated Virtual Account API

    The Dedicated Virtual Account API enables Nigerian merchants to manage
    unique payment accounts of their customers.
    https://paystack.com/docs/api/#dedicated-virtual-account


    Note:
        This feature is only available to businesses in Nigeria.
    """

    async def create(
        self,
        customer: str,
        preferred_bank: Optional[str] = None,
        subaccount: Optional[str] = None,
        split_code: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> Response:
        """Create a dedicated virtual account and assign to a customer

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            customer: Customer ID or code
            preferred_bank: The bank slug for preferred bank. To get a list of available banks, use the
                Miscellaneous API ``.get_providers`` method.
            subaccount: Subaccount code of the account you want to split the transaction with
            split_code: Split code consisting of the lists of accounts you want to split the transaction with
            first_name: Customer's first name
            last_name: Customer's last name
            phone: Customer's phone number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account")
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
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_dedicated_accounts(
        self,
        active: bool = True,
        currency: Currency = Currency.NGN,
        provider_slug: Optional[str] = None,
        bank_id: Optional[str] = None,
        customer: Optional[str] = None,
    ) -> Response:
        """Fetches dedicated virtual accounts available on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            active: Status of the dedicated virtual account
            currency: The currency of the dedicated virtual account. Only ``Currency.NGN`` is currently allowed
            provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank
            bank_id: The bank's ID e.g. 035
            customer: The customer's ID

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        query_params = [
            ("currency", currency),
            ("provider_slug", provider_slug),
            ("bank_id", bank_id),
            ("customer", customer),
        ]
        url = self._parse_url(f"/dedicated_account?active={active}")
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_dedicated_account(self, dedicated_account_id: int) -> Response:
        """Get details of a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            dedicated_account_id: ID of dedicated virtual account

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dedicated_account/{dedicated_account_id}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def requery(
        self, account_number: str, provider_slug: str, date: Optional[str]
    ) -> Response:
        """Get details of a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            account_number: Virtual account number to requery
            provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank
            date: The day the transfer was made in YYYY-MM-DD ISO format

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dedicated_account?account_number={account_number}")
        query_params = [
            ("provider_slug", provider_slug),
            ("date", date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def deactivate(self, dedicated_account_id: int) -> Response:
        """Deactivate a dedicated virtual account on your integration.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            dedicated_account_id: ID of dedicated virtual account

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/dedicated_account/{dedicated_account_id}")
        return await self._handle_request(HTTPMethod.DELETE, url)

    async def split(
        self,
        customer: str,
        subaccount: Optional[str] = None,
        split_code: Optional[str] = None,
        preferred_bank: Optional[str] = None,
    ) -> Response:
        """Split a dedicated virtual account transaction with one or more accounts

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            customer: Customer ID or code
            subaccount: Subaccount code of the account you want to split the transaction with
            split_code: Split code consisting of the lists of accounts you want to split the transaction with
            preferred_bank: The bank slug for preferred bank. To get a list of available banks,
                use the Miscellaneous API ``.get_providers`` method

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account/split")
        payload = {"customer": customer}

        optional_params = [
            ("subaccount", subaccount),
            ("split_code", split_code),
            ("preferred_bank", preferred_bank),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def remove_split(self, account_number: str) -> Response:
        """Removes a split.

        If you've previously set up split payment for transactions on a dedicated virtual
        account, you can remove it with this method.

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Args:
            account_number: Dedicated virtual account number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account/split")
        payload = {
            "account_number": account_number,
        }
        return await self._handle_request(HTTPMethod.DELETE, url, payload)

    async def get_providers(self) -> Response:
        """Get available bank providers for a dedicated virtual account

        Note:
            * This feature is only available to businesses in Nigeria.
            * Paystack currently supports Access Bank and Wema Bank.
            * To create Dedicated Virtual Accounts using your test secret key, use ``test-bank`` as the
                ``preferred_bank`` You can also make a transfer to the test virtual accounts using
                paystack's demo bank app. https://demobank.paystackintegrations.com/

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/dedicated_account/available_providers")
        return await self._handle_request(HTTPMethod.GET, url)
