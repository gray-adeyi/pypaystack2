from typing import Optional

from ..baseapi import BaseAPI, Response
from ..utils import (
    PlanStatus,
    add_to_payload,
    Interval,
    Currency,
    append_query_params,
    validate_amount,
    validate_interval,
)


class Plan(BaseAPI):
    """Provides a wrapper for paystack Plans API

    The Plans API allows you create and manage installment payment options on your integration.
    https://paystack.com/docs/api/#plan
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

        Parameters
        ----------
        name: str
            Name of plan
        amount: int
            Amount should be in kobo if currency is ``Currency.NGN``, pesewas,
            if currency is ``Currency.GHS``, and cents, if currency is ``Currency.ZAR``
        interval: Interval
            Any value from the ``Interval`` enum.
        description: Optional[str]
            A description for this plan
        currency: Optional[Currency]
            Currency in which amount is set. Any of the value from
            the ``Currency`` enum
        invoice_limit: Optional[int]
            Number of invoices to raise during subscription to this plan.
            Can be overridden by specifying an ``invoice_limit`` while subscribing
        send_invoices: bool
            Set to ``False`` if you don't want invoices to be sent to your customers
        send_sms: bool
            Set to ``False`` if you don't want text messages to be sent to your customers

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._url("/plan/")

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
        return self._handle_request("POST", url, payload)

    def get_plans(
        self,
        page=1,
        pagination=50,
        status: Optional[PlanStatus] = None,
        interval: Optional[Interval] = None,
        amount: Optional[int] = None,
    ) -> Response:
        """Fetch plans available on your integration.

        Parameters
        ----------
        page: int
            Specify exactly what page you want to retrieve.
            If not specify we use a default value of 1.
        pagination:int
            Specify how many records you want to retrieve per page.
            If not specify we use a default value of 50.
        status: Optional[PlanStatus]
            Filter list by plans with specified status
        interval: Optional[Interval]
            Filter list by plans with specified interval
        amount: Optional[int]
            Filter list by plans with specified amount ( kobo if currency
            is ``Currency.NGN``, pesewas, if currency is ``Currency.GHS``,
            and cents, if currency is ``Currency.ZAR``)

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        if amount:
            amount = validate_amount(amount)

        url = self._url(f"/plan/?perPage={pagination}")
        query_params = [
            ("page", page),
            ("status", status),
            ("interval", interval),
            ("amount", amount),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_plan(self, id_or_code: str) -> Response:
        """Get details of a plan on your integration.

        Parameters
        ----------
        id_or_code: str
            The plan ``ID`` or ``code`` you want to fetch

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._url("/plan/{}/".format(id_or_code))
        return self._handle_request("GET", url)

    def update(
        self,
        id_or_code: str,
        name: str,
        amount: int,
        interval: Interval,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        invoice_limit: Optional[int] = None,
        send_invoices: bool = False,
        send_sms: bool = False,
    ) -> Response:
        """

        Parameters
        ----------
        id_or_code: str
            Plan's ID or code
        name: str
            Name of plan
        amount: int
            Amount should be in kobo if currency is
            ``Currency.NGN`` and pesewas for ``Currency.GHS``
        interval: Interval
            Any value from the ``Interval`` enum.
        description: Optional[str]
            A description for this plan.
        currency: Optional[Currency]
            Any value from the ``Currency`` enum.
        invoice_limit: Optional[int]
            Number of invoices to raise during subscription to this plan.
            Can be overridden by specifying an ``invoice_limit`` while subscribing.
        send_invoices: bool
            Set to ``False`` if you don't want invoices
            to be sent to your customers
        send_sms: bool
            Set to ``False`` if you don't want text messages to
            be sent to your customers

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._url("/plan/{}/".format(id_or_code))
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
        return self._handle_request("PUT", url, payload)
