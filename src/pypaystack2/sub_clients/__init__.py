"""A package containing several wrappers for interfacing Paystack API, like apple pay sub_clients, bulk charges sub_clients e.t.c.
Modules exported by this package:
    - `apple_pay`: A module containing implementations for interfacing with Paystack's Apple Pay API
    - `bulk_charges`: A module containing implementations for interfacing with Paystack's Bulk Charges API
    - `charge`: A module containing implementations for interfacing with Paystack's Charge API
    - `control_panel`: A module containing implementations for interfacing with Paystack's Control Panel API
    - `customer`: A module containing implementations for interfacing with Paystack's Customer API
    - `dedicated_accounts`: A module containing implementations for interfacing with Paystack's Dedicated Accounts API
    - `disputes`: A module containing implementations for interfacing with Paystack's Disputes API
    - `invoices`: A module containing implementations for interfacing with Paystack's Invoices API
    - `miscellaneous`: A module containing implementations for interfacing with Paystack's Miscellaneous API
    - `payment_pages`: A module containing implementations for interfacing with Paystack's Payment Page API
    - `plans`: A module containing implementations for interfacing with Paystack's Plans API
    - `products`: A module containing implementations for interfacing with Paystack's Products API
    - `refunds`: A module containing implementations for interfacing with Paystack's Refunds API
    - `settlements`: A module containing implementations for interfacing with Paystack's Settlements API
    - `splits`: A module containing implementations for interfacing with Paystack's Splits API
    - `subaccounts`: A module containing implementations for interfacing with Paystack's Sub Account API
    - `subscriptions`: A module containing implementations for interfacing with Paystack's Subscriptions API
    - `transactions`: A module containing implementations for interfacing with Paystack's Transactions API
    - `transfer_recipients`: A module containing implementations for interfacing with Paystack's Transfer Recipients API
    - `transfers`: A module containing implementations for interfacing with Paystack's Transfers API
    - `transfers_control`: A module containing implementations for interfacing with Paystack's Transfers Control API
    - `verification`: A module containing implementations for interfacing with Paystack's Verification API
"""

from pypaystack2.sub_clients.subscriptions import SubscriptionClient

# ruff: noqa: F401
from pypaystack2.sub_clients.sync_clients.apple_pay import ApplePayClient
from pypaystack2.sub_clients.sync_clients.bulk_charges import BulkChargeClient
from pypaystack2.sub_clients.sync_clients.charge import ChargeClient
from pypaystack2.sub_clients.sync_clients.customers import CustomerClient
from pypaystack2.sub_clients.sync_clients.dedicated_accounts import (
    DedicatedAccountClient,
)
from pypaystack2.sub_clients.sync_clients.disputes import DisputeClient
from pypaystack2.sub_clients.sync_clients.integration import IntegrationClient
from pypaystack2.sub_clients.sync_clients.miscellaneous import MiscellaneousClient
from pypaystack2.sub_clients.sync_clients.payment_pages import PaymentPageClient
from pypaystack2.sub_clients.sync_clients.payment_requests import PaymentRequestClient
from pypaystack2.sub_clients.sync_clients.plans import PlanClient
from pypaystack2.sub_clients.sync_clients.products import ProductClient
from pypaystack2.sub_clients.sync_clients.refunds import RefundClient
from pypaystack2.sub_clients.sync_clients.settlements import SettlementClient
from pypaystack2.sub_clients.sync_clients.splits import TransactionSplitClient
from pypaystack2.sub_clients.sync_clients.subaccounts import SubAccountClient
from pypaystack2.sub_clients.terminals import TerminalClient
from pypaystack2.sub_clients.transactions import TransactionClient
from pypaystack2.sub_clients.transfers import TransferClient
from pypaystack2.sub_clients.transfers_control import TransferControlClient
from pypaystack2.sub_clients.verification import VerificationClient
