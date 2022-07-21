from unittest import TestCase
from pypaystack2.api import Transaction, Plan, Customer
from uuid import uuid4
from dotenv import load_dotenv
import os

load_dotenv()
test_auth_key = os.environ["PAYSTACK_AUTHORIZATION_KEY"]
