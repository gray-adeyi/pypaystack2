from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import (
    BaseAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.models import Response
from pypaystack2.models.response_models import PaymentPage
from pypaystack2.types import PaystackDataModel


class PaymentPageClient(BaseAPIClient):
    """Provides a wrapper for paystack Payment Pages API

    The Payment Pages API provides a quick and secure way to collect payment for products.
    https://paystack.com/docs/api/page/
    """

    def create(
        self,
        name: str,
        description: str | None = None,
        amount: int | None = None,
        split_code: str | None = None,
        slug: str | None = None,
        metadata: dict[str, Any] | None = None,
        redirect_url: str | None = None,
        custom_fields: list[Any] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentPage] | Response[PaystackDataModel]:
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

        url = self._full_url("/page")

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
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or PaymentPage,
        )

    def get_pages(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[PaymentPage]] | Response[PaystackDataModel]:
        """Fetch payment pages available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
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

        url = self._full_url("/page?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaymentPage,
        )

    def get_page(
        self,
        id_or_slug: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentPage] | Response[PaystackDataModel]:
        """Get details of a payment page on your integration.

        Args:
            id_or_slug: The page ``ID`` or ``slug`` you want to fetch
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

        url = self._full_url(f"/page/{id_or_slug}")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or PaymentPage,
        )

    def update(
        self,
        id_or_slug: int | str,
        name: str,
        description: str | None = None,
        amount: int | None = None,
        active: bool | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentPage] | Response[PaystackDataModel]:
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

        url = self._full_url(f"/page/{id_or_slug}")
        payload = {
            "name": name,
        }
        optional_params = [
            ("amount", amount),
            ("active", active),
            ("description", description),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or PaymentPage,
        )

    def check_slug_available(
        self,
        slug: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Check the availability of a slug for a payment page.

        Args:
            slug: URL slug to be confirmed
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

        url = self._full_url(f"/page/check_slug_availability/{slug}")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    def add_products(
        self,
        id_: str,
        products: list[int],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaymentPage] | Response[PaystackDataModel]:
        """Add products to a payment page

        Args:
            id_: ID of the payment page
            products: Ids of all the products
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

        url = self._full_url(f"/page/{id_}/product")
        payload = {"products": products}
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or PaymentPage,
        )
