from unittest import skip
from unittest.async_case import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.enums import Currency
from pypaystack2.models import (
    InitTransaction,
    Response,
    Transaction,
    TransactionLog,
    TransactionTotal,
    TransactionExport,
)
from pypaystack2.sub_clients import AsyncTransactionClient


class AsyncTransactionTestCase(IsolatedAsyncioTestCase):
    client: AsyncTransactionClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncTransactionClient()

    async def test_can_initialize(self) -> None:
        response: Response[InitTransaction] = await self.client.initialize(
            amount=10_000, email="coyotedevmail@gmail.com"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Authorization URL created")
        self.assertIsInstance(response.data, InitTransaction)

    async def test_can_verify(self) -> None:
        response: Response[Transaction] = await self.client.verify(
            reference="6nqd9ulpqc"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Verification successful")
        self.assertIsInstance(response.data, Transaction)

    async def test_can_get_transactions(self) -> None:
        response: Response[list[Transaction]] = await self.client.get_transactions()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transactions retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Transaction)

    async def test_can_get_transaction(self) -> None:
        response: Response[Transaction] = await self.client.get_transaction(
            id_="1728885471"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transaction retrieved")
        self.assertIsInstance(response.data, Transaction)

    async def test_can_charge(self) -> None:
        response: Response[Transaction] = await self.client.charge(
            amount=250_000, email="coyotedevmail@gmail.com", auth_code="AUTH_w1renosr9o"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charge attempted")
        self.assertIsInstance(response.data, Transaction)

    async def test_can_get_timeline(self) -> None:
        response: Response[TransactionLog] = await self.client.get_timeline(
            id_or_ref="1728885471"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Timeline retrieved")
        self.assertIsInstance(response.data, TransactionLog)

    async def test_can_get_totals(self) -> None:
        response: Response[TransactionTotal] = await self.client.totals()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transaction totals")
        self.assertIsInstance(response.data, TransactionTotal)

    async def test_can_export(self) -> None:
        response: Response[TransactionExport] = await self.client.export()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Export successful")
        self.assertTrue(response.data, TransactionExport)

    @skip("incompelte test")
    async def test_can_partial_debit(self) -> None:
        # TODO: Test properly.
        await self.client.partial_debit(
            auth_code="AUTH_72btv547",
            currency=Currency.NGN,
            amount=10_000,
            email="coyotedevmail@gmail.com",
        )
