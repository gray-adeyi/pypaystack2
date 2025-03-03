from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.sync_clients.transfers import TransferClient
from pypaystack2.utils.models import TransferInstruction


class TransferTestCase(TestCase):
    client: TransferClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = TransferClient()

    def test_can_initiate(self) -> None:
        # TODO: Test properly
        response = self.client.initiate(amount=1000, recipient="RCP_dv0jwap08v8niic")
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    def test_can_finalize(self) -> None:
        # TODO: Test properly
        response = self.client.finalize(transfer_code="", otp="")
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    def test_can_bulk_transfer(self) -> None:
        # TODO: Test properly
        tx_instructions = [{"amount": 1000, "recipient": "RCP_dv0jwap08v8niic"}]
        response = self.client.bulk_transfer(
            transfers=[
                TransferInstruction.model_validate(item) for item in tx_instructions
            ]
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    def test_can_get_transfers(self) -> None:
        response = self.client.get_transfers()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfers retrieved")

    def test_can_get_transfer(self) -> None: ...

    def test_can_verify(self) -> None: ...
