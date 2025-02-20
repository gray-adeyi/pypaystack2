from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import SettlementClient
from tests.test_sub_clients.mocked_api_testcase import MockedAPITestCase


class MockedSettlementTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = SettlementClient()

    def test_can_get_settlements(self):
        response = self.wrapper.get_settlements()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_settlement_transactions(self):
        # TODO: Test properly
        response = self.wrapper.get_settlement_transactions(id="hello")
        self.assertEqual(response.status_code, httpx.codes.OK)


class SettlementTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = SettlementClient()

    def test_can_get_settlements(self):
        response = self.wrapper.get_settlements()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Settlements retrieved")

    def test_can_get_settlement_transactions(self):
        # TODO: Test properly
        response = self.wrapper.get_settlement_transactions(id="hello")
        self.assertEqual(response.status_code, httpx.codes.INTERNAL_SERVER_ERROR)
