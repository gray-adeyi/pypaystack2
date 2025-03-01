from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import SettlementClient


class SettlementTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = SettlementClient()

    def test_can_get_settlements(self):
        response = self.client.get_settlements()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Settlements retrieved")

    def test_can_get_settlement_transactions(self):
        # TODO: Test properly
        response = self.client.get_settlement_transactions(id="hello")
        self.assertEqual(response.status_code, httpx.codes.INTERNAL_SERVER_ERROR)
