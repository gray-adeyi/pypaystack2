from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import IntegrationClient
from tests.test_sub_clients.mocked_api_testcase import MockedAPITestCase


class MockedIntegrationTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = IntegrationClient()

    def test_can_get_payment_session_timeout(self):
        response = self.wrapper.get_payment_session_timeout()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_update_payment_session_timeout(self):
        response = self.wrapper.update_payment_session_timeout(timeout=5)
        self.assertEqual(response.status_code, httpx.codes.OK)


class ControlIntegrationTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = IntegrationClient()

    def test_can_get_payment_session_timeout(self):
        response = self.wrapper.get_payment_session_timeout()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout retrieved")

    def test_can_update_payment_session_timeout(self):
        response = self.wrapper.update_payment_session_timeout(timeout=60)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout updated")
