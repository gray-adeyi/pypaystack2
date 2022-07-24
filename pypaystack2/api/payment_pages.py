from typing import Optional


from ..baseapi import BaseAPI, Response
from ..utils import add_to_payload, append_query_params


class Page(BaseAPI):
    """Provides a wrapper for paystack Payment Pages API

    The Payment Pages API provides a quick and secure way to collect payment for products.
    https://paystack.com/docs/api/#page
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
    ) -> Response:
        """Create a payment page on your integration

        Parameters
        ----------
        name: str
            Name of page
        description: Optional[str]
            A description for this page
        amount: Optional[int]
            Amount should be in kobo if currency is ``Currency.NGN``, pesewas, if
            currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
        slug: Optional[str]
            URL slug you would like to be associated with this page.
            Page will be accessible at ``https://paystack.com/pay/[slug]``
        metadata: Optional[str]
            Extra data to configure the payment page including subaccount,
            logo image, transaction charge
        redirect_url: Optional[str]
            If you would like Paystack to redirect someplace upon
            successful payment, specify the URL here.
        custom_fields: Optional[list]
            If you would like to accept custom fields,
            specify them here.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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
    ) -> Response:
        """Fetch payment pages available on your integration.

        Parameters
        ----------
        page: int
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        pagination:int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        start_date: Optional[str]
            A timestamp from which to start listing page
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing page
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/page?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_page(self, id_or_slug: str):
        """Get details of a payment page on your integration.

        Parameters
        ----------
        id_or_slug: str
            The page ``ID`` or ``slug`` you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/page/{id_or_slug}")
        return self._handle_request("GET", url)

    def update(
        self,
        id_or_slug: str,
        name: str,
        description: str,
        amount: int,
        active: Optional[bool] = None,
    ) -> Response:
        """Get details of a payment page on your integration.

        Parameters
        ----------
        id_or_slug: str
            The page ``ID`` or ``slug`` you want to fetch
        name: str
            Name of page
        description: str
            A description for the page
        amount: int
            Default amount you want to accept using this page.
            If none is set, customer is free to provide any amount
            of their choice. The latter scenario is useful for
            accepting donations
        active: Optional[bool]
            Set to ``False`` to deactivate page url

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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

    def check_slug_available(self, slug: str) -> Response:
        """Check the availability of a slug for a payment page.

        Parameters
        ----------
        slug: str
            URL slug to be confirmed

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/page/check_slug_availability/{slug}")
        return self._handle_request("GET", url)

    def add_products(self, id: str, products: list[int]):
        """Add products to a payment page

        Parameters
        ----------
        id: str
            Id of the payment page
        products: list[int]
            Ids of all the products

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/page/{id}/product")
        payload = {"product": products}
        return self._handle_request("POST", url, payload)
