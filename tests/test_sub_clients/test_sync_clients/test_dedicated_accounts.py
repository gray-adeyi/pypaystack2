from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import DedicatedAccountClient


class DedicatedAccountTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = DedicatedAccountClient()

    def test_can_create(self):
        # TODO: Test properly.
        self.client.create(customer="CUS_5qmwswiljybyyne")

    def test_can_get_dedicated_accounts(self): ...

    def test_can_get_dedicated_account(self): ...

    def test_can_requery(self): ...

    def test_can_deactivate(self): ...

    def test_can_split(self): ...

    def test_can_remove_split(self): ...

    def test_can_get_providers(self):
        # TODO: Test properly.
        response = self.client.get_providers()
        self.assertEqual(response.status_code, httpx.codes.UNAUTHORIZED)
