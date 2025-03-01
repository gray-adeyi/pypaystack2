from datetime import timedelta
from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.integration import AsyncIntegrationClient
from pypaystack2.utils.response_models import IntegrationTimeout



class AsyncIntegrationTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncIntegrationClient()

    async def test_can_get_payment_session_timeout(self):
        response = await self.client.get_payment_session_timeout()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout retrieved")
        self.assertIsInstance(response.data, IntegrationTimeout)
        self.assertEqual(response.data.payment_session_timeout, timedelta(seconds=60))

    async def test_can_update_payment_session_timeout(self):
        response = await self.client.update_payment_session_timeout(timeout=60)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout updated")
        self.assertIsInstance(response.data, IntegrationTimeout)
        self.assertEqual(response.data.payment_session_timeout, timedelta(seconds=60))
