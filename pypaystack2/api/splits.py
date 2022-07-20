from typing import Mapping, Optional

from ..baseapi import BaseAPI
from ..utils import (
    Bearer,
    Channel,
    Currency,
    SplitType,
    TransactionStatus,
    add_to_payload,
    prepend_query_params,
    validate_amount,
)
from ..errors import InvalidDataError


class Split(BaseAPI):
    """
    The Transaction Splits API enables merchants split
    the settlement for a transaction across their
    payout account, and one or more Subaccounts.
    """

    def create(
        self,
        name: str,
        type: SplitType,
        currency: Currency,
        subaccounts: list[Mapping],
        bearer_type: Bearer,
        bearer_subaccount: str,
    ):
        """
        Create a split payment on your integration
        """

        url = self._url("/split")
        payload = {
            "name": name,
            "type": type,
            "currency": currency,
            "subaccounts": subaccounts,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount,
        }
        return self._handle_request("POST", url, payload)

    def getall(
        self,
        name: str,
        sort_by: Optional[str],
        page: Optional[int],
        start_date: Optional[str],
        end_date: Optional[str],
        active: bool = True,
        pagination=50,
    ):
        """
        List/search for the transaction splits available on your integration.
        """
        url = self._url(f"/split?perPage={pagination}")
        query_params = [
            ("name", name),
            ("sort_by", sort_by),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("active", active),
        ]
        url = prepend_query_params(query_params)

        return self._handle_request("GET", url)

    def getone(self, id: str):
        """
        Get details of a split on your integration.
        """
        url = self._url(f"/split/{id}/")
        return self._handle_request("GET", url)

    def update(
        self,
        id: str,
        name: str,
        active: bool,
        bearer_type: Optional[Bearer],
        bearer_subaccount: Optional[str],
    ):
        """
        Update a transaction split details on your integration
        """
        if bearer_subaccount:
            if bearer_type != Bearer.SUBACCOUNT:
                raise InvalidDataError(
                    "`bearer_subaccount` can only have a value if `bearer_type` is `Bearer.SUBACCOUNT`"
                )

        payload = {
            "name": name,
            "active": active,
        }
        optional_params = [
            ("bearer_type", bearer_type),
            ("bearer_subaccount", bearer_subaccount),
        ]
        payload = add_to_payload()
        url = self._url(f"/split/{id}/")
        return self._handle_request("PUT", url, payload)

    def add_or_update(self, id: str, subaccount: str, share: int):
        """
        Add a Subaccount to a Transaction Split, or update
        the share of an existing Subaccount in a Transaction Split
        """
        share = validate_amount(share)
        payload = {"subaccount": subaccount, "share": share}
        url = self._url(f"/split/{id}/subaccount/add")
        return self._handle_request("POST", url, payload)

    def remove(self, id: str, subaccount: str):
        """
        Remove a subaccount from a transaction split
        """
        payload = {"subaccount": subaccount}
        url = self._url(f"/split/{id}/subaccount/remove")
        return self._handle_request("POST", url, payload)

    def getall(
        self,
        customer: Optional[int],
        start_date: Optional[str],
        end_date: Optional[str],
        status: Optional[TransactionStatus],
        page: Optional[int],
        amount: Optional[Currency],
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
        url = prepend_query_params(query_params)

        return self._handle_request("GET", url)

    def getone(self, transaction_id: str):
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
        reference: Optional[str],
        currency: Optional[Currency],
        metadata: Optional[str],
        channels: Optional[list[Channel]],
        subaccount: Optional[str],
        transaction_charge: Optional[int],
        bearer: Optional[Bearer],
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
        self, amount: int, email: str, auth_code: str, currency=Optional[Currency]
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
        page=Optional[int],
        start_date=Optional[str],
        end_date=Optional[str],
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
        page=Optional[int],
        start_date=Optional[str],
        end_date=Optional[str],
        customer=Optional[int],
        status=Optional[TransactionStatus],
        currency=Optional[Currency],
        amount=Optional[int],
        settled=Optional[bool],
        settlement=Optional[int],
        payment_page=Optional[int],
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
        url = prepend_query_params(query_params)
        return self._handle_request("GET", url)

    def partial_debit(
        self,
        auth_code: str,
        currency: Currency,
        amount: int,
        email: str,
        reference: Optional[str],
        at_least: Optional[int],
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

    def fetch_transfer_banks(self):
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
        self, recipient_code: str, amount: int, reason: str, reference: Optional[str]
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
