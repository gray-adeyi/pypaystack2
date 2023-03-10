from dotenv import load_dotenv
import os

load_dotenv()
test_auth_key = os.environ["PAYSTACK_AUTHORIZATION_KEY"]
