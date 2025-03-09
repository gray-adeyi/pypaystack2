from unittest import TestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import DisputeClient


class DisputeClientTestCase(TestCase):
    client: DisputeClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = DisputeClient()

    def test_can_get_disputes(self) -> None:
        response = self.client.get_disputes(
            start_date="2022-01-01", end_date="2023-05-11"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Disputes retrieved")

    @skip("incomplete test")
    def test_can_get_dispute(self) -> None:
        # TODO: Test properly.
        ...

    @skip("incomplete test")
    def test_can_get_transaction_disputes(self) -> None:
        # TODO: Test properly.
        self.client.get_transaction_disputes(id_="114782792")

    @skip("incomplete test")
    def test_can_update_dispute(self) -> None: ...

    @skip("incomplete test")
    def test_can_add_evidence(self) -> None: ...

    @skip("incomplete test")
    def test_can_get_upload_url(self) -> None: ...

    @skip("incomplete test")
    def test_can_resolve_dispute(self) -> None: ...

    @skip("incomplete test")
    def test_can_export_disputes(self) -> None: ...
