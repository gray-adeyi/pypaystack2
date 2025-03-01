from unittest.async_case import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.subaccounts import AsyncSubAccountClient
from pypaystack2.utils.response_models import SubAccount


class AsyncSubAccountTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncSubAccountClient()

    async def test_can_create(self):
        response = await self.client.create(
            business_name="Coyote solutions",
            settlement_bank="214",
            account_number="5273681014",
            percentage_charge=18.2,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subaccount created")
        self.assertIsInstance(response.data, SubAccount)

    async def test_can_get_subaccounts(self):
        response = await self.client.get_subaccounts()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subaccounts retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], SubAccount)

    async def test_can_get_subaccount(self):
        response = await self.client.get_subaccount(id_or_code=1270193)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subaccount retrieved")
        self.assertIsInstance(response.data, SubAccount)

    async def test_can_update(self):
        response = await self.client.update(
            id_or_code=1270193, business_name="Jiggy Tools"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subaccount updated")
        self.assertIsInstance(response.data, SubAccount)
