from unittest import skip
from unittest.async_case import IsolatedAsyncioTestCase
from uuid import uuid4

import httpx
from dotenv import load_dotenv

from pypaystack2.models import Response, PaymentPage
from pypaystack2.sub_clients import AsyncPaymentPageClient


class AsyncPaymentPageClientTestCase(IsolatedAsyncioTestCase):
    client: AsyncPaymentPageClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncPaymentPageClient()

    async def test_can_create_payment_page(self) -> None:
        response: Response[PaymentPage] = await self.client.create(
            "PyPaystack2 Test payment page", amount=1_000_000
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Page created")
        self.assertIsInstance(response.data, PaymentPage)

    async def test_can_get_payment_pages(self) -> None:
        response: Response[list[PaymentPage]] = await self.client.get_pages()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Pages retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], PaymentPage)

    async def test_can_get_payment_page(self) -> None:
        response: Response[PaymentPage] = await self.client.get_page(
            id_or_slug="cgc4jh2uvv"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Page retrieved")
        self.assertIsInstance(response.data, PaymentPage)

    async def test_can_update_payment_page(self) -> None:
        new_name = "Jiggy Fund raiser"
        new_description = "A test description"
        response: Response[PaymentPage] = await self.client.update(
            id_or_slug="cgc4jh2uvv", name=new_name, description=new_description
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Page updated")
        self.assertIsInstance(response.data, PaymentPage)
        self.assertEqual(response.data.name, new_name)
        self.assertEqual(response.data.description, new_description)

    async def test_can_check_slug_available(self) -> None:
        response: Response[None] = await self.client.check_slug_available(
            slug=f"{uuid4()}"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Slug is available")

    @skip("incomplete test")
    async def test_can_add_products(self) -> None:
        # TODO: Test properly when endpoint is fixed
        response: Response[PaymentPage] = await self.client.add_products(
            id_="cgc4jh2uvv", products=[1803331, 1803324]
        )
        self.assertEqual(response.status_code, httpx.codes.INTERNAL_SERVER_ERROR)
