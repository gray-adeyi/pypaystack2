from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.payment_requests import AsyncPaymentRequest
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncPaymentRequestTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncPaymentRequest()

    async def test_can_create(self):
        response = await self.wrapper.create(customer="87620726", amount=900_000)
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_payment_requests(self):
        response = await self.wrapper.get_payment_requests(
            customer="87620726",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_request(self):
        response = await self.wrapper.get_payment_request(
            id_or_code="PRQ_jy9zqp89329qx12"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_verify(self):
        response = await self.wrapper.verify(code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_send_notification(self):
        response = await self.wrapper.send_notification(
            id_or_code="PRQ_hj7hi07q6oibdof"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_get_total(self):
        response = await self.wrapper.get_total()
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_finalize(self):
        response = await self.wrapper.finalize(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_update(self):
        response = await self.wrapper.update(
            id_or_code="PRQ_886l127ke0on6jg",
            amount=300_000,
            customer="CUS_7khpwdrlvde8c6h",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_archive(self):
        response = await self.wrapper.archive(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncPaymentRequestTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncPaymentRequest()

    async def test_can_create(self):
        response = await self.wrapper.create(customer="87620726", amount=900_000)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request created")

    async def test_can_get_payment_requests(self):
        response = await self.wrapper.get_payment_requests(
            customer="87620726",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment requests retrieved")

    async def test_can_get_request(self):
        response = await self.wrapper.get_payment_request(
            id_or_code="PRQ_jy9zqp89329qx12"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request retrieved")

    async def test_can_verify(self):
        response = await self.wrapper.verify(code="PRQ_hj7hi07q6oibdof")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request retrieved")

    async def test_can_send_notification(self):
        response = await self.wrapper.send_notification(
            id_or_code="PRQ_hj7hi07q6oibdof"
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Notification sent")

    async def test_can_get_total(self):
        response = await self.wrapper.get_total()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request totals")

    async def test_can_finalize(self):
        # TODO: Test Properly
        response = await self.wrapper.finalize(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    async def test_can_update(self):
        # TODO: Test Properly
        response = await self.wrapper.update(
            id_or_code="PRQ_886l127ke0on6jg",
            amount=300_000,
            customer="CUS_7khpwdrlvde8c6h",
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    async def test_can_archive(self):
        response = await self.wrapper.archive(id_or_code="PRQ_886l127ke0on6jg")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Payment request has been archived")
