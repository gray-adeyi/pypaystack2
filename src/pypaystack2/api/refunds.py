from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    Currency,
    add_to_payload,
    append_query_params,
    validate_amount,
    HTTPMethod,
    Response,
)


class Refund(BaseAPI):
    """Provides a wrapper for paystack Refunds API

    The Refunds API allows you to create and manage transaction refunds.
    https://paystack.com/docs/api/refund/
    """

    def create(
        self,
        transaction: str,
        amount: Optional[int] = None,
        currency: Optional[Currency] = None,
        customer_note: Optional[str] = None,
        merchant_note: Optional[str] = None,
    ) -> Response:
        """Initiate a refund on your integration

        Args:
            transaction: Transaction reference or id
            amount: Amount ( in kobo if currency is NGN, pesewas, if currency is
                GHS, and cents, if currency is ZAR ) to be refunded to the
                customer. Amount is optional(defaults to original
                transaction amount) and cannot be more than the original
                transaction amount
            currency: Any value from the ``Currency`` enum
            customer_note: Customer reason
            merchant_note: Merchant reason

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if amount is not None:
            amount = validate_amount(amount)
        url = self._parse_url("/refund")
        payload = {"transaction": transaction}
        optional_params = [
            ("amount", amount),
            ("currency", currency),
            ("customer_note", customer_note),
            ("merchant_note", merchant_note),
        ]
        payload = add_to_payload(optional_params, payload)
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_refunds(
        self,
        reference: Optional[str] = None,
        currency: Optional[Currency] = None,
        pagination: int = 50,
        page: int = 1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch refunds available on your integration.

        Args:
            reference: Identifier for transaction to be refunded
            currency: Any value from the ``Currency`` enum
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specifies exactly what refund you want to page.
                If not specified we use a default value of 1.
            start_date: A timestamp from which to start listing refund e.g. 2016-09-21
            end_date: A timestamp at which to stop listing refund e.g. 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/refund?perPage={pagination}")
        query_params = [
            ("reference", reference),
            ("currency", currency),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_refund(self, reference: str) -> Response:
        """Get details of a refund on your integration.

        Args:
            reference: Identifier for transaction to be refunded

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/refund/{reference}")
        return self._handle_request(HTTPMethod.GET, url)


class AsyncRefund(BaseAsyncAPI):
    """Provides a wrapper for paystack Refunds API

    The Refunds API allows you to create and manage transaction refunds.
    https://paystack.com/docs/api/refund/
    """

    async def create(
        self,
        transaction: str,
        amount: Optional[int] = None,
        currency: Optional[Currency] = None,
        customer_note: Optional[str] = None,
        merchant_note: Optional[str] = None,
    ) -> Response:
        """Initiate a refund on your integration

        Args:
            transaction: Transaction reference or id
            amount: Amount ( in kobo if currency is NGN, pesewas, if currency is
                GHS, and cents, if currency is ZAR ) to be refunded to the
                customer. Amount is optional(defaults to original
                transaction amount) and cannot be more than the original
                transaction amount
            currency: Any value from the ``Currency`` enum
            customer_note: Customer reason
            merchant_note: Merchant reason

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if amount is not None:
            amount = validate_amount(amount)
        url = self._parse_url("/refund")
        payload = {"transaction": transaction}
        optional_params = [
            ("amount", amount),
            ("currency", currency),
            ("customer_note", customer_note),
            ("merchant_note", merchant_note),
        ]
        payload = add_to_payload(optional_params, payload)
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_refunds(
        self,
        reference: Optional[str] = None,
        currency: Optional[Currency] = None,
        pagination: int = 50,
        page: int = 1,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Response:
        """Fetch refunds available on your integration.

        Args:
            reference: Identifier for transaction to be refunded
            currency: Any value from the ``Currency`` enum
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            page: Specifies exactly what refund you want to page.
                If not specified we use a default value of 1.
            start_date: A timestamp from which to start listing refund e.g. 2016-09-21
            end_date: A timestamp at which to stop listing refund e.g. 2016-09-21

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/refund?perPage={pagination}")
        query_params = [
            ("reference", reference),
            ("currency", currency),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_refund(self, reference: str) -> Response:
        """Get details of a refund on your integration.

        Args:
            reference: Identifier for transaction to be refunded

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/refund/{reference}")
        return await self._handle_request(HTTPMethod.GET, url)
