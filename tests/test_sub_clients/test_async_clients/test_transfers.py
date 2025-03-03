from typing import cast
from unittest.async_case import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.transfers import AsyncTransferClient
from pypaystack2.utils.models import Response
from pypaystack2.utils.models import TransferInstruction
from pypaystack2.utils.response_models import Transfer, BulkTransferItem


class TransferTestCase(IsolatedAsyncioTestCase):
    client: AsyncTransferClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncTransferClient()

    async def test_can_initiate(self) -> None:
        # TODO: Test properly
        response: Response[Transfer] = await self.client.initiate(
            amount=1000, recipient="RCP_dv0jwap08v8niic"
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    async def test_can_finalize(self) -> None:
        # TODO: Test properly
        response: Response[Transfer] = await self.client.finalize(
            transfer_code="", otp=""
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    async def test_can_bulk_transfer(self) -> None:
        # TODO: Test properly
        tx_instructions = [{"amount": 1000, "recipient": "RCP_dv0jwap08v8niic"}]
        response: Response[list[BulkTransferItem]] = await self.client.bulk_transfer(
            transfers=[
                TransferInstruction.model_validate(item) for item in tx_instructions
            ]
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    async def test_can_get_transfers(self) -> None:
        response = cast(Response[list[Transfer]], await self.client.get_transfers())
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfers retrieved")

    async def test_can_get_transfer(self) -> None: ...

    async def test_can_verify(self) -> None: ...
