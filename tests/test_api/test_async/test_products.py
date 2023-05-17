from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.products import AsyncProduct
from pypaystack2.utils import Currency
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncProductTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncProduct()

    async def test_can_create(self):
        response = await self.wrapper.create(
            name="Test product",
            description="test product desc",
            price=100_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_products(self):
        response = await self.wrapper.get_products()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_product(self):
        response = await self.wrapper.get_product(id="1209661")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_update(self):
        response = await self.wrapper.update(
            id="1209661",
            name="Updated test product",
            description="the test description",
            price=600_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncProductTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncProduct()

    async def test_can_create(self):
        response = await self.wrapper.create(
            name="Test product",
            description="test product desc",
            price=100_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product successfully created")

    async def test_can_get_products(self):
        response = await self.wrapper.get_products()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Products retrieved")

    async def test_can_get_product(self):
        response = await self.wrapper.get_product(id="1209661")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product retrieved")

    async def test_update(self):
        response = await self.wrapper.update(
            id="1209661",
            name="Updated test product",
            description="the test description",
            price=600_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.ACCEPTED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product successfully updated")
