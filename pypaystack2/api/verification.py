from ..baseapi import BaseAPI, Response
from ..utils import AccountType, Country, DocumentType


class Verification(BaseAPI):
    """Provides a wrapper for paystack Verification API

    The Verification API allows you perform KYC processes.
    https://paystack.com/docs/api/#verification

    Note
    ----
    This feature is only available to businesses in Nigeria.
    """

    def resolve_account_number(
        self,
        account_number: str,
        bank_code: str,
    ) -> Response:
        """Confirm an account belongs to the right customer

        Parameters
        ----------
        account_number: str
            Account Number
        bank_code: str
            You can get the list of bank codes by calling the
            Miscellaneous API wrapper ``.get_banks`` method.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.

        Note
        ----
        Feature Availability
            This feature is only available to businesses in Nigeria.
        """
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
    ) -> Response:
        """Confirm the authenticity of a customer's account number before sending money

        Parameters
        ----------
        account_name: str
            Customer's first and last name registered with their bank
        account_number: str
            Customer's account number
        account_type: AccountType
        bank_code: str
            The bank code of the customer’s bank. You can fetch the bank codes by
            using Miscellaneous API wrapper ``.get_banks`` method.
        country_code: Country
            Any value from the ``Country`` enum
        document_type: DocumentType
            Customer’s mode of identity. any value from the
            ``DocumentType`` enum.

        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

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

    def resolve_card_BIN(self, bin: str) -> Response:
        """Get more information about a customer's card

        Parameters
        ----------
        bin: str
            First 6 characters of card


        Returns
        -------
        Response
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._url(f"/decision/bin/{bin}")
        return self._handle_request("GET", url)
