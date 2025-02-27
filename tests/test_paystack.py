from unittest import TestCase

from dotenv import load_dotenv

from pypaystack2 import PaystackClient, AsyncPaystackClient
from pypaystack2.sub_clients import (
    PaymentPageClient,
    ApplePayClient,
    BulkChargeClient,
    ChargeClient,
    IntegrationClient,
    CustomerClient,
    DedicatedAccountClient,
    DisputeClient,
    PaymentRequestClient,
    MiscellaneousClient,
    PlanClient,
    ProductClient,
    RefundClient,
    SettlementClient,
    SubAccountClient,
    SubscriptionClient,
    TransactionSplitClient,
    TerminalClient,
    TransactionClient,
    TransferClient,
    TransferControlClient,
    VerificationClient,
)
from pypaystack2.sub_clients.async_clients.apple_pay import AsyncApplePayClient
from pypaystack2.sub_clients.async_clients.bulk_charges import AsyncBulkChargeClient
from pypaystack2.sub_clients.charge import AsyncChargeClient
from pypaystack2.sub_clients.customers import AsyncCustomerClient
from pypaystack2.sub_clients.dedicated_accounts import AsyncDedicatedAccountClient
from pypaystack2.sub_clients.disputes import AsyncDisputeClient
from pypaystack2.sub_clients.integration import AsyncIntegrationClient
from pypaystack2.sub_clients.miscellaneous import AsyncMiscellaneousClient
from pypaystack2.sub_clients.payment_pages import AsyncPaymentPageClient
from pypaystack2.sub_clients.payment_requests import AsyncPaymentRequestClient
from pypaystack2.sub_clients.plans import AsyncPlanClient
from pypaystack2.sub_clients.products import AsyncProductClient
from pypaystack2.sub_clients.refunds import AsyncRefundClient
from pypaystack2.sub_clients.settlements import AsyncSettlementClient
from pypaystack2.sub_clients.splits import AsyncTransactionSplitClient
from pypaystack2.sub_clients.subaccounts import AsyncSubAccountClient
from pypaystack2.sub_clients.subscriptions import AsyncSubscriptionClient
from pypaystack2.sub_clients.terminals import AsyncTerminalClient
from pypaystack2.sub_clients.transactions import AsyncTransactionClient
from pypaystack2.sub_clients.transfer_recipients import (
    TransferRecipientClient,
    AsyncTransferRecipientClient,
)
from pypaystack2.sub_clients.transfers import AsyncTransferClient
from pypaystack2.sub_clients.transfers_control import AsyncTransferControlClient
from pypaystack2.sub_clients.verification import AsyncVerificationClient


class PaystackTestcase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = PaystackClient()

    def test_attributes(self):
        self.assertIsInstance(getattr(self.wrapper, "apple_pay", None), ApplePayClient)
        self.assertIsInstance(
            getattr(self.wrapper, "bulk_charges", None), BulkChargeClient
        )
        self.assertIsInstance(getattr(self.wrapper, "charge", None), ChargeClient)
        self.assertIsInstance(
            getattr(self.wrapper, "integration", None), IntegrationClient
        )
        self.assertIsInstance(getattr(self.wrapper, "customers", None), CustomerClient)
        self.assertIsInstance(
            getattr(self.wrapper, "dedicated_accounts", None), DedicatedAccountClient
        )
        self.assertIsInstance(getattr(self.wrapper, "disputes", None), DisputeClient)
        self.assertIsInstance(
            getattr(self.wrapper, "payment_requests", None), PaymentRequestClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "miscellaneous", None), MiscellaneousClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "payment_pages", None), PaymentPageClient
        )
        self.assertIsInstance(getattr(self.wrapper, "plans", None), PlanClient)
        self.assertIsInstance(getattr(self.wrapper, "products", None), ProductClient)
        self.assertIsInstance(getattr(self.wrapper, "refunds", None), RefundClient)
        self.assertIsInstance(
            getattr(self.wrapper, "settlements", None), SettlementClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "splits", None), TransactionSplitClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "subaccounts", None), SubAccountClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "subscriptions", None), SubscriptionClient
        )
        self.assertIsInstance(getattr(self.wrapper, "terminals", None), TerminalClient)
        self.assertIsInstance(
            getattr(self.wrapper, "transactions", None), TransactionClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_recipients", None), TransferRecipientClient
        )
        self.assertIsInstance(getattr(self.wrapper, "transfers", None), TransferClient)
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_control", None), TransferControlClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "verification", None), VerificationClient
        )


class AsyncPaystackTestcase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncPaystackClient()

    def test_attributes(self):
        self.assertIsInstance(
            getattr(self.wrapper, "apple_pay", None), AsyncApplePayClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "bulk_charges", None), AsyncBulkChargeClient
        )
        self.assertIsInstance(getattr(self.wrapper, "charge", None), AsyncChargeClient)
        self.assertIsInstance(
            getattr(self.wrapper, "integration", None), AsyncIntegrationClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "customers", None), AsyncCustomerClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "dedicated_accounts", None),
            AsyncDedicatedAccountClient,
        )
        self.assertIsInstance(
            getattr(self.wrapper, "disputes", None), AsyncDisputeClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "payment_requests", None), AsyncPaymentRequestClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "miscellaneous", None), AsyncMiscellaneousClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "payment_pages", None), AsyncPaymentPageClient
        )
        self.assertIsInstance(getattr(self.wrapper, "plans", None), AsyncPlanClient)
        self.assertIsInstance(
            getattr(self.wrapper, "products", None), AsyncProductClient
        )
        self.assertIsInstance(getattr(self.wrapper, "refunds", None), AsyncRefundClient)
        self.assertIsInstance(
            getattr(self.wrapper, "settlements", None), AsyncSettlementClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "splits", None), AsyncTransactionSplitClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "subaccounts", None), AsyncSubAccountClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "subscriptions", None), AsyncSubscriptionClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "terminals", None), AsyncTerminalClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "transactions", None), AsyncTransactionClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_recipients", None),
            AsyncTransferRecipientClient,
        )
        self.assertIsInstance(
            getattr(self.wrapper, "transfers", None), AsyncTransferClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_control", None), AsyncTransferControlClient
        )
        self.assertIsInstance(
            getattr(self.wrapper, "verification", None), AsyncVerificationClient
        )
