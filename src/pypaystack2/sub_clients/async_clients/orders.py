from http import HTTPMethod
from pypaystack2.models import Response
from pypaystack2.types import PaystackDataModel
from pypaystack2.models.payload_models import OrderLineItem
from pypaystack2.base_clients import append_query_params, BaseAsyncAPIClient


class AsyncOrderClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Orders API

    The Orders API allows you to create and manage orders for your products.
    """

    async def create(
        self,
        customer: int | str,
        line_items: list[OrderLineItem],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Create an order for selected items

        Args:
            customer: The customer code or ID whom the order belongs to
            line_items: The items in the order, it is a list of pydantic model
                `OrderLineItem` that contains the fields `product` which is the
                id of the product and `quantity` which is the amount of that product
                the customer ordered.
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
        _line_items = [item.model_dump(mode="json") for item in line_items]
        payload = {
            "customer": customer,
            "line_items": _line_items,
        }
        url = self._full_url("/order")
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            data=payload,
            response_data_model_class=alternate_model_class,
        )

    async def get_orders(
        self,
        pagination: int = 50,
        page: int = 1,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """List the orders available on your integration

        Args:
            pagination: Specifies how many orders you want to retrieve call.
            page: Specifies the page to retrieve from the pagination.
            start_date: A timestamp at which to start listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
            end_date: A timestamp at which to stop listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
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
        query_params = [("page", page), ("from", start_date), ("to", end_date)]
        url = self._full_url(f"/order/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def get_order(
        self,
        id: int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Fetch the details of an order on your integration

        Args:
            id: The ID of the order you want to retrieve.
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
        url = self._full_url(f"/order/{id}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def get_product_orders(
        self,
        id: int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Fetch all orders for a particular product

        Args:
            id: The id of the product you want to retrieve associated orders for.
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
        url = self._full_url(f"/order/product/{id}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def validate(
        self,
        code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Validate a pay for me order

        Args:
            code: The code for the order you want to validate.
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
        url = self._full_url(f"/order/{code}/validate")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )
