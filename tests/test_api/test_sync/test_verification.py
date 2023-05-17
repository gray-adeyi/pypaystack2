from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api import Verification
from pypaystack2.utils import AccountType, Country, Document
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedVerificationTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = Verification()


class VerificationTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Verification()

    def test_can_resolve_account_number(self):
        response = self.wrapper.resolve_account_number(
            bank_code="214", account_number="5273681014"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Account number resolved")

    def test_can_validate_account(self):
        response = self.wrapper.validate_account(
            account_number="0123456789",
            account_name="Ann Bron",
            account_type=AccountType.PERSONAL,
            country_code=Country.SOUTH_AFRICA,
            bank_code="632005",
            document_type=Document.IDENTITY_NUMBER,
            document_number="1234567890123"

        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, 'Personal Account Verification attempted')

    def test_can_resolve_card_bin(self):
        response = self.wrapper.resolve_card_bin(bin="539983")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, 'Bin resolved')
