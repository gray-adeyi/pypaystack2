from pypaystack2.models import Response
from pypaystack2.types import PaystackDataModel
from http import HTTPMethod
from typing import Literal, Any
from pypaystack2.enums import Currency, Bearer
from pypaystack2.base_clients import (
    append_query_params,
    add_to_payload,
    BaseAsyncAPIClient,
)


class AsyncPreauthorizationClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Preauthorization API

    The Preauthorization API enables South African merchants to hold an amount
    from a customer's account, and charge it later."""

    async def initialize(
        self,
        amount: int,
        email: str,
        currency: Currency = Currency.ZAR,
        reference: str | None = None,
        callback_url: str | None = None,
        metadata: dict[str, Any] | None = None,
        split_code: str | None = None,
        subaccount: str | None = None,
        transaction_charge: int | None = None,
        bearer: Bearer | None = None,
        expire_action: Literal["capture", "release"] | None = None,
        expire_after_days: int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Initialize a preauthorization transaction for a new customer

        Args:
            amount: The amount to preauthorize in subunit.
            email: The customer's email address.
            currency: The target currency. Only ZAR is supported for now.
            reference: Unique transaction reference. Only -, ., = and
                alphanumeric characters allowed.
            callback_url: Fully qualified url, e.g. https://example.com/ .
                Use this to override the callback url provided on the dashboard for this transaction
            metadata: Additional data
            split_code: The split code of the transaction split. e.g. `SPL_98WF13Eb3w`
            subaccount: The code for the subaccount that owns the payment. e.g. `ACCT_8f4s1eq7ml6rlzj`
            transaction_charge: An amount used to override the split configuration for a single split payment. If set,
                the amount specified goes to the main account regardless of the split configuration.
            bearer: Specifies who will pay the Paystack transaction charges for this transaction.
            expire_action: Specifies the action to take on the expiry date.
            expire_after_days:The number of days until the `expire_action` is executed. The minimum is 1 day and maximum 30 days.
                Defaults to 5 days.
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
        url = self._full_url("/preauthorization/initialize")
        payload = {"amount": amount, "email": email, "currency": currency}
        optional_params = [
            ("reference", reference),
            ("callback_url", callback_url),
            ("metadata", metadata),
            ("split_code", split_code),
            ("subaccount", subaccount),
            ("transaction_charge", transaction_charge),
            ("bearer", bearer),
            ("expire_action", expire_action),
            ("expire_after_days", expire_after_days),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def capture(
        self,
        reference: str,
        amount: int,
        currency: Currency = Currency.ZAR,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Charge a preauthorized transaction upon service delivery

        Args:
            reference: Unique transaction reference. Only -, ., = and
                alphanumeric characters allowed.
            amount: The amount to capture in subunit.
            currency: The target currency. Only ZAR is supported for now.
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
        url = self._full_url("/preauthorization/capture")
        payload = {"reference": reference, "amount": amount, "currency": currency}
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def reserve(
        self,
        email: str,
        amount: int,
        authorization_code: str,
        currency: Currency = Currency.ZAR,
        reference: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Hold an amount using an existing customer's authorization that's marked reusable.

        Args:
            email: The customer's email address.
            amount: The amount to capture in subunit.
            authorization_code: This is the code that is used to charge and identify a customer's previously used card
            currency: The target currency. Only ZAR is supported for now.
            reference: Unique transaction reference. Only -, ., = and
                alphanumeric characters allowed.
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
        url = self._full_url("/preauthorization/reserve_authorization")
        payload = {
            "email": email,
            "amount": amount,
            "authorization_code": authorization_code,
            "currency": currency,
        }
        optional_params = [
            ("reference", reference),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def verify(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """Fetch and confirm the status of a preauthorized transaction.


        Note:
            If you plan to store or make use of the transaction ID, you should represent it as a
            unsigned 64-bit integer. To learn more,
            see https://paystack.com/docs/changelog/api/#june-2022

        Args:
            reference: The transaction reference used to intiate the transaction.
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
        url = self._full_url(f"/preauthorization/verify/{reference}")
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )

    async def release(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """For when a customer cancels an order or you want
        to release the hold from their card.

        Args:
            reference: Unique transaction reference. Only -, ., = and
                alphanumeric characters allowed.
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
        url = self._full_url("/preauthorization/release")
        payload = {
            "reference": reference,
        }
        return await self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def get_transactions(
        self,
        pagination: int = 50,
        page: int = 1,
        customer: int | None = None,
        status: Literal[
            "authorized", "captured", "released", "ongoing", "failed", "abandoned"
        ]
        | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        amount: int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[PaystackDataModel]:
        """List preauthorizations carried out on your integration

        Args:
            pagination: Specifies how many preauthorizations you want to retrieve call.
            page: Specifies the page to retrieve from the pagination.
            customer: The unique customer ID to retrieve transactions belonging to that customer
            status: Filter transactions by status.
            start_date: A timestamp at which to start listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
            end_date: A timestamp at which to stop listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
            amount: Filter transactions by amount
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
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("customer", customer),
            ("status", status),
            ("amount", amount),
        ]
        url = self._full_url(f"/transaction/?perPage={pagination}")
        url = append_query_params(query_params, url)
        return await self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class,
        )
