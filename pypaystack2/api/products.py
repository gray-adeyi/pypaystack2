from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.exceptions import InvalidDataException
from pypaystack2.utils import (
    Currency,
    add_to_payload,
    append_query_params,
    HTTPMethod,
    Response,
)


class Product(BaseAPI):
    """Provides a wrapper for paystack Products API

    The Products API allows you to create and manage inventories on your integration.
    https://paystack.com/docs/api/product/
    """

    def create(
        self,
        name: str,
        description: str,
        price: int,
        currency: Currency,
        unlimited: Optional[bool] = None,
        quantity: Optional[int] = None,
    ) -> Response:
        """Create a product on your integration

        Args:
            name: Name of product
            description: A description for this product
            price: Price should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            currency: Any value from the ``Currency`` enum
            unlimited: Set to ``True`` if the product has unlimited stock.
                Leave as ``False`` if the product has limited stock
            quantity: Number of products in stock. Use if unlimited is ``False``

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise InvalidDataException(
                "You can't have unlimited set to True and have a quantity value."
            )

        url = self._parse_url("/product")

        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
        }
        optional_params = [
            ("unlimited", unlimited),
            ("quantity", quantity),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_products(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetches products available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: timestamp at which to stop listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/product?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_product(self, id: str) -> Response:
        """Get details of a product on your integration.

        Args:
            id: The product ``ID`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/product/{id}")
        return self._handle_request(HTTPMethod.GET, url)

    def update(
        self,
        id: str,
        name: str,
        description: str,
        price: int,
        currency: Currency,
        unlimited: Optional[bool] = None,
        quantity: Optional[int] = None,
    ) -> Response:
        """Update a product details on your integration

        Args:
            id: Product ID
            name: Name of product
            description: A description for this product
            price: Price should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is GHS, and cents, if currency is ``Currency.ZAR``
            currency: Any value from the ``Currency`` enum
            unlimited: Set to ``True`` if the product has unlimited stock.
                Leave as ``False`` if the product has limited stock
            quantity: Number of products in stock. Use if unlimited is ``False``

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise InvalidDataException(
                "You can't have unlimited set to True and quantity have a value."
            )
        url = self._parse_url(f"/product/{id}")
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
        }
        optional_params = [
            ("unlimited", unlimited),
            ("quantity", quantity),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.PUT, url, payload)


class AsyncProduct(BaseAsyncAPI):
    """Provides a wrapper for paystack Products API

    The Products API allows you to create and manage inventories on your integration.
    https://paystack.com/docs/api/product/
    """

    async def create(
        self,
        name: str,
        description: str,
        price: int,
        currency: Currency,
        unlimited: Optional[bool] = None,
        quantity: Optional[int] = None,
    ) -> Response:
        """Create a product on your integration

        Args:
            name: Name of product
            description: A description for this product
            price: Price should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            currency: Any value from the ``Currency`` enum
            unlimited: Set to ``True`` if the product has unlimited stock.
                Leave as ``False`` if the product has limited stock
            quantity: Number of products in stock. Use if unlimited is ``False``

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise InvalidDataException(
                "You can't have unlimited set to True and have a quantity value."
            )

        url = self._parse_url("/product")

        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
        }
        optional_params = [
            ("unlimited", unlimited),
            ("quantity", quantity),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_products(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetches products available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: timestamp at which to stop listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/product?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_product(self, id: str) -> Response:
        """Get details of a product on your integration.

        Args:
            id: The product ``ID`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/product/{id}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update(
        self,
        id: str,
        name: str,
        description: str,
        price: int,
        currency: Currency,
        unlimited: Optional[bool] = None,
        quantity: Optional[int] = None,
    ) -> Response:
        """Update a product details on your integration

        Args:
            id: Product ID
            name: Name of product
            description: A description for this product
            price: Price should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is GHS, and cents, if currency is ``Currency.ZAR``
            currency: Any value from the ``Currency`` enum
            unlimited: Set to ``True`` if the product has unlimited stock.
                Leave as ``False`` if the product has limited stock
            quantity: Number of products in stock. Use if unlimited is ``False``

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise InvalidDataException(
                "You can't have unlimited set to True and quantity have a value."
            )
        url = self._parse_url(f"/product/{id}")
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
        }
        optional_params = [
            ("unlimited", unlimited),
            ("quantity", quantity),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.PUT, url, payload)
