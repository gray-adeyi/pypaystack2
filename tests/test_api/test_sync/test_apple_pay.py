from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api import ApplePay
from pypaystack2.utils import Response
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedApplePayTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = ApplePay()

    def test_can_register_domain(self):
        response = self.wrapper.register_domain(domain_name="example.com")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_domains(self):
        response = self.wrapper.get_domains()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_unregister_domain(self):
        response = self.wrapper.unregister_domain(domain_name="example.com")
        self.assertEqual(response.status_code, httpx.codes.OK)


class ApplePayTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = ApplePay()

    def test_can_register_domain(self):
        response = self.wrapper.register_domain(domain_name="example.com")
        expected_response = Response(
            status_code=400,
            status=False,
            message=(
                "Domain could not be registered on Apple Pay. Please verify that the "
                "correct file is hosted at https://example.com/.well-known/apple-deve"
                "loper-merchantid-domain-association"
            ),
            data=None,
            meta=None,
            type=None,
            code=None,
        )
        self.assertEqual(response, expected_response)

    def test_can_get_domains(self):
        response = self.wrapper.get_domains()
        expected_response = Response(
            status_code=404,
            status=False,
            message="pypaystack2 was unable to serialize response as json data",
            data={"content": b""},
            meta=None,
            type=None,
            code=None,
        )
        self.assertEqual(response, expected_response)

    def test_can_unregister_domain(self):
        response = self.wrapper.unregister_domain(domain_name="example.com")
        expected_response = Response(
            status_code=200,
            status=True,
            message="Domain successfully unregistered on Apple Pay",
            data=None,
            meta=None,
            type=None,
            code=None,
        )
        self.assertEqual(response, expected_response)
