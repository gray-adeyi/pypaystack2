from typing import Any, Optional

from ..baseapi import BaseAPI, Response

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
    """Provides a wrapper for paystack Transactions API

    The Transactions API allows you create and manage payments on your integration.
    https://paystack.com/docs/api/#transaction
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
        metadata: Optional[dict[str, Any]] = None,
        channels: Optional[list[Channel]] = None,
        split_code: Optional[str] = None,
        subaccount: Optional[str] = None,
        transfer_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
    ) -> Response:
        """Initialize a transaction from your backend

        Parameters
        ----------
        amount: int
            Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
            if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
        email: str
            Customer's email address
        currency: Optional[Currency]
            Any value from the ``Currency`` enum.
        reference: Optional[str]
            Unique transaction reference. Only ``-, ., =`` and alphanumeric characters allowed.
        callback_url: Optional[str]
            Fully qualified url, e.g. ``https://example.com/`` . Use this to override the callback url
            provided on the dashboard for this transaction
        plan: Optional[str]
            If transaction is to create a subscription to a predefined plan, provide plan code here.
            This would invalidate the value provided in ``amount``
        invoice_limit: Optional[int]
            Number of times to charge customer during subscription to plan
        metadata: Optional[dict[str,Any]]
            A dictionary of additional info. check out this link
            for more information.
            https://paystack.com/docs/payments/metadata
        channels: Optional[list[Channel]]
            A list of ``Channel`` enum values to control what channels you want to make available
            to the user to make a payment with
        split_code: Optional[str]
            The split code of the transaction split.
            e.g. SPL_98WF13Eb3w
        subaccount: Optional[str]
            The code for the subaccount that owns the payment.
            e.g. ACCT_8f4s1eq7ml6rlzj
        transfer_charge: Optional[int]
            An amount used to override the split configuration for a single split payment. If set,
            the amount specified goes to the main account regardless of the split configuration.
        bearer: Optional[Bearer]
            Any value from the ``Bearer`` enum. Who bears Paystack charges?

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Raises
        ------
        InvalidDataError
            When email is not provided.
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

    def verify(self, reference: str) -> Response:
        """Confirm the status of a transaction

        Parameters
        ----------
        reference: str
            The transaction reference used to intiate the transaction

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        reference = str(reference)
        url = self._url(f"/transaction/verify/{reference}")
        return self._handle_request("GET", url)

    def get_transactions(
        self,
        customer: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[TransactionStatus] = None,
        page: Optional[int] = None,
        amount: Optional[int] = None,
        pagination=50,
    ) -> Response:
        """Fetch transactions carried out on your integration.

        Parameters
        ----------
        customer: Optional[int]
            Specify an ID for the customer whose transactions you want to retrieve
        start_date: Optional[str]
            A timestamp from which to start listing transaction
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing transaction
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        status: Optional[TransactionStatus]
            Filter transactions by status. any value from the
            ``TransactionStatus`` enum
        page: Optional[int]
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        amount: Optional[int]
            Filter transactions by amount. Specify the amount (in kobo if currency is
            ``Currency.NGN``, pesewas, if currency is ``Currency.GHS``, and cents, if
            currency is ``Currency.ZAR``)
        pagination: int
            Specify how many records you want to retrieve per page. If not specify we
            use a default value of 50.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
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

    def get_transaction(self, id: str) -> Response:
        """Get details of a transaction carried out on your integration.

        Parameters
        ----------
        id: str
            An ID for the transaction to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/transaction/{id}/")
        return self._handle_request("GET", url)

    def charge(
        self,
        amount: int,
        email: str,
        auth_code: str,
        reference: Optional[str] = None,
        currency: Optional[Currency] = None,
        metadata: Optional[dict[str, Any]] = None,
        channels: Optional[list[Channel]] = None,
        subaccount: Optional[str] = None,
        transaction_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
        queue: bool = False,
    ) -> Response:
        """
        All authorizations marked as reusable can be charged with this
        endpoint whenever you need to receive payments.

        Parameters
        ----------
        amount: int
        email: str
            Customer's email address
        auth_code: str
            Valid authorization code to charge
        reference: Optional[str]
            Unique transaction reference. Only ``-, ., =`` and alphanumeric
            characters allowed.
        currency: Optional[Currency]
            Currency in which amount should be charged. Any value from the
            ``Currency`` enum.
        metadata: Optional[dict[str,Any]]
            Add a custom_fields attribute which has an array of objects if
            you would like the fields to be added to your transaction when
            displayed on the dashboard.
            Sample: ``{"custom_fields":[{"display_name":"Cart ID",
            "variable_name": "cart_id","value": "8393"}]}``
        channels: Optional[list[Channel]]
            A list of ``Channel`` enum values to control what channels you want to make available
            to the user to make a payment with
        subaccount: Optional[str]
            The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj
        transaction_charge: Optional[int]
            A flat fee to charge the subaccount for this transaction (in kobo if currency is NGN,
            pesewas, if currency is GHS, and cents, if currency is ZAR). This overrides the split
            percentage set when the subaccount was created. Ideally, you will need to use this if
            you are splitting in flat rates (since subaccount creation only allows for percentage split).
            e.g. 7000 for a 70 naira
        bearer: Optional[Bearer]
            Who bears Paystack charges? any value from the ``Beaer`` enum
        queue: bool
            If you are making a scheduled charge call, it is a good idea to queue them so the processing
            system does not get overloaded causing transaction processing errors. Set ``queue=True`` to
            take advantage of our queued charging.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
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
    ) -> Response:
        """All Mastercard and Visa authorizations can be checked with
        this endpoint to know if they have funds for the payment you seek.

        This method should be used when you do not know the exact amount
        to charge a card when rendering a service. It should be used to
        check if a card has enough funds based on a maximum range value.

        It is well suited:
            - Ride hailing services
            - Logistics services

        You shouldn't use this method to check a card for sufficient
        funds if you are going to charge the user immediately. This is
        because we hold funds when this endpoint is called which can lead
        to an insufficient funds error.

        Parameters
        ----------
        amount: int
            Amount should be in kobo if currency is ``Currency.NGN``, pesewas, if currency is
            ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
        email: str
            Customer's email address
        auth_code: str
            Valid authorization code to charge
        currency: Optional[Currency]
            Currency in which amount should be charged. Any value from the ``Currency`` enum.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        This feature is only available to businesses in Nigeria.
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

    def get_timeline(self, id_or_ref: str) -> Response:
        """View the timeline of a transaction

        Parameters
        ----------
        id_or_reference: str
            The ID or the reference of the transaction

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
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
        """Total amount received on your account

        Parameters
        ----------
        page: Optional[int]
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        start_date: Optional[str]
            A timestamp from which to start listing transaction
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing transaction
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
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
    ) -> Response:
        """Fetch transactions carried out on your integration.

        Parameters
        ----------
        page: Optional[int]
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        start_date: Optional[str]
            A timestamp from which to start listing transaction
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing transaction
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        customer: Optional[int]
            Specify an ID for the customer whose transactions you
            want to retrieve
        status: Optional[TransactionStatus]
            Filter transactions by status. Any value from the
            ``TransactionStatus`` enum
        currency: Optional[Currency]
            Specify the transaction currency to export. Any value
            from the ``Currency`` enum
        amount: Optional[int]
            Filter transactions by amount. Specify the amount, in
            kobo if currency is ``Currency.NGN``, pesewas, if currency
            is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
        settled: Optional[bool]
            Set to ``True`` to export only settled transactions. ``False`` for
            pending transactions. Leave undefined to export all transactions
        settlement: Optional[int]
            An ID for the settlement whose transactions we should export
        payment_page: Optional[int]
            Specify a payment page's id to export only transactions conducted on said page
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
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
        """Retrieve part of a payment from a customer

        Parameters
        ----------
        auth_code: str
            Authorization Code
        currency: Currency
            Specify the currency you want to debit. Any value
            from the ``Currency`` enum.
        amount: int
            Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
            if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
        email: str
            Customer's email address (attached to the authorization code)
        reference: Optional[str]
            Unique transaction reference. Only `-, ., =`
             and alphanumeric characters allowed.
        at_least: Optional[int]
            Minimum amount to charge

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Raises
        ------
        InvalidDataError
            - When Customer's email is not provided.
            - When Customer's auth code is not provided.
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
        # TODO: Deprecate. it's available in Miscellaneous API
        """Fetch transfer banks

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Deprecation Notice
            it's available in Miscellaneous API wrapper. may be removed in future release
        """

        url = self._url("/bank")
        return self._handle_request("GET", url)

    def create_transfer_customer(
        self, bank_code: str, account_number: int, account_name: str
    ) -> Response:
        # TODO: Deprecate. it's available in TransferReceipt API
        """Create a transfer customer

        Parameters
        ----------
        bank_code
        account_number
        int
        account_name

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        -----
        Deprecation Notice
            it's available in TransferReceipt API wrapper. may be removed in future release
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
    ) -> Response:
        # TODO: Deprecate. it's available in Transfer API
        """Initiates transfer to a customer

        Parameters
        ----------
        recipient_code
        amount
        reason
        reference

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Deprecation Notice
            it's available in Transfer API wrapper. may be removed in future release
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
