from typing import Literal
from http import HTTPMethod
from pypaystack2.types import PaystackDataModel
from pypaystack2.base_clients import BaseAsyncAPIClient, append_query_params


class AsyncDirectDebitClient(BaseAsyncAPIClient):
    """This client provides API for interacting with Paystack's Direct Debit API

    The Direct Debit API allows you manage the authorization on your customer's bank accounts.
    """

    async def trigger_activation_charge(
        self,
        customer_ids: list[str | int],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """Trigger an activation charge on an inactive mandate on behalf of your customer.

        Args:
            customer_ids: A list of customer IDs with pending mandate authorizations.
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
        url = self._full_url("/directdebit/activation-charge")
        payload = {
            "customer_ids": customer_ids,
        }
        return await self._handle_request(
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def get_mandate_authorizations(
        self,
        cursor: str | None = None,
        status: Literal["pending", "active", "revoked"] | None = None,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """Get the list of direct debit mandates associated with a customer.

        Args:
            cursor: The cursor value of the next set of authorizations to fetch.
                You can get this from the meta object of the response
            status: Filter by the authorization status.
            pagination: The number of authorizations to fetch per call
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
            ("cursor", cursor),
            ("status", status),
        ]
        url = self._full_url(
            f"/directdebit/mandate-authorizations?per_page={pagination}"
        )
        url = append_query_params(query_params, url)
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )
