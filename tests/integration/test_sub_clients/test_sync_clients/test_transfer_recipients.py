from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.enums import Currency, RecipientType
from pypaystack2.models import (
    TransferRecipient,
    Recipient,
    TransferRecipientBulkCreateData,
)
from pypaystack2.sub_clients import TransferRecipientClient


class TransferRecipientClientTestCase(TestCase):
    client: TransferRecipientClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = TransferRecipientClient()

    def test_can_create(self) -> None:
        response = self.client.create(
            type_=RecipientType.NUBAN,
            name="Adeyi Gbenga Michael",
            account_number="5273681014",
            bank_code="214",
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient created successfully")
        self.assertIsInstance(response.data, TransferRecipient)

    def test_can_bulk_create(self) -> None:
        batch = [
            {
                "type": RecipientType.NUBAN,
                "name": "Adeyi Gbenga Michael",
                "account_number": "5273681014",
                "bank_code": "214",
            }
        ]
        response = self.client.bulk_create(
            batch=[Recipient.model_validate(item) for item in batch]
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients added successfully")
        self.assertIsInstance(response.data, TransferRecipientBulkCreateData)

    def test_can_get_transfer_recipients(self) -> None:
        response = self.client.get_transfer_recipients()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients retrieved")
        self.assertIsInstance(response.data, list)
        if len(response.data) > 1:
            self.assertIsInstance(response.data[0], TransferRecipient)

    def test_can_get_transfer_recipient(self) -> None:
        response = self.client.get_transfer_recipient(id_or_code="54134578")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient retrieved")
        self.assertIsInstance(response.data, TransferRecipient)

    def test_can_update(self) -> None:
        response = self.client.update(
            id_or_code="54134578",
            name="Adeyi Gbenga Michael",
            email="coyotedevmail@gmail.com",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient updated")

    def test_can_delete(self) -> None:
        all_recipients_response = self.client.get_transfer_recipients()
        response = self.client.delete(id_or_code=all_recipients_response.data[0].id)
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient set as inactive")
