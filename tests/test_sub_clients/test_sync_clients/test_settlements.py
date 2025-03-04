from unittest import TestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import SettlementClient


class SettlementClientTestCase(TestCase):
    client: SettlementClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = SettlementClient()

    def test_can_get_settlements(self) -> None:
        response = self.client.get_settlements()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Settlements retrieved")

    @skip("incomplete test")
    def test_can_get_settlement_transactions(self) -> None:
        # TODO: Test properly
        response = self.client.get_settlement_transactions(id_="hello")
        self.assertEqual(response.status_code, httpx.codes.INTERNAL_SERVER_ERROR)
