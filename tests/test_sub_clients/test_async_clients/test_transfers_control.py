from unittest import TestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.enums import Reason
from pypaystack2.models import Response
from pypaystack2.models.response_models import IntegrationBalance, BalanceLedgerItem
from pypaystack2.sub_clients import AsyncTransferControlClient


class AsyncTransferControlClientTestCase(TestCase):
    client: AsyncTransferControlClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncTransferControlClient()

    async def test_can_check_balance(self) -> None:
        response: Response[list[IntegrationBalance]] = await self.client.check_balance()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Balances retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], IntegrationBalance)

    async def test_can_get_balance_ledger(self) -> None:
        response: Response[
            list[BalanceLedgerItem]
        ] = await self.client.get_balance_ledger()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Balance ledger retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], BalanceLedgerItem)

    async def test_can_resend_otp(self) -> None:
        response: Response[None] = await self.client.resend_otp(
            transfer_code="TRF_vsyqdmlzble3uii", reason=Reason.DISABLE_OTP
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "OTP has been resent")

    async def test_can_disable_otp(self) -> None:
        response: Response[None] = await self.client.disable_otp()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(
            response.message,
            "OTP has been sent to mobile number ending with 9831 and to email a******@g******.com",
        )

    @skip("incomplete test")
    async def test_can_finalize_disable_otp(self) -> None:
        # TODO: Test properly
        response: Response[None] = await self.client.finalize_disable_otp(otp="123456")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_enable_otp(self) -> None:
        response: Response[None] = await self.client.enable_otp()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(
            response.message, "OTP requirement for transfers has been enabled"
        )
