from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api import Dispute
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedDisputeTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = Dispute()


class DisputeTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Dispute()

    def test_can_get_disputes(self):
        response = self.wrapper.get_disputes(
            start_date="2022-01-01", end_date="2023-05-11"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Disputes retrieved")

    def test_can_get_dispute(self):
        # TODO: Test properly.
        response = self.wrapper.get_dispute(id="114782792")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_transaction_disputes(self):
        # TODO: Test properly.
        response = self.wrapper.get_transaction_disputes(id="114782792")

    def test_can_update_dispute(self):
        ...

    def test_can_add_evidence(self):
        ...

    def test_can_get_upload_url(self):
        ...

    def test_can_resolve_dispute(self):
        ...

    def test_can_export_disputes(self):
        ...
