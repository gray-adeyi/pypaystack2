from typing import Optional

from ..baseapi import BaseAPI
from ..utils import (
    add_to_payload,
    Interval,
    Currency,
    validate_amount,
    validate_interval,
)


class Plan(BaseAPI):
    """
    The Plans API allows you create
    and manage installment payment
    options on your integration
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
    ):
        """
        Creates a new plan. Returns the plan details created

        args:
        name -- Name of the plan to create
        amount -- Amount to attach to this plan
        interval -- enum pypaystack2.utils.Interval.[HOURLY,DAILY,WEEKLY,MONTHLY,ANNUALLY]
        description -- Plan Description (optional)

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

    def get_plan(self, id_or_code: str):
        """
        Gets one plan with the given plan id
        Requires: plan_id
        """
        url = self._url("/plan/{}/".format(id_or_code))
        return self._handle_request("GET", url)

    def get_plans(self, pagination=50):
        """
        Gets all plans
        """
        url = self._url(f"/plan/?perPage=" + str(pagination))
        return self._handle_request("GET", url)

    def update(
        self,
        plan_id: str,
        name: str,
        amount: int,
        interval: Interval,
        description: Optional[str] = None,
        currency: Optional[Currency] = None,
        invoice_limit: Optional[int] = None,
        send_invoices: bool = False,
        send_sms: bool = False,
    ):
        """
        Updates an existing plan given a plan id. Returns the plan details updated.

        args:
        plan_id -- Plan Id to update
        name -- New plan name
        amount -- New Amount to attach to this plan
        interval -- enum pypaystack2.utils.Interval.[HOURLY,DAILY,WEEKLY,MONTHLY,ANNUALLY]
        description -- Plan Description (optional)
        """
        interval = validate_interval(interval)
        amount = validate_amount(amount)

        url = self._url("/plan/{}/".format(plan_id))
        required_params = {
            "name": name,
            "amount": amount,
            "interval": interval,
        }
        optional_params = {"send_invoices": send_invoices, "send_sms": send_sms}
        # TODO: find a cleaner way to update optinal parameters dict.
        if description is not None:
            optional_params["description"] = description

        if currency is not None:
            optional_params["currency"] = currency

        if invoice_limit is not None:
            optional_params["invoice_limit"] = invoice_limit

        payload = {**required_params, **optional_params}
        return self._handle_request("PUT", url, payload)
