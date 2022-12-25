"""A package containing several wrappers for interfacing Paystack API, like apple pay api, bulk charges api e.t.c.
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
from .apple_pay import ApplePay
from .bulk_charges import BulkCharge
from .charge import Charge
from .control_panel import ControlPanel
from .customers import Customer
from .dedicated_accounts import DedicatedAccount
from .disputes import Dispute
from .invoices import Invoice
from .miscellaneous import Miscellaneous
from .payment_pages import Page
from .plans import Plan
from .products import Product
from .refunds import Refund
from .settlements import Settlement
from .splits import Split
from .subaccounts import SubAccount
from .subscriptions import Subscription
from .transactions import Transaction
from .transfer_recipients import TransferRecipient
from .transfers_control import TransferControl
from .transfers import Transfer
from .verification import Verification
