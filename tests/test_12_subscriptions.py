from uuid import uuid4

from . import test_auth_key, Subscription, Customer, Plan, TestCase


class TestProduct(TestCase):
    def setUp(self):
        super().setUp()
        self.assertNotEqual(test_auth_key, None)
        self.sub = Subscription(auth_key=test_auth_key)

    def test_can_create_subscription(self):
        customer = Customer(auth_key=test_auth_key).get_customers().data[0]
        plan = Plan(auth_key=test_auth_key).get_plans().data[0]
        resp = self.sub.create(customer=customer["email"], plan=plan["plan_code"])
        self.assertTrue(resp.status)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.message, "")
