from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.refunds import AsyncRefundClient
from pypaystack2.utils.response_models import Refund


class AsyncRefundTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncRefundClient()

    async def test_can_create(self):
        response = await self.client.create(transaction="1699903748", amount=5000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund has been queued for processing")

    async def test_can_get_refunds(self):
        response = await self.client.get_refunds()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refunds retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Refund)

    async def test_can_get_refund(self):
        response = await self.client.get_refund(reference="9501470")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund retrieved")
        self.assertIsInstance(response.data, Refund)
