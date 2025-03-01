from unittest.async_case import IsolatedAsyncioTestCase
from uuid import uuid4

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.payment_pages import AsyncPaymentPageClient
from pypaystack2.utils.response_models import PaymentPage


class AsyncPaymentPageTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncPaymentPageClient()

    async def test_can_create_payment_page(self):
        response = await self.client.create(
            "PyPaystack2 Test payment page", amount=1_000_000
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Page created")
        self.assertIsInstance(response.data, PaymentPage)

    async def test_can_get_payment_pages(self):
        response = await self.client.get_pages()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Pages retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], PaymentPage)

    async def test_can_get_payment_page(self):
        response = await self.client.get_page(id_or_slug="cgc4jh2uvv")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Page retrieved")
        self.assertIsInstance(response.data, PaymentPage)

    async def test_can_update_payment_page(self):
        new_name = "Jiggy Fund raiser"
        new_description = "A test description"
        response = await self.client.update(
            id_or_slug="cgc4jh2uvv", name=new_name, description=new_description
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Page updated")
        self.assertIsInstance(response.data, PaymentPage)
        self.assertEqual(response.data.name, new_name)
        self.assertEqual(response.data.description, new_description)

    async def test_can_check_slug_available(self):
        response = await self.client.check_slug_available(slug=f"{uuid4()}")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Slug is available")

    async def test_can_add_products(self):
        # TODO: Test properly when endpoint is fixed
        response = await self.client.add_products(
            id="cgc4jh2uvv", products=[1803331, 1803324]
        )
        self.assertEqual(response.status_code, httpx.codes.INTERNAL_SERVER_ERROR)
