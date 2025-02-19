from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.plans import AsyncPlanClient
from pypaystack2.utils import Interval
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncPlanTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncPlanClient()

    async def test_can_create(self):
        response = await self.wrapper.create(
            name="test plan", amount=600_000, interval=Interval.MONTHLY
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_plans(self):
        response = await self.wrapper.get_plans()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_plan(self):
        response = await self.wrapper.get_plan(id_or_code="710965")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_update(self):
        response = await self.wrapper.update(
            id_or_code="PLN_h5yiku242iq0sx5",
            name="Test plan pro",
            amount=700_000,
            interval=Interval.WEEKLY,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncPlanTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncPlanClient()

    async def test_can_create(self):
        response = await self.wrapper.create(
            name="test plan", amount=600_000, interval=Interval.MONTHLY
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan created")

    async def test_can_get_plans(self):
        response = await self.wrapper.get_plans()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plans retrieved")

    async def test_can_get_plan(self):
        response = await self.wrapper.get_plan(id_or_code="710965")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan retrieved")

    async def test_can_update(self):
        response = await self.wrapper.update(
            id_or_code="PLN_h5yiku242iq0sx5",
            name="Test plan pro",
            amount=700_000,
            interval=Interval.WEEKLY,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan updated. 0 subscription(s) affected")
