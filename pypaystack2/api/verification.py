from typing import Optional

from pypaystack2.baseapi import BaseAPI, BaseAsyncAPI
from pypaystack2.utils import AccountType, Country, Document, HTTPMethod, Response


class Verification(BaseAPI):
    """Provides a wrapper for paystack Verification API

    The Verification API allows you to perform KYC processes.
    https://paystack.com/docs/api/verification/

    Note:
        This feature is only available to businesses in Nigeria.
    """

    def resolve_account_number(
        self,
        account_number: str,
        bank_code: str,
    ) -> Response:
        """Confirm an account belongs to the right customer

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria.

        Args:
            account_number: Account Number
            bank_code: You can get the list of bank codes by calling the
                Miscellaneous API wrapper ``.get_banks`` method.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(
            f"/bank/resolve?account_number={account_number}&bank_code={bank_code}"
        )
        return self._handle_request(HTTPMethod.GET, url)

    def validate_account(
        self,
        account_name: str,
        account_number: str,
        account_type: AccountType,
        bank_code: str,
        country_code: Country,
        document_type: Document,
        document_number: Optional[str] = None,
    ) -> Response:
        """Confirm the authenticity of a customer's account number before sending money

        Args:
            account_name: Customer's first and last name registered with their bank
            account_number: Customer's account number
            account_type: bank_code: The bank code of the customer’s bank. You can fetch the bank codes by
                using Miscellaneous API wrapper ``.get_banks`` method.
            bank_code: The bank code of the customer’s bank
            country_code: Any value from the ``Country`` enum
            document_type: Customer’s mode of identity. any value from the
                ``DocumentType`` enum.
            document_number: Customer’s mode of identity number

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        payload = {
            "account_name": account_name,
            "account_number": account_number,
            "account_type": account_type,
            "bank_code": bank_code,
            "country_code": country_code,
            "document_type": document_type,
            "document_number": document_number,
        }
        url = self._parse_url("/bank/validate")

        return self._handle_request(HTTPMethod.POST, url, payload)

    def resolve_card_bin(self, bin: str) -> Response:
        """Get more information about a customer's card

        Args:
            bin: First 6 characters of card


        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/decision/bin/{bin}")
        return self._handle_request(HTTPMethod.GET, url)


class AsyncVerification(BaseAsyncAPI):
    """Provides a wrapper for paystack Verification API

    The Verification API allows you to perform KYC processes.
    https://paystack.com/docs/api/verification/

    Note:
        This feature is only available to businesses in Nigeria.
    """

    async def resolve_account_number(
        self,
        account_number: str,
        bank_code: str,
    ) -> Response:
        """Confirm an account belongs to the right customer

        Note:
            Feature Availability
                This feature is only available to businesses in Nigeria.

        Args:
            account_number: Account Number
            bank_code: You can get the list of bank codes by calling the
                Miscellaneous API wrapper ``.get_banks`` method.

        Returns:
            A named tuple containing the response gotten from paystack's server.
        """
        url = self._parse_url(
            f"/bank/resolve?account_number={account_number}&bank_code={bank_code}"
        )
        return await self._handle_request(HTTPMethod.GET, url)

    async def validate_account(
        self,
        account_name: str,
        account_number: str,
        account_type: AccountType,
        bank_code: str,
        country_code: Country,
        document_type: Document,
        document_number: Optional[str] = None,
    ) -> Response:
        """Confirm the authenticity of a customer's account number before sending money

        Args:
            account_name: Customer's first and last name registered with their bank
            account_number: Customer's account number
            account_type: bank_code: The bank code of the customer’s bank. You can fetch the bank codes by
                using Miscellaneous API wrapper ``.get_banks`` method.
            bank_code: The bank code of the customer’s bank
            country_code: Any value from the ``Country`` enum
            document_type: Customer’s mode of identity. any value from the
                ``DocumentType`` enum.
            document_number: Customer’s mode of identity number

        Returns:
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
        url = self._parse_url("/bank/validate")

        return await self._handle_request(HTTPMethod.POST, url, payload)

    async def resolve_card_bin(self, bin: str) -> Response:
        """Get more information about a customer's card

        Args:
            bin: First 6 characters of card


        Returns:
            A named tuple containing the response gotten from paystack's server.
        """

        url = self._parse_url(f"/decision/bin/{bin}")
        return await self._handle_request(HTTPMethod.GET, url)
