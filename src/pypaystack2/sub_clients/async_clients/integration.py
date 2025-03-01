from http import HTTPMethod
from typing import Type

from pypaystack2.base_api_client import BaseAsyncAPIClient
from pypaystack2.utils.models import PaystackDataModel
from pypaystack2.utils.models import Response
from pypaystack2.utils.response_models import IntegrationTimeout


class AsyncIntegrationClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Integration API

    The Integration API allows you to manage some settings on your integration.
    https://paystack.com/docs/api/integration/
    """

    async def get_payment_session_timeout(
        self,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[IntegrationTimeout]:
        """Fetch the payment session timeout on your integration

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

        url = self._full_url("/integration/payment_session_timeout")
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or IntegrationTimeout,
        )

    async def update_payment_session_timeout(
        self,
        timeout: int,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[IntegrationTimeout]:
        """Update the payment session timeout on your integration

        Args:
            timeout: Time before stopping session (in seconds). Set to 0 to cancel session timeouts
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

        payload = {"timeout": timeout}
        url = self._full_url("/integration/payment_session_timeout")
        return await self._handle_request(
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or IntegrationTimeout,
        )
