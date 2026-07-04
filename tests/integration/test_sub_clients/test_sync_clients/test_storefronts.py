from uuid import uuid1
from unittest import TestCase, skip
from dotenv import load_dotenv
from pypaystack2.sub_clients.sync_clients.storefronts import StorefrontClient


class StorefrontClientTestCase(TestCase):
    client: StorefrontClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = StorefrontClient()

    @skip("bypass")
    def test_create(self):
        id = uuid1()
        response = self.client.create(
            name=f"Test Storefront {id.time_mid}", slug=id.hex
        )
        print(response)
