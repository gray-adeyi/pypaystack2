from unittest import TestCase
from uuid import uuid4

import httpx
from dotenv import load_dotenv

from pypaystack2.api import Customer
from pypaystack2.utils import Country, Identification, RiskAction
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedCustomerTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = Customer()

    def test_can_create(self):
        response = self.wrapper.create(
            email=f"jd{uuid4()}@example.com", first_name="John", last_name="Doe"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_customers(self):
        response = self.wrapper.get_customers()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_customer(self):
        response = self.wrapper.get_customer(email_or_code="CUS_kul59mkqwd0rn16")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_update(self):
        response = self.wrapper.update(
            code="CUS_kd197ej30zxr34v", metadata={"username": "jigani"}
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_validate(self):
        response = self.wrapper.validate(
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

    def test_can_flag(self):
        response = self.wrapper.flag(
            customer="CUS_7khpwdrlvde8c6h", risk_action=RiskAction.BLACKLIST
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_deactivate(self):
        # TODO: Test properly
        response = self.wrapper.deactivate(auth_code="AUTH_72btv547")
        self.assertEqual(response.status_code, httpx.codes.OK)


class CustomerTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Customer()

    def test_can_create(self):
        response = self.wrapper.create(
            email=f"jd{uuid4()}@example.com", first_name="John", last_name="Doe"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer created")

    def test_can_get_customers(self):
        response = self.wrapper.get_customers()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customers retrieved")

    def test_can_get_customer(self):
        response = self.wrapper.get_customer(email_or_code="CUS_kul59mkqwd0rn16")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer retrieved")

    def test_can_update(self):
        response = self.wrapper.update(
            code="CUS_kd197ej30zxr34v", metadata={"username": "jigani"}
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer updated")

    def test_can_validate(self):
        new_user_response = self.wrapper.create(
            email=f"jd{uuid4()}@example.com", first_name="John", last_name="Doe"
        )
        response = self.wrapper.validate(
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

    def test_can_flag(self):
        response = self.wrapper.flag(
            customer="CUS_7khpwdrlvde8c6h", risk_action=RiskAction.BLACKLIST
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer updated")

    def test_can_deactivate(self):
        # TODO: Test properly
        response = self.wrapper.deactivate(auth_code="AUTH_72btv547")
        self.assertEqual(response.status_code, httpx.codes.OK)
