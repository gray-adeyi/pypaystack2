from unittest import TestCase
from unittest.async_case import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.utils.models import Response
from pypaystack2.sub_clients.async_clients.verification import AsyncVerificationClient
from pypaystack2.utils.enums import AccountType, Country, Document
from pypaystack2.utils.response_models import (
    BankAccountInfo,
    AccountVerificationInfo,
    CardBin,
)


class AsyncVerificationTestCase(IsolatedAsyncioTestCase):
    client: AsyncVerificationClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncVerificationClient()

    async def test_can_resolve_account_number(self) -> None:
        response: Response[BankAccountInfo] = await self.client.resolve_account_number(
            bank_code="214", account_number="5273681014"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Account number resolved")
        self.assertIsInstance(response.data, BankAccountInfo)

    async def test_can_validate_account(self) -> None:
        response: Response[
            AccountVerificationInfo
        ] = await self.client.validate_account(
            account_number="0123456789",
            account_name="Ann Bron",
            account_type=AccountType.PERSONAL,
            country_code=Country.SOUTH_AFRICA,
            bank_code="632005",
            document_type=Document.IDENTITY_NUMBER,
            document_number="1234567890123",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Personal Account Verification attempted")
        self.assertIsInstance(response.data, AccountVerificationInfo)

    async def test_can_resolve_card_bin(self) -> None:
        response: Response[CardBin] = await self.client.resolve_card_bin(bin="539983")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Bin resolved")
        self.assertIsInstance(response.data, CardBin)
