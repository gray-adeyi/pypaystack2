from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Currency
from pypaystack2.models import Response
from pypaystack2.models.response_models import Product
from pypaystack2.types import PaystackDataModel


class AsyncProductClient(BaseAsyncAPIClient):
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
        unlimited: bool | None = None,
        quantity: int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Product] | Response[PaystackDataModel]:
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

        Raises:
            InvalidDataError: When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise ValueError(
                "You can't have unlimited set to True and have a quantity value."
            )

        url = self._full_url("/product")

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
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Product,
        )

    async def get_products(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Product]] | Response[PaystackDataModel]:
        """Fetches products available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: timestamp at which to stop listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
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

        url = self._full_url("/product?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Product,
        )

    async def get_product(
        self,
        id_: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Product] | Response[PaystackDataModel]:
        """Get details of a product on your integration.

        Args:
            id_: The product ``ID`` you want to fetch
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

        url = self._full_url(f"/product/{id_}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Product,
        )

    async def update(
        self,
        id_: str | int,
        name: str,
        description: str,
        price: int,
        currency: Currency,
        unlimited: bool | None = None,
        quantity: int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Product] | Response[PaystackDataModel]:
        """Update a product details on your integration

        Args:
            id_: Product ID
            name: Name of product
            description: A description for this product
            price: Price should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is GHS, and cents, if currency is ``Currency.ZAR``
            currency: Any value from the ``Currency`` enum
            unlimited: Set to ``True`` if the product has unlimited stock.
                Leave as ``False`` if the product has limited stock
            quantity: Number of products in stock. Use if unlimited is ``False``
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

        Raises:
            InvalidDataError: When unlimited is set to True and quantity has a value.
        """

        if unlimited is True and quantity is not None:
            raise ValueError(
                "You can't have unlimited set to True and quantity have a value."
            )
        url = self._full_url(f"/product/{id_}")
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
        return await self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or Product,
        )
