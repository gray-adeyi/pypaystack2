from typing import cast
from unittest import IsolatedAsyncioTestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.sub_clients.async_clients.transfer_recipients import (
    AsyncTransferRecipientClient,
)
from pypaystack2.utils.enums import RecipientType, Currency
from pypaystack2.utils.models import Recipient, Response
from pypaystack2.utils.response_models import (
    TransferRecipient,
    TransferRecipientBulkCreateData,
)


class AsyncTransferRecipientTestCase(IsolatedAsyncioTestCase):
    client: AsyncTransferRecipientClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncTransferRecipientClient()

    async def test_can_create(self) -> None:
        response: Response[TransferRecipient] = await self.client.create(
            type=RecipientType.NUBAN,
            name="Adeyi Gbenga Michael",
            account_number="5273681014",
            bank_code="214",
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient created successfully")
        self.assertIsInstance(response.data, TransferRecipient)

    async def test_can_bulk_create(self) -> None:
        batch = [
            {
                "type": RecipientType.NUBAN,
                "name": "Adeyi Gbenga Michael",
                "account_number": "5273681014",
                "bank_code": "214",
            }
        ]
        response: Response[
            TransferRecipientBulkCreateData
        ] = await self.client.bulk_create(
            batch=[Recipient.model_validate(item) for item in batch]
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients added successfully")
        self.assertIsInstance(response.data, TransferRecipientBulkCreateData)

    async def test_can_get_transfer_recipients(self) -> None:
        response = cast(
            Response[list[TransferRecipient]],
            await self.client.get_transfer_recipients(),
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 1:
            self.assertIsInstance(response.data[0], TransferRecipient)

    async def test_can_get_transfer_recipient(self) -> None:
        response: Response[
            TransferRecipient
        ] = await self.client.get_transfer_recipient(id_or_code="54134578")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient retrieved")
        self.assertIsInstance(response.data, TransferRecipient)

    async def test_can_update(self) -> None:
        response: Response[None] = await self.client.update(
            id_or_code="54134578",
            name="Adeyi Gbenga Michael",
            email="coyotedevmail@gmail.com",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient updated")

    async def test_can_delete(self) -> None:
        all_recipients_response = cast(
            Response[TransferRecipient], await self.client.get_transfer_recipients()
        )
        response: Response[None] = await self.client.delete(
            id_or_code=all_recipients_response.data[0].id
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient set as inactive")
