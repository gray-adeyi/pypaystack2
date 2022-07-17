from typing import Optional

from pypaystack2.errors import InvalidDataError
from .baseapi import BaseAPI
from . import utils
from .utils import Currency, add_to_payload, append_query_params


class Product(BaseAPI):
    """
    The Products API allows you create
    and manage inventories on your integration
    """

    def create(
        self,
        name: str,
        description: str,
        price: int,
        currency: Currency,
        unlimited: Optional[bool] = None,
        quantity: Optional[int] = None,
    ):
        """
        Create a subscription on your integration

        """
        if unlimited is True and quantity is not None:
            raise InvalidDataError(
                "You can't have unlimited set to True and quantity hava a value."
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
    ):
        """ """
        url = self._url(f"/product?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_product(self, id: str):
        """ """
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
    ):
        """ """
        if unlimited is True and quantity is not None:
            raise InvalidDataError(
                "You can't have unlimited set to True and quantity hava a value."
            )
        url = self._url("/product/{id}")
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
