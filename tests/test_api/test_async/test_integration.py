from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.integration import AsyncIntegration
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncIntegrationTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncIntegration()

    async def test_can_get_payment_session_timeout(self):
        response = await self.wrapper.get_payment_session_timeout()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_update_payment_session_timeout(self):
        response = await self.wrapper.update_payment_session_timeout(timeout=5)
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncIntegrationTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncIntegration()

    async def test_can_get_payment_session_timeout(self):
        response = await self.wrapper.get_payment_session_timeout()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout retrieved")

    async def test_can_update_payment_session_timeout(self):
        response = await self.wrapper.update_payment_session_timeout(timeout=60)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment session timeout updated")
