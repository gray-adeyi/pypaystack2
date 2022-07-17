from typing import Mapping, Optional

from pypaystack2.errors import InvalidDataError
from .baseapi import BaseAPI
from . import utils
from .utils import TRType, add_to_payload, append_query_params


class TransferReceipt(BaseAPI):
    """
    The Plans API allows you create
    and manage installment payment
    options on your integration
    """

    def create(
        self,
        type: TRType,
        name: str,
        account_number: str,
        bank_code: Optional[str] = None,
        description: Optional[str] = None,
        currency: Optional[utils.Currency] = None,
        auth_code: Optional[str] = None,
        metadata: Optional[Mapping] = None,
    ):
        """ """
        # TODO: type is a keyword arg, might replace
        # if it raises issues.
        if type == TRType.NUBAN or type == TRType.BASA:
            if bank_code is None:
                raise InvalidDataError(
                    "`bank_code` is required if type is `TRType.NUBAN` or `TRType.BASA`"
                )

        interval = utils.validate_interval(interval)
        amount = utils.validate_amount(amount)

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

    def bulk_create(self, batch: list):  # TODO: create a pydantic model
        """
        type: TRType,
        name: str,
        account_number: str,
        bank_code: Optional[str] = None,
        description: Optional[str] = None,
        currency: Optional[utils.Currency] = None,
        auth_code: Optional[str] = None,
        metadata: Optional[Mapping] = None,
        """
        # TODO: type is a keyword arg, might replace
        # if it raises issues.
        for tr in batch:
            if tr.type == TRType.NUBAN or tr.type == TRType.BASA:
                if tr.bank_code is None:
                    raise InvalidDataError(
                        "`bank_code` is required if type is `TRType.NUBAN` or `TRType.BASA`"
                    )

        interval = utils.validate_interval(interval)
        amount = utils.validate_amount(amount)

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
    ):
        """ """
        url = self._url(f"/transferrecipient?perPage={pagination}")
        query_params = [
            ("page", page),
            ("from", start_date),
            ("to", end_date),
        ]
        url = append_query_params(query_params, url)
        return self._handle_request("GET", url)

    def get_transfer_receipt(self, id_or_code: str):
        """ """
        url = self._url(f"/transferrecipient/{id_or_code}")
        return self._handle_request("GET", url)

    def update(self, id_or_code: str, name: str, email: Optional[str] = None):
        """"""

        url = self._url(f"/transferrecipient/{id_or_code}")
        payload = {"name": name}
        optional_params = {"email": email}
        payload = add_to_payload(optional_params, payload)
        return self._handle_request("PUT", url, payload)

    def delete(self, id_or_code: str):
        """"""

        url = self._url(f"/transferrecipient/{id_or_code}")
        return self._handle_request("DELETE", url)
