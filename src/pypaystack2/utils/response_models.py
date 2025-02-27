from datetime import datetime
from typing import Any, Optional, Literal, Generic, TypeVar

from pydantic import BaseModel

from pypaystack2 import DisputeStatus
from pypaystack2.utils.enums import (
    Domain,
    BulkChargeStatus,
    Country,
    Currency,
    RiskAction,
    SupportedCountryRelationshipType,
)
from pypaystack2.utils.models import LineItem, Tax


class ApplePayDomains(BaseModel):
    domain_names: list[str]


class BulkCharge(BaseModel):
    batch_code: str
    reference: str | None
    id: int
    integration: int | None
    domain: Domain
    status: BulkChargeStatus
    total_charges: int | None
    pending_charges: int | None
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
    integration: int
    id: int
    first_name: str
    last_name: str
    email: str
    customer_code: str
    phone: str
    metadata: dict[str, Any]
    risk_action: RiskAction
    international_phone_format: str | None
    identified: bool | None
    identifications: Any | None
    transactions: list["Transaction"] | None
    subscriptions: list["Subscription"] | None
    authorizations: list["Authorization"] | None
    created_at: str | None
    updated_at: str | None
    total_transactions: int | None
    total_transaction_value: list[Any] | None
    dedicated_account: str | None
    dedicated_accounts: list[Any] | None


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
    account_name: str


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
    identifier: Any | None
    entry_point: str = "charge"


class Transaction(BaseModel):
    id: int
    domain: Domain
    status: str
    reference: str
    amount: int
    message: str | None
    gateway_response: str
    paid_at: str
    channel: str
    currency: Currency
    ip_address: str | None
    metadata: dict[str, Any]
    log: TransactionLog | None
    fees: int | None
    fees_split: Any | None
    customer: Customer | dict[str, Any]
    authorization: Authorization | dict[str, Any]
    plan: "Plan" | dict[str, Any]
    split: "TransactionSplit" | dict[str, Any]
    subaccount: "SubAccount" | dict[str, Any]
    order_id: str | None
    created_at: datetime
    requested_amount: int
    source: TransactionSource
    connect: Any | None
    post_transaction_data: Any | None


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
    bearer_subaccount: str | None
    created_at: datetime
    updated_at: datetime
    is_dynamic: bool
    subaccounts: list[TransactionSplitSubAccount]
    total_subaccounts: int


class Subscription(BaseModel):
    customer: int | Customer
    plan: int | "Plan"
    integration: int
    domain: Domain
    start: int
    status: str  # TODO: find all the supported status for subscription
    quantity: int
    amount: int
    subscription_code: str
    email_token: str
    authorization: int | Authorization
    easy_cron_id: str | None
    cron_expression: str
    next_payment_date: datetime | None
    open_invoice: Any | None
    invoice_limit: int
    id: int
    split_code: str | None
    cancelled_at: datetime | None
    updated_at: datetime | None
    payments_count: int
    most_recent_invoice: Optional["Invoice"]
    cancelled_at: datetime | None
    invoices: list["Invoice"]
    invoice_history: list[Any] | None


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
    paid_at: str
    next_notification: str
    notification_flag: Any | None
    description: str | None
    id: int
    created_at: datetime
    update_at: datetime


class PaymentPage(BaseModel):
    integration: str
    plan: int | None
    domain: Domain
    name: str
    description: str | None
    amount: int | None
    currency: Currency
    slug: str
    custom_fields: dict[str, Any] | None  # TODO: find custom_field types
    type: str
    redirect_url: str
    success_message: str | None
    collect_phone: bool
    active: bool
    published: bool
    migrate: bool
    notification_email: str | None
    metadata: dict[str, Any] | None
    split_code: str | None
    id: int
    created_at: datetime
    updated_at: datetime
    products: list["Product"]


class PaymentRequestNotification(BaseModel):
    sent_at: datetime
    channel: str  # TODO: Find all the supported channels for notifcations


class PaymentRequest(BaseModel):
    id: int
    integration: int
    domain: Domain
    amount: int
    currency: Currency
    due_date: datetime | None
    has_invoice: bool | None
    invoice_number: str | None
    description: str | None
    pdf_url: str | None
    line_items: list[LineItem]
    tax: list[Tax]
    request_code: str
    status: str
    paid: bool
    paid_at: datetime | None
    metadata: dict[str, Any]
    notifications: list[PaymentRequestNotification]
    offline_reference: str
    customer: Customer
    created_at: datetime
    discount: str | None
    split_code: str | None
    transactions: list[Transaction] | None
    archived: bool | None
    source: str | None
    payment_method: Any | None
    note: Any | None
    amount_paid: int | None
    updated_at: datetime
    pending_amount: int | None


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
    subscriptions: list[Subscription]
    pages: list[PaymentPage]
    domain: Domain
    name: str
    plan_code: str
    description: str | None
    amount: int
    interval: "Interval"
    invoice_limit: int
    send_invoices: bool
    send_sms: bool
    hosted_page: bool
    hosted_page_url: str | None
    hosted_page_summary: str | None
    currency: Currency
    migrate: bool
    is_deleted: bool
    is_archived: bool
    id: int
    integration: int
    created_at: datetime
    updated_at: datetime
    total_subscriptions: int | None
    active_subscriptions: int | None
    total_subscriptions_revenue: int | None
    pages_count: int | None
    subscribers_count: int | None
    subscriptions_count: int | None
    active_subscriptions_count: int | None
    total_revenue: int | None
    subscribers: list[PlanSubscriber]


class SubAccount(BaseModel):
    id: int
    subaccount_code: str
    business_name: str
    description: str | None
    primary_contact_name: str | None
    primary_contact_email: str | None
    primary_contact_phone: str | None
    metadata: dict[str, Any]
    percentage_charge: int
    settlement_bank: str
    bank_id: int
    account_number: str
    currency: Currency
    active: int | bool
    is_verified: bool
    integration: int | None
    bank: str | None
    managed_by_integration: int | None
    domain: Domain | None
    migrate: bool | None
    account_name: str | None
    product: str | None


class Product(BaseModel):
    id: int
    name: str
    description: str | None
    product_code: str
    slug: str
    currency: Currency
    price: int
    quantity: int
    quantity_sold: int
    active: bool
    domain: Domain
    type: str
    in_stock: bool
    unlimited: bool
    metadata: dict[str, Any]
    files: list[Any]  # TODO: Find all the type of files
    file_path: str | None
    success_message: str | None
    redirect_url: str | None
    split_code: str | None
    notifications_emails: list[Any] | None
    minimum_orderable: int
    maximum_orderable: int
    created_at: datetime
    updated_at: datetime
    features: Any | None
    digital_assets: list[Any]  # TODO: Find the type of digital_assets
    variant_options: list[Any]  # TODO: Find the type of variant_options
    is_shippable: bool
    shipping_fields: dict[str, Any]
    integration: int
    low_stock_alert: int | bool
    stock_threshold: Any | None
    expires_in: Any | None


class Terminal(BaseModel):
    id: int
    serial_number: str | None
    device_make: str | None
    terminal_id: str
    integration: int
    domain: Domain
    name: str
    address: str | None
    status: str | None  # TODO: Find all the supported status


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
    customer: Customer
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
    deductions: Any | None
    settlement_date: datetime
    settled_by: Any | None
    created_at: datetime
    update_at: datetime


class TransferRecipientDetail(BaseModel):
    authorization_code: int | None
    account_name: str
    bank_code: str
    bank_name: str


class TransferRecipient(BaseModel):
    active: bool
    created_at: datetime
    currency: Currency
    description: str | None
    domain: Domain
    email: str | None
    id: int
    integration: int
    metadata: dict[str, Any]
    name: str
    recipient_code: str
    type: str  # TODO: Find out all the supported types
    updated_at: datetime
    is_deleted: bool
    recipient_account: str | None
    institution_code: str | None
    details: TransferRecipientDetail


class TransferSession(BaseModel):
    provider: Any | None
    id: Any | None


class Transfer(BaseModel):
    integration: int
    domain: Domain
    amount: int
    currency: Currency
    source: str
    source_details: Any | None
    failures: Any | None
    titian_code: Any | None
    transferred_at: str | None
    reference: str | None
    request: int | None
    reason: str
    recipient: int | TransferRecipient
    status: str  # TODO: Find all the supported status for transfer
    transfer_code: str
    id: int
    created_at: datetime
    updated_at: datetime
    session: TransferSession
    fee_charged: int | None
    fees_breakdown: Any | None
    gateway_response: Any | None


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
    refund_amount: int | None
    currency: Currency | None
    status: DisputeStatus
    resolution: Any | None
    domain: Domain
    transaction: Transaction
    transaction_reference: str | None
    category: Any | None
    customer: Customer
    bin: str | None
    last4: str | None
    due_at: str | None
    resolved_at: str | None
    evidence: Any | None
    attachments: Any
    note: Any | None
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
    transaction: int
    dispute: Any | None
    settlement: Any | None
    id: int
    domain: Domain
    currency: Currency
    amount: int
    status: str  # TODO: Find all the status types
    refunded_at: datetime | None
    refunded_by: str
    customer_note: str
    merchant_note: str
    deducted_amount: int
    fully_deducted: int | bool
    created_at: datetime
    bank_reference: Any | None
    transaction_reference: str
    reason: str
    customer: Customer
    refund_type: str
    transaction_amount: int
    initiated_by: str
    refund_channel: str
    session_id: Any | None
    collect_account_number: bool


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
    gateway: str | None
    pay_with_bank: bool
    supports_transfer: bool
    active: bool
    is_deleted: bool
    country: str
    currency: Currency
    type: str
    id: int
    created_at: datetime
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
    can_go_live_automatically: bool


T = TypeVar("T", SupportedCountryRelationshipType, str)
D = TypeVar("D")


class SupportedCountryRelationship(BaseModel, Generic[T, D]):
    type: T
    data: list[D]


class SupportedCountryCurrencyRelationship(
    SupportedCountryRelationship[SupportedCountryRelationshipType.CURRENCY, list[str]]
):
    supported_currencies: dict[Currency, "SupportedCountryCurrency"]


class SupportedCountryCurrencyMobileMoney(BaseModel):
    bank: Literal["mobile_money", "mobile_money_business"]
    phone_number_label: str
    account_number_pattern: "AccountNumberPattern"
    placeholder: str | None
    account_verification_required: bool | None


class SupportedCountryCurrencyEFT(BaseModel):
    account_number_pattern: "AccountNumberPattern"
    placeholder: str


class SupportedCountryCurrency(BaseModel):
    bank: "SupportedCountryBank"
    mobile_money: SupportedCountryCurrencyMobileMoney | None
    mobile_money_business: SupportedCountryCurrencyMobileMoney | None
    eft: SupportedCountryCurrencyEFT | None


class SupportedCountryBank(BaseModel):
    bank_type: str
    required_fields: list[str] | None
    branch_code: str
    branch_code_type: str
    account_name: str
    account_verification_required: bool
    account_number_label: str
    account_number_pattern: "AccountNumberPattern"
    documents: list[str]
    notices: list[str] | None
    show_account_number_tooltip: bool | None


class AccountNumberPattern(BaseModel):
    exact_match: bool
    pattern: str
