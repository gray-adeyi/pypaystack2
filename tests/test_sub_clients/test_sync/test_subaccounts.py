from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import SubAccountClient
from tests.test_sub_clients.mocked_api_testcase import MockedAPITestCase


class MockedSubAccountTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = SubAccountClient()


class SubAccountTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = SubAccountClient()

    def test_can_create(self):
        # TODO: Test properly
        self.wrapper.create(
            business_name="Coyote solutions",
            settlement_bank="044",
            account_number="0193274682",
            percentage_charge=18.2,
        )

    def test_can_get_subaccounts(self):
        response = self.wrapper.get_subaccounts(
            start_date="2020-01-01", end_date="2023-01-01"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subaccounts retrieved")

    def test_can_get_subaccount(self): ...

    def test_can_update(self): ...
