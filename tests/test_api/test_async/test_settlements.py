from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.settlements import AsyncSettlementClient
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncSettlementTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncSettlementClient()

    async def test_can_get_settlements(self):
        response = await self.wrapper.get_settlements()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_settlement_transactions(self):
        # TODO: Test properly
        response = await self.wrapper.get_settlement_transactions(id="hello")
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncSettlementTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncSettlementClient()

    async def test_can_get_settlements(self):
        response = await self.wrapper.get_settlements()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Settlements retrieved")

    async def test_can_get_settlement_transactions(self):
        # TODO: Test properly
        response = await self.wrapper.get_settlement_transactions(id="hello")
        self.assertEqual(response.status_code, httpx.codes.INTERNAL_SERVER_ERROR)
