from unittest import IsolatedAsyncioTestCase
from uuid import uuid4

import httpx
from dotenv import load_dotenv

from pypaystack2.api.customers import AsyncCustomer
from pypaystack2.utils import Identification, RiskAction, Country
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncCustomerTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncCustomer()

    async def test_can_create(self):
        response = await self.wrapper.create(
            email=f"jd{uuid4()}@example.com", first_name="John", last_name="Doe"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_customers(self):
        response = await self.wrapper.get_customers()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_customer(self):
        response = await self.wrapper.get_customer(email_or_code="CUS_kul59mkqwd0rn16")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_update(self):
        response = await self.wrapper.update(
            code="CUS_kd197ej30zxr34v", metadata={"username": "jigani"}
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_validate(self):
        response = await self.wrapper.validate(
            email_or_code="test-code",
            first_name="John",
            last_name="Doe",
            identification_type=Identification.BANK_ACCOUNT,
            country=Country.NIGERIA,
            bvn="12324353543",
            bank_code="121",
            account_number="342432422",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_flag(self):
        response = await self.wrapper.flag(
            customer="CUS_7khpwdrlvde8c6h", risk_action=RiskAction.BLACKLIST
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_deactivate(self):
        # TODO: Test properly
        response = await self.wrapper.deactivate(auth_code="AUTH_72btv547")
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncCustomerTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncCustomer()

    async def test_can_create(self):
        response = await self.wrapper.create(
            email=f"jd{uuid4()}@example.com", first_name="John", last_name="Doe"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer created")

    async def test_can_get_customers(self):
        response = await self.wrapper.get_customers()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customers retrieved")

    async def test_can_get_customer(self):
        response = await self.wrapper.get_customer(email_or_code="CUS_kul59mkqwd0rn16")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer retrieved")

    async def test_can_update(self):
        response = await self.wrapper.update(
            code="CUS_kd197ej30zxr34v", metadata={"username": "jigani"}
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer updated")

    async def test_can_validate(self):
        new_user_response = await self.wrapper.create(
            email=f"jd{uuid4()}@example.com", first_name="John", last_name="Doe"
        )
        response = await self.wrapper.validate(
            email_or_code=new_user_response.data["email"],
            first_name="John",
            last_name="Doe",
            identification_type=Identification.BANK_ACCOUNT,
            country=Country.NIGERIA,
            bvn="12324353543",
            bank_code="121",
            account_number="342432422",
        )
        self.assertEqual(response.status_code, httpx.codes.ACCEPTED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer Identification in progress")

    async def test_can_flag(self):
        response = await self.wrapper.flag(
            customer="CUS_7khpwdrlvde8c6h", risk_action=RiskAction.BLACKLIST
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer updated")

    async def test_can_deactivate(self):
        # TODO: Test properly
        response = await self.wrapper.deactivate(auth_code="AUTH_72btv547")
        self.assertEqual(response.status_code, httpx.codes.NOT_FOUND)
