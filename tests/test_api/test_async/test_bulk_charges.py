from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.bulk_charges import AsyncBulkCharge
from pypaystack2.utils import BulkChargeInstruction, Status
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncBulkChargeTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncBulkCharge()

    async def test_can_initiate(self):
        instructions = [{"authorization": "", "amount": 1000, "reference": "qwerty"}]
        response = await self.wrapper.initiate(
            body=BulkChargeInstruction.from_dict_many(instructions)
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_batches(self):
        response = await self.wrapper.get_batches()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_batch(self):
        response = await self.wrapper.get_batch(id_or_code="BCH_weit42xwwmqlh39")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_charges_in_batch(self):
        response = await self.wrapper.get_charges_in_batch(
            id_or_code="BCH_weit42xwwmqlh39", status=Status.FAILED
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_pause_batch(self):
        response = await self.wrapper.pause_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_resume_batch(self):
        response = await self.wrapper.resume_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncBulkChargeTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncBulkCharge()

    async def test_can_initiate(self):
        instructions = [{"authorization": "", "amount": 1000, "reference": "qwerty"}]
        response = await self.wrapper.initiate(
            body=BulkChargeInstruction.from_dict_many(instructions)
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charges have been queued")

    async def test_can_get_batches(self):
        response = await self.wrapper.get_batches()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charges retrieved")

    async def test_can_get_batch(self):
        response = await self.wrapper.get_batch(id_or_code="BCH_weit42xwwmqlh39")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge retrieved")

    async def test_can_get_charges_in_batch(self):
        response = await self.wrapper.get_charges_in_batch(
            id_or_code="BCH_weit42xwwmqlh39", status=Status.FAILED
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge items retrieved")

    async def test_can_pause_batch(self):
        response = await self.wrapper.pause_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge batch has been paused")

    async def test_can_resume_batch(self):
        response = await self.wrapper.resume_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge batch has been resumed")
