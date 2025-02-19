from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import TransferControlClient
from pypaystack2.utils import Reason
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedTransferControlTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = TransferControlClient()


class TransferControlTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = TransferControlClient()

    def test_can_check_balance(self):
        response = self.wrapper.check_balance()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Balances retrieved")

    def test_can_get_balance_ledger(self):
        response = self.wrapper.get_balance_ledger()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Balance ledger retrieved")

    def test_can_resend_otp(self):
        response = self.wrapper.resend_otp(
            transfer_code="TRF_vsyqdmlzble3uii", reason=Reason.DISABLE_OTP
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "OTP has been resent")

    def test_can_disable_otp(self):
        response = self.wrapper.disable_otp()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(
            response.message,
            "OTP has been sent to mobile number ending with 9831 and to email a******@g******.com",
        )

    def test_can_finalize_disable_otp(self):
        # TODO: Test properly
        response = self.wrapper.finalize_disable_otp(otp="123456")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_enable_otp(self):
        response = self.wrapper.enable_otp()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(
            response.message, "OTP requirement for transfers has been enabled"
        )
