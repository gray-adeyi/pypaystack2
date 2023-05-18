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

from pypaystack2.api.apple_pay import ApplePay
from pypaystack2.api.bulk_charges import BulkCharge
from pypaystack2.api.charge import Charge
from pypaystack2.api.integration import Integration
from pypaystack2.api.customers import Customer
from pypaystack2.api.dedicated_accounts import DedicatedAccount
from pypaystack2.api.disputes import Dispute
from pypaystack2.api.payment_requests import PaymentRequest
from pypaystack2.api.miscellaneous import Miscellaneous
from pypaystack2.api.payment_pages import PaymentPage
from pypaystack2.api.plans import Plan
from pypaystack2.api.products import Product
from pypaystack2.api.refunds import Refund
from pypaystack2.api.settlements import Settlement
from pypaystack2.api.splits import TransactionSplit
from pypaystack2.api.subaccounts import SubAccount
from pypaystack2.api.subscriptions import Subscription
from pypaystack2.api.terminals import Terminal
from pypaystack2.api.transactions import Transaction
from pypaystack2.api.transfer_recipients import RecipientType
from pypaystack2.api.transfers import Transfer
from pypaystack2.api.transfers_control import TransferControl
from pypaystack2.api.verification import Verification

# prevent removal of unused import
ApplePay
BulkCharge
Charge
Integration
Customer
DedicatedAccount
Dispute
PaymentRequest
Miscellaneous
PaymentPage
Plan
Product
Refund
Settlement
TransactionSplit
SubAccount
Subscription
Terminal
Transaction
RecipientType
Transfer
TransferControl
Verification
