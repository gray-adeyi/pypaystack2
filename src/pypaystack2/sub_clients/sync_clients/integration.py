from http import HTTPMethod

from pypaystack2.base_clients import BaseAPIClient
from pypaystack2.models import Response
from pypaystack2.models.response_models import IntegrationTimeout
from pypaystack2.types import PaystackDataModel


class IntegrationClient(BaseAPIClient):
    """Provides a wrapper for paystack Integration API

    The Integration API allows you to manage some settings on your integration.
    https://paystack.com/docs/api/integration/
    """

    def get_payment_session_timeout(
        self,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[IntegrationTimeout] | Response[PaystackDataModel]:
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
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or IntegrationTimeout,
        )

    def update_payment_session_timeout(
        self,
        timeout: int,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[IntegrationTimeout] | Response[PaystackDataModel]:
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
        return self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or IntegrationTimeout,
        )
