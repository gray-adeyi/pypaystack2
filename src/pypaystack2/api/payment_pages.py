from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import add_to_payload, append_query_params, HTTPMethod, Response


class PaymentPage(BaseAPI):
    """Provides a wrapper for paystack Payment Pages API

    The Payment Pages API provides a quick and secure way to collect payment for products.
    https://paystack.com/docs/api/page/
    """

    def create(
        self,
        name: str,
        description: Optional[str] = None,
        amount: Optional[int] = None,
        split_code: Optional[str] = None,
        slug: Optional[str] = None,
        metadata: Optional[str] = None,
        redirect_url: Optional[str] = None,
        custom_fields: Optional[list] = None,
    ) -> Response:
        """Create a payment page on your integration

        Args:
            name: Name of page
            description: A description for this page
            amount: Amount should be in kobo if currency is ``Currency.NGN``, pesewas, if
                currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w
            slug: URL slug you would like to be associated with this page.
                Page will be accessible at ``https://paystack.com/pay/[slug]``
            metadata: Extra data to configure the payment page including subaccount,
                logo image, transaction charge
            redirect_url: If you would like Paystack to redirect someplace upon
                successful payment, specify the URL here.
            custom_fields: If you would like to accept custom fields,
                specify them here.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/page")

        payload = {"name": name}
        optional_params = [
            ("description", description),
            ("amount", amount),
            ("split_code", split_code),
            ("slug", slug),
            ("metadata", metadata),
            ("redirect_url", redirect_url),
            ("custom_fields", custom_fields),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_pages(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch payment pages available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/page?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_page(self, id_or_slug: str) -> Response:
        """Get details of a payment page on your integration.

        Args:
            id_or_slug: The page ``ID`` or ``slug`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/{id_or_slug}")
        return self._handle_request(HTTPMethod.GET, url)

    def update(
        self,
        id_or_slug: str,
        name: str,
        description: str,
        amount: Optional[int] = None,
        active: Optional[bool] = None,
    ) -> Response:
        """Get details of a payment page on your integration.

        Args:
            id_or_slug: The page ``ID`` or ``slug`` you want to fetch
            name: Name of page
            description: A description for the page
            amount: Default amount you want to accept using this page.
                If none is set, customer is free to provide any amount
                of their choice. The latter scenario is useful for
                accepting donations
            active: Set to ``False`` to deactivate page url

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/{id_or_slug}")
        payload = {
            "name": name,
            "description": description,
        }
        optional_params = [
            ("amount", amount),
            ("active", active),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.PUT, url, payload)

    def check_slug_available(self, slug: str) -> Response:
        """Check the availability of a slug for a payment page.

        Args:
            slug: URL slug to be confirmed

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/check_slug_availability/{slug}")
        return self._handle_request(HTTPMethod.GET, url)

    def add_products(self, id: str, products: list[int]) -> Response:
        """Add products to a payment page

        Args:
            id: ID of the payment page
            products: Ids of all the products

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/{id}/product")
        payload = {"product": products}
        return self._handle_request(HTTPMethod.POST, url, payload)


class AsyncPaymentPage(BaseAsyncAPI):
    """Provides a wrapper for paystack Payment Pages API

    The Payment Pages API provides a quick and secure way to collect payment for products.
    https://paystack.com/docs/api/page/
    """

    async def create(
        self,
        name: str,
        description: Optional[str] = None,
        amount: Optional[int] = None,
        split_code: Optional[str] = None,
        slug: Optional[str] = None,
        metadata: Optional[str] = None,
        redirect_url: Optional[str] = None,
        custom_fields: Optional[list] = None,
    ) -> Response:
        """Create a payment page on your integration

        Args:
            name: Name of page
            description: A description for this page
            amount: Amount should be in kobo if currency is ``Currency.NGN``, pesewas, if
                currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w
            slug: URL slug you would like to be associated with this page.
                Page will be accessible at ``https://paystack.com/pay/[slug]``
            metadata: Extra data to configure the payment page including subaccount,
                logo image, transaction charge
            redirect_url: If you would like Paystack to redirect someplace upon
                successful payment, specify the URL here.
            custom_fields: If you would like to accept custom fields,
                specify them here.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/page")

        payload = {"name": name}
        optional_params = [
            ("description", description),
            ("amount", amount),
            ("split_code", split_code),
            ("slug", slug),
            ("metadata", metadata),
            ("redirect_url", redirect_url),
            ("custom_fields", custom_fields),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_pages(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch payment pages available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/page?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_page(self, id_or_slug: str) -> Response:
        """Get details of a payment page on your integration.

        Args:
            id_or_slug: The page ``ID`` or ``slug`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/{id_or_slug}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update(
        self,
        id_or_slug: str,
        name: str,
        description: str,
        amount: Optional[int] = None,
        active: Optional[bool] = None,
    ) -> Response:
        """Get details of a payment page on your integration.

        Args:
            id_or_slug: The page ``ID`` or ``slug`` you want to fetch
            name: Name of page
            description: A description for the page
            amount: Default amount you want to accept using this page.
                If none is set, customer is free to provide any amount
                of their choice. The latter scenario is useful for
                accepting donations
            active: Set to ``False`` to deactivate page url

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/{id_or_slug}")
        payload = {
            "name": name,
            "description": description,
        }
        optional_params = [
            ("amount", amount),
            ("active", active),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def check_slug_available(self, slug: str) -> Response:
        """Check the availability of a slug for a payment page.

        Args:
            slug: URL slug to be confirmed

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/check_slug_availability/{slug}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def add_products(self, id: str, products: list[int]) -> Response:
        """Add products to a payment page

        Args:
            id: ID of the payment page
            products: Ids of all the products

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/page/{id}/product")
        payload = {"product": products}
        return await self._handle_request(HTTPMethod.POST, url, payload)
