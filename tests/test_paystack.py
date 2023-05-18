from unittest import TestCase

from dotenv import load_dotenv

from pypaystack2 import Paystack, Split, AsyncPaystack
from pypaystack2.api import (
    PaymentPage,
    ApplePay,
    BulkCharge,
    Charge,
    Integration,
    Customer,
    DedicatedAccount,
    Dispute,
    PaymentRequest,
    Miscellaneous,
    Plan,
    Product,
    Refund,
    Settlement,
    SubAccount,
    Subscription,
    TransactionSplit,
    Terminal,
    Transaction,
    Transfer,
    TransferControl,
    Verification,
)
from pypaystack2.api.apple_pay import AsyncApplePay
from pypaystack2.api.bulk_charges import AsyncBulkCharge
from pypaystack2.api.charge import AsyncCharge
from pypaystack2.api.customers import AsyncCustomer
from pypaystack2.api.dedicated_accounts import AsyncDedicatedAccount
from pypaystack2.api.disputes import AsyncDispute
from pypaystack2.api.integration import AsyncIntegration
from pypaystack2.api.miscellaneous import AsyncMiscellaneous
from pypaystack2.api.payment_pages import AsyncPaymentPage
from pypaystack2.api.payment_requests import AsyncPaymentRequest
from pypaystack2.api.plans import AsyncPlan
from pypaystack2.api.products import AsyncProduct
from pypaystack2.api.refunds import AsyncRefund
from pypaystack2.api.settlements import AsyncSettlement
from pypaystack2.api.splits import AsyncTransactionSplit
from pypaystack2.api.subaccounts import AsyncSubAccount
from pypaystack2.api.subscriptions import AsyncSubscription
from pypaystack2.api.terminals import AsyncTerminal
from pypaystack2.api.transactions import AsyncTransaction
from pypaystack2.api.transfer_recipients import (
    TransferRecipient,
    AsyncTransferRecipient,
)
from pypaystack2.api.transfers import AsyncTransfer
from pypaystack2.api.transfers_control import AsyncTransferControl
from pypaystack2.api.verification import AsyncVerification


class PaystackTestcase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = Paystack()

    def test_attributes(self):
        self.assertIsInstance(getattr(self.wrapper, "apple_pay", None), ApplePay)
        self.assertIsInstance(getattr(self.wrapper, "bulk_charges", None), BulkCharge)
        self.assertIsInstance(getattr(self.wrapper, "charge", None), Charge)
        self.assertIsInstance(getattr(self.wrapper, "integration", None), Integration)
        self.assertIsInstance(getattr(self.wrapper, "customers", None), Customer)
        self.assertIsInstance(
            getattr(self.wrapper, "dedicated_accounts", None), DedicatedAccount
        )
        self.assertIsInstance(getattr(self.wrapper, "disputes", None), Dispute)
        self.assertIsInstance(
            getattr(self.wrapper, "payment_requests", None), PaymentRequest
        )
        self.assertIsInstance(
            getattr(self.wrapper, "miscellaneous", None), Miscellaneous
        )
        self.assertIsInstance(getattr(self.wrapper, "payment_pages", None), PaymentPage)
        self.assertIsInstance(getattr(self.wrapper, "plans", None), Plan)
        self.assertIsInstance(getattr(self.wrapper, "products", None), Product)
        self.assertIsInstance(getattr(self.wrapper, "refunds", None), Refund)
        self.assertIsInstance(getattr(self.wrapper, "settlements", None), Settlement)
        self.assertIsInstance(getattr(self.wrapper, "splits", None), TransactionSplit)
        self.assertIsInstance(getattr(self.wrapper, "subaccounts", None), SubAccount)
        self.assertIsInstance(
            getattr(self.wrapper, "subscriptions", None), Subscription
        )
        self.assertIsInstance(getattr(self.wrapper, "terminals", None), Terminal)
        self.assertIsInstance(getattr(self.wrapper, "transactions", None), Transaction)
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_recipients", None), TransferRecipient
        )
        self.assertIsInstance(getattr(self.wrapper, "transfers", None), Transfer)
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_control", None), TransferControl
        )
        self.assertIsInstance(getattr(self.wrapper, "verification", None), Verification)


class AsyncPaystackTestcase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.wrapper = AsyncPaystack()

    def test_attributes(self):
        self.assertIsInstance(getattr(self.wrapper, "apple_pay", None), AsyncApplePay)
        self.assertIsInstance(
            getattr(self.wrapper, "bulk_charges", None), AsyncBulkCharge
        )
        self.assertIsInstance(getattr(self.wrapper, "charge", None), AsyncCharge)
        self.assertIsInstance(
            getattr(self.wrapper, "integration", None), AsyncIntegration
        )
        self.assertIsInstance(getattr(self.wrapper, "customers", None), AsyncCustomer)
        self.assertIsInstance(
            getattr(self.wrapper, "dedicated_accounts", None), AsyncDedicatedAccount
        )
        self.assertIsInstance(getattr(self.wrapper, "disputes", None), AsyncDispute)
        self.assertIsInstance(
            getattr(self.wrapper, "payment_requests", None), AsyncPaymentRequest
        )
        self.assertIsInstance(
            getattr(self.wrapper, "miscellaneous", None), AsyncMiscellaneous
        )
        self.assertIsInstance(
            getattr(self.wrapper, "payment_pages", None), AsyncPaymentPage
        )
        self.assertIsInstance(getattr(self.wrapper, "plans", None), AsyncPlan)
        self.assertIsInstance(getattr(self.wrapper, "products", None), AsyncProduct)
        self.assertIsInstance(getattr(self.wrapper, "refunds", None), AsyncRefund)
        self.assertIsInstance(
            getattr(self.wrapper, "settlements", None), AsyncSettlement
        )
        self.assertIsInstance(
            getattr(self.wrapper, "splits", None), AsyncTransactionSplit
        )
        self.assertIsInstance(
            getattr(self.wrapper, "subaccounts", None), AsyncSubAccount
        )
        self.assertIsInstance(
            getattr(self.wrapper, "subscriptions", None), AsyncSubscription
        )
        self.assertIsInstance(getattr(self.wrapper, "terminals", None), AsyncTerminal)
        self.assertIsInstance(
            getattr(self.wrapper, "transactions", None), AsyncTransaction
        )
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_recipients", None), AsyncTransferRecipient
        )
        self.assertIsInstance(getattr(self.wrapper, "transfers", None), AsyncTransfer)
        self.assertIsInstance(
            getattr(self.wrapper, "transfer_control", None), AsyncTransferControl
        )
        self.assertIsInstance(
            getattr(self.wrapper, "verification", None), AsyncVerification
        )
