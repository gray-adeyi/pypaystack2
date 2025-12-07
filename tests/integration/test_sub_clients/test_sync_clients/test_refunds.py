from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.models import Refund
from pypaystack2.sub_clients import RefundClient


class RefundClientTestCase(TestCase):
    client: RefundClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = RefundClient()

    def test_can_create(self) -> None:
        response = self.client.create(transaction="1699903748", amount=5000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund has been queued for processing")

    def test_can_get_refunds(self) -> None:
        response = self.client.get_refunds()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refunds retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Refund)

    def test_can_get_refund(self) -> None:
        response = self.client.get_refund(reference="9501470")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund retrieved")
        self.assertIsInstance(response.data, Refund)
