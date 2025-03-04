from http import HTTPMethod
from typing import Any

from pypaystack2.base_clients import BaseAPIClient, append_query_params
from pypaystack2.enums import TerminalEvent, TerminalEventAction
from pypaystack2.models import Response
from pypaystack2.models.response_models import (
    TerminalEventData,
    TerminalEventStatusData,
    TerminalStatusData,
    Terminal,
)
from pypaystack2.types import PaystackDataModel


class TerminalClient(BaseAPIClient):
    """Provides a wrapper for paystack Terminal API

    The Terminal API allows you to build delightful in-person payment experiences.
    https://paystack.com/docs/api/terminal/
    """

    def send_event(
        self,
        terminal_id: int | str,
        type_: TerminalEvent,
        action: TerminalEventAction,
        data: dict[str, Any],
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TerminalEventData] | Response[PaystackDataModel]:
        """Send an event from your application to the Paystack Terminal

        Args:
            terminal_id: The ID of the Terminal the event should be sent to.
            type_: The type of event to push. Paystack currently supports `TerminalEventType.INVOICE` and
                `TerminalEventType.TRANSACTION`.
            action: The action the Terminal needs to perform. For the `TerminalEventType.INVOICE` type,
                the action can either be `TerminalEventAction.PROCESS` or TerminalEventAction.VIEW.
                For the `TerminalEventType.TRANSACTION` type, the action can either be
                `TerminalEventAction.PROCESS` or `TerminalEventAction.PRINT`.
            data: The parameters needed to perform the specified action. For the invoice type, you need to
                pass the invoice id and offline reference: {id: invoice_id, reference: offline_reference}.
                For the transaction type, you can pass the transaction id: {id: transaction_id}
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
        supported_actions_mapping = {
            TerminalEvent.TRANSACTION: {
                TerminalEventAction.PROCESS,
                TerminalEventAction.PRINT,
            },
            TerminalEvent.INVOICE: {
                TerminalEventAction.PROCESS,
                TerminalEventAction.VIEW,
            },
        }
        if action not in supported_actions_mapping[type_]:
            raise ValueError(
                f"Terminal Event: {type_} does not support Terminal Event Action: {action}"
            )

        url = self._full_url(f"/terminal/{terminal_id}/event")

        payload = {
            "type": type_,
            "action": action,
            "data": data,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or TerminalEventData,
        )

    def get_event_status(
        self,
        terminal_id: int | str,
        event_id: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TerminalEventStatusData] | Response[PaystackDataModel]:
        """Check the status of an event sent to the Terminal

        Args:
            terminal_id: The ID of the Terminal the event was sent to.
            event_id: The ID of the event that was sent to the Terminal
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
        url = self._full_url(f"/terminal/{terminal_id}/event/{event_id}")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TerminalEventStatusData,
        )

    def get_terminal_status(
        self,
        terminal_id: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TerminalStatusData] | Response[PaystackDataModel]:
        """Check the availability of a Terminal before sending an event to it.

        Args:
            terminal_id: The ID of the Terminal you want to check
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
        url = self._full_url(f"/terminal/{terminal_id}/presence")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TerminalStatusData,
        )

    def get_terminals(
        self,
        pagination: int = 50,
        next_: str | None = None,
        previous: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[Terminal]] | Response[PaystackDataModel]:
        """List the Terminals available on your integration

        Args:
            pagination: Specifies how many records you want to retrieve per page. If not specified, it defaults to 50.
            next_: Specifies how many records you want to retrieve per page. If not specified
                we use a default value of 50.
            previous: A cursor that indicates your place in the list. It should be used to fetch the
                previous page of the list after an initial next request
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
        url = self._full_url(f"/terminal?perPage={pagination}")
        query_params = [
            ("next", next_),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Terminal,
        )

    def get_terminal(
        self,
        terminal_id: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[Terminal] | Response[PaystackDataModel]:
        """Get the details of a Terminal

        Args:
            terminal_id: The ID of the Terminal the event was sent to.
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
        url = self._full_url(f"/terminal/{terminal_id}/")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Terminal,
        )

    def update_terminal(
        self,
        terminal_id: int | str,
        name: str,
        address: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Update the details of a Terminal

        Args:
            terminal_id: The ID of the Terminal you want to update
            name: Name of the terminal
            address: The address of the Terminal
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
        url = self._full_url(f"/terminal/{terminal_id}")

        payload = {"name": name, "address": address}
        return self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def commission_terminal(
        self,
        serial_number: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Activate your debug device by linking it to your integration

        Args:
            serial_number: Device Serial Number
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

        url = self._full_url("/terminal/commission_device")

        payload = {
            "serial_number": serial_number,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )

    def decommission_terminal(
        self,
        serial_number: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Unlink your debug device from your integration

        Args:
            serial_number: Device Serial Number
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
        url = self._full_url("/terminal/decommission_device")

        payload = {
            "serial_number": serial_number,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )
