from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.disputes import AsyncDispute
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncDisputeTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncDispute()


class AsyncDisputeTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncDispute()

    async def test_can_get_disputes(self):
        response = await self.wrapper.get_disputes(
            start_date="2022-01-01", end_date="2023-05-11"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Disputes retrieved")

    async def test_can_get_dispute(self):
        # TODO: Test properly.
        response = await self.wrapper.get_dispute(id="114782792")
        self.assertEqual(response.status_code, httpx.codes.NOT_FOUND)

    async def test_can_get_transaction_disputes(self):
        # TODO: Test properly.
        ...

    async def test_can_update_dispute(self): ...

    async def test_can_add_evidence(self): ...

    async def test_can_get_upload_url(self): ...

    async def test_can_resolve_dispute(self): ...

    async def test_can_export_disputes(self): ...
