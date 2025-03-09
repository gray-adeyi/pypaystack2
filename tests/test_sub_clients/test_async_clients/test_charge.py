from unittest import IsolatedAsyncioTestCase, skip

import httpx
from dotenv import load_dotenv

from pypaystack2.models import Transaction, Response
from pypaystack2.sub_clients import AsyncChargeClient


class AsyncChargeClientTestCase(IsolatedAsyncioTestCase):
    client: AsyncChargeClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncChargeClient()

    async def test_can_charge(self) -> None:
        bank_data = {"code": "057", "account_number": "0000000000"}
        response: Response[Transaction] = await self.client.charge(
            email="coyotedevmail@gmail.com",
            amount=1000,
            bank=bank_data,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charge attempted")

    @skip("incomplete test")
    async def test_can_submit_pin(self) -> None:
        # TODO: Test properly
        response: Response[Transaction] = await self.client.submit_pin(
            pin="2345", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.message, "Charge attempted")

    @skip("incomplete test")
    async def test_can_submit_otp(self) -> None:
        # TODO: Test properly
        response: Response[Transaction] = await self.client.submit_otp(
            otp="234545", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.message, "Charge attempted")

    @skip("incomplete test")
    async def test_can_submit_phone(self) -> None:
        # TODO: Test properly
        response: Response[Transaction] = await self.client.submit_phone(
            phone="07012345678", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_submit_birthday(self) -> None:
        response: Response[Transaction] = await self.client.submit_birthday(
            birthday="1999-04-29", reference="kv7ecgjrit1fxgs"
        )
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_set_address(self) -> None:
        # TODO: Test properly
        response: Response[Transaction] = await self.client.set_address(
            address="1 John Doe street",
            reference="kv7ecgjrit1fxgs",
            city="Iyana Ipaja",
            state="Lagos",
            zipcode="20101",
        )
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_check_pending_charge(self) -> None:
        response: Response[Transaction] = await self.client.check_pending_charge(
            reference="kv7ecgjrit1fxgs"
        )
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Reference check successful")
