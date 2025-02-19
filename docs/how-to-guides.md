## How to use the new Paystack class

In previous versions of `pypaystack2`, it is required to import all the various API
wrappers required to achieve a goal. E.g. say you want to work with the transactions
API wrapper and the customer API wrapper, the code below demonstrates how it's achieved

```python
from pypaystack2.sub_clients import TransactionClient, CustomerClient
```

Besides having to import these different wrappers, you'll also have to instantiate them,
individually. While this kind of import will continue to be supported, I've added
a new `Paystack` class which has all the wrappers bound to it. So now the preferred
way to use `pypaystack2` is demonstrated below

```python
from pypaystack2 import PaystackClient
```

Here's a comparison of how a goal is achieved using the old API and the new API

### Old API

```python
from pypaystack2.sub_clients import PaymentRequestClient, TransactionClient, CustomerClient

invoice_api_wrapper = PaymentRequestClient()  # assumes your PAYSTACK_AUTHORIZATION_KEY is set
invoice_api_response = invoice_api_wrapper.create(customer="CUS_xwaj0txjryg393b",
                                                  amount=1000)  # Creates an invoice with a charge of ₦100
transaction_api_wrapper = TransactionClient()
transaction_api_response = transaction_api_wrapper.get_transactions()
customer_api_wrapper = CustomerClient()
customer_api_response = customer_api_wrapper.get_customers()
```

### New API

```python
from pypaystack2 import PaystackClient

paystack_api = PaystackClient()  # assumes your PAYSTACK_AUTHORIZATION_KEY is set
payment_requests_api_response = paystack_api.payment_requests.create(customer="CUS_xwaj0txjryg393b",
                                                                     amount=1000)  # Creates an invoice with a charge of ₦100
transaction_api_response = paystack_api.transactions.get_transactions()
customer_api_response = paystack_api.transactions.get_transactions()
```

For `async/await`

```python
from pypaystack2 import AsyncPaystackClient

paystack_api = AsyncPaystackClient()  # assumes your PAYSTACK_AUTHORIZATION_KEY is set
payment_requests_api_response = await paystack_api.payment_requests.create(customer="CUS_xwaj0txjryg393b",
                                                                           amount=1000)  # Creates an invoice with a charge of ₦100
transaction_api_response = await paystack_api.transactions.get_transactions()
customer_api_response = await paystack_api.transactions.get_transactions()
```

!!! note

        For the async equivalent to work start your interpreter in async mode with `python -m asyncio`
        You should get a prompt similar to this.
        ```python
        asyncio REPL 3.9.15 (main, May 14 2023, 15:13:34) 
        [GCC 12.2.1 20230201] on linux
        Use "await" directly instead of "asyncio.run()".
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import asyncio
        >>>
        ```

### Bindings on the Paystack object

| API wrapper         | binding name on `Paystack` class |
|---------------------|----------------------------------|
| `ApplePay`          | `apple_pay`                      |
| `BulkCharge`        | `bulk_charges`                   |
| `Charge`            | `charge`                         |
| `Integration`       | `integration`                    |
| `Customer`          | `customer`                       |
| `DedicatedAccount`  | `dedicated_account`              |
| `Dispute`           | `disputes`                       |
| `PaymentRequest`    | `payment_requests`               |
| `Miscellaneous`     | `miscellaneous`                  |
| `Page`              | `payment_pages`                  |
| `Product`           | `products`                       |
| `Refund`            | `refunds`                        |
| `Settlement`        | `settlements`                    |
| `Split`             | `split`                          |
| `SubAccount`        | `subaccount`                     |
| `Subscription`      | `subscriptions`                  |
| `Terminal`          | `terminals`                      |
| `Transaction`       | `transactions`                   |
| `TransferRecipient` | `transfer_recipients`            |
| `Transfer`          | `transfers`                      |
| `TransferControl`   | `transfer_control`               |
| `Verification`      | `verification`                   |

### Bindings on the AsyncPaystack object

| API wrapper              | binding name on `Paystack` class |
|--------------------------|----------------------------------|
| `AsyncApplePay`          | `apple_pay`                      |
| `AsyncBulkCharge`        | `bulk_charges`                   |
| `AsyncCharge`            | `charge`                         |
| `AsyncIntegration`       | `integration`                    |
| `AsyncCustomer`          | `customer`                       |
| `AsyncDedicatedAccount`  | `dedicated_account`              |
| `AsyncDispute`           | `disputes`                       |
| `AsyncPaymentRequest`    | `payment_requests`               |
| `AsyncMiscellaneous`     | `miscellaneous`                  |
| `AsyncPage`              | `payment_pages`                  |
| `AsyncProduct`           | `products`                       |
| `AsyncRefund`            | `refunds`                        |
| `AsyncSettlement`        | `settlements`                    |
| `AsyncSplit`             | `split`                          |
| `AsyncSubAccount`        | `subaccount`                     |
| `AsyncSubscription`      | `subscriptions`                  |
| `AsyncTerminal`          | `terminals`                      |
| `AsyncTransaction`       | `transactions`                   |
| `AsyncTransferRecipient` | `transfer_recipients`            |
| `AsyncTransfer`          | `transfers`                      |
| `AsyncTransferControl`   | `transfer_control`               |
| `AsyncVerification`      | `verification`                   |
