from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Currency
from pypaystack2.models import Response
from pypaystack2.models.response_models import Refund
from pypaystack2.types import PaystackDataModel


class AsyncRefundClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Refunds API

    The Refunds API allows you to create and manage transaction refunds.
    https://paystack.com/docs/api/refund/
    """

    async def create(
        self,
        transaction: str,
        amount: int | None = None,
        currency: Currency | None = None,
        customer_note: str | None = None,
        merchant_note: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Refund] | Response[PaystackDataModel]:
        """Initiate a refund on your integration

        Args:
            transaction: Transaction reference or id
            amount: Amount ( in kobo if currency is NGN, pesewas, if currency is
                GHS, and cents, if currency is ZAR ) to be refunded to the
                customer. Amount is optional(defaults to original
                transaction amount) and cannot be more than the original
                transaction amount
            currency: Any value from the ``Currency`` enum
            customer_note: Customer reason
            merchant_note: Merchant reason
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

        url = self._full_url("/refund")
        payload = {"transaction": transaction}
        optional_params = [
            ("amount", amount),
            ("currency", currency),
            ("customer_note", customer_note),
            ("merchant_note", merchant_note),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Refund,
        )

    async def get_refunds(
        self,
        reference: str | None = None,
        currency: Currency | None = None,
        pagination: int = 50,
        page: int = 1,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Refund]] | Response[PaystackDataModel]:
        """Fetch refunds available on your integration.

        Args:
            reference: Identifier for transaction to be refunded
            currency: Any value from the ``Currency`` enum
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specifies exactly what refund you want to page.
                If not specified we use a default value of 1.
            start_date: A timestamp from which to start listing refund e.g. 2016-09-21
            end_date: A timestamp at which to stop listing refund e.g. 2016-09-21
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

        url = self._full_url(f"/refund?perPage={pagination}")
        query_params = [
            ("reference", reference),
            ("currency", currency),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Refund,
        )

    async def get_refund(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Refund] | Response[PaystackDataModel]:
        """Get details of a refund on your integration.

        Args:
            reference: Identifier for transaction to be refunded
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

        url = self._full_url(f"/refund/{reference}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Refund,
        )
