from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.dedicated_accounts import AsyncDedicatedAccountClient
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncDedicatedAccountTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncDedicatedAccountClient()


class AsyncDedicatedAccountTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncDedicatedAccountClient()

    async def test_can_create(self):
        # TODO: Test properly.
        await self.wrapper.create(customer="CUS_5qmwswiljybyyne")

    async def test_can_get_dedicated_accounts(self): ...

    async def test_can_get_dedicated_account(self): ...

    async def test_can_requery(self): ...

    async def test_can_deactivate(self): ...

    async def test_can_split(self): ...

    async def test_can_remove_split(self): ...

    async def test_can_get_providers(self):
        # TODO: Test properly.
        response = await self.wrapper.get_providers()
        self.assertEqual(response.status_code, httpx.codes.UNAUTHORIZED)
