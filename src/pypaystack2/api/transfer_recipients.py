from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.exceptions import InvalidDataException
from pypaystack2.utils import (
    Currency,
    RecipientType,
    add_to_payload,
    append_query_params,
    HTTPMethod,
    Response,
    Recipient,
)


class TransferRecipient(BaseAPI):
    """Provides a wrapper for paystack Transfer Receipts API

    The Transfer Recipients API allows you to create and manage beneficiaries that you send money to.
    https://paystack.com/docs/api/transfer-recipient/

    Note:
        Feature Availability
            This feature is only available to businesses in Nigeria and Ghana.
    """

    def create(
        self,
        type: RecipientType,
        name: str,
        account_number: str,
        bank_code: Optional[str] = None,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        auth_code: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """
        Creates a new recipient. A duplicate account number will lead to the
        retrieval of the existing record.

        Args:
            type: Recipient Type. any value from the ``TRType`` enum
            name: A name for the recipient
            account_number: Required if ``type`` is ``TRType.NUBAN`` or ``TRType.BASA``
            bank_code: Required if ``type`` is ``TRType.NUBAN`` or ``TRType.BASA``.
                You can get the list of Bank Codes by calling the ``.get_banks``
                method from the Miscellaneous API wrapper.
            description: description
            currency: currency
            auth_code: auth code
            metadata: metadata

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        # FIXME: type is a keyword arg, might replace
        # if it raises issues.
        if type == RecipientType.NUBAN or type == RecipientType.BASA:
            if bank_code is None:
                raise InvalidDataException(
                    "`bank_code` is required if type is `TRType.NUBAN` or `TRType.BASA`"
                )

        url = self._parse_url("/transferrecipient")

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
        return self._handle_request(HTTPMethod.POST, url, payload)

    def bulk_create(self, batch: list[Recipient]) -> Response:
        # TODO: create a pydantic model
        # for batch using the fields below.
        # type: RecipientType,
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

        Ars:
            batch: A list of dictionaries of transfer recipients. Each dictionary should contain
                ``type``, ``name``, and ``bank_code``. Any Create Transfer Recipient param
                can also be passed.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        batch = [item.dict for item in batch]

        url = self._parse_url("/transferrecipient/bulk")

        payload = {
            "batch": batch,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_transfer_recipients(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch transfer recipients available on your integration

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing transfer recipients
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transferrecipient?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_transfer_recipient(self, id_or_code: str) -> Response:
        """Fetch the details of a transfer recipient

        Args:
            id_or_code: An ID or code for the recipient whose details you want to receive.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transferrecipient/{id_or_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def update(
        self, id_or_code: str, name: str, email: Optional[str] = None
    ) -> Response:
        """
        Update an existing recipient. An duplicate account number will lead
        to the retrieval of the existing record.

        Args:
            id_or_code: Transfer Recipient's ID or code
            name: A name for the recipient
            email: Email address of the recipient

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transferrecipient/{id_or_code}")
        payload = {"name": name}
        optional_params = [("email", email)]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.PUT, url, payload)

    def delete(self, id_or_code: str) -> Response:
        """Deletes a transfer recipient (sets the transfer recipient to inactive)

        Args:
            id_or_code: An ID or code for the recipient who you want to delete.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transferrecipient/{id_or_code}")
        return self._handle_request(HTTPMethod.DELETE, url)


class AsyncTransferRecipient(BaseAsyncAPI):
    """Provides a wrapper for paystack Transfer Receipts API

    The Transfer Recipients API allows you to create and manage beneficiaries that you send money to.
    https://paystack.com/docs/api/transfer-recipient/

    Note:
        Feature Availability
            This feature is only available to businesses in Nigeria and Ghana.
    """

    async def create(
        self,
        type: TransferRecipient,
        name: str,
        account_number: str,
        bank_code: Optional[str] = None,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        auth_code: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Response:
        """
        Creates a new recipient. A duplicate account number will lead to the
        retrieval of the existing record.

        Args:
            type: Recipient Type. any value from the ``TRType`` enum
            name: A name for the recipient
            account_number: Required if ``type`` is ``TRType.NUBAN`` or ``TRType.BASA``
            bank_code: Required if ``type`` is ``TRType.NUBAN`` or ``TRType.BASA``.
                You can get the list of Bank Codes by calling the ``.get_banks``
                method from the Miscellaneous API wrapper.
            description: description
            currency: currency
            auth_code: auth code
            metadata: metadata

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        # FIXME: type is a keyword arg, might replace
        # if it raises issues.
        if type == RecipientType.NUBAN or type == RecipientType.BASA:
            if bank_code is None:
                raise InvalidDataException(
                    "`bank_code` is required if type is `TRType.NUBAN` or `TRType.BASA`"
                )

        url = self._parse_url("/transferrecipient")

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
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def bulk_create(self, batch: list[Recipient]) -> Response:
        # TODO: create a pydantic model
        # for batch using the fields below.
        # type: RecipientType,
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

        Ars:
            batch: A list of dictionaries of transfer recipients. Each dictionary should contain
                ``type``, ``name``, and ``bank_code``. Any Create Transfer Recipient param
                can also be passed.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        # FIXME: type is a keyword arg, might replace
        # if it raises issues.

        batch = [item.dict for item in batch]

        url = self._parse_url("/transferrecipient/bulk")

        payload = {
            "batch": batch,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_transfer_recipients(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch transfer recipients available on your integration

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing transfer recipients
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transferrecipient?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_transfer_recipient(self, id_or_code: str) -> Response:
        """Fetch the details of a transfer recipient

        Args:
            id_or_code: An ID or code for the recipient whose details you want to receive.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transferrecipient/{id_or_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def update(
        self, id_or_code: str, name: str, email: Optional[str] = None
    ) -> Response:
        """
        Update an existing recipient. An duplicate account number will lead
        to the retrieval of the existing record.

        Args:
            id_or_code: Transfer Recipient's ID or code
            name: A name for the recipient
            email: Email address of the recipient

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transferrecipient/{id_or_code}")
        payload = {"name": name}
        optional_params = [("email", email)]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.PUT, url, payload)

    async def delete(self, id_or_code: str) -> Response:
        """Deletes a transfer recipient (sets the transfer recipient to inactive)

        Args:
            id_or_code: An ID or code for the recipient who you want to delete.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/transferrecipient/{id_or_code}")
        return await self._handle_request(HTTPMethod.DELETE, url)
