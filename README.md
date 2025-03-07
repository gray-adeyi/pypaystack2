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
Python 3.11.11 (main, Feb 12 2025, 14:51:05) [Clang 19.1.6 ] on linux
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
    plan=2237384,
    integration=630606,
    domain=<Domain.TEST: 'test'>,
    start=1741208073,
    status='active',
    quantity=1,
    amount=100000,
    subscription_code='SUB_4sje2s7kb30m5bt',
    email_token='uqzg0vneparuxtm',
    authorization=368220905,
    easy_cron_id=None,
    cron_expression='54 20 5 3 *',
    next_payment_date=datetime.datetime(2026, 3, 5, 20, 54, tzinfo=TzInfo(UTC)),
    open_invoice=None,
    invoice_limit=0,
    id=759264,
    split_code=None,
    cancelled_at=None,
    updated_at=datetime.datetime(2025, 3, 5, 20, 54, 33, tzinfo=TzInfo(UTC)),
    payments_count=None,
    most_recent_invoice=None,
    invoices=None,
    invoice_history=None),
  meta=None,
  type=None,
  code=None,
  raw={
    'status': True,
    'message': 'Subscription successfully created',
    'data': {
      'customer': 87934333,
      'plan': 2237384,
      'integration': 630606,
      'domain': 'test',
      'start': 1741208073,
      'status': 'active',
      'quantity': 1,
      'amount': 100000,
      'authorization': 368220905,
      'invoice_limit': 0,
      'split_code': None,
      'metadata': None,
      'subscription_code': 'SUB_4sje2s7kb30m5bt',
      'email_token': 'uqzg0vneparuxtm',
      'id': 759264,
      'cancelledAt': None,
      'createdAt': '2025-03-05T20:54:33.000Z',
      'updatedAt': '2025-03-05T20:54:33.000Z',
      'cron_expression': '54 20 5 3 *',
      'next_payment_date': '2026-03-05T20:54:00.000Z',
      'easy_cron_id': None,
      'open_invoice': None}
    })
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
