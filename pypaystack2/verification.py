from typing import Mapping, Optional

from pypaystack2.errors import InvalidDataError
from .baseapi import BaseAPI
from . import utils
from .utils import (
    AccountType,
    ChargeStatus,
    Country,
    Currency,
    DisputeStatus,
    DocumentType,
    Resolution,
    TRType,
    add_to_payload,
    append_query_params,
    validate_amount,
)


class Verification(BaseAPI):
    """
    The Verification API allows you perform KYC processes
    """

    def resolve_account_number(
        self,
        account_number: str,
        bank_code: str,
    ):
        """ """
        url = self._url(
            f"/bank/resolve?account_number={account_number}&bank_code={bank_code}"
        )
        return self._handle_request("GET", url)

    def validate_account(
        self,
        account_name: str,
        account_number: str,
        account_type: AccountType,
        bank_code: str,
        country_code: Country,
        document_type: DocumentType,
    ):
        payload = {
            "account_name": account_name,
            "account_number": account_number,
            "account_type": account_type,
            "bank_code": bank_code,
            "country_code": country_code,
            "document_type": document_type,
        }
        url = self._url(f"/bank/validate")

        return self._handle_request("POST", url, payload)

    def resolve_card_BIN(self, bin: str):
        url = self._url(f"/decision/bin/{bin}")
        return self._handle_request("GET", url)
