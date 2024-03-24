from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.exceptions import InvalidDataException
from pypaystack2.utils import (
    Bearer,
    Channel,
    Currency,
    TransactionStatus,
    add_to_payload,
    append_query_params,
    validate_amount,
    HTTPMethod,
    Response,
)


class Transaction(BaseAPI):
    """Provides a wrapper for paystack Transactions API

    The Transactions API allows you to create and manage payments on your integration.
    see https://paystack.com/docs/api/transaction/
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
        metadata: Optional[dict] = None,
        channels: Optional[list[Channel]] = None,
        split_code: Optional[str] = None,
        subaccount: Optional[str] = None,
        transfer_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
    ) -> Response:
        """Initialize a transaction from your backend

        Args:
            amount: Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            email: Customer's email address
            currency: Any value from the ``Currency`` enum.
            reference: Unique transaction reference. Only ``-, ., =`` and alphanumeric characters allowed.
            callback_url: Fully qualified url, e.g. ``https://example.com/`` . Use this to override the callback url
                provided on the dashboard for this transaction
            plan: If transaction is to create a subscription to a predefined plan, provide plan code here.
                This would invalidate the value provided in ``amount``
            invoice_limit: Number of times to charge customer during subscription to plan
            metadata: A dictionary of additional info. check out this link
                for more information. https://paystack.com/docs/payments/metadata
            channels: A list of ``Channel`` enum values to control what channels you want to make available
                to the user to make a payment with
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w
            subaccount: The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj
            transfer_charge: An amount used to override the split configuration for a single split payment. If set,
                the amount specified goes to the main account regardless of the split configuration.
            bearer: Any value from the ``Bearer`` enum. Who bears Paystack charges?

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When email is not provided.
        """
        amount = validate_amount(amount)

        if not email:
            raise InvalidDataException(
                "Customer's Email is required for initialization"
            )

        url = self._parse_url("/transaction/initialize")
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

        return self._handle_request(HTTPMethod.POST, url, payload)

    def verify(self, reference: str) -> Response:
        """Confirm the status of a transaction

        Args:
            reference: The transaction reference used to intiate the transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        reference = str(reference)
        url = self._parse_url(f"/transaction/verify/{reference}")
        return self._handle_request(HTTPMethod.GET, url)

    def get_transactions(
        self,
        customer: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[TransactionStatus] = None,
        page: Optional[int] = None,
        amount: Optional[int] = None,
        pagination: int = 50,
    ) -> Response:
        """Fetch transactions carried out on your integration.

        Args:
            customer: Specify an ID for the customer whose transactions you want to retrieve
            start_date: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            status: Filter transactions by status. any value from the ``TransactionStatus`` enum
            page: Specify exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            amount: Optional[int]
                Filter transactions by amount. Specify the amount (in kobo if currency is
                ``Currency.NGN``, pesewas, if currency is ``Currency.GHS``, and cents, if
                currency is ``Currency.ZAR``)
            pagination: Specifies how many records you want to retrieve per page. If not specified, we
                use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("customer", customer),
            ("status", status),
            ("from", start_date),
            ("to", end_date),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)

        return self._handle_request(HTTPMethod.GET, url)

    def get_transaction(self, id: str) -> Response:
        """Get details of a transaction carried out on your integration.

        Args:
            id: An ID for the transaction to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/{id}/")
        return self._handle_request(HTTPMethod.GET, url)

    def charge(
        self,
        amount: int,
        email: str,
        auth_code: str,
        reference: Optional[str] = None,
        currency: Optional[Currency] = None,
        metadata: Optional[dict] = None,
        channels: Optional[list[Channel]] = None,
        subaccount: Optional[str] = None,
        transaction_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
        queue: bool = False,
    ) -> Response:
        """
        All authorizations marked as reusable can be charged with this
        endpoint whenever you need to receive payments.

        Args:
            amount: amount to charge.
            email: Customer's email address
            auth_code: Valid authorization code to charge
            reference: Unique transaction reference. Only ``-, ., =`` and alphanumeric
                characters allowed.
            currency: Currency in which amount should be charged. Any value from the
                ``Currency`` enum.
            metadata: Add a custom_fields attribute which has an array of objects if
                you would like the fields to be added to your transaction when
                displayed on the dashboard.
                Sample: ``{"custom_fields":[{"display_name":"Cart ID",
                "variable_name": "cart_id","value": "8393"}]}``
            channels: A list of ``Channel`` enum values to control what channels you want to make available
                to the user to make a payment with
            subaccount: The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj
            transaction_charge: A flat fee to charge the subaccount for this transaction (in kobo if currency is NGN,
                pesewas, if currency is GHS, and cents, if currency is ZAR). This overrides the split
                percentage set when the subaccount was created. Ideally, you will need to use this if
                you are splitting in flat rates (since subaccount creation only allows for percentage split).
                e.g., 7000 for a 70 naira
            bearer: Who bears Paystack charges? any value from the ``Beaer`` enum
            queue: If you are making a scheduled charge call, it is a good idea to queue them so the processing
                system does not get overloaded causing transaction processing errors. Set ``queue=True`` to
                take advantage of our queued charging.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)

        if not email:
            raise InvalidDataException("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataException("Customer's Auth code is required to charge")

        url = self._parse_url("/transaction/charge_authorization")
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

        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_timeline(self, id_or_ref: str) -> Response:
        """View the timeline of a transaction

        Args:
            id_or_ref: The ID or the reference of the transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/timeline/{id_or_ref}")
        return self._handle_request(HTTPMethod.GET, url)

    def totals(
        self,
        page: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        pagination: int = 50,
    ) -> Response:
        """Total amount received on your account

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            start_date: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/totals/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

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
        pagination: int = 50,
    ) -> Response:
        """Fetch transactions carried out on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            start_date: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            customer: Specify an ID for the customer whose transactions you want to retrieve
            status: Filter transactions by status. Any value from the ``TransactionStatus`` enum
            currency: Specify the transaction currency to export. Any value from the ``Currency`` enum
            amount: Filter transactions by amount. Specify the amount, in
                kobo if currency is ``Currency.NGN``, pesewas, if currency
                is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            settled: Set to ``True`` to export only settled transactions. ``False`` for
                pending transactions. Leave undefined to export all transaction
            settlement: An ID for the settlement whose transactions we should export
            payment_page: Optional[int]
                Specify a payment page's id to export only transactions conducted on said page
            pagination: int
                Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if amount:
            amount = validate_amount(amount)
        url = self._parse_url(f"/transaction/export/?perPage={pagination}")
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
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def partial_debit(
        self,
        auth_code: str,
        currency: Currency,
        amount: int,
        email: str,
        reference: Optional[str] = None,
        at_least: Optional[int] = None,
    ) -> Response:
        """Retrieve part of a payment from a customer

        Args:
            auth_code: Authorization Code
            currency: Specify the currency you want to debit. Any value
                from the ``Currency`` enum.
            amount: Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            email: Customer's email address (attached to the authorization code)
            reference: Unique transaction reference. Only `-, ., =`
                 and alphanumeric characters allowed.
            at_least: Minimum amount to charge

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When Customer's email is not provided. When Customer's auth code is not provided.
        """
        amount = validate_amount(amount)
        if at_least:
            at_least = validate_amount(at_least)

        if not email:
            raise InvalidDataException("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataException("Customer's Auth code is required to charge")

        url = self._parse_url("/transaction/partial_debit")
        payload = {
            "authorization_code": auth_code,
            "currency": currency,
            "amount": amount,
            "email": email,
        }
        optional_params = [("reference", reference), ("at_least", at_least)]
        payload = add_to_payload(optional_params, payload)

        return self._handle_request(HTTPMethod.POST, url, payload)


class AsyncTransaction(BaseAsyncAPI):
    """Provides a wrapper for paystack Transactions API

    The Transactions API allows you to create and manage payments on your integration.
    https://paystack.com/docs/api/transaction/
    """

    async def initialize(
        self,
        amount: int,
        email: str,
        currency: Optional[Currency] = None,
        reference: Optional[str] = None,
        callback_url: Optional[str] = None,
        plan: Optional[str] = None,
        invoice_limit: Optional[int] = None,
        metadata: Optional[dict] = None,
        channels: Optional[list[Channel]] = None,
        split_code: Optional[str] = None,
        subaccount: Optional[str] = None,
        transfer_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
    ) -> Response:
        """Initialize a transaction from your backend

        Args:
            amount: Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            email: Customer's email address
            currency: Any value from the ``Currency`` enum.
            reference: Unique transaction reference. Only ``-, ., =`` and alphanumeric characters allowed.
            callback_url: Fully qualified url, e.g. ``https://example.com/`` . Use this to override the callback url
                provided on the dashboard for this transaction
            plan: If transaction is to create a subscription to a predefined plan, provide plan code here.
                This would invalidate the value provided in ``amount``
            invoice_limit: Number of times to charge customer during subscription to plan
            metadata: A dictionary of additional info. check out this link
                for more information. https://paystack.com/docs/payments/metadata
            channels: A list of ``Channel`` enum values to control what channels you want to make available
                to the user to make a payment with
            split_code: The split code of the transaction split. e.g. SPL_98WF13Eb3w
            subaccount: The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj
            transfer_charge: An amount used to override the split configuration for a single split payment. If set,
                the amount specified goes to the main account regardless of the split configuration.
            bearer: Any value from the ``Bearer`` enum. Who bears Paystack charges?

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When email is not provided.
        """
        amount = validate_amount(amount)

        if not email:
            raise InvalidDataException(
                "Customer's Email is required for initialization"
            )

        url = self._parse_url("/transaction/initialize")
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

        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def verify(self, reference: str) -> Response:
        """Confirm the status of a transaction

        Args:
            reference: The transaction reference used to intiate the transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        reference = str(reference)
        url = self._parse_url(f"/transaction/verify/{reference}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_transactions(
        self,
        customer: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[TransactionStatus] = None,
        page: Optional[int] = None,
        amount: Optional[int] = None,
        pagination: int = 50,
    ) -> Response:
        """Fetch transactions carried out on your integration.

        Args:
            customer: Specify an ID for the customer whose transactions you want to retrieve
            start_date: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            status: Filter transactions by status. any value from the ``TransactionStatus`` enum
            page: Specify exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            amount: Optional[int]
                Filter transactions by amount. Specify the amount (in kobo if currency is
                ``Currency.NGN``, pesewas, if currency is ``Currency.GHS``, and cents, if
                currency is ``Currency.ZAR``)
            pagination: Specifies how many records you want to retrieve per page. If not specified, we
                use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("customer", customer),
            ("status", status),
            ("from", start_date),
            ("to", end_date),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)

        return await self._handle_request(HTTPMethod.GET, url)

    async def get_transaction(self, id: str) -> Response:
        """Get details of a transaction carried out on your integration.

        Args:
            id: An ID for the transaction to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/{id}/")
        return await self._handle_request(HTTPMethod.GET, url)

    async def charge(
        self,
        amount: int,
        email: str,
        auth_code: str,
        reference: Optional[str] = None,
        currency: Optional[Currency] = None,
        metadata: Optional[dict] = None,
        channels: Optional[list[Channel]] = None,
        subaccount: Optional[str] = None,
        transaction_charge: Optional[int] = None,
        bearer: Optional[Bearer] = None,
        queue: bool = False,
    ) -> Response:
        """
        All authorizations marked as reusable can be charged with this
        endpoint whenever you need to receive payments.

        Args:
            amount: amount to charge.
            email: Customer's email address
            auth_code: Valid authorization code to charge
            reference: Unique transaction reference. Only ``-, ., =`` and alphanumeric
                characters allowed.
            currency: Currency in which amount should be charged. Any value from the
                ``Currency`` enum.
            metadata: Add a custom_fields attribute which has an array of objects if
                you would like the fields to be added to your transaction when
                displayed on the dashboard.
                Sample: ``{"custom_fields":[{"display_name":"Cart ID",
                "variable_name": "cart_id","value": "8393"}]}``
            channels: A list of ``Channel`` enum values to control what channels you want to make available
                to the user to make a payment with
            subaccount: The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj
            transaction_charge: A flat fee to charge the subaccount for this transaction (in kobo if currency is NGN,
                pesewas, if currency is GHS, and cents, if currency is ZAR). This overrides the split
                percentage set when the subaccount was created. Ideally, you will need to use this if
                you are splitting in flat rates (since subaccount creation only allows for percentage split).
                e.g., 7000 for a 70 naira
            bearer: Who bears Paystack charges? any value from the ``Beaer`` enum
            queue: If you are making a scheduled charge call, it is a good idea to queue them so the processing
                system does not get overloaded causing transaction processing errors. Set ``queue=True`` to
                take advantage of our queued charging.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        amount = validate_amount(amount)

        if not email:
            raise InvalidDataException("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataException("Customer's Auth code is required to charge")

        url = self._parse_url("/transaction/charge_authorization")
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

        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_timeline(self, id_or_ref: str) -> Response:
        """View the timeline of a transaction

        Args:
            id_or_ref: The ID or the reference of the transaction

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/timeline/{id_or_ref}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def totals(
        self,
        page: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        pagination: int = 50,
    ) -> Response:
        """Total amount received on your account

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            start_date: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transaction/totals/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def export(
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
        pagination: int = 50,
    ) -> Response:
        """Fetch transactions carried out on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            start_date: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            customer: Specify an ID for the customer whose transactions you want to retrieve
            status: Filter transactions by status. Any value from the ``TransactionStatus`` enum
            currency: Specify the transaction currency to export. Any value from the ``Currency`` enum
            amount: Filter transactions by amount. Specify the amount, in
                kobo if currency is ``Currency.NGN``, pesewas, if currency
                is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            settled: Set to ``True`` to export only settled transactions. ``False`` for
                pending transactions. Leave undefined to export all transaction
            settlement: An ID for the settlement whose transactions we should export
            payment_page: Optional[int]
                Specify a payment page's id to export only transactions conducted on said page
            pagination: int
                Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if amount:
            amount = validate_amount(amount)
        url = self._parse_url(f"/transaction/export/?perPage={pagination}")
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
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def partial_debit(
        self,
        auth_code: str,
        currency: Currency,
        amount: int,
        email: str,
        reference: Optional[str] = None,
        at_least: Optional[int] = None,
    ) -> Response:
        """Retrieve part of a payment from a customer

        Args:
            auth_code: Authorization Code
            currency: Specify the currency you want to debit. Any value
                from the ``Currency`` enum.
            amount: Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            email: Customer's email address (attached to the authorization code)
            reference: Unique transaction reference. Only `-, ., =`
                 and alphanumeric characters allowed.
            at_least: Minimum amount to charge

        Returns:
            A named tuple containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When Customer's email is not provided. When Customer's auth code is not provided.
        """
        amount = validate_amount(amount)
        if at_least:
            at_least = validate_amount(at_least)

        if not email:
            raise InvalidDataException("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataException("Customer's Auth code is required to charge")

        url = self._parse_url("/transaction/partial_debit")
        payload = {
            "authorization_code": auth_code,
            "currency": currency,
            "amount": amount,
            "email": email,
        }
        optional_params = [("reference", reference), ("at_least", at_least)]
        payload = add_to_payload(optional_params, payload)

        return await self._handle_request(HTTPMethod.POST, url, payload)
