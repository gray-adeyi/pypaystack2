import os
from typing import Any, Dict, NamedTuple, Union
from pyparsing import Optional
import requests
from requests import Response as RResponse
import json
from pypaystack2 import version
from .errors import *

# namedtuple Response to extend the
# capabilities of the tuple sent as
# response
ResponseData = Union[dict[str, Any], list[dict[str, Any]]]


class Response(NamedTuple):
    """A namedtuple that models the data gotten from making a request to
    paystacks API endpoints.

    Parameters
    ----------
    status_code: int
        The response status code
    status: bool
        A flag for the response status
    message: str
        paystack response message
    data: Optional[ResponseData]
        data sent from paystack's server if any.
    """

    status_code: int
    status: str
    message: str
    data: ResponseData


class BaseAPI:
    """
    Base class for the pypaystack python API wrapper for paystack
    Not to be instantiated directly.
    """

    _CONTENT_TYPE = "application/json"
    _BASE_END_POINT = "https://api.paystack.co"

    def __init__(self, auth_key: str = None):
        """
        Parameters
        ----------
        auth_key:
            Your paystack authorization key. Required only
            if it is not provided in your enviromental
            variables as ``PAYSTACK_AUTHORIZATION_KEY=your_key``

        """
        if auth_key:
            self._PAYSTACK_AUTHORIZATION_KEY = auth_key
        else:
            self._PAYSTACK_AUTHORIZATION_KEY = os.getenv(
                "PAYSTACK_AUTHORIZATION_KEY", None
            )
        if not self._PAYSTACK_AUTHORIZATION_KEY:
            raise MissingAuthKeyError(
                "Missing Authorization key argument or env variable"
            )

    def _url(self, path: str) -> str:
        return self._BASE_END_POINT + path

    def _headers(self) -> dict[str, str]:
        return {
            "Content-Type": self._CONTENT_TYPE,
            "Authorization": "Bearer " + self._PAYSTACK_AUTHORIZATION_KEY,
            "user-agent": f"pyPaystack2-{version.__version__}",
        }

    def _parse_json(self, response_obj: RResponse) -> Response:
        """
        This function takes in every json response sent back by the
        server and trys to get out the important return variables

        Returns a python namedtuple of Response which contains
        status code, status(bool), message, data
        """
        parsed_response = response_obj.json()

        status = parsed_response.get("status", None)
        message = parsed_response.get("message", None)
        data = parsed_response.get("data", None)
        return Response(response_obj.status_code, status, message, data)

    def _handle_request(
        self, method: str, url: str, data: Dict[str, any] = None
    ) -> Response:
        """
        Generic function to handle all API url calls

        Returns a python namedtuple of Response which contains
        status code, status(bool), message, data
        """
        method_map = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete,
        }

        payload = json.dumps(data) if data else data
        request = method_map.get(method)

        if not request:
            raise InvalidMethodError("Request method not recognised or implemented")

        response = request(url, headers=self._headers(), data=payload, verify=True)
        if response.status_code == 404:
            return Response(
                response.status_code, False, "The object request cannot be found", None
            )

        if response.status_code in [200, 201]:
            return self._parse_json(response)
        else:
            body = response.json()
            return Response(
                status_code=response.status_code,
                status=body.get("status"),
                message=body.get("message"),
                data=body.get("errors"),
            )
