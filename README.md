# PyPaystack2

[![Downloads](https://static.pepy.tech/badge/pypaystack2)](https://pepy.tech/project/pypaystack2)
[![Downloads](https://static.pepy.tech/badge/pypaystack2/month)](https://pepy.tech/project/pypaystack2)
[![Downloads](https://static.pepy.tech/badge/pypaystack2/week)](https://pepy.tech/project/pypaystack2)

PyPaystack2 is an Open Source Python client library for integrating [Paystack](https://paystack.com/) into your python
projects. It aims at being developer friendly and easy to use.

**Version 3 is here now**

## Features

- 1st class support for type annotations.
- Synchronous and Asynchronous clients.
- Pydantic for data modelling.
- Fees Calculation utilities.
- Webhook support & utilities (>= v3.1.0).

## Installation

```bash
$ pip install -U pypaystack2
# or install with uv
$ uv add pypaystack2
```

## Usage Preview

In the REPL session below, we're using PyPaystack2 to create a `Customer` (user) and a `Plan` on
[Paystack](https://paystack.com/) and then add the newly created customer as a subscriber to the plan.

### Note

The REPL session below assumes the environmental variable `PAYSTACK_SECRET_KEY="YOUR_SECRET_KEY"` is set. if not,
you can alternatively pass it into the `PaystackClient` on instantiation like so
`PaystackClient(secret_key='YOUR_SECRET_KEY')` otherwise, you will get a `MissingSecretKeyException` raised prompting
you to provide a secret key. It also does not handle likely exceptions that calling client methods like
`client.customers.create`, `client.plans.create` & `client.subscriptions.create` may raise like `ClientNetworkError`
for network related issues and `ValueError` for validation related issues.

```bash
Python 3.11.13 (main, Sep  2 2025, 14:20:25) [Clang 20.1.4 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pypaystack2 import __version__
>>> print(__version__)
3.0.0 # Ensure you're running PyPaystack2 version >= 3.0.0 for the following entries to work
>>> from pypaystack2 import PaystackClient
>>> from pypaystack2.enums import Interval
>>> from pypaystack2.models import Customer, Plan
>>> client = PaystackClient()
>>> new_customer_response = client.customers.create(email="johndoe@example.com",first_name="John",last_name="Doe")
>>> assert new_customer_response.status # Validating the request is successful
>>> new_customer = new_customer_response.data
>>> assert isinstance(new_customer,Customer) # Showing that we indeed get an instance of a pydantic model name `Customer` a modelled representation of the data returned by paystack as a result of the request to create a new user
>>> new_plan_response = client.plans.create(name="Test 1k Daily Contributions", amount=client.to_subunit(1000), interval=Interval.DAILY)
>>> assert new_plan_response.status # Validating the request is successful
>>> new_plan = new_plan_response.data # Validating the request is successful
>>> assert isinstance(new_plan,Plan)
>>> new_subscription_response = client.subscriptions.create(customer=new_customer.customer_code,plan=new_plan.plan_code)
>>> assert new_subscription_response.status == True # Validating the request is successful
>>> print(repr(new_subscription_response))
Response(
  status_code=<HTTPStatus.OK: 200>,
  status=True,
  message='Subscription successfully created',
  data=Subscription(
    customer=87934333,
    plan=2237384,...
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
>>> payload = ... # webhook payload e.g.{"event": "customeridentification.success", "data": {"customer_id": 324345768, "customer_code": "CUS_e7urjebaoyk1ze2", "email": "jddae8446e-e54c-42ab-bf37-e5abff14527e@example.com", "identification": {"country": "NG", "type": "bank_account", "bvn": "123*****543", "account_number": "342****22", "bank_code": "121"}}}
>>> signature = ... # x-paystack-signature
>>> is_verified_webhook_payload = client.is_verified_webhook_payload(payload,signature)
>>> print(is_verified_webhook_payload)
True
```

#### Forward webhook events from paystack to your app running locally

```bash
pypaystack2 webhook start-tunnel-server --addr localhost:8000 --ngrok-auth-token
```

## Documentation

See [Documentation](https://gray-adeyi.github.io/pypaystack2/) for more on this package.

## Disclaimer

This project is an Open Source client library for [Paystack](https://paystack.com/). It is not officially endorsed or
affiliated with [Paystack](https://paystack.com/). All trademarks and company names belong to their respective owners.

## Contributions

Thank you for being interested in contributing to PyPaystack2.
There are many ways you can contribute to the project:

- [Star on GitHub](https://github.com/gray-adeyi/pypaystack2/)
- Try PyPaystack2 and [report bugs/issues you find](https://github.com/gray-adeyi/pypaystack2/issues/new)
- [Buy me a coffee](https://www.buymeacoffee.com/jigani)

## Other Related Projects

| Name                                                                               | Language              | Functionality                                                                    |
|------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------------------------------------|
| [Paystack CLI](https://pypi.org/project/paystack-cli/)                             | Python                | A command line app for interacting with paystack APIs                            |
| [paystack](https://github.com/gray-adeyi/paystack)                                 | Go                    | A client library for integration paystack in go                                  |
| [@gray-adeyi/paystack-sdk](https://www.npmjs.com/package/@gray-adeyi/paystack-sdk) | Typescript/Javascript | A client library for integrating paystack in Javascript runtimes (Node,Deno,Bun) |
| [paystack](https://pub.dev/packages/paystack)                                      | Dart                  | A client library for integration paystack in Dart                                |
