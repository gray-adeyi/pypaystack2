from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.charge import AsyncCharge
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncChargeTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncCharge()

    async def test_can_charge(self):
        bank_data = {"code": "057", "account_number": "0000000000"}
        response = await self.wrapper.charge(
            email="coyotedevmail@gmail.com",
            amount=1000,
            bank=bank_data,
            birthday="1999-04-29",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_submit_pin(self):
        # TODO: Test properly
        response = await self.wrapper.submit_pin(
            pin="2345", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_submit_otp(self):
        # TODO: Test properly
        response = await self.wrapper.submit_otp(
            otp="234545", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_submit_phone(self):
        # TODO: Test properly
        response = await self.wrapper.submit_phone(
            phone="07012345678", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_submit_birthday(self):
        response = await self.wrapper.submit_birthday(
            birthday="1999-04-29", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_set_address(self):
        # TODO: Test properly
        response = await self.wrapper.set_address(
            address="1 John Doe street",
            reference="kv7ecgjrit1fxgs",
            city="Iyana Ipaja",
            state="Lagos",
            zipcode="20101",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_check_pending_charge(self):
        response = await self.wrapper.check_pending_charge(reference="kv7ecgjrit1fxgs")
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncChargeTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncCharge()

    async def test_can_charge(self):
        bank_data = {"code": "057", "account_number": "0000000000"}
        response = await self.wrapper.charge(
            email="coyotedevmail@gmail.com",
            amount=1000,
            bank=bank_data,
            birthday="1999-04-29",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_submit_pin(self):
        # TODO: Test properly
        response = await self.wrapper.submit_pin(
            pin="2345", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_submit_otp(self):
        # TODO: Test properly
        response = await self.wrapper.submit_otp(
            otp="234545", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_submit_phone(self):
        # TODO: Test properly
        response = await self.wrapper.submit_phone(
            phone="07012345678", reference="kv7ecgjrit1fxgs"
        )
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_submit_birthday(self):
        response = await self.wrapper.submit_birthday(
            birthday="1999-04-29", reference="kv7ecgjrit1fxgs"
        )
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_set_address(self):
        # TODO: Test properly
        response = await self.wrapper.set_address(
            address="1 John Doe street",
            reference="kv7ecgjrit1fxgs",
            city="Iyana Ipaja",
            state="Lagos",
            zipcode="20101",
        )
        self.assertEqual(response.message, "Charge attempted")

    async def test_can_check_pending_charge(self):
        response = await self.wrapper.check_pending_charge(reference="kv7ecgjrit1fxgs")
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Reference check successful")
