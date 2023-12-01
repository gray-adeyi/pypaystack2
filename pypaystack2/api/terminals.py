from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.exceptions import InvalidDataException
from pypaystack2.utils import (
    TerminalEvent,
    TerminalEventAction,
    append_query_params,
    HTTPMethod,
    Response,
)


class Terminal(BaseAPI):
    """Provides a wrapper for paystack Terminal API

    The Terminal API allows you to build delightful in-person payment experiences.
    https://paystack.com/docs/api/terminal/
    """

    def send_event(
        self,
        terminal_id: str,
        type: TerminalEvent,
        action: TerminalEventAction,
        data: dict,
    ) -> Response:
        """Send an event from your application to the Paystack Terminal

        Args:
            terminal_id: The ID of the Terminal the event should be sent to.
            type: The type of event to push. Paystack currently supports `TerminalEventType.INVOICE` and
                `TerminalEventType.TRANSACTION`.
            action: The action the Terminal needs to perform. For the `TerminalEventType.INVOICE` type,
                the action can either be `TerminalEventAction.PROCESS` or TerminalEventAction.VIEW.
                For the `TerminalEventType.TRANSACTION` type, the action can either be
                `TerminalEventAction.PROCESS` or `TerminalEventAction.PRINT`.
            data: The parameters needed to perform the specified action. For the invoice type, you need to
                pass the invoice id and offline reference: {id: invoice_id, reference: offline_reference}.
                For the transaction type, you can pass the transaction id: {id: transaction_id}

        Returns:
            A named tuple containing the response gotten from paystack's server.
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
        if action not in supported_actions_mapping[type]:
            raise InvalidDataException(
                f"Terminal Event: {type} does not support Terminal Event Action: {action}"
            )

        url = self._parse_url(f"/terminal/{terminal_id}/event")

        payload = {
            "type": type,
            "action": action,
            "data": data,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_event_status(self, terminal_id: str, event_id: str) -> Response:
        """Check the status of an event sent to the Terminal

        Args:
            terminal_id: The ID of the Terminal the event was sent to.
            event_id: The ID of the event that was sent to the Terminal

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}/event/{event_id}")
        return self._handle_request(HTTPMethod.GET, url)

    def get_terminal_status(self, terminal_id: str) -> Response:
        """Check the availability of a Terminal before sending an event to it.

        Args:
            terminal_id: The ID of the Terminal you want to check

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}/presence")
        return self._handle_request(HTTPMethod.GET, url)

    def get_terminals(
        self,
        pagination: int = 50,
        next: Optional[str] = None,
        previous: Optional[str] = None,
    ) -> Response:
        """List the Terminals available on your integration

        Args:
            pagination: Specifies how many records you want to retrieve per page. If not specified, it defaults to 50.
            next: Specifies how many records you want to retrieve per page. If not specified
                we use a default value of 50.
            previous: A cursor that indicates your place in the list. It should be used to fetch the
                previous page of the list after an initial next request

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal?perPage={pagination}")
        query_params = [
            ("next", next),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_terminal(self, terminal_id: str) -> Response:
        """Get the details of a Terminal

        Args:
            terminal_id: The ID of the Terminal the event was sent to.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}/")
        return self._handle_request(HTTPMethod.GET, url)

    def update_terminal(self, terminal_id: str, name: str, address: str) -> Response:
        """Update the details of a Terminal

        Args:
            terminal_id: The ID of the Terminal you want to update
            name: Name of the terminal
            address: The address of the Terminal

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}")

        payload = {"name": name, "address": address}
        return self._handle_request(HTTPMethod.PUT, url, payload)

    def commission_terminal(self, serial_number: str) -> Response:
        """Activate your debug device by linking it to your integration

        Args:
            serial_number: Device Serial Number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/terminal/commission_device")

        payload = {
            "serial_number": serial_number,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def decommission_terminal(self, serial_number: str) -> Response:
        """Unlink your debug device from your integration

        Args:
            serial_number: Device Serial Number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/terminal/decommission_device")

        payload = {
            "serial_number": serial_number,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)


class AsyncTerminal(BaseAsyncAPI):
    """Provides a wrapper for paystack Terminal API

    The Terminal API allows you to create and manage recurring
    payment on your integration.
    https://paystack.com/docs/api/terminal/
    """

    async def send_event(
        self,
        terminal_id: str,
        type: TerminalEvent,
        action: TerminalEventAction,
        data: dict,
    ) -> Response:
        """Send an event from your application to the Paystack Terminal

        Args:
            terminal_id: The ID of the Terminal the event should be sent to.
            type: The type of event to push. Paystack currently supports `TerminalEventType.INVOICE` and
                `TerminalEventType.TRANSACTION`.
            action: The action the Terminal needs to perform. For the `TerminalEventType.INVOICE` type,
                the action can either be `TerminalEventAction.PROCESS` or TerminalEventAction.VIEW.
                For the `TerminalEventType.TRANSACTION` type, the action can either be
                `TerminalEventAction.PROCESS` or `TerminalEventAction.PRINT`.
            data: The parameters needed to perform the specified action. For the invoice type, you need to
                pass the invoice id and offline reference: {id: invoice_id, reference: offline_reference}.
                For the transaction type, you can pass the transaction id: {id: transaction_id}

        Returns:
            A named tuple containing the response gotten from paystack's server.
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
        if action not in supported_actions_mapping[type]:
            raise InvalidDataException(
                f"Terminal Event: {type} does not support Terminal Event Action: {action}"
            )

        url = self._parse_url(f"/terminal/{terminal_id}/event")

        payload = {
            "type": type,
            "action": action,
            "data": data,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_event_status(self, terminal_id: str, event_id: str) -> Response:
        """Check the status of an event sent to the Terminal

        Args:
            terminal_id: The ID of the Terminal the event was sent to.
            event_id: The ID of the event that was sent to the Terminal

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}/event/{event_id}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_terminal_status(self, terminal_id: str) -> Response:
        """Check the availability of a Terminal before sending an event to it.

        Args:
            terminal_id: The ID of the Terminal you want to check

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}/presence")
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_terminals(
        self,
        pagination: int = 50,
        next: Optional[str] = None,
        previous: Optional[str] = None,
    ) -> Response:
        """List the Terminals available on your integration

        Args:
            pagination: Specifies how many records you want to retrieve per page. If not specified, it defaults to 50.
            next: Specifies how many records you want to retrieve per page. If not specified
                we use a default value of 50.
            previous: A cursor that indicates your place in the list. It should be used to fetch the
                previous page of the list after an initial next request

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal?perPage={pagination}")
        query_params = [
            ("next", next),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_terminal(self, terminal_id: str) -> Response:
        """Get the details of a Terminal

        Args:
            terminal_id: The ID of the Terminal the event was sent to.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}/")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update_terminal(
        self, terminal_id: str, name: str, address: str
    ) -> Response:
        """Update the details of a Terminal

        Args:
            terminal_id: The ID of the Terminal you want to update
            name: Name of the terminal
            address: The address of the Terminal

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/terminal/{terminal_id}")

        payload = {"name": name, "address": address}
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def commission_terminal(self, serial_number: str) -> Response:
        """Activate your debug device by linking it to your integration

        Args:
            serial_number: Device Serial Number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/terminal/commission_device")

        payload = {
            "serial_number": serial_number,
        }
        return await self._handle_request("POST", url, payload)

    async def decommission_terminal(self, serial_number: str) -> Response:
        """Unlink your debug device from your integration

        Args:
            serial_number: Device Serial Number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/terminal/decommission_device")

        payload = {
            "serial_number": serial_number,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)
