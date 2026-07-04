from pypaystack2.enums import Currency
from pypaystack2.models import Response
from http import HTTPMethod
from pypaystack2.types import PaystackDataModel
from typing import Literal
from pypaystack2.base_clients import (
    add_to_payload,
    append_query_params,
    BaseAsyncAPIClient,
)


class AsyncStorefrontClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Storefronts API

    The Storefronts API allows you to create and manage digital shops
    to display and sell your products.
    """

    async def create(
        self,
        name: str,
        slug: str | None = None,
        description: str | None = None,
        currency: Currency | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Create a digital shop to manage and display your products

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
        url = self._full_url("/storefront")
        payload = {"name": name}
        optional_params = [
            ("slug", slug),
            ("description", description),
            ("currency", currency),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def get_storefronts(
        self,
        pagination: int = 50,
        page: int = 1,
        status: Literal["active", "inactive"] | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """List the storefronts available on your integration

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
        query_params = [
            ("page", page),
            ("status", status),
        ]
        url = self._full_url(f"/storefront/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def get_storefront(
        self,
        id: int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Get the details of a storefront on your integration

        Args:
            id: The ID of thhe storefront you want to retrieve
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
        url = self._full_url(f"/storefront/{id}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def update(
        self,
        id: int,
        name: str | None,
        description: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Update the details of a storefront on your integration

        Args:
            id: The ID of the storefront you want to update.
            name: The new name you want to update the storefront to.
            description: The new description for the storefront.
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
        url = self._full_url(f"/storefront/{id}")
        optional_params = [
            ("name", name),
            ("description", description),
        ]
        payload = add_to_payload(optional_params, {})
        return await self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def delete(
        self,
        id: int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Delete a storefront on your integration

        Args:
            id: The ID of the storefront you want to delete
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
        url = self._full_url(f"/storefront/{id}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.DELETE,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def verify_slug(
        self,
        slug: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Verify the availability of a slug before using it for your storefront

        Args:
            slug: The slug you want to verify.
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
        url = self._full_url(f"/storefront/verify/{slug}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def get_orders(
        self,
        id: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Fetch all orders in your storefront

        Args:
            id: The ID of the storefront
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
        url = self._full_url(f"/storefront/{id}/order")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def add_products(
        self,
        id: str,
        products: list[int],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Add products created prior to a storefront

        Args:
            id: The ID of the storefront you want to add products to.
            product: The IDs of the products you want to add to the storefront.
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
        url = self._full_url(f"/storefront/{id}/product")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            data={"products": products},
            response_data_model_class=alternate_model_class,
        )

    async def get_products(
        self,
        id: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """List the products in a storefront

        Args:
            id: The ID of the storefront you want to retrieve its products.
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
        url = self._full_url(f"/storefront/{id}/product")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def publish(
        self,
        id: int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Make your storefront publicly available

        Args:
            id: The ID of the storefront you want to publish.
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
        url = self._full_url(f"/storefront/{id}/publish")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def duplicate(
        self,
        id: int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Duplicate an existing storefront

        Args:
            id: The ID of the storefront you want to make a duplicate of
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
        url = self._full_url(f"/storefront/{id}/duplicate")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )
