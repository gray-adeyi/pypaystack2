from pypaystack2.api import (
    ApplePay,
    BulkCharge,
    Charge,
    ControlPanel,
    Customer,
    DedicatedAccount,
    Dispute,
    Invoice,
    Miscellaneous,
    Page,
    Plan,
    Product,
    Refund,
    Settlement,
    Split,
    SubAccount,
    Subscription,
    Transaction,
    TransferRecipient,
    Transfer,
    TransferControl,
    Verification,
)
from pypaystack2.api.apple_pay import AsyncApplePay
from pypaystack2.api.bulk_charges import AsyncBulkCharge
from pypaystack2.api.charge import AsyncCharge
from pypaystack2.api.control_panel import AsyncControlPanel
from pypaystack2.api.customers import AsyncCustomer
from pypaystack2.api.dedicated_accounts import AsyncDedicatedAccount
from pypaystack2.api.disputes import AsyncDispute
from pypaystack2.api.invoices import AsyncInvoice
from pypaystack2.api.miscellaneous import AsyncMiscellaneous
from pypaystack2.api.payment_pages import AsyncPage
from pypaystack2.api.plans import AsyncPlan
from pypaystack2.api.products import AsyncProduct
from pypaystack2.api.refunds import AsyncRefund
from pypaystack2.api.settlements import AsyncSettlement
from pypaystack2.api.splits import AsyncSplit
from pypaystack2.api.subaccounts import AsyncSubAccount
from pypaystack2.api.subscriptions import AsyncSubscription
from pypaystack2.api.terminals import Terminal, AsyncTerminal
from pypaystack2.api.transactions import AsyncTransaction
from pypaystack2.api.transfer_recipients import AsyncTransferRecipient
from pypaystack2.api.transfers import AsyncTransfer
from pypaystack2.api.transfers_control import AsyncTransferControl
from pypaystack2.api.verification import AsyncVerification
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
        self.control_panel = ControlPanel(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.customers = Customer(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.dedicated_accounts = DedicatedAccount(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.disputes = Dispute(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.invoices = Invoice(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.miscellaneous = Miscellaneous(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.payment_pages = Page(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.plans = Plan(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.products = Product(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.refunds = Refund(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.settlements = Settlement(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.splits = Split(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
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
        self.control_panel = AsyncControlPanel(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.customers = AsyncCustomer(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.dedicated_accounts = AsyncDedicatedAccount(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.disputes = AsyncDispute(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.invoices = AsyncInvoice(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.miscellaneous = AsyncMiscellaneous(
            auth_key=self._PAYSTACK_AUTHORIZATION_KEY
        )
        self.payment_pages = AsyncPage(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.plans = AsyncPlan(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.products = AsyncProduct(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.refunds = AsyncRefund(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.settlements = AsyncSettlement(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
        self.splits = AsyncSplit(auth_key=self._PAYSTACK_AUTHORIZATION_KEY)
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
