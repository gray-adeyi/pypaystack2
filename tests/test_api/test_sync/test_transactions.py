from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api import Transaction
from pypaystack2.utils import Currency
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedTransactionTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = Transaction()


class TransactionTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Transaction()

    def test_can_initialize(self):
        response = self.wrapper.initialize(
            amount=10_000, email="coyotedevmail@gmail.com"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Authorization URL created")

    def test_can_verify(self):
        response = self.wrapper.verify(reference="6nqd9ulpqc")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Verification successful")

    def test_can_get_transactions(self):
        response = self.wrapper.get_transactions()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transactions retrieved")

    def test_can_get_transaction(self):
        response = self.wrapper.get_transaction(id="1728885471")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transaction retrieved")

    def test_can_charge(self):
        response = self.wrapper.charge(
            amount=250_000, email="coyotedevmail@gmail.com", auth_code="AUTH_w1renosr9o"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charge attempted")

    def test_can_get_timeline(self):
        response = self.wrapper.get_timeline(id_or_ref="1728885471")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Timeline retrieved")

    def test_can_get_totals(self):
        response = self.wrapper.totals()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transaction totals")

    def test_can_export(self):
        response = self.wrapper.export()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Export successful")

    def test_can_partial_debit(self):
        # TODO: Test properly.
        response = self.wrapper.partial_debit(
            auth_code="AUTH_72btv547",
            currency=Currency.NGN,
            amount=10_000,
            email="coyotedevmail@gmail.com",
        )
