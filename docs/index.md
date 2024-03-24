![PyPaystack2 logo](assets/pypaystack2.svg)
<center>**A developer friendly wrapper for Paystack API**</center>
<hr/>
Documentation: [https://github.com/gray-adeyi/pypaystack2](https://github.com/gray-adeyi/pypaystack2)

Source Code: [https://gray-adeyi.github.io/pypaystack2/](https://gray-adeyi.github.io/pypaystack2/)
<hr/>
PyPaystack2 is a python wrapper over the [Paystack API](https://paystack.com/docs/api). It aims at being 
developer friendly and easy to use.

The key features are:

* **Type hints**: All methods provided by PyPaystack2 are type annotated, so you can easily infer. This improves the
  development experience.
* **Async support**: PyPaystack2 allow you to also make calls to Paystack API using `async/await` which is super great,
  for example, if your project is in [FastAPI](https://fastapi.tiangolo.com/) where every chance of a performance
  improvement adds up.

## Requirements

Python 3.9+

PyPaystack2 now uses [httpx](https://www.python-httpx.org/) under the hood to make API calls to Paystack. Compared
to previous version `1.1.3` and down which use `requests`. This switch has made it possible to support `async/await`
based wrappers.

## Installation

```bash
$ pip install pypaystack2
```

## Example

```bash
Python 3.9.15 (main, Dec 12 2022, 21:54:43) 
[GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pypaystack2 import Paystack
>>> paystack = Paystack() # assumes the environmental variable `PAYSTACK_AUTHORIZATION_KEY=paystack integration secret key` is set. if not, you can alternatively pass it into the `Paystack` instantiation like so Paystack(auth_key='paystack integration secret key')
>>> response = paystack.customers.get_customer(email_or_code="CUS_8x2byd6x3dk5hp0")
>>> print(response)
Response(status_code=200, status=True, message='Customer retrieved', data={'transactions': [], 'subscriptions': [], 'authorizations': [{'authorization_code': 'AUTH_ohnpjcd7z9', 'bin': '408408', 'last4': '4081', 'exp_month': '12', 'exp_year': '2030', 'channel': 'card', 'card_type': 'visa ', 'bank': 'TEST BANK', 'country_code': 'NG', 'brand': 'visa', 'reusable': True, 'signature': 'SIG_JOdryeujwrsZryg0Lkrg', 'account_name': None}], 'first_name': 'john', 'last_name': 'doe', 'email': 'johndoe@example.com', 'phone': None, 'metadata': None, 'domain': 'test', 'customer_code': 'CUS_8x2byd6x3dk5hp0', 'risk_action': 'default', 'id': 87934333, 'integration': 630606, 'createdAt': '2022-07-25T03:46:01.000Z', 'updatedAt': '2022-07-25T03:46:01.000Z', 'created_at': '2022-07-25T03:46:01.000Z', 'updated_at': '2022-07-25T03:46:01.000Z', 'total_transactions': 0, 'total_transaction_value': [], 'dedicated_account': None, 'identified': False, 'identifications': None})
>>> print(response.status_code)
200
>>> print(response.message)
Customer retrieved
>>> 

```

All you need to interact with Paystack's API in your python project is the `Paystack class` it
has [attributes](how-to-guides.md#bindings-on-the-paystack-object)
bounded to it that provides methods you can call in your code to make API calls to Paystack. Every method call on the
wrapper
has the same return type, which is a [Response](reference/index.md#pypaystack2.utils.Response). A namedtuple containing
the data from making the actual call to Paystack servers

## Async Now!

PyPaystack2 now supports asynchronous wrappers to Paystack's API. `AsyncPaystack` is an asynchronous mirror equivalent
of the `Paystack` wrapper. i.e. `AsyncPaystack` provides the same functionality as the `Paystack` wrapper but is more
useful in the context of `async\await` code. All the bindings on the `AsyncPaystack` are the same as on the `Paystack`
wrapper except that the methods on the `AsyncPaystack` are `awaitable`

```bash
asyncio REPL 3.9.15 (main, Dec 12 2022, 21:54:43) 
[GCC 12.2.0] on linux
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> from pypaystack2 import AsyncPaystack
>>> paystack = AsyncPaystack() # assumes the environmental variable `PAYSTACK_AUTHORIZATION_KEY=paystack integration secret key` is set. if not, you can alternatively pass it into the `AsyncPaystack` instantiation like so AsyncPaystack(auth_key='paystack integration secret key')
>>> response = await paystack.customers.get_customer(email_or_code="CUS_8x2byd6x3dk5hp0")
>>> print(response)
Response(status_code=200, status=True, message='Customer retrieved', data={'transactions': [], 'subscriptions': [], 'authorizations': [{'authorization_code': 'AUTH_ohnpjcd7z9', 'bin': '408408', 'last4': '4081', 'exp_month': '12', 'exp_year': '2030', 'channel': 'card', 'card_type': 'visa ', 'bank': 'TEST BANK', 'country_code': 'NG', 'brand': 'visa', 'reusable': True, 'signature': 'SIG_JOdryeujwrsZryg0Lkrg', 'account_name': None}], 'first_name': 'john', 'last_name': 'doe', 'email': 'johndoe@example.com', 'phone': None, 'metadata': None, 'domain': 'test', 'customer_code': 'CUS_8x2byd6x3dk5hp0', 'risk_action': 'default', 'id': 87934333, 'integration': 630606, 'createdAt': '2022-07-25T03:46:01.000Z', 'updatedAt': '2022-07-25T03:46:01.000Z', 'created_at': '2022-07-25T03:46:01.000Z', 'updated_at': '2022-07-25T03:46:01.000Z', 'total_transactions': 0, 'total_transaction_value': [], 'dedicated_account': None, 'identified': False, 'identifications': None})
>>> print(response.status_code)
200
>>> print(response.message)
Customer retrieved
>>> 

```

## License

This project is licensed under the terms of the MIT license.

## Contributors

- [gray-adeyi](https://github.com/gray-adeyi)

## Buy me a coffee

[https://www.buymeacoffee.com/jigani](https://www.buymeacoffee.com/jigani)