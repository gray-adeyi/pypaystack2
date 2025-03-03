from pypaystack2.base_api_client import BaseAPIClient, BaseAsyncAPIClient
from pypaystack2.sub_clients.async_clients.apple_pay import AsyncApplePayClient
from pypaystack2.sub_clients.async_clients.bulk_charges import AsyncBulkChargeClient
from pypaystack2.sub_clients.async_clients.charge import AsyncChargeClient
from pypaystack2.sub_clients.async_clients.customers import AsyncCustomerClient
from pypaystack2.sub_clients.async_clients.dedicated_accounts import (
    AsyncDedicatedAccountClient,
)
from pypaystack2.sub_clients.async_clients.disputes import AsyncDisputeClient
from pypaystack2.sub_clients.async_clients.integration import AsyncIntegrationClient
from pypaystack2.sub_clients.async_clients.miscellaneous import AsyncMiscellaneousClient
from pypaystack2.sub_clients.async_clients.payment_pages import AsyncPaymentPageClient
from pypaystack2.sub_clients.async_clients.payment_requests import (
    AsyncPaymentRequestClient,
)
from pypaystack2.sub_clients.async_clients.plans import AsyncPlanClient
from pypaystack2.sub_clients.async_clients.products import AsyncProductClient
from pypaystack2.sub_clients.async_clients.refunds import AsyncRefundClient
from pypaystack2.sub_clients.async_clients.settlements import AsyncSettlementClient
from pypaystack2.sub_clients.async_clients.splits import AsyncTransactionSplitClient
from pypaystack2.sub_clients.async_clients.subaccounts import AsyncSubAccountClient
from pypaystack2.sub_clients.async_clients.subscriptions import AsyncSubscriptionClient
from pypaystack2.sub_clients.async_clients.terminals import AsyncTerminalClient
from pypaystack2.sub_clients.async_clients.transactions import AsyncTransactionClient
from pypaystack2.sub_clients.async_clients.transfer_recipients import (
    AsyncTransferRecipientClient,
)
from pypaystack2.sub_clients.async_clients.transfers import AsyncTransferClient
from pypaystack2.sub_clients.async_clients.transfers_control import (
    AsyncTransferControlClient,
)
from pypaystack2.sub_clients.async_clients.verification import AsyncVerificationClient
from pypaystack2.sub_clients.sync_clients.apple_pay import (
    ApplePayClient,
)
from pypaystack2.sub_clients.sync_clients.bulk_charges import (
    BulkChargeClient,
)
from pypaystack2.sub_clients.sync_clients.charge import ChargeClient
from pypaystack2.sub_clients.sync_clients.customers import (
    CustomerClient,
)
from pypaystack2.sub_clients.sync_clients.dedicated_accounts import (
    DedicatedAccountClient,
)
from pypaystack2.sub_clients.sync_clients.disputes import (
    DisputeClient,
)
from pypaystack2.sub_clients.sync_clients.integration import (
    IntegrationClient,
)
from pypaystack2.sub_clients.sync_clients.miscellaneous import (
    MiscellaneousClient,
)
from pypaystack2.sub_clients.sync_clients.payment_pages import (
    PaymentPageClient,
)
from pypaystack2.sub_clients.sync_clients.payment_requests import (
    PaymentRequestClient,
)
from pypaystack2.sub_clients.sync_clients.plans import PlanClient
from pypaystack2.sub_clients.sync_clients.products import (
    ProductClient,
)
from pypaystack2.sub_clients.sync_clients.refunds import RefundClient
from pypaystack2.sub_clients.sync_clients.settlements import (
    SettlementClient,
)
from pypaystack2.sub_clients.sync_clients.splits import (
    TransactionSplitClient,
)
from pypaystack2.sub_clients.sync_clients.subaccounts import (
    SubAccountClient,
)
from pypaystack2.sub_clients.sync_clients.subscriptions import (
    SubscriptionClient,
)
from pypaystack2.sub_clients.sync_clients.terminals import (
    TerminalClient,
)
from pypaystack2.sub_clients.sync_clients.transactions import (
    TransactionClient,
)
from pypaystack2.sub_clients.sync_clients.transfer_recipients import (
    TransferRecipientClient,
)
from pypaystack2.sub_clients.sync_clients.transfers import (
    TransferClient,
)
from pypaystack2.sub_clients.sync_clients.transfers_control import (
    TransferControlClient,
)
from pypaystack2.sub_clients.sync_clients.verification import (
    VerificationClient,
)


class PaystackClient(BaseAPIClient):
    """A Paystack API client class with all the wrappers supported by pypaystack2.

    This class has all the individual sub_clients classes like `ApplePay`, `BulkCharge` bound to it.
    its intent is to reduce the number of imports by exposing all the sub_clients bound to it via an
    instance of this class.
    """

    def __init__(self, secret_key: str = None):
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
