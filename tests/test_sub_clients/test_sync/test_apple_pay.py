from http import HTTPStatus
from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import ApplePayClient
from pypaystack2.utils import Response
from tests.test_sub_clients.mocked_api_testcase import MockedAPITestCase


class MockedApplePayTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.client = ApplePayClient()

    def test_can_register_domain(self):
        response = self.client.register_domain(domain_name="example.com")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_domains(self):
        response = self.client.get_domains()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_unregister_domain(self):
        response = self.client.unregister_domain(domain_name="example.com")
        self.assertEqual(response.status_code, httpx.codes.OK)


class ApplePayTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = ApplePayClient()

    def test_can_register_domain(self):
        response = self.client.register_domain(domain_name="example.com")
        raw_data = {
            "status": False,
            "message": "Domain could not be registered on Apple Pay. Please verify that the correct file is hosted at https://example.com/.well-known/apple-developer-merchantid-domain-association",
            "meta": {"nextStep": "Try again later"},
            "type": "api_error",
            "code": "unknown",
        }
        expected_response = Response(
            status_code=HTTPStatus.BAD_REQUEST,
            status=False,
            message=(
                "Domain could not be registered on Apple Pay. Please verify that the "
                "correct file is hosted at https://example.com/.well-known/apple-deve"
                "loper-merchantid-domain-association"
            ),
            data=None,
            meta={"nextStep": "Try again later"},
            type="api_error",
            code="unknown",
            raw=raw_data,
        )
        self.assertEqual(response, expected_response)

    def test_can_get_domains(self):
        response = self.client.get_domains()
        expected_response = Response(
            status_code=HTTPStatus.NOT_FOUND,
            status=False,
            message="pypaystack2 was unable to serialize response as json data",
            data={"content": b""},
            meta=None,
            type=None,
            code=None,
            raw=b"",
        )
        self.assertEqual(response, expected_response)

    def test_can_unregister_domain(self):
        response = self.client.unregister_domain(domain_name="example.com")
        raw_data = {
            "status": True,
            "message": "Domain successfully unregistered on Apple Pay",
        }
        expected_response = Response(
            status_code=HTTPStatus.OK,
            status=True,
            message="Domain successfully unregistered on Apple Pay",
            data=None,
            meta=None,
            type=None,
            code=None,
            raw=raw_data,
        )
        self.assertEqual(response, expected_response)
