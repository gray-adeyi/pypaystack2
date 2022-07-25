from unittest import TestCase
from . import test_auth_key, BulkCharge
from uuid import uuid4


class TestBulkCharge(TestCase):
    def setUp(self):
        super().setUp()
        self.assertNotEqual(test_auth_key, None)
        self.bulk_charge = BulkCharge(auth_key=test_auth_key)

    def test_can_initiage(self):
        data = [
            {"code": str(uuid4()), "amount": 1000},
            {"code": str(uuid4()), "amount": 1000},
        ]
        response = self.bulk_charge.initiate(body=data)
        self.assertEqual(response.message, "")
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, [])
        # self.assertEqual(response.message, "")
        # self.assertEqual(response.status_code, "")
