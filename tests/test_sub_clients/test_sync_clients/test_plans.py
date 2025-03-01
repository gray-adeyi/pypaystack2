from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import PlanClient
from pypaystack2.utils import Interval
from pypaystack2.utils.response_models import Plan


class PlanTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = PlanClient()

    def test_can_create(self):
        response = self.client.create(
            name="test plan", amount=600_000, interval=Interval.ANNUALLY
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan created")
        self.assertIsInstance(response.data, Plan)

    def test_can_get_plans(self):
        response = self.client.get_plans()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plans retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Plan)

    def test_can_get_plan(self):
        response = self.client.get_plan(id_or_code="710965")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan retrieved")
        self.assertIsInstance(response.data, Plan)

    def test_can_update(self):
        response = self.client.update(
            id_or_code="PLN_h5yiku242iq0sx5",
            name="Test plan pro",
            amount=700_000,
            interval=Interval.QUARTERLY,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Plan updated. 0 subscription(s) affected")
