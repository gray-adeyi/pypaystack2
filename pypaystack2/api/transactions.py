from typing import Optional

from ..baseapi import BaseAPI

from ..utils import (
    Bearer,
    Channel,
    Currency,
    TransactionStatus,
    add_to_payload,
    append_query_params,
    validate_amount,
)
from ..errors import InvalidDataError


class Transaction(BaseAPI):
    """
    The Transaction API allows you create and manage
    payments on your integration
    """

    def initialize(
        self,
        amount: int,
        email: str,
        currency: Optional[Currency] = None,
        reference: Optional[str] = None,
        callback_url: Optional[str] = None,
        plan: Optional[str] = None,
        invoice_limit: Optional[int] = None,
        metadata: Optional[str] = None,
        channels: Optional[list[Channel]] = None,
        split_code: Optional[str] = None,
        subaccount: Optional[str] = None,
        transfer_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
    ):
        """
        Initialize a transaction and returns the response

        args:
        email -- Customer's email address
        amount -- Amount to charge
        plan -- optional
        Reference -- optional
        channel -- channel type to use
        metadata -- a list if json data objects/dicts
        """
        amount = validate_amount(amount)

        if not email:
            raise InvalidDataError("Customer's Email is required for initialization")

        url = self._url("/transaction/initialize")
        payload = {
            "email": email,
            "amount": amount,
        }

        optional_params = [
            ("currency", currency),
            ("reference", reference),
            ("callback_url", callback_url),
            ("plan", plan),
            ("invoice_limit", invoice_limit),
            ("metadata", metadata),
            ("channels", channels),
            ("split_code", split_code),
            ("subaccount", subaccount),
            ("transfer_charge", transfer_charge),
            ("bearer", bearer),
        ]
        payload = add_to_payload(optional_params, payload)

        return self._handle_request("POST", url, payload)

    def verify(self, reference: str):
        """
        Verifies a transaction using the provided reference number

        args:
        reference -- reference of the transaction to verify
        """

        reference = str(reference)
        url = self._url(f"/transaction/verify/{reference}")
        return self._handle_request("GET", url)

    def list_transactions(
        self,
        customer: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[TransactionStatus] = None,
        page: Optional[int] = None,
        amount: Optional[Currency] = None,
        pagination=50,
    ):
        """
        List transactions carried out on your integration.
        Gets all your transactions

        args:
        pagination -- Count of data to return per call
        from: start date
        to: end date
        """
        url = self._url(f"/transaction/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("customer", customer),
            ("status", status),
            ("from", start_date),
            ("to", end_date),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)

        return self._handle_request("GET", url)

    def get_transaction(self, transaction_id: str):
        """
        Get details of a transaction carried out on your integration.
        Gets one customer with the given transaction id

        args:
        Transaction_id -- transaction we want to get
        """
        url = self._url(f"/transaction/{transaction_id}/")
        return self._handle_request("GET", url)

    def charge(
        self,
        amount: int,
        email: str,
        auth_code: str,
        reference: Optional[str] = None,
        currency: Optional[Currency] = None,
        metadata: Optional[str] = None,
        channels: Optional[list[Channel]] = None,
        subaccount: Optional[str] = None,
        transaction_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
        queue: bool = False,
    ):
        """
        Charges a customer and returns the response

        args:
        auth_code -- Customer's auth code
        email -- Customer's email address
        amount -- Amount to charge
        reference -- optional
        metadata -- a list if json data objects/dicts
        """
        amount = validate_amount(amount)

        if not email:
            raise InvalidDataError("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataError("Customer's Auth code is required to charge")

        url = self._url("/transaction/charge_authorization")
        payload = {
            "authorization_code": auth_code,
            "email": email,
            "amount": amount,
        }
        optional_params = [
            ("reference", reference),
            ("currency", currency),
            ("metadata", metadata),
            ("channels", channels),
            ("subaccount", subaccount),
            ("transaction_charge", transaction_charge),
            ("bearer", bearer),
            ("queue", queue),
        ]
        payload = add_to_payload(optional_params, payload)

        return self._handle_request("POST", url, payload)

    def check_authorization(
        self,
        amount: int,
        email: str,
        auth_code: str,
        currency: Optional[Currency] = None,
    ):
        """
        Note: This feature is only available to businesses in Nigeria.
        """
        amount = validate_amount(amount)

        if not email:
            raise InvalidDataError("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataError("Customer's Auth code is required to charge")

        url = self._url("/transaction/check_authorization")
        payload = {
            "authorization_code": auth_code,
            "email": email,
            "amount": amount,
        }
        optional_params = [
            ("currency", currency),
        ]
        payload = add_to_payload(optional_params, payload)

        return self._handle_request("POST", url, payload)

    def get_timeline(self, id_or_ref: str):
        """
        View the timeline of a transaction
        """
        url = self._url(f"/transaction/timeline/{id_or_ref}")
        return self._handle_request("GET", url)

    def totals(
        self,
        page: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        pagination=50,
    ):
        """
        Gets transaction totals
        """
        url = self._url(f"/transaction/totals/?perPage={pagination}")
        url = url + f"&page={page}" if page else url
        url = url + f"&from={start_date}" if start_date else url
        url = url + f"&page={end_date}" if end_date else url
        return self._handle_request("GET", url)

    def export(
        self,
        page: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        customer: Optional[int] = None,
        status: Optional[TransactionStatus] = None,
        currency: Optional[Currency] = None,
        amount: Optional[int] = None,
        settled: Optional[bool] = None,
        settlement: Optional[int] = None,
        payment_page: Optional[int] = None,
        pagination=50,
    ):
        """
        Exports a list of transactions
        carried out on your integration.
        """
        if amount:
            amount = validate_amount(amount)
        url = self._url(f"/transaction/export/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("customer", customer),
            ("status", status),
            ("currency", currency),
            ("settled", settled),
            ("settlement", settlement),
            ("payment_page", payment_page),
        ]
        url = append_query_params(query_params)
        return self._handle_request("GET", url)

    def partial_debit(
        self,
        auth_code: str,
        currency: Currency,
        amount: int,
        email: str,
        reference: Optional[str] = None,
        at_least: Optional[int] = None,
    ):
        """
        Charges a customer and returns the response

        args:
        auth_code -- Customer's auth code
        email -- Customer's email address
        amount -- Amount to charge
        reference -- optional
        metadata -- a list if json data objects/dicts
        """
        amount = validate_amount(amount)
        if at_least:
            at_least = validate_amount(at_least)

        if not email:
            raise InvalidDataError("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataError("Customer's Auth code is required to charge")

        url = self._url("/transaction/partial_debit")
        payload = {
            "authorization_code": auth_code,
            "currency": currency,
            "amount": amount,
            "email": email,
        }
        optional_params = [("reference", reference), ("at_least", at_least)]
        payload = add_to_payload(optional_params, payload)

        return self._handle_request("POST", url, payload)

    def get_transfer_banks(self):
        """
        Fetch transfer banks
        """

        url = self._url("/bank")
        return self._handle_request("GET", url)

    def create_transfer_customer(
        self, bank_code: str, account_number: int, account_name: str
    ):
        """
        Create a transfer customer
        """
        url = self._url("/transferrecipient")
        payload = {
            "type": "nuban",
            "currency": "NGN",
            "bank_code": bank_code,
            "account_number": account_number,
            "name": account_name,
        }
        return self._handle_request("POST", url, payload)

    def transfer(
        self,
        recipient_code: str,
        amount: int,
        reason: str,
        reference: Optional[str] = None,
    ):
        """
        Initiates transfer to a customer
        """
        amount = validate_amount(amount)
        url = self._url("/transfer")
        payload = {
            "amount": amount,
            "reason": reason,
            "recipient": recipient_code,
            "source": "balance",
            "currency": "NGN",
        }
        if reference:
            payload.update({"reference": reference})

        return self._handle_request("POST", url, payload)
