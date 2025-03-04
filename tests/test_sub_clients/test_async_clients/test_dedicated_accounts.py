from unittest import IsolatedAsyncioTestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.models import Response, DedicatedAccountProvider
from pypaystack2.sub_clients import AsyncDedicatedAccountClient


class AsyncDedicatedAccountClientTestCase(IsolatedAsyncioTestCase):
    client: AsyncDedicatedAccountClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncDedicatedAccountClient()

    @skip("incomplete test")
    async def test_can_create(self) -> None:
        # TODO: Test properly.
        await self.client.create(customer="CUS_5qmwswiljybyyne")

    @skip("incomplete test")
    async def test_can_get_dedicated_accounts(self) -> None: ...

    @skip("incomplete test")
    async def test_can_get_dedicated_account(self) -> None: ...

    @skip("incomplete test")
    async def test_can_requery(self) -> None: ...

    @skip("incomplete test")
    async def test_can_deactivate(self) -> None: ...

    @skip("incomplete test")
    async def test_can_split(self) -> None: ...

    @skip("incomplete test")
    async def test_can_remove_split(self) -> None: ...

    @skip("incomplete test")
    async def test_can_get_providers(self) -> None:
        # TODO: Test properly.
        response: Response[
            list[DedicatedAccountProvider]
        ] = await self.client.get_providers()
        self.assertEqual(response.status_code, httpx.codes.UNAUTHORIZED)
