from unittest import TestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.models.payload_models import TransferInstruction
from pypaystack2.sub_clients.sync_clients.transfers import TransferClient


class TransferClientTestCase(TestCase):
    client: TransferClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = TransferClient()

    @skip("incomplete test")
    def test_can_initiate(self) -> None:
        # TODO: Test properly
        response = self.client.initiate(amount=1000, recipient="RCP_dv0jwap08v8niic")
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    @skip("incomplete test")
    def test_can_finalize(self) -> None:
        # TODO: Test properly
        response = self.client.finalize(transfer_code="", otp="")
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    @skip("incomplete test")
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

    @skip("incomplete test")
    def test_can_get_transfer(self) -> None: ...

    @skip("incomplete test")
    def test_can_verify(self) -> None: ...
