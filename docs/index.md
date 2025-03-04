![PyPaystack2 logo](assets/pypaystack2.svg)
<center>**A developer friendly wrapper for Paystack API**</center>
<hr/>
Documentation: [https://github.com/gray-adeyi/pypaystack2](https://gray-adeyi.github.io/pypaystack2/)

Source Code: [https://gray-adeyi.github.io/pypaystack2/](https://github.com/gray-adeyi/pypaystack2)
<hr/>
PyPaystack2 is an Open Source Python client library for integrating [Paystack](https://paystack.com/) into your python
projects. It aims at being developer friendly and easy to use.

The key features are:

* **Type hints**: All methods provided by PyPaystack2 are type annotated, so you can infer. This improves the
  development experience.
* **Async support**: PyPaystack2 allow you to also make calls to Paystack API using `async/await` which is super great,
  for example, if your project is in [FastAPI](https://fastapi.tiangolo.com/) where every chance of a performance
  improvement adds up.
* **Pydantic**: PyPaystack2 now uses pydantic for data presentation. client methods return `Response` which is
  a pydantic model, the data in the response are also presented with pydantic e.g.  `Response[Transaction]` is
  an example of a response that may be returned by client method. This can be interpreted as the response contains
  a transaction resource as the data. i.e. `Response.data` is `Transaction` which is also a pydantic model
* **Fees Calculation utilities**:

## Requirements

Paypaystack2 `<=3.0.0` requires a minimum Python version of `>=3.11`. For python `<3.11` See older versions of
this project

## Installation

```bash
$ pip install pypaystack2
# or with uv
$ uv add pypaystack2
```

## Examples

### Usage in a synchronous context

```bash
Python 3.9.15 (main, Dec 12 2022, 21:54:43) 
[GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pypaystack2 import PaystackClient
>>> client = PaystackClient() # assumes the environmental variable `PAYSTACK_AUTHORIZATION_KEY=paystack integration secret key` is set. if not, you can alternatively pass it into the `Paystack` instantiation like so Paystack(auth_key='paystack integration secret key')
>>> response = client.customers.get_customer(email_or_code="CUS_8x2byd6x3dk5hp0")
>>> print(response)
Response(status_code=200, status=True, message='Customer retrieved', data={'transactions': [], 'subscriptions': [], 'authorizations': [{'authorization_code': 'AUTH_ohnpjcd7z9', 'bin': '408408', 'last4': '4081', 'exp_month': '12', 'exp_year': '2030', 'channel': 'card', 'card_type': 'visa ', 'bank': 'TEST BANK', 'country_code': 'NG', 'brand': 'visa', 'reusable': True, 'signature': 'SIG_JOdryeujwrsZryg0Lkrg', 'account_name': None}], 'first_name': 'john', 'last_name': 'doe', 'email': 'johndoe@example.com', 'phone': None, 'metadata': None, 'domain': 'test', 'customer_code': 'CUS_8x2byd6x3dk5hp0', 'risk_action': 'default', 'id': 87934333, 'integration': 630606, 'createdAt': '2022-07-25T03:46:01.000Z', 'updatedAt': '2022-07-25T03:46:01.000Z', 'created_at': '2022-07-25T03:46:01.000Z', 'updated_at': '2022-07-25T03:46:01.000Z', 'total_transactions': 0, 'total_transaction_value': [], 'dedicated_account': None, 'identified': False, 'identifications': None})
>>> print(response.status_code)
200
>>> print(response.message)
Customer retrieved
>>> print(response.data)
>>> print(response.raw)

```

All you need to interact with Paystack's API in your python project is the `Paystack class` it
has [attributes](how-to-guides.md#bindings-on-the-paystack-object)
bounded to it that provides methods you can call in your code to make API calls to Paystack. Every method call on the
wrapper
has the same return type, which is a [Response](reference/index.md#pypaystack2.utils.Response). A namedtuple containing
the data from making the actual call to Paystack servers

### Usage in an asynchronous context

`AsyncPaystackClient` is an asynchronous mirror equivalent of the `PaystackClient` client. i.e. `AsyncPaystackClient`
provides the same functionality as `PaystackClient` but is more useful in the context of non-blocking `async\await`
code. All the bindings on the `AsyncPaystackClient` are the same as ones in `PaystackClient`
except that the methods on the `AsyncPaystack` are `awaitable`

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

## Related Projects

| Name                                                                               | Language              | Functionality                                                                    |
|------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------------------------------------|
| [Paystack CLI](https://pypi.org/project/paystack-cli/)                             | Python                | A command line app for interacting with paystack API's                           |
| [paystack](https://github.com/gray-adeyi/paystack)                                 | Go                    | A client library for integration paystack in go                                  |
| [@gray-adeyi/paystack-sdk](https://www.npmjs.com/package/@gray-adeyi/paystack-sdk) | Typescript/Javascript | A client library for integrating paystack in Javascript runtimes (Node,Deno,Bun) |
| [paystack](https://pub.dev/packages/paystack)                                      | Dart                  | A client library for integration paystack in Dart                                | 

## Buy me a coffee

[https://www.buymeacoffee.com/jigani](https://www.buymeacoffee.com/jigani)