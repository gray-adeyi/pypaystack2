from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import (
    add_to_payload,
    Interval,
    Currency,
    append_query_params,
    validate_amount,
    validate_interval,
    HTTPMethod,
    Response,
    Status,
)


class Plan(BaseAPI):
    """Provides a wrapper for paystack Plans API

    The Plans API allows you to create and manage installment payment options on your integration.
    https://paystack.com/docs/api/plan/
    """

    def create(
        self,
        name: str,
        amount: int,
        interval: Interval,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        invoice_limit: Optional[int] = None,
        send_invoices: bool = False,
        send_sms: bool = False,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._parse_url("/plan/")

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
        return self._handle_request(HTTPMethod.POST, url, payload)

    def get_plans(
        self,
        page: int = 1,
        pagination: int = 50,
        status: Optional[Status] = None,
        interval: Optional[Interval] = None,
        amount: Optional[int] = None,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if amount:
            amount = validate_amount(amount)

        url = self._parse_url(f"/plan/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("status", status),
            ("interval", interval),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request(HTTPMethod.GET, url)

    def get_plan(self, id_or_code: str) -> Response:
        """Get details of a plan on your integration.

        Args:
            id_or_code: The plan ``ID`` or ``code`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/plan/{}/".format(id_or_code))
        return self._handle_request(HTTPMethod.GET, url)

    def update(
        self,
        id_or_code: str,
        name: Optional[str],
        amount: Optional[int],
        interval: Optional[Interval],
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        invoice_limit: Optional[int] = None,
        send_invoices: bool = False,
        send_sms: bool = False,
    ) -> Response:
        """

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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._parse_url("/plan/{}/".format(id_or_code))
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
        return self._handle_request(HTTPMethod.PUT, url, payload)


class AsyncPlan(BaseAsyncAPI):
    """Provides a wrapper for paystack Plans API

    The Plans API allows you to create and manage installment payment options on your integration.
    https://paystack.com/docs/api/plan/
    """

    async def create(
        self,
        name: str,
        amount: int,
        interval: Interval,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        invoice_limit: Optional[int] = None,
        send_invoices: bool = False,
        send_sms: bool = False,
    ) -> Response:
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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._parse_url("/plan/")

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
        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def get_plans(
        self,
        page: int = 1,
        pagination: int = 50,
        status: Optional[Status] = None,
        interval: Optional[Interval] = None,
        amount: Optional[int] = None,
    ) -> Response:
        """Fetch plans available on your integration.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            status: Filter list by plans with specified status
            interval: Filter list by plans with specified interval
            amount: Filter list by plans with specified amount ( kobo if currency
                is ``Currency.NGN``, pesewas, if currency is ``Currency.GHS``,
                and cents, if currency is ``Currency.ZAR``)

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        if amount:
            amount = validate_amount(amount)

        url = self._parse_url(f"/plan/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("status", status),
            ("interval", interval),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(HTTPMethod.GET, url)

    async def get_plan(self, id_or_code: str) -> Response:
        """Get details of a plan on your integration.

        Args:
            id_or_code: The plan ``ID`` or ``code`` you want to fetch

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url("/plan/{}/".format(id_or_code))
        return await self._handle_request(HTTPMethod.GET, url)

    async def update(
        self,
        id_or_code: str,
        name: Optional[str] = None,
        amount: Optional[int] = None,
        interval: Optional[Interval] = None,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        invoice_limit: Optional[int] = None,
        send_invoices: bool = False,
        send_sms: bool = False,
    ) -> Response:
        """

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

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._parse_url("/plan/{}/".format(id_or_code))
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
        return await self._handle_request(HTTPMethod.PUT, url, payload)
