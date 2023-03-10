from unittest import TestCase

from pypaystack2.api import Subscription, Customer, Plan
from . import test_auth_key


class TestProduct(TestCase):
    def setUp(self):
        super().setUp()
        self.assertNotEqual(test_auth_key, None)
        self.sub = Subscription(auth_key=test_auth_key)

    def test_can_create_subscription(self):
        customer = Customer(auth_key=test_auth_key).get_customers().data[0]
        plan = Plan(auth_key=test_auth_key).get_plans().data[0]
        resp = self.sub.create(
            customer=customer["email"],
            plan=plan["plan_code"],
            authorization=customer["customer_code"],
        )
        self.assertTrue(resp.status)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.message, "")
