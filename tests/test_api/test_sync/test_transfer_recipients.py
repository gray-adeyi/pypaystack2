from unittest import TestCase

import httpx
from dotenv import load_dotenv

from pypaystack2.api import RecipientType
from pypaystack2.api.transfer_recipients import TransferRecipient
from pypaystack2.utils import Currency, Recipient
from tests.test_api.mocked_api_testcase import MockedAPITestCase


class MockedTransferRecipientTestCase(MockedAPITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_dotenv()
        cls.wrapper = TransferRecipient()

    def test_can_create(self):
        response = self.wrapper.create(
            type=RecipientType.NUBAN,
            name="Adeyi Gbenga Michael",
            account_number="5273681014",
            bank_code="214",
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_bulk_create(self):
        batch = [
            {
                "type": RecipientType.NUBAN,
                "name": "Adeyi Gbenga Michael",
                "account_number": "5273681014",
                "bank_code": "214",
            }
        ]
        response = self.wrapper.bulk_create(batch=Recipient.from_dict_many(batch))
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_transfer_recipients(self):
        response = self.wrapper.get_transfer_recipients()
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_get_transfer_recipient(self):
        response = self.wrapper.get_transfer_recipient(id_or_code="54134578")
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_update(self):
        response = self.wrapper.update(
            id_or_code="54134578",
            name="Adeyi Gbenga Michael",
            email="coyotedevmail@gmail.com",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)

    def test_can_delete(self):
        all_recipients_response = self.wrapper.get_transfer_recipients()
        response = self.wrapper.delete(id_or_code="54134578")
        self.assertEqual(response.status_code, httpx.codes.OK)


class TransferRecipientTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = TransferRecipient()

    def test_can_create(self):
        response = self.wrapper.create(
            type=RecipientType.NUBAN,
            name="Adeyi Gbenga Michael",
            account_number="5273681014",
            bank_code="214",
            currency=Currency.NGN,
        )
        self.assertEqual(response.status_code, httpx.codes.CREATED)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient created successfully")

    def test_can_bulk_create(self):
        batch = [
            {
                "type": RecipientType.NUBAN,
                "name": "Adeyi Gbenga Michael",
                "account_number": "5273681014",
                "bank_code": "214",
            }
        ]
        response = self.wrapper.bulk_create(batch=Recipient.from_dict_many(batch))
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients added successfully")

    def test_can_get_transfer_recipients(self):
        response = self.wrapper.get_transfer_recipients()
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipients retrieved")

    def test_can_get_transfer_recipient(self):
        response = self.wrapper.get_transfer_recipient(id_or_code="54134578")
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient retrieved")

    def test_can_update(self):
        response = self.wrapper.update(
            id_or_code="54134578",
            name="Adeyi Gbenga Michael",
            email="coyotedevmail@gmail.com",
        )
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Recipient updated")

    def test_can_delete(self):
        all_recipients_response = self.wrapper.get_transfer_recipients()
        response = self.wrapper.delete(id_or_code=all_recipients_response.data[0]["id"])
        self.assertEqual(response.status_code, httpx.codes.OK)
        self.assertTrue(response.status)
        self.assertEqual(response.message, "Transfer recipient set as inactive")
