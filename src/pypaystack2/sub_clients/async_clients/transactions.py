from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Currency, Channel, Bearer, TransactionStatus
from pypaystack2.models import Response
from pypaystack2.models.response_models import (
    InitTransaction,
    Transaction,
    TransactionLog,
    TransactionExport,
    TransactionTotal,
)
from pypaystack2.types import PaystackDataModel


class AsyncTransactionClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Transactions API

    The Transactions API allows you to create and manage payments on your integration.
    https://paystack.com/docs/api/transaction/
    """

    async def initialize(
        self,
        amount: int,
        email: str,
        currency: Currency | None = None,
        reference: str | None = None,
        callback_url: str | None = None,
        plan: str | None = None,
        invoice_limit: int | None = None,
        metadata: dict[str, Any] | None = None,
        channels: list[Channel] | None = None,
        split_code: str | None = None,
        subaccount: str | None = None,
        transfer_charge: int | None = None,
        bearer: Bearer | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[InitTransaction] | Response[PaystackDataModel]:
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
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When email is not provided.
        """

        if not email:
            raise ValueError("Customer's Email is required for initialization")

        url = self._full_url("/transaction/initialize")
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
        payload = add_to_payload(
            optional_params,
            payload,
        )

        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,  # type: ignore
            response_data_model_class=alternate_model_class or InitTransaction,
        )

    async def verify(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """Confirm the status of a transaction

        Args:
            reference: The transaction reference used to initiate the transaction
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        reference = str(reference)
        url = self._full_url(f"/transaction/verify/{reference}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def get_transactions(
        self,
        customer: int | str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        status: TransactionStatus | None = None,
        page: int | None = None,
        amount: int | None = None,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Transaction]] | Response[PaystackDataModel]:
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
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/transaction/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("customer", customer),
            ("status", status),
            ("from", start_date),
            ("to", end_date),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)

        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def get_transaction(
        self,
        id_: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
        """Get details of a transaction carried out on your integration.

        Args:
            id_: An ID for the transaction to fetch
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/transaction/{id_}/")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def charge(
        self,
        amount: int,
        email: str,
        auth_code: str,
        reference: str | None = None,
        currency: Currency | None = None,
        metadata: dict[str, Any] | None = None,
        channels: list[Channel] | None = None,
        subaccount: str | None = None,
        transaction_charge: int | None = None,
        bearer: Bearer | None = None,
        queue: bool = False,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
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
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        if not email:
            raise ValueError("Customer's Email is required to charge")

        if not auth_code:
            raise ValueError("Customer's Auth code is required to charge")

        url = self._full_url("/transaction/charge_authorization")
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

        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )

    async def get_timeline(
        self,
        id_or_ref: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransactionLog] | Response[PaystackDataModel]:
        """View the timeline of a transaction

        Args:
            id_or_ref: The ID or the reference of the transaction
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/transaction/timeline/{id_or_ref}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TransactionLog,
        )

    async def totals(
        self,
        page: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransactionTotal] | Response[PaystackDataModel]:
        """Total amount received on your account

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            start_date: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/transaction/totals/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TransactionTotal,
        )

    async def export(
        self,
        page: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        customer: str | int | None = None,
        status: TransactionStatus | None = None,
        currency: Currency | None = None,
        amount: int | None = None,
        settled: bool | None = None,
        settlement: str | None = None,
        payment_page: str | None = None,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransactionExport] | Response[PaystackDataModel]:
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
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/transaction/export/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("customer", customer),
            ("status", status),
            ("currency", currency),
            ("amount", amount),
            ("settled", settled),
            ("settlement", settlement),
            ("payment_page", payment_page),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TransactionExport,
        )

    async def partial_debit(
        self,
        auth_code: str,
        currency: Currency,
        amount: int,
        email: str,
        reference: str | None = None,
        at_least: int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Transaction] | Response[PaystackDataModel]:
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
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.

        Raises:
            InvalidDataError: When Customer's email is not provided. When Customer's auth code is not provided.
        """

        if not email:
            raise ValueError("Customer's Email is required to charge")

        if not auth_code:
            raise ValueError("Customer's Auth code is required to charge")

        url = self._full_url("/transaction/partial_debit")
        payload = {
            "authorization_code": auth_code,
            "currency": currency,
            "amount": amount,
            "email": email,
        }
        optional_params = [("reference", reference), ("at_least", at_least)]
        payload = add_to_payload(optional_params, payload)

        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Transaction,
        )
