from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api.transfer_recipients import AsyncTransferRecipient
from pypaystack2.utils import RecipientType, Currency, Recipient
from tests.test_api.mocked_api_testcase import MockedAsyncAPITestCase


class MockedAsyncTransferRecipientTestCase(MockedAsyncAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = AsyncTransferRecipient()

    async def test_can_create(self):
        response = await self.wrapper.create(
            type=RecipientType.NUBAN,
            name="Adeyi Gbenga Michael",
            account_number="5273681014",
            bank_code="214",
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_bulk_create(self):
        batch = [
            {
                "type": RecipientType.NUBAN,
                "name": "Adeyi Gbenga Michael",
                "account_number": "5273681014",
                "bank_code": "214",
            }
        ]
        response = await self.wrapper.bulk_create(batch=Recipient.from_dict_many(batch))
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_update(self):
        response = await self.wrapper.update(
            id_or_code="54134578",
            name="Adeyi Gbenga Michael",
            email="coyotedevmail@gmail.com",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    async def test_can_delete(self):
        response = await self.wrapper.delete(id_or_code="54134578")
        self.assertEqual(response.status_code, httpx.codes.OK)


class AsyncTransferRecipientTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncTransferRecipient()

    async def test_can_create(self):
        response = await self.wrapper.create(
            type=RecipientType.NUBAN,
            name="Adeyi Gbenga Michael",
            account_number="5273681014",
            bank_code="214",
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient created successfully")

    async def test_can_bulk_create(self):
        batch = [
            {
                "type": RecipientType.NUBAN,
                "name": "Adeyi Gbenga Michael",
                "account_number": "5273681014",
                "bank_code": "214",
            }
        ]
        response = await self.wrapper.bulk_create(batch=Recipient.from_dict_many(batch))
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients added successfully")

    async def test_can_get_transfer_recipients(self):
        response = await self.wrapper.get_transfer_recipients()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients retrieved")

    async def test_can_get_transfer_recipient(self):
        response = await self.wrapper.get_transfer_recipient(id_or_code="54134578")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient retrieved")

    async def test_can_update(self):
        response = await self.wrapper.update(
            id_or_code="54134578",
            name="Adeyi Gbenga Michael",
            email="coyotedevmail@gmail.com",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient updated")

    async def test_can_delete(self):
        all_recipients_response = await self.wrapper.get_transfer_recipients()
        response = await self.wrapper.delete(
            id_or_code=all_recipients_response.data[0]["id"]
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient set as inactive")
