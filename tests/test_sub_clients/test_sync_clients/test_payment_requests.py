from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import PaymentRequestClient
from pypaystack2.utils.response_models import PaymentRequest, PaymentRequestStat


class PaymentRequestTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = PaymentRequestClient()

    def test_can_create(self):
        response = self.client.create(customer="87620726", amount=900_000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request created")
        self.assertIsInstance(response.data, PaymentRequest)

    def test_can_get_payment_requests(self):
        response = self.client.get_payment_requests()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment requests retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], PaymentRequest)

    def test_can_get_request(self):
        response = self.client.get_payment_request(id_or_code="PRQ_jy9zqp89329qx12")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request retrieved")
        self.assertIsInstance(response.data, PaymentRequest)

    def test_can_verify(self):
        response = self.client.verify(code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request retrieved")
        self.assertIsInstance(response.data, PaymentRequest)

    def test_can_send_notification(self):
        response = self.client.send_notification(id_or_code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Notification sent")

    def test_can_get_total(self):
        response = self.client.get_total()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request totals")
        self.assertIsInstance(response.data, PaymentRequestStat)

    def test_can_finalize(self):
        create_response = self.client.create(
            customer="87620726", amount=900_000, draft=True
        )
        response = self.client.finalize(id_or_code=create_response.data.request_code)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request finalized")
        self.assertIsInstance(response.data, PaymentRequest)

    def test_can_update(self):
        create_response = self.client.create(
            customer="87620726", amount=900_000, draft=True
        )
        response = self.client.update(
            id_or_code=create_response.data.request_code,
            amount=300_000,
            customer="CUS_7khpwdrlvde8c6h",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request updated")
        self.assertIsInstance(response.data, PaymentRequest)

    def test_can_archive(self):
        response = self.client.archive(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request has been archived")
