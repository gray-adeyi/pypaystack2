import os

import httpx
from dotenv import load_dotenv

from pypaystack2 import __version__
from pypaystack2.base_api_client import BaseAPIClient, BaseAsyncAPIClient
from pypaystack2.exceptions import MissingSecretKeyException
from pypaystack2.utils import Response, HTTPMethod
from tests.test_sub_clients.mocked_api_testcase import (
    MockedAPITestCase,
    MockedAsyncAPITestCase,
)


class BaseAPITestCase(MockedAPITestCase):
    def test_raises_exception_for_missing_key(self):
        os.environ.pop("PAYSTACK_AUTHORIZATION_KEY", None)
        with self.assertRaises(MissingSecretKeyException):
            BaseAPIClient()

    def test__parse_url(self):
        load_dotenv()
        wrapper = BaseAPIClient()
        self.assertEqual(
            wrapper._full_url("/transactions"), "https://api.paystack.co/transactions"
        )

    def test__headers(self):
        load_dotenv()
        wrapper = BaseAPIClient()
        self.assertDictEqual(
            wrapper._headers,
            {
                "Authorization": f"Bearer {os.getenv('PAYSTACK_AUTHORIZATION_KEY')}",
                "Content-Type": "application/json",
                "User-Agent": f"PyPaystack2-{__version__}",
            },
        )

    def test__parse_response(self):
        load_dotenv()
        wrapper = BaseAPIClient()
        raw_response = httpx.Response(
            status_code=httpx.codes.OK,
            json={
                "status": True,
                "message": "valid response",
                "data": {"isValid": True},
            },
        )
        self.assertEqual(
            wrapper._deserialize_response(raw_response),
            Response(
                status_code=httpx.codes.OK,
                status=True,
                message="valid response",
                data={"isValid": True},
                meta=None,
                type=None,
                code=None,
            ),
        )

    def test__parse_http_method_kwargs(self):
        load_dotenv()
        wrapper = BaseAPIClient()
        with self.assertRaises(ValueError):
            wrapper._serialize_request_kwargs(url="", method=HTTPMethod.GET, data=None)
        headers = {
            "Authorization": f"Bearer {os.getenv('PAYSTACK_AUTHORIZATION_KEY')}",
            "Content-Type": "application/json",
            "User-Agent": f"PyPaystack2-{__version__}",
        }
        url = "https://api.paystack.co/transactions"
        self.assertDictEqual(
            wrapper._serialize_request_kwargs(
                url=wrapper._full_url("/transactions"),
                method=HTTPMethod.GET,
                data=None,
            ),
            {"headers": headers, "url": url},
        )
        self.assertDictEqual(
            wrapper._serialize_request_kwargs(
                url=wrapper._full_url("/transactions"),
                method=HTTPMethod.POST,
                data={"isValid": True},
            ),
            {"headers": headers, "url": url, "json": {"isValid": True}},
        )

    def test__handle_request(self):
        load_dotenv()
        wrapper = BaseAPIClient()
        expected_response = Response(
            status_code=httpx.codes.OK,
            status=True,
            message="This is a mocked response. No real API call to Paystack servers was made.",
            data={"isValid": True},
            meta=None,
            type=None,
            code=None,
        )
        self.assertEqual(
            wrapper._handle_request(
                method=HTTPMethod.GET,
                url=wrapper._full_url("/transactions"),
                data={"id_or_code": "qwerty"},
            ),
            expected_response,
        )
        self.assertEqual(
            wrapper._handle_request(
                method=HTTPMethod.POST,
                url=wrapper._full_url("/transactions"),
                data={"id_or_code": "qwerty"},
            ),
            expected_response,
        )


class BaseAsyncAPITestCase(MockedAsyncAPITestCase):
    async def test__handle_request(self):
        load_dotenv()
        wrapper = BaseAsyncAPIClient()
        expected_response = Response(
            status_code=httpx.codes.OK,
            status=True,
            message="This is a mocked response. No real API call to Paystack servers was made.",
            data={"isValid": True},
            meta=None,
            type=None,
            code=None,
        )
        self.assertEqual(
            await wrapper._handle_request(
                method=HTTPMethod.GET,
                url=wrapper._full_url("/transactions"),
                data={"id_or_code": "qwerty"},
            ),
            expected_response,
        )
        self.assertEqual(
            await wrapper._handle_request(
                method=HTTPMethod.POST,
                url=wrapper._full_url("/transactions"),
                data={"id_or_code": "qwerty"},
            ),
            expected_response,
        )
