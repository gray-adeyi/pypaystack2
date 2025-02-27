import logging
import os
import re
from abc import ABC, abstractmethod
from http import HTTPMethod
from json import JSONDecodeError
from typing import Type

import httpx
from pydantic import ValidationError

from pypaystack2._metadata import __version__
from pypaystack2.exceptions import InvalidMethodException, MissingSecretKeyException
from pypaystack2.fees_calculation_mixin import FeesCalculationMixin
from pypaystack2.utils import Response
from pypaystack2.utils.models import PaystackDataModel

logger = logging.getLogger(__name__)


class AbstractAPIClient(FeesCalculationMixin, ABC):
    _CONTENT_TYPE = "application/json"
    _BASE_URL = "https://api.paystack.co"
    _SECRET_KEY_IN_ENV_KEY = "PAYSTACK_SECRET_KEY"

    def __init__(self, secret_key: str | None = None):
        """
        Args:
            secret_key:
                Your paystack integration secret key. Required only
                if it is not provided in your environmental
                variables as ``PAYSTACK_SECRET_KEY=your_key``
        """
        if secret_key:
            self._secret_key = secret_key
        else:
            self._secret_key = os.getenv(self._SECRET_KEY_IN_ENV_KEY, None)
        if not self._secret_key:
            raise MissingSecretKeyException(
                "secret key was not provided on client instantiation "
                f"or set in env variables as `{self._SECRET_KEY_IN_ENV_KEY}`"
            )

    def _full_url(self, endpoint: str) -> str:
        return f"{self._BASE_URL}{endpoint}"

    @property
    def _headers(self) -> dict[str, str]:
        return {
            "Content-Type": self._CONTENT_TYPE,
            "Authorization": f"Bearer {self._secret_key}",
            "User-Agent": f"PyPaystack2-{__version__}",
        }

    def _deserialize_response(
        self,
        raw_response: httpx.Response,
        response_data_model_class: Type[PaystackDataModel] | None = None,
        raise_serialization_exception: bool = False,
    ) -> Response[PaystackDataModel]:
        """
        Parses an `httpx.Response` into a `Response`.

        Returns:
            A python namedtuple of Response which contains
            status code, status(bool), message, data
        """
        try:
            response_body = raw_response.json()
        except JSONDecodeError:
            return Response(
                status_code=raw_response.status_code,
                status=False,
                message="pypaystack2 was unable to serialize response as json data",
                data=None,
                meta=None,
                type=None,
                code=None,
                raw=raw_response.content,
            )

        status = response_body.get("status", False)
        message = response_body.get("message", "")
        meta = response_body.get("meta", None)
        type_ = response_body.get("type", None)
        code = response_body.get("code", None)
        if data := response_body.get("data", None):
            data = self._to_pydantic_model(
                self._normalize_data(data),
                response_data_model_class,
                raise_serialization_exception,
            )
        return Response(
            status_code=raw_response.status_code,
            status=status,
            message=message,
            data=data,
            meta=meta,
            type=type_,
            code=code,
            raw=response_body,
        )

    def _to_pydantic_model(
        self,
        data,
        response_data_model_class: Type[PaystackDataModel] | None = None,
        raise_serialization_exception: bool = False,
    ):
        """Tries to convert the provided data to the provided pydantic instance, on failure to do so,
        it returns None.
        """
        if not response_data_model_class:
            return None
        try:
            if isinstance(data, dict):
                return response_data_model_class.model_validate(data)
            if isinstance(data, list):
                return [response_data_model_class.model_validate(item) for item in data]
        except ValidationError as error:
            if raise_serialization_exception:
                raise error
            warning_message = f"""An validation error occurred while trying to serialize the data returned
by paystack with the pydantic model `{response_data_model_class}` but has been allowed to
fail silently. `Response.data` has been set to `None` but this data is still available in
`Response.raw`. If the pydantic model that raised this error is from the
library, It's not your fault, Its either I goofed up in the model definitions
or the response data doesn't match the model.
please create an issue at https://github.com/gray-adeyi/pypaystack2/issues
If you're using a custom pydantic model other than the one from the library,
please see that your model definitions match the data returned by paystack
            
These are the validation errors:
{error}
"""
            logger.warning(warning_message)
        return None

    def _serialize_request_kwargs(
        self, url: str, method: HTTPMethod, data: dict | list | None
    ) -> dict:
        if url == "":
            raise ValueError("No url provided")
        request_kwargs = {"url": url, "json": data, "headers": self._headers}
        if method in {HTTPMethod.GET, HTTPMethod.DELETE}:
            request_kwargs.pop("json", None)
        return request_kwargs

    def _normalize_data(self, data: dict | list) -> dict | list:
        """Converts keys in the data from camelCase to snake_case"""
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                new_key = self._camel_to_snake_case(key)
                new_dict[new_key] = self._normalize_data(value)
            return new_dict
        elif isinstance(data, list):
            return [self._normalize_data(item) for item in data]
        return data

    def _camel_to_snake_case(self, value: str) -> str:
        """Converts a camelCase value to a snake_case value"""
        return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()

    @abstractmethod
    def _handle_request(
        self,
        method: HTTPMethod,
        url: str,
        data: dict | list | None = None,
        response_data_model_class: Type[PaystackDataModel] | None = None,
        raise_serialization_exception: bool = False,
    ) -> Response[PaystackDataModel]: ...


class BaseAPIClient(AbstractAPIClient):
    """
    Base class for the pypaystack API wrappers.
    """

    def _handle_request(
        self,
        method: HTTPMethod,
        url: str,
        data: dict | list | None = None,
        response_data_model_class: Type[PaystackDataModel] = None,
        raise_serialization_exception: bool = False,
    ) -> Response[PaystackDataModel]:
        """
        Makes request to paystack servers.

        Args:
            raise_serialization_exception: Set to `True` to raise pydantic validation errors when it fails
                to serialize the data returned by paystack with the response model or
                `alternate_response_model` if provided. The default behaviour is to fail
                silently and set `Response.data` to None

        Returns:
            Returns a python namedtuple of Response which contains
            status code, status(bool), message, data
        """
        http_method_handlers_mapping = {
            HTTPMethod.GET: httpx.get,
            HTTPMethod.POST: httpx.post,
            HTTPMethod.PUT: httpx.put,
            HTTPMethod.PATCH: httpx.patch,
            HTTPMethod.DELETE: httpx.delete,
            HTTPMethod.OPTIONS: httpx.options,
            HTTPMethod.HEAD: httpx.head,
        }

        http_method_handler = http_method_handlers_mapping.get(method)

        request_kwargs = self._serialize_request_kwargs(
            url=url, method=method, data=data
        )

        if not http_method_handler:
            raise InvalidMethodException(
                "HTTP Request method not recognised or implemented"
            )

        response = http_method_handler(**request_kwargs)
        return self._deserialize_response(
            response, response_data_model_class, raise_serialization_exception
        )


class BaseAsyncAPIClient(AbstractAPIClient):
    async def _handle_request(
        self,
        method: HTTPMethod,
        url: str,
        data: dict | list | None = None,
        response_data_model_class: Type[PaystackDataModel] | None = None,
        raise_serialization_exception: bool = False,
    ) -> Response[PaystackDataModel]:
        """
        Makes request to paystack servers.

        Args:
            raise_serialization_exception: Set to `True` to raise pydantic validation errors when it fails
                to serialize the data returned by paystack with the response model or
                `alternate_response_model` if provided. The default behaviour is to fail
                silently and set `Response.data` to None

        Returns:
            Returns a python namedtuple of Response which contains
            status code, status(bool), message, data
        """
        async with httpx.AsyncClient() as client:
            http_method_handler = getattr(client, method.value.lower(), None)
            request_kwargs = self._serialize_request_kwargs(
                url=url, method=method, data=data
            )
            if not http_method_handler:
                raise InvalidMethodException(
                    "HTTP Request method not recognised or implemented"
                )
            response = await http_method_handler(**request_kwargs)

        return self._deserialize_response(
            response, response_data_model_class, raise_serialization_exception
        )
