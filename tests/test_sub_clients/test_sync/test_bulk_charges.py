from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import BulkChargeClient
from pypaystack2.utils import BulkChargeInstruction, Status
from tests.test_sub_clients.mocked_api_testcase import MockedAPITestCase


class MockedBulkChargeTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = BulkChargeClient()

    def test_can_initiate(self):
        instructions = [{"authorization": "", "amount": 1000, "reference": "qwerty"}]
        response = self.wrapper.initiate(
            body=BulkChargeInstruction.from_dict_many(instructions)
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_batches(self):
        response = self.wrapper.get_batches()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_batch(self):
        response = self.wrapper.get_batch(id_or_code="BCH_weit42xwwmqlh39")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_charges_in_batch(self):
        response = self.wrapper.get_charges_in_batch(
            id_or_code="BCH_weit42xwwmqlh39", status=Status.FAILED
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_pause_batch(self):
        response = self.wrapper.pause_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_resume_batch(self):
        response = self.wrapper.resume_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)


class BulkChargeTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = BulkChargeClient()

    def test_can_initiate(self):
        instructions = [{"authorization": "", "amount": 1000, "reference": "qwerty"}]
        response = self.wrapper.initiate(
            body=BulkChargeInstruction.from_dict_many(instructions)
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    def test_can_get_batches(self):
        response = self.wrapper.get_batches()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charges retrieved")

    def test_can_get_batch(self):
        response = self.wrapper.get_batch(id_or_code="BCH_weit42xwwmqlh39")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge retrieved")

    def test_can_get_charges_in_batch(self):
        response = self.wrapper.get_charges_in_batch(
            id_or_code="BCH_weit42xwwmqlh39", status=Status.FAILED
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge items retrieved")

    def test_can_pause_batch(self):
        response = self.wrapper.pause_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge batch has been paused")

    def test_can_resume_batch(self):
        response = self.wrapper.resume_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge batch has been resumed")
