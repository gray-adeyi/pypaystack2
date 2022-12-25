from typing import Optional

from pypaystack2.baseapi import BaseAPI, Response
from pypaystack2.errors import InvalidDataError
from pypaystack2.utils import (
    TerminalEventType,
    TerminalEventAction,
    append_query_params,
)


class Terminal(BaseAPI):
    """Provides a wrapper for paystack Terminal API

    The Terminal API allows you to create and manage recurring
    payment on your integration.
    https://paystack.com/docs/api/#terminal
    """

    def send_event(
        self,
        terminal_id: str,
        type: TerminalEventType,
        action: TerminalEventAction,
        data: dict,
    ) -> Response:
        """Send an event from your application to the Paystack Terminal

        Parameters
        ----------
        terminal_id: str
            The ID of the Terminal the event should be sent to.
        type: TerminalEventType
            The type of event to push. Paystack currently supports `TerminalEventType.INVOICE` and
            `TerminalEventType.TRANSACTION`.
        action: TerminalEventAction
            The action the Terminal needs to perform. For the `TerminalEventType.INVOICE` type,
            the action can either be `TerminalEventAction.PROCESS` or TerminalEventAction.VIEW.
            For the `TerminalEventType.TRANSACTION` type, the action can either be
            `TerminalEventAction.PROCESS` or `TerminalEventAction.PRINT`.
        data: dict
            The parameters needed to perform the specified action. For the invoice type, you need to
            pass the invoice id and offline reference: {id: invoice_id, reference: offline_reference}.
            For the transaction type, you can pass the transaction id: {id: transaction_id}

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        supported_actions_mapping = {
            TerminalEventType.TRANSACTION: {
                TerminalEventAction.PROCESS,
                TerminalEventAction.PRINT,
            },
            TerminalEventType.INVOICE: {
                TerminalEventAction.PROCESS,
                TerminalEventAction.VIEW,
            },
        }
        if action not in supported_actions_mapping[type]:
            raise InvalidDataError(
                f"Terminal Event: {type} does not support Terminal Event Action: {action}"
            )

        url = self._url(f"/terminal/{terminal_id}/event")

        payload = {
            "type": type,
            "action": action,
            "data": data,
        }
        return self._handle_request("POST", url, payload)

    def get_event_status(self, terminal_id: str, event_id: str) -> Response:
        """Check the status of an event sent to the Terminal

        Parameters
        ----------
        terminal_id: str
            The ID of the Terminal the event was sent to.
        event_id: str
            The ID of the event that was sent to the Terminal

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/terminal/{terminal_id}/event/{event_id}")
        return self._handle_request("GET", url)

    def get_terminal_status(self, terminal_id: str) -> Response:
        """Check the availiability of a Terminal before sending an event to it.

        Parameters
        ----------
        terminal_id: str
            The ID of the Terminal you want to check

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/terminal/{terminal_id}/presence")
        return self._handle_request("GET", url)

    def get_terminals(
        self, pagination=50, next: Optional[str] = None, previous: Optional[str] = None
    ) -> Response:
        """List the Terminals available on your integration

        Parameters
        ----------
        pagination: int
            Specify how many records you want to retrieve per page. If not specified, it defaults to 50.
        next: str
            Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        previous: str
            A cursor that indicates your place in the list. It should be used to fetch the previous page of the
            list after an intial next request

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/terminal?perPage={pagination}")
        query_params = [
            ("next", next),
            ("previous", previous),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_terminal(self, terminal_id: str) -> Response:
        """Get the details of a Terminal

        Parameters
        ----------
        terminal_id: str
            The ID of the Terminal the event was sent to.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/terminal/{terminal_id}/")
        return self._handle_request("GET", url)

    def updated_terminal(self, terminal_id: str, name: str, address: str) -> Response:
        """Update the details of a Terminal

        Parameters
        ----------
        terminal_id: str
            The ID of the Terminal you want to update
        name: str
            Name of the terminal
        address: str
            The address of the Terminal

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/terminal/{terminal_id}")

        payload = {"name": name, "address": address}
        return self._handle_request("PUT", url, payload)

    def commission_terminal(self, serial_number: str) -> Response:
        """Activate your debug device by linking it to your integration

        Parameters
        ----------
        serial_number: str
            Device Serial Number

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/terminal/commission_device")

        payload = {
            "serial_number": serial_number,
        }
        return self._handle_request("POST", url, payload)

    def decommission_terminal(self, serial_number: str) -> Response:
        """Unlink your debug device from your integration

        Parameters
        ----------
        serial_number: str
            Device Serial Number

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/terminal/decommission_device")

        payload = {
            "serial_number": serial_number,
        }
        return self._handle_request("POST", url, payload)
