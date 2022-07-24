from typing import Optional

from pypaystack2.errors import InvalidDataError
from ..baseapi import BaseAPI, Response
from ..utils import Currency, add_to_payload, append_query_params


class Product(BaseAPI):
    """Provides a wrapper for paystack Products API

    The Products API allows you create and manage inventories on your integration.
    https://paystack.com/docs/api/#product
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

        Parameters
        ----------
        name: str
            Name of product
        description: str
            A description for this product
        price: int
            Price should be in kobo if currency is ``Currency.NGN``, pesewas,
            if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
        currency: Currency
            Any value from the ``Currency`` enum
        unlimited: Optional[bool]
            Set to ``True`` if the product has unlimited stock.
            Leave as ``False`` if the product has limited stock
        quantity: Optional[int]
            Number of products in stock. Use if unlimited is ``False``

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Raises
        ------
        InvalidDataError
            When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise InvalidDataError(
                "You can't have unlimited set to True and have a quantity value."
            )

        url = self._url("/product")

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
        return self._handle_request("POST", url, payload)

    def get_products(
        self,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetches products available on your integration.

        Parameters
        ----------
        page: int
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        start_date: Optional[str]
            A timestamp from which to start listing product
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
             timestamp at which to stop listing product
             e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/product?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_product(self, id: str) -> Response:
        """Get details of a product on your integration.

        Parameters
        ----------
        id: str
            The product ``ID`` you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/product/{id}")
        return self._handle_request("GET", url)

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

        Parameters
        ----------
        id: str
            Product ID
        name: str
            Name of product
        description: str
            A description for this product
        price: int
            Price should be in kobo if currency is ``Currency.NGN``, pesewas,
            if currency is GHS, and cents, if currency is ``Currency.ZAR``
        currency: Currency
            Any value from the ``Currency`` enum
        unlimited: Optional[bool]
            Set to ``True`` if the product has unlimited stock.
            Leave as ``False`` if the product has limited stock
        quantity: Optional[int]
            Number of products in stock. Use if unlimited is ``False``

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Raises
        ------
        InvalidDataError
            When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise InvalidDataError(
                "You can't have unlimited set to True and quantity have a value."
            )
        url = self._url(f"/product/{id}")
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
        return self._handle_request("PUT", url, payload)
