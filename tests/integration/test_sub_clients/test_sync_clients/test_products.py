from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.enums import Currency
from pypaystack2.models import Product
from pypaystack2.sub_clients import ProductClient


class ProductClientTestCase(TestCase):
    client: ProductClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = ProductClient()

    def test_can_create(self) -> None:
        response = self.client.create(
            name="Test product",
            description="test product desc",
            price=100_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product successfully created")
        self.assertIsInstance(response.data, Product)

    def test_can_get_products(self) -> None:
        response = self.client.get_products()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Products retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Product)

    def test_can_get_product(self) -> None:
        response = self.client.get_product(id_="1209661")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product retrieved")
        self.assertIsInstance(response.data, Product)

    def test_update(self) -> None:
        response = self.client.update(
            id_="1209661",
            name="Updated test product",
            description="the test description",
            price=600_000,
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.ACCEPTED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Product successfully updated")
        self.assertIsInstance(response.data, Product)
