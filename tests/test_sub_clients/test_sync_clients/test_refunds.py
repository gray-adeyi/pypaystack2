from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import RefundClient
from pypaystack2.utils.response_models import Refund


class RefundTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = RefundClient()

    def test_can_create(self):
        response = self.client.create(transaction="1699903748", amount=5000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund has been queued for processing")

    def test_can_get_refunds(self):
        response = self.client.get_refunds()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refunds retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Refund)

    def test_can_get_refund(self):
        response = self.client.get_refund(reference="9501470")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund retrieved")
        self.assertIsInstance(response.data, Refund)
