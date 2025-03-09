from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.enums import Status
from pypaystack2.sub_clients import BulkChargeClient
from pypaystack2.models import BulkChargeInstruction, BulkChargeUnitCharge, BulkCharge


class BulkChargeClientTestCase(TestCase):
    client: BulkChargeClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = BulkChargeClient()

    def test_can_initiate(self) -> None:
        instructions = [{"authorization": "", "amount": 1000, "reference": "qwerty"}]
        response = self.client.initiate(
            body=[
                BulkChargeInstruction.model_validate(instruction)
                for instruction in instructions
            ],
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    def test_can_get_batches(self) -> None:
        response = self.client.get_batches()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charges retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], BulkCharge)

    def test_can_get_batch(self) -> None:
        response = self.client.get_batch(id_or_code="BCH_weit42xwwmqlh39")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge retrieved")
        self.assertIsInstance(response.data, BulkCharge)

    def test_can_get_charges_in_batch(self) -> None:
        response = self.client.get_charges_in_batch(
            id_or_code="BCH_weit42xwwmqlh39", status=Status.FAILED
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge items retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], BulkChargeUnitCharge)

    def test_can_pause_batch(self) -> None:
        response = self.client.pause_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge batch has been paused")

    def test_can_resume_batch(self) -> None:
        response = self.client.resume_batch(batch_code="BCH_mpnk3lozhd4vnd5")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bulk charge batch has been resumed")
