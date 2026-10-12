from collections.abc import Sequence
from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAsyncAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import WebhookDeliveryStatus, WebhookEventType
from pypaystack2.models import Response
from pypaystack2.models.response_models import WebhookEvent
from pypaystack2.types import PaystackDataModel


class AsyncWebhookEventClient(BaseAsyncAPIClient):
    """This client provides API for interacting with Paystack's Webhook Event API

    The Webhook Events API lets you inspect events, server responses, and resend
    the webhook events sent to your integration.
    """

    async def all(
        self,
        category: str | None = None,
        event_type: WebhookEventType | None = None,
        status: WebhookDeliveryStatus | None = None,
        category_row_id: str | int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
        next_: str | None = None,
        previous: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[WebhookEvent]] | Response[PaystackDataModel]:
        """Fetch a paginated list of webhook events for your integration.

        Args:
            category: Filter by category, e.g. `transactions`
            event_type: Filter by event
            status: Filter by the delivery status
            category_row_id: Filter by the id of the underlying resource e.g. a transaction id
            start_date: A timestamp at which to start listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
            end_date: A timestamp at which to stop listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
            limit: The number of webook events to retrieve per call
            next: The next page cursor.
            previous: The previous page cursor.
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url("/integration/webhooks/events")
        query_params = [
            ("category", category),
            ("event_type", event_type),
            ("status", status),
            ("category_row_id", category_row_id),
            ("from", start_date),
            ("to", end_date),
            ("limit", limit),
            ("next", next_),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or WebhookEvent,
        )

    async def lookup(
        self,
        reference: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[WebhookEvent] | Response[PaystackDataModel]:
        """Find a webhook event by its transaction id

        Args:
            reference: The transaction id or event id to look up,
                not the transaction reference. An event id matches
                directly; anything else is matched against
                the underlying transaction id
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Note:
            reference is not the transaction reference or event id.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(
            f"/integration/webhooks/events/lookup?reference={reference}"
        )
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or WebhookEvent,
        )

    async def get(
        self,
        id: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[WebhookEvent] | Response[PaystackDataModel]:
        """Get the full detail of a single webhook event, including
        the payload sent and the response your endpoint returned.

        Args:
            id: The event's id
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url(f"/integration/webhooks/events/{id}")
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or WebhookEvent,
        )

    async def resend(
        self,
        ids: Sequence[str],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """Resend a specific set of webhook events to your current webhook URL.

        Args:
            ids: A list of ids of the events to resend
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.


        Note:
            Resending isn't idempotent—submitting the same event id twice delivers it twice.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url("/integration/webhooks/events/resend")
        payload = {"ids": ids}
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    async def resend_matching(
        self,
        preview: bool | None = None,
        category: str | None = None,
        event_type: WebhookEventType | None = None,
        status: WebhookDeliveryStatus | None = None,
        category_row_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ):
        """Resend every webhook event matching a filter.
        Pass `preview=true` first to confirm how many events match before you commit to the resend.

        Args:
            preview: Flag to confirm how many events match before you commit to the resend
            category: Filter matching events by category
            event_type: Filter matching events by type
            status: Filter matching events by delivery status
            category_row_id: Filter matching events by underlying resource id
            start_date: A timestamp at which to start listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
            end_date: A timestamp at which to stop listing orders e.g. `2016-09-24T00:00:05.000Z`, `2016-09-21`
            alternate_model_class: A pydantic model that can be used in place of the
                the default provided by the library to serailize the response data.


        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """
        url = self._full_url("/integration/webhooks/events/resend-matching")
        query_params = [
            ("preview", preview),
        ]
        url = append_query_params(query_params, url)
        optional_filters = [
            ("category", category),
            ("event_type", event_type),
            ("status", status),
            ("category_row_id", category_row_id),
            ("from", start_date),
            ("to", end_date),
        ]
        filters = add_to_payload(optional_filters, {})
        payload = {"filters": filters}
        return await self._handle_request(
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )
