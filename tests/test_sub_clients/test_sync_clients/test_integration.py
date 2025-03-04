from datetime import timedelta
from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.models import IntegrationTimeout
from pypaystack2.sub_clients import IntegrationClient


class IntegrationClientTestCase(TestCase):
    client: IntegrationClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = IntegrationClient()

    def test_can_get_payment_session_timeout(self) -> None:
        response = self.client.get_payment_session_timeout()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout retrieved")
        self.assertIsInstance(response.data, IntegrationTimeout)
        self.assertEqual(response.data.payment_session_timeout, timedelta(seconds=60))

    def test_can_update_payment_session_timeout(self) -> None:
        response = self.client.update_payment_session_timeout(timeout=60)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout updated")
        self.assertIsInstance(response.data, IntegrationTimeout)
        self.assertEqual(response.data.payment_session_timeout, timedelta(seconds=60))
