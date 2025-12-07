from unittest import TestCase

from dotenv import load_dotenv

from pypaystack2 import PaystackClient, AsyncPaystackClient
from pypaystack2.sub_clients import (
    ApplePayClient,
    BulkChargeClient,
    IntegrationClient,
    CustomerClient,
    DedicatedAccountClient,
    DisputeClient,
    PaymentRequestClient,
    MiscellaneousClient,
    PaymentPageClient,
    PlanClient,
    ProductClient,
    RefundClient,
    SettlementClient,
    TransactionSplitClient,
    SubAccountClient,
    SubscriptionClient,
    TerminalClient,
    TransactionClient,
    TransferRecipientClient,
    TransferClient,
    TransferControlClient,
    VerificationClient,
    AsyncApplePayClient,
    AsyncBulkChargeClient,
    AsyncChargeClient,
    AsyncIntegrationClient,
    AsyncCustomerClient,
    AsyncDedicatedAccountClient,
    AsyncDisputeClient,
    AsyncPaymentRequestClient,
    AsyncMiscellaneousClient,
    ChargeClient,
    AsyncPaymentPageClient,
    AsyncPlanClient,
    AsyncProductClient,
    AsyncRefundClient,
    AsyncSettlementClient,
    AsyncTransactionSplitClient,
    AsyncVerificationClient,
    AsyncTransferControlClient,
    AsyncTransferClient,
    AsyncTransferRecipientClient,
    AsyncTransactionClient,
    AsyncTerminalClient,
    AsyncSubscriptionClient,
    AsyncSubAccountClient,
)


class PaystackClientTestcase(TestCase):
    client: PaystackClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = PaystackClient()

    def test_attributes(self) -> None:
        self.assertIsInstance(getattr(self.client, "apple_pay", None), ApplePayClient)
        self.assertIsInstance(
            getattr(self.client, "bulk_charges", None), BulkChargeClient
        )
        self.assertIsInstance(getattr(self.client, "charge", None), ChargeClient)
        self.assertIsInstance(
            getattr(self.client, "integration", None), IntegrationClient
        )
        self.assertIsInstance(getattr(self.client, "customers", None), CustomerClient)
        self.assertIsInstance(
            getattr(self.client, "dedicated_accounts", None), DedicatedAccountClient
        )
        self.assertIsInstance(getattr(self.client, "disputes", None), DisputeClient)
        self.assertIsInstance(
            getattr(self.client, "payment_requests", None), PaymentRequestClient
        )
        self.assertIsInstance(
            getattr(self.client, "miscellaneous", None), MiscellaneousClient
        )
        self.assertIsInstance(
            getattr(self.client, "payment_pages", None), PaymentPageClient
        )
        self.assertIsInstance(getattr(self.client, "plans", None), PlanClient)
        self.assertIsInstance(getattr(self.client, "products", None), ProductClient)
        self.assertIsInstance(getattr(self.client, "refunds", None), RefundClient)
        self.assertIsInstance(
            getattr(self.client, "settlements", None), SettlementClient
        )
        self.assertIsInstance(
            getattr(self.client, "splits", None), TransactionSplitClient
        )
        self.assertIsInstance(
            getattr(self.client, "subaccounts", None), SubAccountClient
        )
        self.assertIsInstance(
            getattr(self.client, "subscriptions", None), SubscriptionClient
        )
        self.assertIsInstance(getattr(self.client, "terminals", None), TerminalClient)
        self.assertIsInstance(
            getattr(self.client, "transactions", None), TransactionClient
        )
        self.assertIsInstance(
            getattr(self.client, "transfer_recipients", None), TransferRecipientClient
        )
        self.assertIsInstance(getattr(self.client, "transfers", None), TransferClient)
        self.assertIsInstance(
            getattr(self.client, "transfer_control", None), TransferControlClient
        )
        self.assertIsInstance(
            getattr(self.client, "verification", None), VerificationClient
        )


class AsyncPaystackClientTestcase(TestCase):
    client: AsyncPaystackClient

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.client = AsyncPaystackClient()

    def test_attributes(self) -> None:
        self.assertIsInstance(
            getattr(self.client, "apple_pay", None), AsyncApplePayClient
        )
        self.assertIsInstance(
            getattr(self.client, "bulk_charges", None), AsyncBulkChargeClient
        )
        self.assertIsInstance(getattr(self.client, "charge", None), AsyncChargeClient)
        self.assertIsInstance(
            getattr(self.client, "integration", None), AsyncIntegrationClient
        )
        self.assertIsInstance(
            getattr(self.client, "customers", None), AsyncCustomerClient
        )
        self.assertIsInstance(
            getattr(self.client, "dedicated_accounts", None),
            AsyncDedicatedAccountClient,
        )
        self.assertIsInstance(
            getattr(self.client, "disputes", None), AsyncDisputeClient
        )
        self.assertIsInstance(
            getattr(self.client, "payment_requests", None), AsyncPaymentRequestClient
        )
        self.assertIsInstance(
            getattr(self.client, "miscellaneous", None), AsyncMiscellaneousClient
        )
        self.assertIsInstance(
            getattr(self.client, "payment_pages", None), AsyncPaymentPageClient
        )
        self.assertIsInstance(getattr(self.client, "plans", None), AsyncPlanClient)
        self.assertIsInstance(
            getattr(self.client, "products", None), AsyncProductClient
        )
        self.assertIsInstance(getattr(self.client, "refunds", None), AsyncRefundClient)
        self.assertIsInstance(
            getattr(self.client, "settlements", None), AsyncSettlementClient
        )
        self.assertIsInstance(
            getattr(self.client, "splits", None), AsyncTransactionSplitClient
        )
        self.assertIsInstance(
            getattr(self.client, "subaccounts", None), AsyncSubAccountClient
        )
        self.assertIsInstance(
            getattr(self.client, "subscriptions", None), AsyncSubscriptionClient
        )
        self.assertIsInstance(
            getattr(self.client, "terminals", None), AsyncTerminalClient
        )
        self.assertIsInstance(
            getattr(self.client, "transactions", None), AsyncTransactionClient
        )
        self.assertIsInstance(
            getattr(self.client, "transfer_recipients", None),
            AsyncTransferRecipientClient,
        )
        self.assertIsInstance(
            getattr(self.client, "transfers", None), AsyncTransferClient
        )
        self.assertIsInstance(
            getattr(self.client, "transfer_control", None), AsyncTransferControlClient
        )
        self.assertIsInstance(
            getattr(self.client, "verification", None), AsyncVerificationClient
        )
