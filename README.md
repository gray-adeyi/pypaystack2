# PyPaystack2

A fork of [PyPaystack](https://github.com/edwardpopoola/pypaystack). A simple python wrapper for Paystack API.

This package works as you'd expect pypaystack package to work, except
that all imports are from `pypaystack2` instead of `pypaystack`

e.g

```python
from pypaystack2 import Transaction
```

instead of

```python
from pypaystack import Transaction
```

## Features

- Charge customers
- Verify transactions
- Create Plans
- Get single or multiple transactions
- Get single or multiple customers

## Installation

1. Create your [Paystack account](https://paystack.com/) to get your Authorization key that is required to use this package.
2. Store your authorization key in your environment variable as "PAYSTACK_AUTHORIZATION_KEY" or pass it into the pypaystack objects at initiatialization.
3. Install pypaystack2 package.

```bash
pip install -U pypaystack2
```

## Examples

```python
from pypaystack2 import Transaction, Customer, Plan, Interval

"""
Note
=====
All Response objects are namedtuples containing status_code, status, message and data
e.g
transaction = Transaction(authorization_key="sk_myauthorizationkeyfromthepaystackguys")
response = transaction.charge(email="customer@domain.com", auth_code="CustomerAUTHcode", amount=10000)
print(response.status_code)
print(response.status)
print(respons.data)
"""

#Instantiate the transaction object to handle transactions.  
#Pass in your authorization key - if not set as environment variable PAYSTACK_AUTHORIZATION_KEY

transaction = Transaction(authorization_key="sk_myauthorizationkeyfromthepaystackguys")
response = transaction.charge(email="customer@domain.com", auth_code="CustomerAUTHcode", amount=10000) # Charge a customer N100.
response  = transaction.verify(refcode) # Verify a transaction given a reference code "refcode".


#Instantiate the customer class to manage customers

customer = Customer(authorization_key="sk_myauthorizationkeyfromthepaystackguys")
response = customer.create(email="customer2@gmail.com", first_name="John", last_name="Doe", phone="080123456789") #Add new customer
response = customer.getone("CUS_xxxxyy") # Get customer with customer code of  CUS_xxxxyy
response = customer.getall() # Get all customers


#Instantiate the plan class to manage plans

plan = Plan(authorization_key="sk_myauthorizationkeyfromthepaystackguys")
response = plan.create(name="Test Plan", amount=150000, interval=Interval.WEEKLY) # Add new plan
response = plan.getone(240) # Get plan with id of 240
response = plan.getall() # Get all plans

```
