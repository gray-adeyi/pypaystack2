from unittest.async_case import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.subscriptions import AsyncSubscriptionClient
from pypaystack2.utils.response_models import Subscription, SubscriptionLink


class AsyncSubscriptionTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncSubscriptionClient()

    async def test_can_create(self):
        # TODO: Test properly
        response = await self.client.create(
            customer="CUS_73cb3biedlkbe4a", plan="PLN_tfdm2l55hielq0i"
        )
        if response.status_code == httpx.codes.OK:
            self.assertTrue(response.status)
            self.assertEqual(response.message, "Subscription successfully created")
        else:
            self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)
            self.assertFalse(response.status)
            self.assertEqual(response.message, "This subscription is already in place.")

    async def test_can_get_subscriptions(self):
        response = await self.client.get_subscriptions()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subscriptions retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 0:
            self.assertIsInstance(response.data[0], Subscription)

    async def test_can_get_subscription(self):
        response = await self.client.get_subscription(id_or_code="SUB_e1z7pxur2k0a9qk")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Subscription retrieved successfully")
        self.assertIsInstance(response.data, Subscription)

    async def test_can_enable(self):
        # TODO: Test properly
        response = await self.client.enable(
            code="SUB_e1z7pxur2k0a9qk", token="t605d6777fa7zvw"
        )
        self.assertEqual(response.status_code, httpx.codes.BAD_REQUEST)

    async def test_can_disable(self):
        response = await self.client.disable(
            code="SUB_e1z7pxur2k0a9qk", token="t605d6777fa7zvw"
        )
        if response.status_code == httpx.codes.OK:
            self.assertTrue(response.status)
            self.assertEqual(response.message, "Subscription disabled successfully")
        else:
            self.assertEqual(response.status_code, httpx.codes.NOT_FOUND)
            self.assertFalse(response.status)
            self.assertEqual(
                response.message, "Subscription with code not found or already inactive"
            )

    async def test_can_get_update_link(self):
        response = await self.client.get_update_link(code="SUB_e1z7pxur2k0a9qk")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Link generated")
        self.assertIsInstance(response.data, SubscriptionLink)

    async def test_can_send_update_link(self):
        response = await self.client.send_update_link(code="SUB_e1z7pxur2k0a9qk")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Email successfully sent")
