from unittest import TestCase
from pypaystack2 import Transaction, Plan, Customer, Currency, Interval
from uuid import uuid4
from dotenv import load_dotenv
import os

load_dotenv()
test_auth_key = os.environ["PAYSTACK_AUTHORIZATION_KEY"]
