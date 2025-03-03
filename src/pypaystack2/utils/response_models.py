from datetime import datetime, timedelta
from typing import Any, Optional, Literal, Generic, TypeVar, Union

from pydantic import BaseModel

from pypaystack2.utils.enums import (
    Domain,
    BulkChargeStatus,
    Country,
    Currency,
    RiskAction,
    SupportedCountryRelationshipType,
    DisputeStatus,
    Interval,
)
from pypaystack2.utils.models import LineItem, Tax


class State(BaseModel):
    name: str
    slug: str
    abbreviation: str


class IntegrationTimeout(BaseModel):
    payment_session_timeout: timedelta


class Integration(BaseModel):
    key: str
    name: str
    logo: str
    allowed_currencies: list[Currency]


class ApplePayDomains(BaseModel):
    domain_names: list[str]


class BulkCharge(BaseModel):
    batch_code: str
    reference: str | None = None
    id: int
    integration: int | None = None
    domain: Domain
    status: BulkChargeStatus
    total_charges: int | None = None
    pending_charges: int | None = None
    created_at: datetime
    updated_at: datetime


class BulkChargeUnitCharge(BaseModel):
    integration: int
    bulkcharge: int
    customer: "Customer"
    authorization: "Authorization"
    transaction: "Transaction"
    domain: Domain
    amount: int
    currency: Currency
    status: str  # TODO: find bulk charge unit charge status types
    id: str
    created_at: datetime
    updated_at: datetime


class Customer(BaseModel):
    integration: int | None = None
    id: int
    first_name: str | None = None
    last_name: str | None = None
    email: str
    customer_code: str
    phone: str | None = None
    metadata: dict[str, Any] | None = None
    risk_action: RiskAction
    international_phone_format: str | None = None
    identified: bool | None = None
    identifications: Any | None = None
    transactions: list["Transaction"] | None = None
    subscriptions: list["Subscription"] | None = None
    authorizations: list["Authorization"] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    total_transactions: int | None = None
    total_transaction_value: list[Any] | None = None
    dedicated_account: str | None = None
    dedicated_accounts: list[Any] | None = None


class Authorization(BaseModel):
    authorization_code: str
    bin: str
    last4: str
    exp_month: str
    exp_year: str
    channel: str
    card_type: str
    bank: str
    country_code: Country
    brand: str
    reusable: bool
    account_name: str | None = None


class InitTransaction(BaseModel):
    authorization_url: str
    access_code: str
    reference: str


class TransactionHistory(BaseModel):
    type: str
    message: str
    time: int


class TransactionLog(BaseModel):
    start_time: int
    time_spent: int
    attempts: int
    errors: int
    success: bool
    mobile: bool
    input: list[Any]
    history: list[TransactionHistory]


class TransactionTotal(BaseModel):
    total_transactions: int
    total_volume: int
    total_volume_by_currency: list["Money"]
    pending_transfers: int
    pending_transfers_by_currency: list["Money"]


class TransactionExport(BaseModel):
    path: str
    expires_at: str


class TransactionSource(BaseModel):
    source: str = "merchant_api"
    type: str = "api"
    identifier: Any | None = None
    entry_point: str = "charge"


class Transaction(BaseModel):
    id: int
    domain: Domain
    status: str | None = None
    reference: str
    amount: int
    message: str | None = None
    gateway_response: str | None = None
    paid_at: datetime | None = None
    channel: str
    currency: Currency
    ip_address: str | None = None
    metadata: dict[str, Any] | str | int | None = None
    log: TransactionLog | None = None
    fees: int | None = None
    fees_split: Any | None = None
    customer: Customer | dict[str, Any]
    authorization: Authorization | dict[str, Any]
    plan: Optional[Union["Plan", dict[str, Any]]] = None
    split: Optional[Union["TransactionSplit", dict[str, Any]]] = None
    subaccount: Optional[Union["SubAccount", dict[str, Any]]] = None
    order_id: str | None = None
    created_at: datetime | None = None
    requested_amount: int | None = None
    source: TransactionSource | None = None
    connect: Any | None = None
    post_transaction_data: Any | None = None


class TransactionSplitSubAccount(BaseModel):
    subaccount: "SubAccount"
    share: int | float


class TransactionSplit(BaseModel):
    id: int
    name: str
    type: str  # TODO: Find the supported types for splits
    currency: Currency
    integration: int
    domain: Domain
    split_code: str
    active: bool
    bearer_type: str
    bearer_subaccount: str | None = None
    created_at: datetime
    updated_at: datetime
    is_dynamic: bool
    subaccounts: list[TransactionSplitSubAccount]
    total_subaccounts: int


class Subscription(BaseModel):
    customer: int | Customer
    plan: Union[int, "Plan"]
    integration: int
    domain: Domain
    start: int | None = None
    status: str  # TODO: find all the supported status for subscription
    quantity: int | None = None
    amount: int
    subscription_code: str
    email_token: str
    authorization: int | Authorization
    easy_cron_id: str | None = None
    cron_expression: str
    next_payment_date: datetime | None = None
    open_invoice: Any | None = None
    invoice_limit: int
    id: int
    split_code: str | None = None
    cancelled_at: datetime | None = None
    updated_at: datetime | None = None
    payments_count: int | None = None
    most_recent_invoice: Optional["Invoice"] = None
    invoices: list["Invoice"] | None = None
    invoice_history: list[Any] | None = None


class SubscriptionLink(BaseModel):
    link: str


class Invoice(BaseModel):
    subscription: int
    integration: int
    domain: Domain
    invoice_code: str
    customer: int
    transaction: int
    amount: int
    period_start: str
    period_end: str
    status: str  # TODO: Find all invoice types
    paid: int | bool
    retries: int
    authorization: int
    paid_at: datetime | None = None
    next_notification: str
    notification_flag: Any | None = None
    description: str | None = None
    id: int
    created_at: datetime
    updated_at: datetime


class PaymentPage(BaseModel):
    integration: int
    plan: int | None = None
    domain: Domain
    name: str
    description: str | None = None
    amount: int | None = None
    currency: Currency
    slug: str
    custom_fields: dict[str, Any] | None = None  # TODO: find custom_field types
    type: str
    redirect_url: str | None = None
    success_message: str | None = None
    collect_phone: bool
    active: bool
    published: bool
    migrate: bool
    notification_email: str | None = None
    metadata: dict[str, Any] | None = None
    split_code: str | None = None
    id: int
    created_at: datetime
    updated_at: datetime
    products: list["Product"] | None = None


class PaymentRequestNotification(BaseModel):
    sent_at: datetime
    channel: str  # TODO: Find all the supported channels for notifcations


class PaymentRequest(BaseModel):
    id: int
    integration: int | Integration
    domain: Domain
    amount: int
    currency: Currency
    due_date: datetime | None = None
    has_invoice: bool | None = None
    invoice_number: int | None = None
    description: str | None = None
    pdf_url: str | None = None
    line_items: list[LineItem]
    tax: list[Tax]
    request_code: str
    status: str
    paid: bool
    paid_at: datetime | None = None
    metadata: dict[str, Any] | None = None
    notifications: list[PaymentRequestNotification]
    offline_reference: str
    customer: Customer | int
    created_at: datetime
    discount: str | None = None
    split_code: str | None = None
    transactions: list[Transaction] | None = None
    archived: bool | None = None
    source: str | None = None
    payment_method: Any | None = None
    note: Any | None = None
    amount_paid: int | None = None
    updated_at: datetime | None = None
    pending_amount: int | None = None


class Money(BaseModel):
    currency: Currency
    amount: int


class PaymentRequestStat(BaseModel):
    pending: list[Money]
    successful: list[Money]
    total: list[Money]


class PlanSubscriber(BaseModel):
    customer_code: str
    customer_first_name: str
    customer_last_name: str
    customer_email: str
    subscription_status: str  # TODO: Find all subsciption status types
    currency: Currency
    customer_total_amount_paid: int


class Plan(BaseModel):
    subscriptions: list[Subscription] | None = None
    pages: list[PaymentPage] | None = None
    domain: Domain | None = None
    name: str
    plan_code: str
    description: str | None = None
    amount: int
    interval: Interval
    invoice_limit: int | None = None
    send_invoices: bool
    send_sms: bool
    hosted_page: bool | None = None
    hosted_page_url: str | None = None
    hosted_page_summary: str | None = None
    currency: Currency
    migrate: bool | None = None
    is_deleted: bool | None = None
    is_archived: bool | None = None
    id: int
    integration: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    total_subscriptions: int | None = None
    active_subscriptions: int | None = None
    total_subscriptions_revenue: int | None = None
    pages_count: int | None = None
    subscribers_count: int | None = None
    subscriptions_count: int | None = None
    active_subscriptions_count: int | None = None
    total_revenue: int | None = None
    subscribers: list[PlanSubscriber] | None = None


class SubAccount(BaseModel):
    id: int
    subaccount_code: str
    business_name: str
    description: str | None = None
    primary_contact_name: str | None = None
    primary_contact_email: str | None = None
    primary_contact_phone: str | None = None
    metadata: dict[str, Any] | None = None
    percentage_charge: int | float | None = None
    settlement_bank: str
    bank_id: int | None = None
    account_number: str
    currency: Currency
    active: int | bool | None = None
    is_verified: bool | None = None
    integration: int | None = None
    bank: int | None = None
    managed_by_integration: int | None = None
    domain: Domain | None = None
    migrate: bool | None = None
    account_name: str | None = None
    product: str | None = None


class Product(BaseModel):
    id: int
    name: str
    description: str | None = None
    product_code: str
    slug: str
    currency: Currency
    price: int
    quantity: int
    quantity_sold: int | None = None
    active: bool
    domain: Domain
    type: str
    in_stock: bool
    unlimited: bool
    metadata: dict[str, Any]
    files: list[Any] | None = None  # TODO: Find all the type of files
    file_path: str | None = None
    success_message: str | None = None
    redirect_url: str | None = None
    split_code: str | None = None
    notifications_emails: list[Any] | None = None
    minimum_orderable: int
    maximum_orderable: int | None = None
    created_at: datetime
    updated_at: datetime
    features: Any | None = None
    digital_assets: list[Any] | None = None  # TODO: Find the type of digital_assets
    variant_options: list[Any] | None = None  # TODO: Find the type of variant_options
    is_shippable: bool
    shipping_fields: dict[str, Any]
    integration: int
    low_stock_alert: int | bool
    stock_threshold: Any | None = None
    expires_in: Any | None = None


class Terminal(BaseModel):
    id: int
    serial_number: str | None = None
    device_make: str | None = None
    terminal_id: str
    integration: int
    domain: Domain
    name: str
    address: str | None = None
    status: str | None = None  # TODO: Find all the supported status


class TerminalEventData(BaseModel):
    id: str


class TerminalEventStatusData(BaseModel):
    delivered: bool


class TerminalStatusData(BaseModel):
    online: bool
    available: bool


class DedicatedAccountBank(BaseModel):
    name: str
    id: int
    slug: str


class DedicatedAccountAssignment(BaseModel):
    integration: int
    assignee_id: int
    assignee_type: str
    expired: bool
    account_type: str
    assigned_at: str


class DedicatedAccount(BaseModel):
    bank: DedicatedAccountBank
    account_name: str
    account_number: str
    assigned: bool
    currency: Currency
    metadata: dict[str, Any]
    active: bool
    id: int
    created_at: datetime
    updated_at: datetime
    assignment: DedicatedAccountAssignment
    # customer: Customer
    split_config: dict[str, Any]


class DedicatedAccountProvider(BaseModel):
    provider_slug: str
    bank_id: int
    bank_name: str
    id: int


class Settlement(BaseModel):
    id: int
    domain: Domain
    status: str  # TODO: Find all the supported status for settlement
    currency: Currency
    integration: int
    total_amount: int
    effective_amount: int
    total_fees: int
    total_processed: int
    deductions: Any | None = None
    settlement_date: datetime
    settled_by: Any | None = None
    created_at: datetime
    update_at: datetime


class TransferRecipientDetail(BaseModel):
    authorization_code: str | None = None
    account_name: str | None = None
    bank_code: str
    bank_name: str


class TransferRecipient(BaseModel):
    active: bool
    created_at: datetime
    currency: Currency
    description: str | None = None
    domain: Domain
    email: str | None = None
    id: int
    integration: int
    metadata: dict[str, Any] | None = None
    name: str
    recipient_code: str
    type: str  # TODO: Find out all the supported types
    updated_at: datetime
    is_deleted: bool
    recipient_account: str | None = None
    institution_code: str | None = None
    details: TransferRecipientDetail


class TransferRecipientBulkCreateData(BaseModel):
    success: list[TransferRecipient]
    errors: list[Any]


class TransferSession(BaseModel):
    provider: Any | None = None
    id: Any | None = None


class Transfer(BaseModel):
    integration: int
    domain: Domain
    amount: int
    currency: Currency
    source: str
    source_details: Any | None = None
    failures: Any | None = None
    titian_code: Any | None = None
    transferred_at: str | None = None
    reference: str | None = None
    request: int | None = None
    reason: str
    recipient: int | TransferRecipient
    status: str  # TODO: Find all the supported status for transfer
    transfer_code: str
    id: int
    created_at: datetime
    updated_at: datetime
    session: TransferSession
    fee_charged: int | None = None
    fees_breakdown: Any | None = None
    gateway_response: Any | None = None


class BulkTransferItem(BaseModel):
    reference: str
    recipient: str
    amount: int
    transfer_code: str
    currency: Currency
    status: str  # TODO: Find all the supported status for transfer


class BalanceLedgerItem(BaseModel):
    integration: int
    domain: Domain
    balance: int
    currency: Currency
    difference: int
    reason: str
    model_responsible: str
    model_row: int
    id: int
    created_at: datetime
    update_at: datetime


class DisputeHistory(BaseModel):
    status: DisputeStatus
    by: str
    created_at: datetime


class DisputeMessage(BaseModel):
    sender: str
    body: str
    created_at: datetime


class Dispute(BaseModel):
    id: int
    refund_amount: int | None = None
    currency: Currency | None = None
    status: DisputeStatus
    resolution: Any | None = None
    domain: Domain
    transaction: Transaction
    transaction_reference: str | None = None
    category: Any | None = None
    customer: Customer
    bin: str | None = None
    last4: str | None = None
    due_at: str | None = None
    resolved_at: str | None = None
    evidence: Any | None = None
    attachments: Any
    note: Any | None = None
    history: list[DisputeHistory]
    messages: list[DisputeMessage]
    created_at: datetime
    updated_at: datetime


class DisputeEvidence(BaseModel):
    customer_email: str
    customer_name: str
    customer_phone: str
    service_details: str
    delivery_address: str
    dispute: int
    id: int
    created_at: datetime
    updated_at: datetime


class DisputeUploadInfo(BaseModel):
    signed_url: str
    file_name: str


class DisputeExportInfo(BaseModel):
    path: str
    expires_at: datetime


class Refund(BaseModel):
    integration: int
    transaction: Union[int, "Transaction"]
    dispute: Any | None = None
    settlement: Any | None = None
    id: int
    domain: Domain
    currency: Currency
    amount: int
    status: str  # TODO: Find all the status types
    refunded_at: datetime | None = None
    refunded_by: str
    customer_note: str
    merchant_note: str
    deducted_amount: int
    fully_deducted: int | bool
    created_at: datetime
    bank_reference: Any | None = None
    transaction_reference: str | None = None
    reason: str | None = None
    customer: Customer | None = None
    refund_type: str | None = None
    transaction_amount: int | None = None
    initiated_by: str | None = None
    refund_channel: str | None = None
    session_id: Any | None = None
    collect_account_number: bool | None = None


class CardBin(BaseModel):
    bin: str
    brand: str
    sub_brand: str
    country_code: Country
    country_name: str
    card_type: str
    bank: str
    linked_bank_id: int


class Bank(BaseModel):
    name: str
    slug: str
    code: str
    longcode: str
    gateway: str | None = None
    pay_with_bank: bool
    supports_transfer: bool
    active: bool
    is_deleted: bool
    country: str
    currency: Currency
    type: str
    id: int
    created_at: datetime | None
    updated_at: datetime


class PaystackSupportedCountry(BaseModel):
    id: int
    active_for_dashboard_onboarding: bool
    name: str
    iso_code: str
    default_currency_code: Currency
    integration_defaults: dict[str, Any]
    calling_code: str
    pilot_mode: bool
    relationships: dict[
        SupportedCountryRelationshipType, "SupportedCountryCurrencyRelationship"
    ]
    can_go_live_automatically: bool | None = None


T = TypeVar("T", SupportedCountryRelationshipType, str)
D = TypeVar("D")


class SupportedCountryRelationship(BaseModel, Generic[T, D]):
    type: T
    data: list[D]


class SupportedCountryCurrencyRelationship(BaseModel):
    type: SupportedCountryRelationshipType
    data: list[str]
    supported_currencies: dict[Currency, "SupportedCountryCurrency"] | None = None
    integration_type: dict | None = None
    payment_method: dict | None = None


class SupportedCountryCurrencyMobileMoney(BaseModel):
    bank_type: Literal["mobile_money", "mobile_money_business"]
    phone_number_label: str
    account_number_pattern: "AccountNumberPattern"
    placeholder: str | None = None
    account_verification_required: bool | None = None


class SupportedCountryCurrencyEFT(BaseModel):
    account_number_pattern: "AccountNumberPattern"
    placeholder: str


class SupportedCountryCurrency(BaseModel):
    bank: "SupportedCountryBank"
    mobile_money: SupportedCountryCurrencyMobileMoney | None = None
    mobile_money_business: SupportedCountryCurrencyMobileMoney | None = None
    eft: SupportedCountryCurrencyEFT | None = None


class SupportedCountryBank(BaseModel):
    bank_type: str
    required_fields: list[str] | None = None
    branch_code: str | bool
    branch_code_type: str
    account_name: str | bool
    account_verification_required: bool
    account_number_label: str
    account_number_pattern: "AccountNumberPattern"
    documents: list[str] | None = None
    notices: list[str] | None = None
    show_account_number_tooltip: bool | None = None


class AccountNumberPattern(BaseModel):
    exact_match: bool
    pattern: str
