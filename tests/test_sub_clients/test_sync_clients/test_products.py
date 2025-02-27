from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import ProductClient
from pypaystack2.utils import Currency
from tests.test_sub_clients.mocked_api_testcase import MockedAPITestCase


class MockedProductTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = ProductClient()

    def test_can_create(self):
        response = self.wrapper.create(
            name="Test product",
            description="test product desc",
            price=100_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_products(self):
        response = self.wrapper.get_products()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_product(self):
        response = self.wrapper.get_product(id="1209661")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_update(self):
        response = self.wrapper.update(
            id="1209661",
            name="Updated test product",
            description="the test description",
            price=600_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)


class ProductTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = ProductClient()

    def test_can_create(self):
        response = self.wrapper.create(
            name="Test product",
            description="test product desc",
            price=100_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product successfully created")

    def test_can_get_products(self):
        response = self.wrapper.get_products()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Products retrieved")

    def test_can_get_product(self):
        response = self.wrapper.get_product(id="1209661")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product retrieved")

    def test_update(self):
        response = self.wrapper.update(
            id="1209661",
            name="Updated test product",
            description="the test description",
            price=600_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.ACCEPTED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product successfully updated")
