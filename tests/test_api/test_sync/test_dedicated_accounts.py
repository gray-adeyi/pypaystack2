from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api import DedicatedAccount
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedDedicatedAccountTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = DedicatedAccount()


class DedicatedAccountTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = DedicatedAccount()

    def test_can_create(self):
        # TODO: Test properly.
        response = self.wrapper.create(customer="CUS_5qmwswiljybyyne")

    def test_can_get_dedicated_accounts(self):
        ...

    def test_can_get_dedicated_account(self):
        ...

    def test_can_requery(self):
        ...

    def test_can_deactivate(self):
        ...

    def test_can_split(self):
        ...

    def test_can_remove_split(self):
        ...

    def test_can_get_providers(self):
        # TODO: Test properly.
        response = self.wrapper.get_providers()
        self.assertEqual(response.status_code, httpx.codes.OK)
