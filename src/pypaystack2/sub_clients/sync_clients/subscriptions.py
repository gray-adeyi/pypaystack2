from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.models import Response
from pypaystack2.models.response_models import Subscription, SubscriptionLink
from pypaystack2.types import PaystackDataModel


class SubscriptionClient(BaseAPIClient):
    """Provides a wrapper for paystack Subscriptions API

    The Subscriptions API allows you to create and manage recurring
    payment on your integration.
    https://paystack.com/docs/api/subscription/
    """

    def create(
        self,
        customer: int | str,
        plan: str,
        authorization: str | None = None,
        start_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Subscription] | Response[PaystackDataModel]:
        """Create a subscription on your integration

        Note:
            Email Token
                paystack creates an email token on each subscription to allow customers
                cancel their subscriptions from within the invoices sent to their mailboxes.
                Since they are not authorized, the email tokens are what we use to authenticate
                the requests over the API.

        Args:
            customer: Customer's email address or customer code
            plan: Plan code
            authorization: If customer has multiple authorizations, you can set
                the desired authorization you wish to use for this
                subscription here. If this is not supplied, the
                customer's most recent authorization would be used
            start_date: Set the date for the first debit. (ISO 8601 format) e.g. 2017-05-16T00:30:13+01:00
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

        url = self._full_url("/subscription")

        payload = {"customer": customer, "plan": plan}
        optional_params = [
            ("start_date", start_date),
            ("authorization", authorization),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or Subscription,
        )

    def get_subscriptions(
        self,
        page: int = 1,
        pagination: int = 50,
        customer: int | None = None,
        plan: str | int | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Subscription]] | Response[PaystackDataModel]:
        """Fetch subscriptions available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            customer: Filter by Customer ID
            plan: Filter by Plan ID
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

        url = self._full_url("/subscription/?perPage=" + str(pagination))
        query_params = [
            ("page", page),
            ("customer", customer),
            ("plan", plan),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Subscription,
        )

    def get_subscription(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Subscription] | Response[PaystackDataModel]:
        """Fetch details of a subscription on your integration.

        Args:
            id_or_code: The subscription ``ID`` or ``code`` you want to fetch
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

        url = self._full_url(f"/subscription/{id_or_code}")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Subscription,
        )

    def enable(
        self,
        code: str,
        token: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Enable a subscription on your integration

        Args:
            code: Subscription code
            token: Email token
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

        url = self._full_url("/subscription/enable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def disable(
        self,
        code: str,
        token: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Disable a subscription on your integration

        Args:
            code: Subscription code
            token: Email token
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
        url = self._full_url("/subscription/disable")
        payload = {
            "code": code,
            "token": token,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def get_update_link(
        self,
        code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[SubscriptionLink] | Response[PaystackDataModel]:
        """Generate a link for updating the card on a subscription

        Args:
            code: Subscription code
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

        url = self._full_url(f"/subscription/{code}/manage/link/")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or SubscriptionLink,
        )

    def send_update_link(
        self,
        code: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Email a customer a link for updating the card on their subscription

        Args:
            code: Subscription code
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

        url = self._full_url(f"/subscription/{code}/manage/email/")
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            response_data_model_class=alternate_model_class,
        )
