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
from pypaystack2.api.terminals import Terminal
from pypaystack2.baseapi import BaseAPI


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
