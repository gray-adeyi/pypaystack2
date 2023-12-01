from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    Currency,
    add_to_payload,
    append_query_params,
    validate_amount,
    HTTPMethod,
    Response,
    TransferInstruction,
)


class Transfer(BaseAPI):
    """Provides a wrapper for paystack Transfers API

    The Transfers API allows you to automate sending money on your integration
    https://paystack.com/docs/api/transfer/

    Note
    ----
    This feature is only available to businesses in Nigeria and Ghana.
    """

    def initiate(
        self,
        amount: int,
        recipient: str,
        reason: Optional[str] = None,
        currency: Optional[Currency] = None,
        reference: Optional[str] = None,
        source: str = "balance",
    ) -> Response:
        """Initiate transfer

        Args:
            amount: amount to transfer
            recipient: the beneficiary of the transfer
            reason: narration of the transfer
            currency: transfer currency
            reference: reference id
            source: transfer source

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        amount = validate_amount(amount)

        url = self._parse_url("/transfer")

        payload = {
            "amount": amount,
            "recipient": recipient,
            "source": source,
        }
        optional_params = [
            ("reason", reason),
            ("reference", reference),
            ("currency", currency),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def finalize(
        self,
        transfer_code: str,
        otp: str,
    ) -> Response:
        """Finalize transfer

        Args:
            transfer_code: The code for transfer.
            otp: One time password.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/transfer/finalize_transfer")

        payload = {
            "transfer_code": transfer_code,
            "otp": otp,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def bulk_transfer(
        self, transfers: list[TransferInstruction], source: str = "balance"
    ) -> Response:
        """Transfer in bulk

        Args:
            transfers: list of transfer instructions
            source: source of the funds to transfer

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/transfer/bulk")

        payload = {
            "transfers": [tx.dict for tx in transfers],
            "source": source,
        }
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_transfers(
        self,
        page: int = 1,
        pagination: int = 50,
        customer: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Retrieve transfers made to a customer

        Args:
            customer: customer id
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing refund e.g. 2016-09-21
            end_date: A timestamp at which to stop listing refund e.g. 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transfer?perPage={pagination}")
        query_params = [
            ("customer", customer),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_transfer(
        self,
        id_or_code: str,
    ) -> Response:
        """Retrieve a transfer

        Args:
            id_or_code: transfer ID or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transfer/{id_or_code}")
        return self._handle_request(HTTPMethod.GET, url)

    def verify(
        self,
        reference: str,
    ) -> Response:
        """Verify a transfer

        Args:
            reference: str

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transfer/verify/{reference}")
        return self._handle_request(HTTPMethod.GET, url)


class AsyncTransfer(BaseAsyncAPI):
    """Provides a wrapper for paystack Transfers API

    The Transfers API allows you to automate sending money on your integration
    https://paystack.com/docs/api/transfer/

    Note
    ----
    This feature is only available to businesses in Nigeria and Ghana.
    """

    async def initiate(
        self,
        amount: int,
        recipient: str,
        reason: Optional[str] = None,
        currency: Optional[Currency] = None,
        reference: Optional[str] = None,
        source: str = "balance",
    ) -> Response:
        """Initiate transfer

        Args:
            amount: amount to transfer
            recipient: the beneficiary of the transfer
            reason: narration of the transfer
            currency: transfer currency
            reference: reference id
            source: transfer source

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        amount = validate_amount(amount)

        url = self._parse_url("/transfer")

        payload = {
            "amount": amount,
            "recipient": recipient,
            "source": source,
        }
        optional_params = [
            ("reason", reason),
            ("reference", reference),
            ("currency", currency),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def finalize(
        self,
        transfer_code: str,
        otp: str,
    ) -> Response:
        """Finalize transfer

        Args:
            transfer_code: The code for transfer.
            otp: One time password.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/transfer/finalize_transfer")

        payload = {
            "transfer_code": transfer_code,
            "otp": otp,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def bulk_transfer(
        self, transfers: list[TransferInstruction], source: str = "balance"
    ) -> Response:
        """Transfer in bulk

        Args:
            transfers: list of transfer instructions
            source: source of the funds to transfer

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url("/transfer/bulk")

        payload = {
            "transfers": [tx.dict for tx in transfers],
            "source": source,
        }
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_transfers(
        self,
        page: int = 1,
        pagination: int = 50,
        customer: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Retrieve transfers made to a customer

        Args:
            customer: customer id
            page: Specifies exactly what page you want to retrieve.
                If not specified, we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified, we use a default value of 50.
            start_date: A timestamp from which to start listing refund e.g. 2016-09-21
            end_date: A timestamp at which to stop listing refund e.g. 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transfer?perPage={pagination}")
        query_params = [
            ("customer", customer),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_transfer(
        self,
        id_or_code: str,
    ) -> Response:
        """Retrieve a transfer

        Args:
            id_or_code: transfer ID or code

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transfer/{id_or_code}")
        return await self._handle_request(HTTPMethod.GET, url)

    async def verify(
        self,
        reference: str,
    ) -> Response:
        """Verify a transfer

        Args:
            reference: str

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(f"/transfer/verify/{reference}")
        return await self._handle_request(HTTPMethod.GET, url)
