from typing import Optional
from .baseapi import BaseAPI
from . import utils


class Plan(BaseAPI):

    def create(self, name: str, amount: int, interval: utils.Interval, description: str | None = None,
               send_invoices: bool = False, send_sms: bool = False, currency: Optional[utils.Currency] = None, invoice_limit: Optional[int] = None):
        """
        Creates a new plan. Returns the plan details created

        args:
        name -- Name of the plan to create
        amount -- Amount to attach to this plan
        interval -- enum pypaystack2.utils.Interval.[HOURLY,DAILY,WEEKLY,MONTHLY,ANNUALLY]
        description -- Plan Description (optional)

        """
        # TODO: create enum for interval.
        interval = utils.validate_interval(interval)
        amount = utils.validate_amount(amount)

        url = self._url("/plan/")

        required_params = {
            "name": name,
            "amount": amount,
            "interval": interval,
        }
        optional_params = {
            "send_invoices": send_invoices,
            "send_sms": send_sms,
        }
        # TODO: find a cleaner way to update optinal parameters dict.
        if description is not None:
            optional_params['description'] = description

        if currency is not None:
            optional_params['currency'] = currency

        if invoice_limit is not None:
            optional_params['invoice_limit'] = invoice_limit

        payload = {**required_params, **optional_params}
        return self._handle_request('POST', url, payload)

    def update(self, plan_id: str, name: str, amount: int, interval: utils.Interval, description: str | None = None,
               send_invoices: bool = False, send_sms: bool = False,  currency: Optional[utils.Currency] = None, invoice_limit: Optional[int] = None):
        """
        Updates an existing plan given a plan id. Returns the plan details updated.

        args:
        plan_id -- Plan Id to update
        name -- New plan name
        amount -- New Amount to attach to this plan
        interval -- enum pypaystack2.utils.Interval.[HOURLY,DAILY,WEEKLY,MONTHLY,ANNUALLY]
        description -- Plan Description (optional)
        """
        # TODO: create enum for interval.
        interval = utils.validate_interval(interval)
        amount = utils.validate_amount(amount)

        url = self._url("/plan/{}/".format(plan_id))
        required_params = {
            "name": name,
            "amount": amount,
            "interval": interval,
        }
        optional_params = {
            'send_invoices': send_invoices,
            'send_sms': send_sms
        }
        # TODO: find a cleaner way to update optinal parameters dict.
        if description is not None:
            optional_params['description'] = description

        if currency is not None:
            optional_params['currency'] = currency

        if invoice_limit is not None:
            optional_params['invoice_limit'] = invoice_limit

        payload = {**required_params, **optional_params}
        return self._handle_request('PUT', url, payload)

    def getall(self, pagination=10):
        """
        Gets all plans
        """
        url = self._url("/plan/?perPage="+str(pagination))
        return self._handle_request('GET', url)

    def getone(self, plan_id: int):
        """
        Gets one plan with the given plan id
        Requires: plan_id
        """
        url = self._url("/plan/{}/".format(plan_id))
        return self._handle_request('GET', url)
