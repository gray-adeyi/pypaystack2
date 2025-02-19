from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import PlanClient
from pypaystack2.utils import Interval
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedPlanTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = PlanClient()

    def test_can_create(self):
        response = self.wrapper.create(
            name="test plan", amount=600_000, interval=Interval.MONTHLY
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_plans(self):
        response = self.wrapper.get_plans()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_plan(self):
        response = self.wrapper.get_plan(id_or_code="710965")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_update(self):
        response = self.wrapper.update(
            id_or_code="PLN_h5yiku242iq0sx5",
            name="Test plan pro",
            amount=700_000,
            interval=Interval.WEEKLY,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)


class PlanTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = PlanClient()

    def test_can_create(self):
        response = self.wrapper.create(
            name="test plan", amount=600_000, interval=Interval.MONTHLY
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan created")

    def test_can_get_plans(self):
        response = self.wrapper.get_plans()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plans retrieved")

    def test_can_get_plan(self):
        response = self.wrapper.get_plan(id_or_code="710965")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan retrieved")

    def test_can_update(self):
        response = self.wrapper.update(
            id_or_code="PLN_h5yiku242iq0sx5",
            name="Test plan pro",
            amount=700_000,
            interval=Interval.WEEKLY,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan updated. 0 subscription(s) affected")
