from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api import Transfer
from pypaystack2.utils import Recipient, TransferInstruction
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedTransferTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = Transfer()


class TransferTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Transfer()

    def test_can_initiate(self):
        # TODO: Test properly
        response = self.wrapper.initiate(amount=1000, recipient="RCP_dv0jwap08v8niic")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_finalize(self):
        # TODO: Test properly
        response = self.wrapper.finalize(transfer_code="", otp="")
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient created successfully")

    def test_can_bulk_transfer(self):
        # TODO: Test properly
        tx_instructions = [{"amount": 1000, "recipient": "RCP_dv0jwap08v8niic"}]
        response = self.wrapper.bulk_transfer(
            transfers=TransferInstruction.from_dict_many(tx_instructions)
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_transfers(self):
        response = self.wrapper.get_transfers()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfers retrieved")

    def test_can_get_transfer(self):
        ...

    def test_can_verify(self):
        ...
