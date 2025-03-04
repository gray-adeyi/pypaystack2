from unittest.async_case import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.enums import Split, Currency, Bearer
from pypaystack2.models import SplitAccount, Response, TransactionSplit
from pypaystack2.sub_clients import AsyncTransactionSplitClient


class AsyncTransactionSplitClientTestCase(IsolatedAsyncioTestCase):
    client: AsyncTransactionSplitClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncTransactionSplitClient()

    async def test_can_create(self) -> None:
        sub_accounts = [
            SplitAccount(subaccount="ACCT_l6nz8ofjywrc66k", share=0.5),
            SplitAccount(subaccount="ACCT_iw34h1ss4p1luyd", share=0.5),
        ]
        response: Response[TransactionSplit] = await self.client.create(
            name="Pypaystack2 Test Split",
            type=Split.PERCENTAGE,
            currency=Currency.NGN,
            subaccounts=sub_accounts,
            bearer_type=Bearer.ALL,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Split created")
        self.assertIsInstance(response.data, TransactionSplit)

    async def test_can_get_splits(self) -> None:
        response: Response[list[TransactionSplit]] = await self.client.get_splits()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Split retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], TransactionSplit)

    async def test_can_get_split(self) -> None:
        response: Response[TransactionSplit] = await self.client.get_split(
            id_or_code=3885195
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Split retrieved")
        self.assertIsInstance(response.data, TransactionSplit)

    async def test_can_update(self) -> None:
        response: Response[TransactionSplit] = await self.client.update(
            id="3885195", name="Pypaystack2 Test split updated", active=True
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Split group updated")
        self.assertIsInstance(response.data, TransactionSplit)

    async def test_can_add_or_update(self) -> None:
        response: Response[TransactionSplit] = await self.client.add_or_update(
            id="3885195", subaccount="ACCT_l6nz8ofjywrc66k", share=0.5
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subaccount added")
        self.assertIsInstance(response.data, TransactionSplit)

    async def test_can_remove(self) -> None:
        id_ = "3885195"
        sub_account = "ACCT_l6nz8ofjywrc66k"
        await self.client.add_or_update(id=id_, subaccount=sub_account, share=0.7)
        response: Response[None] = await self.client.remove(
            id=id_, subaccount=sub_account
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subaccount removed")
