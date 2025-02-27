from http import HTTPMethod
from typing import Type

import httpx

from pypaystack2.base_api_client import BaseAPIClient, BaseAsyncAPIClient
from pypaystack2.utils import Response, append_query_params
from pypaystack2.utils.models import PaystackDataModel
from pypaystack2.utils.response_models import ApplePayDomains


class ApplePayClient(BaseAPIClient):
    """Provides a wrapper for paystack Apple Pay API

    The Apple Pay API allows you to register your application's top-level domain or subdomain.
    see https://paystack.com/docs/api/apple-pay/

    Note
      This feature is available to businesses in all markets except South Africa.
    """

    def register_domain(
        self,
        domain_name: str,
        alternate_response_model: Type[PaystackDataModel] | None = None,
    ) -> Response[None]:
        """Register a top-level domain or subdomain for your Apple Pay integration.

        Note:
            * This method can only be called with one domain or subdomain at a time.
            * This feature is available to businesses in all markets except South Africa.


        Args:
            domain_name: Domain name to be registered.
            alternate_response_model: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_response_model,
        )

    def get_domains(
        self,
        use_cursor: bool = False,
        next: str | None = None,
        previous: str | None = None,
        alternate_response_model: Type[PaystackDataModel] | None = None,
    ) -> Response[ApplePayDomains]:
        """Fetches all registered domains on your integration.

        Note
            * This feature is available to businesses in all markets except South Africa.

        Args:
            use_cursor:
            next:
            previous:
            alternate_response_model: A pydantic model class to use instead of the
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

        url = self._full_url("/apple-pay/domain")
        query_params = [
            ("use_cursor", use_cursor),
            ("next", next),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_response_model or ApplePayDomains,
        )

    def unregister_domain(
        self,
        domain_name: str,
        alternate_response_model: Type[PaystackDataModel] | None = None,
    ) -> Response[None]:
        """Unregister a top-level domain or subdomain previously used for your Apple Pay integration.

        Args:
            domain_name: Domain name to be unregistered
            alternate_response_model: A pydantic model class to use instead of the
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

        Note
            * This feature is available to businesses in all markets except South Africa.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        raw_response = httpx.request(
            HTTPMethod.DELETE, url, json=payload, headers=self._headers
        )
        return self._deserialize_response(
            raw_response, response_data_model_class=alternate_response_model
        )


class AsyncApplePayClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Apple Pay API

    The Apple Pay API allows you to register your application's top-level domain or subdomain.
    [Visit paystack sub_clients doc](https://paystack.com/docs/api/apple-pay/)
    """

    async def register_domain(
        self,
        domain_name: str,
        alternate_response_model: Type[PaystackDataModel] | None = None,
    ) -> Response[None]:
        """Register a top-level domain or subdomain for your Apple Pay integration.

        This method can only be called with one domain or subdomain at a time.

        Args:
            domain_name: Domain name to be registered.
            alternate_response_model: A pydantic model class to use instead of the
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

        url = self._full_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_response_model,
        )

    async def get_domains(
        self,
        use_cursor: bool = False,
        next: str | None = None,
        previous: str | None = None,
        alternate_response_model: Type[PaystackDataModel] | None = None,
    ) -> Response[ApplePayDomains]:
        """Fetches all registered domains on your integration.

        Note
            * This feature is available to businesses in all markets except South Africa.

        Args:
            use_cursor:
            next:
            previous:
            alternate_response_model: A pydantic model class to use instead of the
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

        url = self._full_url("/apple-pay/domain")
        query_params = [
            ("use_cursor", use_cursor),
            ("next", next),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_response_model or ApplePayDomains,
        )

    async def unregister_domain(
        self,
        domain_name: str,
        alternate_response_model: Type[PaystackDataModel] | None = None,
    ) -> Response[None]:
        """Unregister a top-level domain or subdomain previously used for your Apple Pay integration.

        Args:
             domain_name: Domain name to be unregistered
             alternate_response_model: A pydantic model class to use instead of the
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

         Note
             * This feature is available to businesses in all markets except South Africa.

         Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url("/apple-pay/domain")
        payload = {
            "domainName": domain_name,
        }
        async with httpx.AsyncClient() as client:
            raw_response = await client.request(
                HTTPMethod.DELETE, url, json=payload, headers=self._headers
            )
        return self._deserialize_response(
            raw_response, response_data_model_class=alternate_response_model
        )
