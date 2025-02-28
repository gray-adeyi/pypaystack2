from unittest import TestCase
from uuid import uuid4

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import CustomerClient
from pypaystack2.utils import Country, Identification, RiskAction
from pypaystack2.utils.response_models import Customer


class CustomerTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = CustomerClient()

    def test_can_create(self):
        email = f"jd{uuid4()}@example.com"
        response = self.client.create(email=email, first_name="John", last_name="Doe")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer created")
        self.assertIsInstance(response.data, Customer)
        self.assertEqual(response.data.email, email)

    def test_can_get_customers(self):
        response = self.client.get_customers()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customers retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Customer)

    def test_can_get_customer(self):
        customer_code = "CUS_kul59mkqwd0rn16"
        response = self.client.get_customer(email_or_code=customer_code)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer retrieved")
        self.assertIsInstance(response.data, Customer)
        self.assertEqual(response.data.customer_code, customer_code)

    def test_can_update(self):
        response = self.client.update(
            code="CUS_kd197ej30zxr34v", metadata={"username": "jigani"}
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer updated")
        self.assertIsInstance(response.data, Customer)

    def test_can_validate(self):
        new_user_response = self.client.create(
            email=f"jd{uuid4()}@example.com", first_name="John", last_name="Doe"
        )
        response = self.client.validate(
            email_or_code=new_user_response.data.email,
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
        response = self.client.flag(
            customer="CUS_7khpwdrlvde8c6h", risk_action=RiskAction.BLACKLIST
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Customer updated")
        self.assertIsInstance(response.data, Customer)

    def test_can_deactivate(self):
        # TODO: Test properly
        response = self.client.deactivate(auth_code="AUTH_72btv547")
        self.assertEqual(response.status_code, httpx.codes.NOT_FOUND)
