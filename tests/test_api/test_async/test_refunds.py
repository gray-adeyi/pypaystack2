from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.refunds import AsyncRefund
from tests.test_api.mocked_api_testcase import MockedAPITestCase, MockedAsyncAPITestCase


class MockedAsyncRefundTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncRefund()

    async def test_can_create(self):
        response = await self.wrapper.create(transaction="1699903748", amount=5000)
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_refunds(self):
        response = await self.wrapper.get_refunds()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_refund(self):
        response = await self.wrapper.get_refund(reference="9501470")
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncRefundTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncRefund()

    async def test_can_create(self):
        response = await self.wrapper.create(transaction="1699903748", amount=5000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund has been queued for processing")

    async def test_can_get_refunds(self):
        response = await self.wrapper.get_refunds()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refunds retrieved")

    async def test_can_get_refund(self):
        response = await self.wrapper.get_refund(reference="9501470")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund retrieved")
