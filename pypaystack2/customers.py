from typing import Optional
from .baseapi import BaseAPI


class Customer(BaseAPI):
    def create(self, email: str, first_name: Optional[str] = None, last_name: Optional[str] = None, phone: Optional[str] = None):
        """
        Creates a new paystack customer account

        args:
        email -- Customer's email address
        first_name-- Customer's first name (Optional)
        last_name-- Customer's last name (Optional)
        phone -- optional
        """
        url = self._url("/customer/")
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
        }
        return self._handle_request("POST", url, payload)

    def update(self, user_id: str, email: str, first_name: Optional[str] = None, last_name: Optional[str] = None, phone: Optional[str] = None):
        """
        Update a customer account given the user id

        args:
        user_id -- id of the customer
        email -- Customer's email address
        first_name-- Customer's first name (Optional)
        last_name-- Customer's last name (Optional)
        phone -- optional
        """
        url = self._url("/customer/{}/".format(user_id))
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
        }
        return self._handle_request("PUT", url, payload)

    def getall(self, pagination: int = 10):
        """
        Gets all the customers we have at paystack in steps of (default) 50 records per page.
        We can provide an optional pagination to indicate how many customer records we want to fetch per time

        args:
        pagination -- Count of data to return per call
        """
        url = self._url("/customer/?perPage=" + str(pagination))
        return self._handle_request("GET", url)

    def getone(self, customer_code: str):
        """
        Gets the customer with the given user id

        args:
        customer_code -- The customer's code
        """
        url = self._url("/customer/{}/".format(customer_code))
        return self._handle_request("GET", url)
