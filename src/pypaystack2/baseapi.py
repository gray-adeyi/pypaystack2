import os
from abc import ABC, abstractmethod
from json import JSONDecodeError
from typing import Union, Optional

import httpx
from httpx import codes

from pypaystack2._metadata import __version__
from pypaystack2.exceptions import InvalidMethodException, MissingAuthKeyException
from pypaystack2.utils import HTTPMethod, Response


class AbstractAPI(ABC):
    _CONTENT_TYPE = "application/json"
    _BASE_URL = "https://api.paystack.co"

    def __init__(self, auth_key: str = None):
        """
        Args:
            auth_key:
                Your paystack authorization key. Required only
                if it is not provided in your environmental
                variables as ``PAYSTACK_AUTHORIZATION_KEY=your_key``
        """
        if auth_key:
            self._PAYSTACK_AUTHORIZATION_KEY = auth_key
        else:
            self._PAYSTACK_AUTHORIZATION_KEY = os.getenv(
                "PAYSTACK_AUTHORIZATION_KEY", None
            )
        if not self._PAYSTACK_AUTHORIZATION_KEY:
            raise MissingAuthKeyException(
                "Missing Authorization key argument or env variable"
            )

    def _parse_url(self, endpoint_path: str) -> str:
        return f"{self._BASE_URL}{endpoint_path}"

    @property
    def _headers(self) -> dict[str, str]:
        return {
            "Content-Type": self._CONTENT_TYPE,
            "Authorization": f"Bearer {self._PAYSTACK_AUTHORIZATION_KEY}",
            "User-Agent": f"PyPaystack2-{__version__}",
        }

    def _parse_response(
        self, raw_response: httpx.Response, as_error: bool = False
    ) -> Response:
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
                data={"content": raw_response.content},
            )

        status = response_body.get("status", None)
        message = response_body.get("message", None)
        data = (
            response_body.get("data", None)
            if not as_error
            else response_body.get("errors")
        )
        return Response(raw_response.status_code, status, message, data)

    def _parse_http_method_kwargs(
        self, url: str, method: HTTPMethod, data: Optional[Union[dict, list]]
    ) -> dict:
        if url == "":
            raise ValueError("No url provided")
        http_method_kwargs = {"url": url, "json": data, "headers": self._headers}
        if method in {HTTPMethod.GET, HTTPMethod.DELETE}:
            http_method_kwargs.pop("json", None)
        return http_method_kwargs

    @abstractmethod
    def _handle_request(
        self, method: HTTPMethod, url: str, data: Optional[Union[dict, list]] = None
    ) -> Response: ...


class BaseAPI(AbstractAPI):
    """
    Base class for the pypaystack API wrappers.
    """

    def _handle_request(
        self, method: HTTPMethod, url: str, data: Union[dict, list] = None
    ) -> Response:
        """
        Makes request to paystack servers.

        Returns:
            Returns a python namedtuple of Response which contains
            status code, status(bool), message, data
        """
        http_methods_map = {
            HTTPMethod.GET: httpx.get,
            HTTPMethod.POST: httpx.post,
            HTTPMethod.PUT: httpx.put,
            HTTPMethod.PATCH: httpx.patch,
            HTTPMethod.DELETE: httpx.delete,
            HTTPMethod.OPTIONS: httpx.options,
            HTTPMethod.HEAD: httpx.head,
        }

        http_method = http_methods_map.get(method)

        http_method_kwargs = self._parse_http_method_kwargs(
            url=url, method=method, data=data
        )

        if not http_method:
            raise InvalidMethodException(
                "HTTP Request method not recognised or implemented"
            )

        response = http_method(**http_method_kwargs)
        if codes.is_success(response.status_code):
            return self._parse_response(response)
        else:
            return self._parse_response(response, as_error=True)


class BaseAsyncAPI(AbstractAPI):
    async def _handle_request(
        self, method: HTTPMethod, url: str, data: Union[dict, list] = None
    ) -> Response:
        """
        Makes request to paystack servers.

        Returns:
            Returns a python namedtuple of Response which contains
            status code, status(bool), message, data
        """
        async with httpx.AsyncClient() as client:
            http_method = getattr(client, method.value.lower(), None)
            http_method_kwargs = self._parse_http_method_kwargs(
                url=url, method=method, data=data
            )
            if not http_method:
                raise InvalidMethodException(
                    "HTTP Request method not recognised or implemented"
                )
            response = await http_method(**http_method_kwargs)

        if codes.is_success(response.status_code):
            return self._parse_response(response)
        else:
            return self._parse_response(response, as_error=True)
