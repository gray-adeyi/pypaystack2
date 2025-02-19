from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import RefundClient
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedRefundTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = RefundClient()

    def test_can_create(self):
        response = self.wrapper.create(transaction="1699903748", amount=5000)
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_refunds(self):
        response = self.wrapper.get_refunds()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_refund(self):
        response = self.wrapper.get_refund(reference="9501470")
        self.assertEqual(response.status_code, httpx.codes.OK)


class RefundTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = RefundClient()

    def test_can_create(self):
        response = self.wrapper.create(transaction="1699903748", amount=5000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund has been queued for processing")

    def test_can_get_refunds(self):
        response = self.wrapper.get_refunds()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refunds retrieved")

    def test_can_get_refund(self):
        response = self.wrapper.get_refund(reference="9501470")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Refund retrieved")
