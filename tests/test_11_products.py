from random import randint
from uuid import uuid4
import uuid
from . import test_auth_key, Product, TestCase
from pypaystack2.utils import Currency


class TestProduct(TestCase):
    def setUp(self):
        super().setUp()
        self.assertNotEqual(test_auth_key, None)
        self.prod = Product(auth_key=test_auth_key)

    def test_can_create_product(self):
        resp = self.prod.create(
            name=f"product-{uuid4()}",
            description="A test product",
            price=1000,
            currency=Currency.NGN,
            quantity=randint(1, 100),
        )
        self.assertTrue(resp.status)
        self.assertEqual(resp.status_code, 201),
        self.assertEqual(resp.message, "Product successfully created")

    def test_can_get_products(self):
        resp = self.prod.get_products()
        self.assertTrue(resp.status)
        self.assertEqual(resp.status_code, 200),
        self.assertEqual(resp.message, "Products retrieved")

    def test_can_get_product(self):
        product = self.prod.get_products().data[0]
        resp = self.prod.get_product(id=product["id"])
        self.assertTrue(resp.status)
        self.assertEqual(resp.status_code, 200),
        self.assertEqual(resp.message, "Product retrieved")

    def test_can_update_product(self):
        product = self.prod.get_products().data[0]
        resp = self.prod.update(
            id=product["id"],
            name=f"Product Updated {uuid4()}",
            description="Updated desciption",
            price=43453,
            currency=Currency.ZAR,
        )
        self.assertTrue(resp.status)
        self.assertEqual(resp.status_code, 202),
        self.assertEqual(resp.message, "Product successfully updated")
