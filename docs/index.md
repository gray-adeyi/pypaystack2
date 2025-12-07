![PyPaystack2 logo](assets/pypaystack2.svg)
<center>A developer friendly client library for Paystack</center>
<hr/>

Documentation: [https://gray-adeyi.github.io/pypaystack2/](https://gray-adeyi.github.io/pypaystack2/)

Source Code: [https://github.com/gray-adeyi/pypaystack2](https://github.com/gray-adeyi/pypaystack2)
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
* **Fees Calculation utilities**: PyPaystack2 provides utilities for calculating paystack's transaction fees and
  converting between base units and subunits of a currency
* **Webhook support & utilities**: From PyPaystack2 (>= v3.1.0), you can verify webhook payloads and also run
  a tunnel server that forwards webhook events from paystack to your app running on localhost

## Requirements

Paypaystack2 `<=3.0.0` requires a minimum Python version of `>=3.11`. For python `<3.11` See older versions of
this project

## Installation

```bash
$ pip install -U pypaystack2
# or install with uv
$ uv add pypaystack2
# For webhook cli
$ pip install -U "pypaystack2[webhook]"
or install with uv
$ uv add "pypaystack2[webhook"
```

## Examples

### Usage in a synchronous context

```bash
Python 3.11.11 (main, Feb 12 2025, 14:51:05) [Clang 19.1.6 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pypaystack2 import PaystackClient
>>> client = PaystackClient() # assumes the environmental variable `PAYSTACK_SECRET_KEY="YOUR_PAYSTACK_SECRET_KEY"` is set. if not, you can alternatively pass it into the `PaystackClient` instantiation like so PaystackClient(secret_key='YOUR_PAYSTACK_SECRET_KEY')
>>> response = client.customers.get_customer(email_or_code="CUS_8x2byd6x3dk5hp0")
>>> print(response)
Response(
  status_code=<HTTPStatus.OK: 200>,
  status=True,
  message='Customer retrieved',
  data=Customer(
    integration=630606,
    id=87934333,
    first_name='john',...
```

All you need to interact with Paystack's API in your python project is the `PaystackClient` class it provides bindings
to different sub clients that provide methods that let you interact with paystack. The `PaystackClient` class also
provides fees calculation utility methods like `to_subunit`, `to_base_unit` and `calculate_fee`.
Every method call on the sub client bindings that makes an HTTP Request to paystack has the same generic return type
, which is a [Response](reference/index.md#pypaystack2.models.Response) a pydantic model representing the result of the
request. The content of the data attribute may vary based on the request that was made.

### Usage in an asynchronous context

`AsyncPaystackClient` is an asynchronous mirror equivalent of the `PaystackClient` client. i.e. `AsyncPaystackClient`
provides the same functionality as `PaystackClient` but is more useful in the context of non-blocking `async\await`
code. All the bindings on the `AsyncPaystackClient` are the same as ones in `PaystackClient`
except that the methods on the `AsyncPaystackClient` are `awaitable`. Run the async REPL with `python -m asyncio`

```bash
asyncio REPL 3.11.11 (main, Feb 12 2025, 14:51:05) [Clang 19.1.6 ] on linux
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> from pypaystack2 import AsyncPaystackClient
>>> paystack = AsyncPaystackClient() # assumes the environmental variable `PAYSTACK_SECRET_KEY="YOUR_SECRET_KEY"` is set. if not, you can alternatively pass it into the `AsyncPaystackClient` instantiation like so AsyncPaystackClient(secret_key='YOUR_SECRET_KEYS')
>>> response = await paystack.customers.get_customer(email_or_code="CUS_8x2byd6x3dk5hp0")
>>> print(response)
Response(
  status_code=<HTTPStatus.OK: 200>,
  status=True,
  message='Customer retrieved',
  data=Customer(
    integration=630606,
    id=87934333,
    first_name='john',...
```

### Webhook

PyPaystack2 now supports verifying the authenticity of a webhook payload and a CLI to make working with webhooks locally
seamless

#### Verifying a webhook payload

```bash
Python 3.11.13 (main, Sep  2 2025, 14:20:25) [Clang 20.1.4 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pypaystack2 import PaystackClient
>>> client = PaystackClient()
>>> payload = ... # webhook payload e.g., b'{"event": "customeridentification.success", "data": {"customer_id": 324345768, "customer_code": "CUS_e7urjebaoyk1ze2", "email": "jddae8446e-e54c-42ab-bf37-e5abff14527e@example.com", "identification": {"country": "NG", "type": "bank_account", "bvn": "123*****543", "account_number": "342****22", "bank_code": "121"}}}'
>>> signature = ... # x-paystack-signature e.g., "5d049eb93c7c71fa098f5215d7297bda401710b62df8b392b9052adf8d1a02ff308f6ca57a1db14ffeabd5b66264e9c42de029b7067b9c71eb9c231fb2a8e383"
>>> is_verified_webhook_payload = client.is_verified_webhook_payload(payload,signature)
>>> print(is_verified_webhook_payload)
True
```

#### Forward webhook events from paystack to your app running locally

**Note:** This requires that you install `pypaystack2[webhook]`

```bash
pypaystack2 webhook start-tunnel-server --addr localhost:8000 --ngrok-auth-token
```

## License

This project is licensed under the terms of the MIT license.

## Contributors

- [gray-adeyi](https://github.com/gray-adeyi)

## Related Projects

| Name                                                                               | Language              | Functionality                                                                    |
|------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------------------------------------|
| [Paystack CLI](https://pypi.org/project/paystack-cli/)                             | Python                | A command line app for interacting with paystack APIs                            |
| [paystack](https://github.com/gray-adeyi/paystack)                                 | Go                    | A client library for integration paystack in go                                  |
| [@gray-adeyi/paystack-sdk](https://www.npmjs.com/package/@gray-adeyi/paystack-sdk) | Typescript/Javascript | A client library for integrating paystack in Javascript runtimes (Node,Deno,Bun) |
| [paystack](https://pub.dev/packages/paystack)                                      | Dart                  | A client library for integration paystack in Dart                                |

## Buy me a coffee

[https://www.buymeacoffee.com/jigani](https://www.buymeacoffee.com/jigani)
