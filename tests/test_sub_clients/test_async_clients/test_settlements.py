from unittest import IsolatedAsyncioTestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.models import Response, Settlement, Transaction
from pypaystack2.sub_clients import AsyncSettlementClient


class AsyncSettlementClientTestCase(IsolatedAsyncioTestCase):
    client: AsyncSettlementClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncSettlementClient()

    async def test_can_get_settlements(self) -> None:
        response: Response[list[Settlement]] = await self.client.get_settlements()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Settlements retrieved")

    @skip("incomplete tests")
    async def test_can_get_settlement_transactions(self) -> None:
        # TODO: Test properly
        response: Response[Transaction] = await self.client.get_settlement_transactions(
            id_="hello"
        )
        self.assertEqual(response.status_code, httpx.codes.INTERNAL_SERVER_ERROR)
