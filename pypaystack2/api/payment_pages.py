from typing import Optional


from ..baseapi import BaseAPI
from ..utils import add_to_payload, append_query_params


class Page(BaseAPI):
    """
    The Payment Pages API provides
    a quick and secure way to collect
    payment for products.
    """

    def create(
        self,
        name: str,
        description: Optional[str] = None,
        amount: Optional[int] = None,
        slug: Optional[str] = None,
        metadata: Optional[str] = None,
        redirect_url: Optional[str] = None,
        custom_fields: Optional[list] = None,
    ):
        """ """

        url = self._url("/page")

        payload = {"name": name}
        optional_params = [
            ("description", description),
            ("amount", amount),
            ("slug", slug),
            ("metadata", metadata),
            ("redirect_url", redirect_url),
            ("custom_fields", custom_fields),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def get_pages(
        self,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        """ """
        url = self._url(f"/page?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_page(self, id_or_slug: str):
        """ """
        url = self._url(f"/page/{id_or_slug}")
        return self._handle_request("GET", url)

    def update(
        self,
        id_or_slug: str,
        name: str,
        description: str,
        amount: int,
        active: Optional[bool] = None,
    ):
        """ """

        url = self._url(f"/page/{id_or_slug}")
        payload = {
            "name": name,
            "description": description,
        }
        optional_params = [
            ("amount", amount),
            ("active", active),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("PUT", url, payload)

    def check_slug_available(self, slug: str):
        """ """
        url = self._url(f"/page/check_slug_availability/{slug}")
        return self._handle_request("GET", url)

    def add_products(self, id: str, products: list[int]):
        """Add products to a payment page"""
        url = self._url(f"/page/{id}/product")
        payload = {"product": products}
        return self._handle_request("POST", url, payload)
