## How to use the new Paystack class

In previous versions of `pypaystack2`, it is required to import all the various API
wrappers required to achieve a goal. e.g. say you want to work with the transactions
API wrapper and the customer API wrapper, the code below demonstrates how it's achieved

```python
from pypaystack2.api import Transaction, Customer
```

Besides having to import these different wrappers, you'll also have to instantiate them
which is just bad. While this kind of import will continue to be supported, I've added
a new `Paystack` class which has all the wrappers bound to it. So now the preferred
way to use `pypaystack2` is demonstrated below

```python
from pypaystack2 import Paystack
# This is all that is required (except cases where enums in the utils are required).
```

Here's a comparison of how a goal is achieved using the old API and the new API

### Old API

```python
from pypaystack2.api import Invoice, Transaction, Customer

invoice_api_wrapper = Invoice()  # assumes your PAYSTACK_AUTHORIZATION_KEY is set
invoice_api_response = invoice_api_wrapper.create(customer="CUS_xwaj0txjryg393b",
                                                  amount=1000)  # Creates an invoice with a charge of ₦100
transaction_api_wrapper = Transaction()
transaction_api_response = transaction_api_wrapper.get_transactions()
customer_api_wrapper = Customer()
customer_api_response = customer_api_wrapper.get_customers()
```

### New API

```python
from pypaystack2 import Paystack

paystack_api = Paystack()  # assumes your PAYSTACK_AUTHORIZATION_KEY is set
invoice_api_response = paystack_api.invoices.create(customer="CUS_xwaj0txjryg393b",
                                                    amount=1000)  # Creates an invoice with a charge of ₦100
transaction_api_response = paystack_api.transactions.get_transactions()
customer_api_response = paystack_api.transactions.get_transactions()
```

### Bindings on the Paystack object

* `Paystack.apple_pay` maps to the `ApplePay` wrapper in `pypaystack2.api.ApplePay`
* `Paystack.bulk_charges` maps to the `BulkCharge` wrapper in `pypaystack2.api.BulkCharge`
* `Paystack.charge` maps to the `Charge` wrapper in `pypaystack2.api.Charge`
* `Paystack.control_panel` maps to the `ControlPanel` wrapper in `pypaystack2.api.ControlPanel`
* `Paystack.customers` maps to the `Customer` wrapper in `pypaystack2.api.Customer`
* `Paystack.dedicated_accounts` maps to the `DedicatedAccount` wrapper in `pypaystack2.api.DedicatedAccount`
* `Paystack.disputes` maps to the `Dispute` wrapper in `pypaystack2.api.Dispute`
* `Paystack.invoices` maps to the `Invoice` wrapper in `pypaystack2.api.Invoice`
* `Paystack.miscellaneous` maps to the `Miscellaneous` wrapper in `pypaystack2.api.Miscellaneous`
* `Paystack.payment_pages` maps to the `Page` wrapper in `pypaystack2.api.Page`
* `Paystack.plans` maps to the `Plan` wrapper in `pypaystack2.api.Plan`
* `Paystack.products` maps to the `Product` wrapper in `pypaystack2.api.Product`
* `Paystack.refunds` maps to the `Refund` wrapper in `pypaystack2.api.Refund`
* `Paystack.settlements` maps to the `Settlement` wrapper in `pypaystack2.api.Settlement`
* `Paystack.splits` maps to the `Split` wrapper in `pypaystack2.api.Split`
* `Paystack.subaccounts` maps to the `SubAccount` wrapper in `pypaystack2.api.SubAccount`
* `Paystack.subscriptions` maps to the `Subscription` wrapper in `pypaystack2.api.Subscription`
* `Paystack.terminals` maps to the `Terminal` wrapper in `pypaystack2.api.Terminal`
* `Paystack.transactions` maps to the `Transaction` wrapper in `pypaystack2.api.Transactions`
* `Paystack.transfer_recipients` maps to the `TransferRecipient` wrapper in `pypaystack2.api.TransferRecipient`
* `Paystack.transfer` maps to the `Transfer` wrapper in `pypaystack2.api.Transfer`
* `Paystack.tranfer_control` maps to the `TransferControl` wrapper in `pypaystack2.api.TransferControl`
* `Paystack.verificaton` maps to the `Verification` wrapper in `pypaystack2.api.Verification`