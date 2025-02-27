from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients import PaymentRequestClient
from tests.test_sub_clients.mocked_api_testcase import MockedAPITestCase


class MockedPaymentRequestTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = PaymentRequestClient()

    def test_can_create(self):
        response = self.wrapper.create(customer="87620726", amount=900_000)
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_payment_requests(self):
        response = self.wrapper.get_payment_requests(
            customer="87620726",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_request(self):
        response = self.wrapper.get_payment_request(id_or_code="PRQ_jy9zqp89329qx12")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_verify(self):
        response = self.wrapper.verify(code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_send_notification(self):
        response = self.wrapper.send_notification(id_or_code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_total(self):
        response = self.wrapper.get_total()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_finalize(self):
        response = self.wrapper.finalize(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_update(self):
        response = self.wrapper.update(
            id_or_code="PRQ_886l127ke0on6jg",
            amount=300_000,
            customer="CUS_7khpwdrlvde8c6h",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_archive(self):
        response = self.wrapper.archive(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.OK)


class PaymentRequestTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = PaymentRequestClient()

    def test_can_create(self):
        response = self.wrapper.create(customer="87620726", amount=900_000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request created")

    def test_can_get_payment_requests(self):
        response = self.wrapper.get_payment_requests(
            customer="87620726",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment requests retrieved")

    def test_can_get_request(self):
        response = self.wrapper.get_payment_request(id_or_code="PRQ_jy9zqp89329qx12")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request retrieved")

    def test_can_verify(self):
        response = self.wrapper.verify(code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request retrieved")

    def test_can_send_notification(self):
        response = self.wrapper.send_notification(id_or_code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Notification sent")

    def test_can_get_total(self):
        response = self.wrapper.get_total()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request totals")

    def test_can_finalize(self):
        # TODO: Test Properly
        response = self.wrapper.finalize(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    def test_can_update(self):
        # TODO: Test Properly
        response = self.wrapper.update(
            id_or_code="PRQ_886l127ke0on6jg",
            amount=300_000,
            customer="CUS_7khpwdrlvde8c6h",
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    def test_can_archive(self):
        response = self.wrapper.archive(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request has been archived")
