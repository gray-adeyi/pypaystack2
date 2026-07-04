from pypaystack2.sub_clients.async_clients.storefronts import AsyncStorefrontClient
from pypaystack2.sub_clients.async_clients.orders import AsyncOrderClient
from pypaystack2.sub_clients.async_clients.preauthorizations import (
    AsyncPreauthorizationClient,
)
from pypaystack2.sub_clients.sync_clients.preauthorizations import (
    PreauthorizationClient,
)
from pypaystack2.sub_clients.sync_clients.orders import OrderClient
from pypaystack2.sub_clients.sync_clients.storefronts import StorefrontClient
from http import HTTPMethod
from pypaystack2.types import PaystackDataModel
from pypaystack2.sub_clients.async_clients.direct_debits import AsyncDirectDebitClient
from pypaystack2.sub_clients.sync_clients.direct_debits import DirectDebitClient
from pypaystack2.sub_clients.async_clients.virtual_terminals import (
    AsyncVirtualTerminalClient,
)
from pypaystack2.sub_clients.sync_clients.virtual_terminals import VirtualTerminalClient
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
    """A Paystack API client class with all the sub clients supported by pypaystack2.

    This class has all the individual sub clients classes like `ApplePayClient`, `BulkChargeClient`
    as bindings to it.

    Attributes:
        apple_pay: A binding to `ApplePayClient` providing methods for interacting Paystack's Apple Pay API
            e.g. `PaystackClient.apple_pay.get_domains`.
        bulk_charges: A binding to `BulkChargeClient` providing methods for interacting Paystack's Bulk charge API
            e.g. `PaystackClient.bulk_charges.initiate`.
        charge: A binding to `ChargeClient` providing methods for interacting Paystack's Charge API
            e.g. `PaystackClient.charge.charge`.
        integration: A binding to `IntegrationClient` providing methods for interacting Paystack's Integration API
            e.g. `PaystackClient.integration.get_payment_session_timeout`.
        customers: A binding to `CustomerClient` providing methods for interacting Paystack's Customer API
            e.g. `PaystackClient.customers.create`.
        dedicated_accounts: A binding to `DedicatedAccountClient` providing methods for interacting
            Paystack's Dedicated account API e.g. `PaystackClient.dedicated_accounts.create`.
        disputes: A binding to `DisputeClient` providing methods for interacting Paystack's Dispute API
            e.g. `PaystackClient.disputes.`.
        payment_requests: A binding to `PaymentRequestClient` providing methods for interacting Paystack's Payment
            request API e.g. `PaystackClient.payment_requests.create`.
        miscellaneous: A binding to `ApplePayClient` providing methods for interacting Paystack's Apple Pay API
            e.g. `PaystackClient.miscellaneous.get_banks`.
        payment_pages: A binding to `PaymentPageClient` providing methods for interacting Paystack's Payment Page API
            e.g. `PaystackClient.payment_pages.create`.
        plans: A binding to `PlanClient` providing methods for interacting Paystack's Plan API
            e.g. `PaystackClient.plans.get_plans`.
        products: A binding to `ProductClient` providing methods for interacting Paystack's Product API
            e.g. `PaystackClient.products.get_product`.
        refunds: A binding to `RefundClient` providing methods for interacting Paystack's Refund API
            e.g. `PaystackClient.refunds.create`.
        settlements: A binding to `SettlementClient` providing methods for interacting Paystack's Settlement API
            e.g. `PaystackClient.settlements.get_settlements`.
        splits: A binding to `TransactionSplitClient` providing methods for interacting Paystack's Transaction split API
            e.g. `PaystackClient.splits.create`.
        subaccounts: A binding to `SubAccountClient` providing methods for interacting Paystack's subaccount API
            e.g. `PaystackClient.subaccounts.create`.
        subscriptions: A binding to `SubscriptionClient` providing methods for interacting Paystack's Subscription API
            e.g. `PaystackClient.subscriptions.create`.
        terminals: A binding to `TerminalClient` providing methods for interacting Paystack's Terminal API
            e.g. `PaystackClient.terminals.send_event`.
        transactions: A binding to `TransactionClient` providing methods for interacting Paystack's Transaction API
            e.g. `PaystackClient.transactions.initiate`.
        transfer_recipients: A binding to `TransferRecipientClient` providing methods for interacting Paystack's
            Transfer recipients API e.g. `PaystackClient.transfer_recipients.create`.
        transfers: A binding to `TransferClient` providing methods for interacting Paystack's Transfer API
            e.g. `PaystackClient.transfers.finalize`.
        transfer_control: A binding to `TransferControlClient` providing methods for interacting Paystack's
            Transfers control API e.g. `PaystackClient.transfer_control.check_balance`.
        verification: A binding to `VerificationClient` providing methods for interacting Paystack's Verification API
            e.g. `PaystackClient.verification.resolve_account_number`.
        virtual_terminals: A binding to `VirtualTerminalClient` providing methods for interacting with Paystack's
            Virtual Terminal API e.g. `VirtualTerminalClient.list`.
        direct_debits: A binding to `DirectDebitClient` providing methods for interacting with Paystack's
            Direct Debit API e.g. `DirectDebitClient.trigger_activation_charge`.
        storefronts: A binding to `StorefrontClient` providing methods for interacting with Paystack's
            Storefront API e.g. `StorefrontClient.create`.
        orders: A binding to `OrderClient` providing methods for interacting with Paystack's
            Order API e.g. `OrderClient.create`.
        preauthorizations: A binding to `PreauthorizationClient` providing methods for interacting with Paystack's
            Preauthorization API e.g. `PreauthorizationClient.initialize`.
    """

    def __init__(self, secret_key: str | None = None):
        super().__init__(secret_key=secret_key)
        self.apple_pay: ApplePayClient = ApplePayClient(secret_key=self._secret_key)
        self.bulk_charges: BulkChargeClient = BulkChargeClient(
            secret_key=self._secret_key
        )
        self.charge: ChargeClient = ChargeClient(secret_key=self._secret_key)
        self.integration: IntegrationClient = IntegrationClient(
            secret_key=self._secret_key
        )
        self.customers: CustomerClient = CustomerClient(secret_key=self._secret_key)
        self.dedicated_accounts: DedicatedAccountClient = DedicatedAccountClient(
            secret_key=self._secret_key
        )
        self.disputes: DisputeClient = DisputeClient(secret_key=self._secret_key)
        self.payment_requests: PaymentRequestClient = PaymentRequestClient(
            secret_key=self._secret_key
        )
        self.miscellaneous: MiscellaneousClient = MiscellaneousClient(
            secret_key=self._secret_key
        )
        self.payment_pages: PaymentPageClient = PaymentPageClient(
            secret_key=self._secret_key
        )
        self.plans: PlanClient = PlanClient(secret_key=self._secret_key)
        self.products: ProductClient = ProductClient(secret_key=self._secret_key)
        self.refunds: RefundClient = RefundClient(secret_key=self._secret_key)
        self.settlements: SettlementClient = SettlementClient(
            secret_key=self._secret_key
        )
        self.splits: TransactionSplitClient = TransactionSplitClient(
            secret_key=self._secret_key
        )
        self.subaccounts: SubAccountClient = SubAccountClient(
            secret_key=self._secret_key
        )
        self.subscriptions: SubscriptionClient = SubscriptionClient(
            secret_key=self._secret_key
        )
        self.terminals: TerminalClient = TerminalClient(secret_key=self._secret_key)
        self.transactions: TransactionClient = TransactionClient(
            secret_key=self._secret_key
        )
        self.transfer_recipients: TransferRecipientClient = TransferRecipientClient(
            secret_key=self._secret_key
        )
        self.transfers: TransferClient = TransferClient(secret_key=self._secret_key)
        self.transfer_control: TransferControlClient = TransferControlClient(
            secret_key=self._secret_key
        )
        self.verification: VerificationClient = VerificationClient(
            secret_key=self._secret_key
        )
        self.virtual_terminals = VirtualTerminalClient(secret_key=self._secret_key)
        self.direct_debits = DirectDebitClient(secret_key=self._secret_key)
        self.storefronts = StorefrontClient(secret_key=self._secret_key)
        self.orders = OrderClient(secret_key=self._secret_key)
        self.preauthorizations = PreauthorizationClient(secret_key=self._secret_key)

    def get_capitec_pay_transaction(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """Check the status of a charge made with Capitec Pay.

        Args:
            reference: The transaction reference from the previously initiated charge request
            alternate_model_class: A pydantic model class to use instead of the
            default pydantic model used by the library to present the data in
            the `Response.data`. The default behaviour of the library is to
            set  `Response.data` to `None` if it fails to serialize the data
            returned from paystack with the model provided in the library.
            Providing a pydantic model class via this parameter overrides
            the library default model with the model class you provide.
            This can come in handy when the models in the library do not
            accurately represent the data returned, and you prefer working with the
            data as a pydantic model instead of as a dict of the response returned
            by  paystack before it is serialized with pydantic models, The original
            data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/capitec-pay/requery/{reference}")
        return self._handle_request(
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )


class AsyncPaystackClient(BaseAsyncAPIClient):
    """An asynchronous Paystack API client class with all the sub clients supported by pypaystack2.

    This class has all the individual sub clients classes like `AsyncApplePayClient`, `AsyncBulkChargeClient`
    as bindings to it.

    Attributes:
        apple_pay: A binding to `AsyncApplePayClient` providing methods for interacting Paystack's Apple Pay API
            e.g. `AsyncPaystackClient.apple_pay.get_domains`.
        bulk_charges: A binding to `AsyncBulkChargeClient` providing methods for interacting Paystack's Bulk charge API
            e.g. `AsyncPaystackClient.bulk_charges.initiate`.
        charge: A binding to `AsyncChargeClient` providing methods for interacting Paystack's Charge API
            e.g. `AsyncPaystackClient.charge.charge`.
        integration: A binding to `AsyncIntegrationClient` providing methods for interacting Paystack's Integration API
            e.g. `AsyncPaystackClient.integration.get_payment_session_timeout`.
        customers: A binding to `AsyncCustomerClient` providing methods for interacting Paystack's Customer API
            e.g. `AsyncPaystackClient.customers.create`.
        dedicated_accounts: A binding to `AsyncDedicatedAccountClient` providing methods for interacting
            Paystack's Dedicated account API e.g. `PaystackClient.dedicated_accounts.create`.
        disputes: A binding to `AsyncDisputeClient` providing methods for interacting Paystack's Dispute API
            e.g. `AsyncPaystackClient.disputes.`.
        payment_requests: A binding to `AsyncPaymentRequestClient` providing methods for interacting Paystack's Payment
            request API e.g. `AsyncPaystackClient.payment_requests.create`.
        miscellaneous: A binding to `AsyncApplePayClient` providing methods for interacting Paystack's Apple Pay API
            e.g. `AsyncPaystackClient.miscellaneous.get_banks`.
        payment_pages: A binding to `AsyncPaymentPageClient` providing methods for interacting Paystack's Payment Page
            API e.g. `PaystackClient.payment_pages.create`.
        plans: A binding to `AsyncPlanClient` providing methods for interacting Paystack's Plan API
            e.g. `AsyncPaystackClient.plans.get_plans`.
        products: A binding to `AsyncProductClient` providing methods for interacting Paystack's Product API
            e.g. `PaystackClient.products.get_product`.
        refunds: A binding to `AsyncRefundClient` providing methods for interacting Paystack's Refund API
            e.g. `AsyncPaystackClient.refunds.create`.
        settlements: A binding to `AsyncSettlementClient` providing methods for interacting Paystack's Settlement API
            e.g. `AsyncPaystackClient.settlements.get_settlements`.
        splits: A binding to `AsyncTransactionSplitClient` providing methods for interacting Paystack's Transaction
            split API e.g. `AsyncPaystackClient.splits.create`.
        subaccounts: A binding to `AsyncSubAccountClient` providing methods for interacting Paystack's subaccount API
            e.g. `AsyncPaystackClient.subaccounts.create`.
        subscriptions: A binding to `AsyncSubscriptionClient` providing methods for interacting Paystack's Subscription
            API e.g. `AsyncPaystackClient.subscriptions.create`.
        terminals: A binding to `AsyncTerminalClient` providing methods for interacting Paystack's Terminal API
            e.g. `AsyncPaystackClient.terminals.send_event`.
        transactions: A binding to `AsyncTransactionClient` providing methods for interacting Paystack's Transaction
            API e.g. `AsyncPaystackClient.transactions.initiate`.
        transfer_recipients: A binding to `AsyncTransferRecipientClient` providing methods for interacting Paystack's
            Transfer recipients API e.g. `AsyncPaystackClient.transfer_recipients.create`.
        transfers: A binding to `AsyncTransferClient` providing methods for interacting Paystack's Transfer API
            e.g. `PaystackClient.transfers.finalize`.
        transfer_control: A binding to `AsyncTransferControlClient` providing methods for interacting Paystack's
            Transfers control API e.g. `AsyncPaystackClient.transfer_control.check_balance`.
        verification: A binding to `AsyncVerificationClient` providing methods for interacting Paystack's Verification
            API e.g. `AsyncPaystackClient.verification.resolve_account_number`.
        virtual_terminals: A binding to `VirtualTerminalClient` providing methods for interacting with Paystack's
            Virtual Terminal API e.g. `AsyncVirtualTerminalClient.list`.
        direct_debits: A binding to `AsyncDirectDebitClient` providing methods for interacting with Paystack's
            Direct Debit API e.g. `AsyncDirectDebitClient.trigger_activation_charge`.
        storefronts: A binding to `AsyncStorefrontClient` providing methods for interacting with Paystack's
            Storefront API e.g. `AsyncStorefrontClient.create`.
        orders: A binding to `AsyncOrderClient` providing methods for interacting with Paystack's
            Order API e.g. `AsyncOrderClient.create`.
        preauthorizations: A binding to `AsyncPreauthorizationClient` providing methods for interacting with Paystack's
            Preauthorization API e.g. `AsyncPreauthorizationClient.initialize`.

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
        self.virtual_terminals = AsyncVirtualTerminalClient(secret_key=self._secret_key)
        self.direct_debits = AsyncDirectDebitClient(secret_key=self._secret_key)
        self.storefronts = AsyncStorefrontClient(secret_key=self._secret_key)
        self.orders = AsyncOrderClient(secret_key=self._secret_key)
        self.preauthorizations = AsyncPreauthorizationClient(
            secret_key=self._secret_key
        )

    async def get_capitec_pay_transaction(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """Check the status of a charge made with Capitec Pay.

        Args:
            reference: The transaction reference from the previously initiated charge request
            alternate_model_class: A pydantic model class to use instead of the
            default pydantic model used by the library to present the data in
            the `Response.data`. The default behaviour of the library is to
            set  `Response.data` to `None` if it fails to serialize the data
            returned from paystack with the model provided in the library.
            Providing a pydantic model class via this parameter overrides
            the library default model with the model class you provide.
            This can come in handy when the models in the library do not
            accurately represent the data returned, and you prefer working with the
            data as a pydantic model instead of as a dict of the response returned
            by  paystack before it is serialized with pydantic models, The original
            data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/capitec-pay/requery/{reference}")
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )
