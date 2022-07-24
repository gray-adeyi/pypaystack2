from typing import Mapping, Optional

from pypaystack2.errors import InvalidDataError
from ..baseapi import BaseAPI, Response
from ..utils import (
    Currency,
    TRType,
    add_to_payload,
    append_query_params,
    validate_amount,
    validate_interval,
)


class TransferReceipt(BaseAPI):
    """Provides a wrapper for paystack Transfer Receipts API

    The Transfer Recipients API allows you create and manage beneficiaries that you send money to.
    https://paystack.com/docs/api/#transfer-recipient

    Note
    ----
    Feature Availability
        This feature is only available to businesses in Nigeria and Ghana.
    """

    def create(
        self,
        type: TRType,
        name: str,
        account_number: str,
        bank_code: Optional[str] = None,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        auth_code: Optional[str] = None,
        metadata: Optional[Mapping] = None,
    ) -> Response:
        """
        Creates a new recipient. A duplicate account number will lead to the
        retrieval of the existing record.

        Parameters
        ----------
        type: TRType
            Recipient Type. any value from the ``TRType`` enum
        name: str
            A name for the recipient
        account_number: str
            Required if ``type`` is ``TRType.NUBAN`` or ``TRType.BASA``
        bank_code: Optional[str]
            Required if ``type`` is ``TRType.NUBAN`` or ``TRType.BASA``.
            You can get the list of Bank Codes by calling the ``.get_banks``
            method from the Miscellaneous API wrapper.
        description: Optional[str]
        currency: Optional[Currency]
        auth_code: Optional[str]
        metadata: Optional[Mapping]

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        # FIXME: type is a keyword arg, might replace
        # if it raises issues.
        if type == TRType.NUBAN or type == TRType.BASA:
            if bank_code is None:
                raise InvalidDataError(
                    "`bank_code` is required if type is `TRType.NUBAN` or `TRType.BASA`"
                )

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._url("/transferrecipient")

        payload = {
            "type": type,
            "name": name,
            "account_number": account_number,
        }
        optional_params = [
            ("bank_code", bank_code),
            ("description", description),
            ("currency", currency),
            ("authorization_code", auth_code),
            ("metadata", metadata),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("POST", url, payload)

    def bulk_create(self, batch: list) -> Response:
        # TODO: create a pydantic model
        # for batch using the fields below.
        # type: TRType,
        # name: str,
        # account_number: str,
        # bank_code: Optional[str] = None,
        # description: Optional[str] = None,
        # currency: Optional[utils.Currency] = None,
        # auth_code: Optional[str] = None,
        # metadata: Optional[Mapping] = None,
        """
        Create multiple transfer recipients in batches. A duplicate account
        number will lead to the retrieval of the existing record.

        Parameters
        ----------
        batch: list
            A list of dictionaries of transfer recipients. Each dictionary should contain
            ``type``, ``name``, and ``bank_code``. Any Create Transfer Recipient param
            can also be passed.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        # FIXME: type is a keyword arg, might replace
        # if it raises issues.
        for tr in batch:
            if tr.type == TRType.NUBAN or tr.type == TRType.BASA:
                if tr.bank_code is None:
                    raise InvalidDataError(
                        "`bank_code` is required if type is `TRType.NUBAN` or `TRType.BASA`"
                    )

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._url("/transferrecipient/bulk")

        payload = {
            "batch": batch,
        }
        return self._handle_request("POST", url, payload)

    def get_transfer_receipts(
        self,
        page=1,
        pagination=50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch transfer recipients available on your integration

        Parameters
        ----------
        page: int
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        pagination: int
            Specify how many records you want to retrieve per page.
            If not specified we use a default value of 50.
        start_date: Optional[str]
            A timestamp from which to start listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        end_date: Optional[str]
            A timestamp at which to stop listing transfer recipients
            e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/transferrecipient?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_transfer_receipt(self, id_or_code: str) -> Response:
        """Fetch the details of a transfer recipient

        Parameters
        ----------
        id_or_code: str
            An ID or code for the recipient whose details you want to receive.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url(f"/transferrecipient/{id_or_code}")
        return self._handle_request("GET", url)

    def update(
        self, id_or_code: str, name: str, email: Optional[str] = None
    ) -> Response:
        """
        Update an existing recipient. An duplicate account number will lead
        to the retrieval of the existing record.

        Parameters
        ----------
        id_or_code: str
            Transfer Recipient's ID or code
        name: str
            A name for the recipient
        email: Optional[str]
            Email address of the recipient

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/transferrecipient/{id_or_code}")
        payload = {"name": name}
        optional_params = {"email": email}
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("PUT", url, payload)

    def delete(self, id_or_code: str) -> Response:
        """Deletes a transfer recipient (sets the transfer recipient to inactive)

        Parameters
        ----------
        id_or_code: str
            An ID or code for the recipient who you want to delete.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/transferrecipient/{id_or_code}")
        return self._handle_request("DELETE", url)
