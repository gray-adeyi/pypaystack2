from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import DisputeClient


class DisputeTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = DisputeClient()

    def test_can_get_disputes(self):
        response = self.client.get_disputes(
            start_date="2022-01-01", end_date="2023-05-11"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Disputes retrieved")

    def test_can_get_dispute(self):
        # TODO: Test properly.
        ...

    def test_can_get_transaction_disputes(self):
        # TODO: Test properly.
        self.client.get_transaction_disputes(id="114782792")

    def test_can_update_dispute(self): ...

    def test_can_add_evidence(self): ...

    def test_can_get_upload_url(self): ...

    def test_can_resolve_dispute(self): ...

    def test_can_export_disputes(self): ...
