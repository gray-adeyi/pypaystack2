from pypaystack2.api.apple_pay import AsyncApplePay, ApplePay
from pypaystack2.api.bulk_charges import AsyncBulkCharge, BulkCharge
from pypaystack2.api.charge import AsyncCharge, Charge
from pypaystack2.api.integration import AsyncIntegration, Integration
from pypaystack2.api.customers import AsyncCustomer, Customer
from pypaystack2.api.dedicated_accounts import AsyncDedicatedAccount, DedicatedAccount
from pypaystack2.api.disputes import AsyncDispute, Dispute
from pypaystack2.api.payment_requests import AsyncPaymentRequest, PaymentRequest
from pypaystack2.api.miscellaneous import AsyncMiscellaneous, Miscellaneous
from pypaystack2.api.payment_pages import AsyncPaymentPage, PaymentPage
from pypaystack2.api.plans import AsyncPlan, Plan
from pypaystack2.api.products import AsyncProduct, Product
from pypaystack2.api.refunds import AsyncRefund, Refund
from pypaystack2.api.settlements import AsyncSettlement, Settlement
from pypaystack2.api.splits import AsyncTransactionSplit, TransactionSplit
from pypaystack2.api.subaccounts import AsyncSubAccount, SubAccount
from pypaystack2.api.subscriptions import AsyncSubscription, Subscription
from pypaystack2.api.terminals import Terminal, AsyncTerminal
from pypaystack2.api.transactions import AsyncTransaction, Transaction
from pypaystack2.api.transfer_recipients import (
    AsyncTransferRecipient,
    TransferRecipient,
)
from pypaystack2.api.transfers import AsyncTransfer, Transfer
from pypaystack2.api.transfers_control import AsyncTransferControl, TransferControl
from pypaystack2.api.verification import AsyncVerification, Verification
from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI


class Paystack(BaseAPI):
    """A Paystack API wrapper class with all the wrappers supported by pypaystack2.

    This class has all the individual api wrapper classes like `ApplePay`, `BulkCharge` bound to it.
    its intent is to reduce the number of imports by exposing all the api wrappers bound to it via an
    instance of this class.
    """

    def __init__(self, auth_key: str = None):
        super().__init__(auth_key=auth_key)
        self.apple_pay = ApplePay(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.bulk_charges = BulkCharge(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.charge = Charge(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.integration = Integration(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.customers = Customer(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.dedicated_accounts = DedicatedAccount(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.disputes = Dispute(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.payment_requests = PaymentRequest(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.miscellaneous = Miscellaneous(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.payment_pages = PaymentPage(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.plans = Plan(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.products = Product(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.refunds = Refund(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.settlements = Settlement(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.splits = TransactionSplit(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.subaccounts = SubAccount(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.subscriptions = Subscription(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.terminals = Terminal(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.transactions = Transaction(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.transfer_recipients = TransferRecipient(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.transfers = Transfer(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.transfer_control = TransferControl(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.verification = Verification(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)


class AsyncPaystack(BaseAsyncAPI):
    """An asynchronous Paystack API wrapper class with all the wrappers supported by pypaystack2.

    This class has all the individual api wrapper classes like `ApplePay`, `BulkCharge` bound to it.
    its intent is to reduce the number of imports by exposing all the api wrappers bound to it via an
    instance of this class.
    """

    def __init__(self, auth_key: str = None):
        super().__init__(auth_key=auth_key)
        self.apple_pay = AsyncApplePay(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.bulk_charges = AsyncBulkCharge(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.charge = AsyncCharge(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.integration = AsyncIntegration(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.customers = AsyncCustomer(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.dedicated_accounts = AsyncDedicatedAccount(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.disputes = AsyncDispute(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.payment_requests = AsyncPaymentRequest(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.miscellaneous = AsyncMiscellaneous(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.payment_pages = AsyncPaymentPage(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.plans = AsyncPlan(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.products = AsyncProduct(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.refunds = AsyncRefund(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.settlements = AsyncSettlement(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.splits = AsyncTransactionSplit(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.subaccounts = AsyncSubAccount(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.subscriptions = AsyncSubscription(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.terminals = AsyncTerminal(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.transactions = AsyncTransaction(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.transfer_recipients = AsyncTransferRecipient(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.transfers = AsyncTransfer(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.transfer_control = AsyncTransferControl(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.verification = AsyncVerification(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
