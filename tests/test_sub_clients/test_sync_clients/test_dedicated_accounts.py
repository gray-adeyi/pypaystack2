from unittest import TestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import DedicatedAccountClient


class DedicatedAccountClientTestCase(TestCase):
    client: DedicatedAccountClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = DedicatedAccountClient()

    @skip("incomplete test")
    def test_can_create(self) -> None:
        # TODO: Test properly.
        self.client.create(customer="CUS_5qmwswiljybyyne")

    @skip("incomplete test")
    def test_can_get_dedicated_accounts(self) -> None: ...

    @skip("incomplete test")
    def test_can_get_dedicated_account(self) -> None: ...

    @skip("incomplete test")
    def test_can_requery(self) -> None: ...

    @skip("incomplete test")
    def test_can_deactivate(self) -> None: ...

    @skip("incomplete test")
    def test_can_split(self) -> None: ...

    @skip("incomplete test")
    def test_can_remove_split(self) -> None: ...

    @skip("incomplete test")
    def test_can_get_providers(self) -> None:
        # TODO: Test properly.
        response = self.client.get_providers()
        self.assertEqual(response.status_code, httpx.codes.UNAUTHORIZED)
