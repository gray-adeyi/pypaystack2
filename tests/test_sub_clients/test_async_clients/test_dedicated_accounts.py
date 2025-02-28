from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.dedicated_accounts import (
    AsyncDedicatedAccountClient,
)


class AsyncDedicatedAccountTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncDedicatedAccountClient()

    async def test_can_create(self):
        # TODO: Test properly.
        await self.client.create(customer="CUS_5qmwswiljybyyne")

    async def test_can_get_dedicated_accounts(self): ...

    async def test_can_get_dedicated_account(self): ...

    async def test_can_requery(self): ...

    async def test_can_deactivate(self): ...

    async def test_can_split(self): ...

    async def test_can_remove_split(self): ...

    async def test_can_get_providers(self):
        # TODO: Test properly.
        response = await self.client.get_providers()
        self.assertEqual(response.status_code, httpx.codes.UNAUTHORIZED)
