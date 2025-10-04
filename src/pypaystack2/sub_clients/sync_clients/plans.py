from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Interval, Currency, Status
from pypaystack2.models import Response
from pypaystack2.models.response_models import Plan
from pypaystack2.types import PaystackDataModel


class PlanClient(BaseAPIClient):
    """Provides a wrapper for paystack Plans API

    The Plans API allows you to create and manage installment payment options on your integration.
    https://paystack.com/docs/api/plan/
    """

    def create(
        self,
        name: str,
        amount: int,
        interval: Interval,
        description: str | None = None,
        currency: Currency | None = None,
        invoice_limit: int | None = None,
        send_invoices: bool = False,
        send_sms: bool = False,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Plan] | Response[PaystackDataModel]:
        """Create a plan on your integration

        Args:
            name: Name of plan
            amount: Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
                if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
            interval: Any value from the ``Interval`` enum.
            description: A description for this plan
            currency: Currency in which amount is set. Any of the value from
                the ``Currency`` enum
            invoice_limit: Number of invoices to raise during subscription to this plan.
                Can be overridden by specifying an ``invoice_limit`` while subscribing
            send_invoices: Set to ``False`` if you don't want invoices to be sent to your customers
            send_sms: Set to ``False`` if you don't want text messages to be sent to your customers
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

        url = self._full_url("/plan/")

        payload = {
            "name": name,
            "amount": amount,
            "interval": interval,
        }
        optional_params = [
            ("send_invoices", send_invoices),
            ("send_sms", send_sms),
            ("description", description),
            ("currency", currency),
            ("invoice_limit", invoice_limit),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Plan,
        )

    def get_plans(
        self,
        page: int = 1,
        pagination: int = 50,
        status: Status | None = None,
        interval: Interval | None = None,
        amount: int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Plan]] | Response[PaystackDataModel]:
        """Fetch plans available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            status: Filter list by plans with specified status
            interval: Filter list by plans with specified interval
            amount: Filter list by plans with specified amount ( kobo if currency
                is ``Currency.NGN``, pesewas, if currency is ``Currency.GHS``,
                and cents, if currency is ``Currency.ZAR``)
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

        url = self._full_url(f"/plan/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("status", status),
            ("interval", interval),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Plan,
        )

    def get_plan(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Plan] | Response[PaystackDataModel]:
        """Get details of a plan on your integration.

        Args:
            id_or_code: The plan ``ID`` or ``code`` you want to fetch
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
        url = self._full_url("/plan/{}/".format(id_or_code))
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Plan,
        )

    def update(
        self,
        id_or_code: int | str,
        name: str | None = None,
        amount: int | None = None,
        interval: Interval | None = None,
        description: str | None = None,
        currency: Currency | None = None,
        invoice_limit: int | None = None,
        send_invoices: bool = False,
        send_sms: bool = False,
        update_existing_subscriptions: bool = True,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """update a plan details on your integration

        Args:
            id_or_code: Plan's ID or code
            name: Name of plan
            amount: Amount should be in kobo if currency is
                ``Currency.NGN`` and pesewas for ``Currency.GHS``
            interval: Any value from the ``Interval`` enum.
            description: A description for this plan.
            currency: Any value from the ``Currency`` enum.
            invoice_limit: Number of invoices to raise during subscription to this plan.
                Can be overridden by specifying an ``invoice_limit`` while subscribing.
            send_invoices: Set to ``False`` if you don't want invoices
                to be sent to your customers
            send_sms: Set to ``False`` if you don't want text messages to
                be sent to your customers
            update_existing_subscriptions: Flag to determine whether to update existing subscriptions based on the new
                changes made to the plan.
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

        url = self._full_url(f"/plan/{id_or_code}/")
        payload = {
            "name": name,
            "amount": amount,
            "interval": interval,
        }

        optional_params = [
            ("send_invoices", send_invoices),
            ("send_sms", send_sms),
            ("description", description),
            ("currency", currency),
            ("invoice_limit", invoice_limit),
            ("update_existing_subscriptions", update_existing_subscriptions),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )
