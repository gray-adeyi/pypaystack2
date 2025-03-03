from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import TransactionClient
from pypaystack2.utils import Currency
from pypaystack2.utils.response_models import (
    InitTransaction,
    Transaction,
    TransactionLog,
    TransactionTotal,
    TransactionExport,
)


class TransactionTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = TransactionClient()

    def test_can_initialize(self):
        response = self.client.initialize(
            amount=10_000, email="coyotedevmail@gmail.com"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Authorization URL created")
        self.assertIsInstance(response.data, InitTransaction)

    def test_can_verify(self):
        response = self.client.verify(reference="6nqd9ulpqc")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Verification successful")
        self.assertIsInstance(response.data, Transaction)

    def test_can_get_transactions(self):
        response = self.client.get_transactions()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transactions retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Transaction)

    def test_can_get_transaction(self):
        response = self.client.get_transaction(id="1728885471")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transaction retrieved")
        self.assertIsInstance(response.data, Transaction)

    def test_can_charge(self):
        response = self.client.charge(
            amount=250_000, email="coyotedevmail@gmail.com", auth_code="AUTH_w1renosr9o"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charge attempted")
        self.assertIsInstance(response.data, Transaction)

    def test_can_get_timeline(self):
        response = self.client.get_timeline(id_or_ref="1728885471")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Timeline retrieved")
        self.assertIsInstance(response.data, TransactionLog)

    def test_can_get_totals(self):
        response = self.client.totals()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transaction totals")
        self.assertIsInstance(response.data, TransactionTotal)

    def test_can_export(self):
        response = self.client.export()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Export successful")
        self.assertTrue(response.data, TransactionExport)

    def test_can_partial_debit(self):
        # TODO: Test properly.
        self.client.partial_debit(
            auth_code="AUTH_72btv547",
            currency=Currency.NGN,
            amount=10_000,
            email="coyotedevmail@gmail.com",
        )
