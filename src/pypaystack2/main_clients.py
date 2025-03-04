from pypaystack2.base_clients import BaseAPIClient, BaseAsyncAPIClient
from pypaystack2.sub_clients import (
    ApplePayClient,
    BulkChargeClient,
    ChargeClient,
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
    AsyncPaymentPageClient,
    AsyncPlanClient,
    AsyncProductClient,
    AsyncRefundClient,
    AsyncSettlementClient,
    AsyncTransactionSplitClient,
    AsyncSubAccountClient,
    AsyncSubscriptionClient,
    AsyncTerminalClient,
    AsyncTransactionClient,
    AsyncTransferRecipientClient,
    AsyncTransferClient,
    AsyncTransferControlClient,
    AsyncVerificationClient,
)


class PaystackClient(BaseAPIClient):
    """A Paystack API client class with all the wrappers supported by pypaystack2.

    This class has all the individual sub_clients classes like `ApplePay`, `BulkCharge` bound to it.
    its intent is to reduce the number of imports by exposing all the sub_clients bound to it via an
    instance of this class.
    """

    def __init__(self, secret_key: str | None = None):
        super().__init__(secret_key=secret_key)
        self.apple_pay = ApplePayClient(secret_key=self._secret_key)
        self.bulk_charges = BulkChargeClient(secret_key=self._secret_key)
        self.charge = ChargeClient(secret_key=self._secret_key)
        self.integration = IntegrationClient(secret_key=self._secret_key)
        self.customers = CustomerClient(secret_key=self._secret_key)
        self.dedicated_accounts = DedicatedAccountClient(secret_key=self._secret_key)
        self.disputes = DisputeClient(secret_key=self._secret_key)
        self.payment_requests = PaymentRequestClient(secret_key=self._secret_key)
        self.miscellaneous = MiscellaneousClient(secret_key=self._secret_key)
        self.payment_pages = PaymentPageClient(secret_key=self._secret_key)
        self.plans = PlanClient(secret_key=self._secret_key)
        self.products = ProductClient(secret_key=self._secret_key)
        self.refunds = RefundClient(secret_key=self._secret_key)
        self.settlements = SettlementClient(secret_key=self._secret_key)
        self.splits = TransactionSplitClient(secret_key=self._secret_key)
        self.subaccounts = SubAccountClient(secret_key=self._secret_key)
        self.subscriptions = SubscriptionClient(secret_key=self._secret_key)
        self.terminals = TerminalClient(secret_key=self._secret_key)
        self.transactions = TransactionClient(secret_key=self._secret_key)
        self.transfer_recipients = TransferRecipientClient(secret_key=self._secret_key)
        self.transfers = TransferClient(secret_key=self._secret_key)
        self.transfer_control = TransferControlClient(secret_key=self._secret_key)
        self.verification = VerificationClient(secret_key=self._secret_key)


class AsyncPaystackClient(BaseAsyncAPIClient):
    """An asynchronous Paystack API client class with all the wrappers supported by pypaystack2.

    This class has all the individual sub_clients wrapper classes like `ApplePay`, `BulkCharge` bound to it.
    its intent is to reduce the number of imports by exposing all the sub_clients wrappers bound to it via an
    instance of this class.
    """

    def __init__(self, secret_key: str | None = None):
        super().__init__(secret_key=secret_key)
        self.apple_pay = AsyncApplePayClient(secret_key=self._secret_key)
        self.bulk_charges = AsyncBulkChargeClient(secret_key=self._secret_key)
        self.charge = AsyncChargeClient(secret_key=self._secret_key)
        self.integration = AsyncIntegrationClient(secret_key=self._secret_key)
        self.customers = AsyncCustomerClient(secret_key=self._secret_key)
        self.dedicated_accounts = AsyncDedicatedAccountClient(
            secret_key=self._secret_key
        )
        self.disputes = AsyncDisputeClient(secret_key=self._secret_key)
        self.payment_requests = AsyncPaymentRequestClient(secret_key=self._secret_key)
        self.miscellaneous = AsyncMiscellaneousClient(secret_key=self._secret_key)
        self.payment_pages = AsyncPaymentPageClient(secret_key=self._secret_key)
        self.plans = AsyncPlanClient(secret_key=self._secret_key)
        self.products = AsyncProductClient(secret_key=self._secret_key)
        self.refunds = AsyncRefundClient(secret_key=self._secret_key)
        self.settlements = AsyncSettlementClient(secret_key=self._secret_key)
        self.splits = AsyncTransactionSplitClient(secret_key=self._secret_key)
        self.subaccounts = AsyncSubAccountClient(secret_key=self._secret_key)
        self.subscriptions = AsyncSubscriptionClient(secret_key=self._secret_key)
        self.terminals = AsyncTerminalClient(secret_key=self._secret_key)
        self.transactions = AsyncTransactionClient(secret_key=self._secret_key)
        self.transfer_recipients = AsyncTransferRecipientClient(
            secret_key=self._secret_key
        )
        self.transfers = AsyncTransferClient(secret_key=self._secret_key)
        self.transfer_control = AsyncTransferControlClient(secret_key=self._secret_key)
        self.verification = AsyncVerificationClient(secret_key=self._secret_key)
