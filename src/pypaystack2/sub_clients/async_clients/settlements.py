from http import HTTPMethod
from typing import Type

from pypaystack2 import Response
from pypaystack2.base_api_client import BaseAsyncAPIClient
from pypaystack2.utils import append_query_params
from pypaystack2.utils.models import PaystackDataModel
from pypaystack2.utils.response_models import Settlement, Transaction


class AsyncSettlementClient(BaseAsyncAPIClient):
    """Provides a wrapper for paystack Settlement API

    The Settlements API allows you to gain insights into payouts made by Paystack to your bank account.
    https://paystack.com/docs/api/settlement/
    """

    async def get_settlements(
        self,
        page: int = 1,
        pagination: int = 50,
        start_date: str | None = None,
        end_date: str | None = None,
        subaccount: str | None = None,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[Settlement]:
        """Fetch settlements made to your settlement accounts.

        Args:
            page: Specifies exactly what page you want to retrieve.
                If not specified we use a default value of 1.
            pagination: Specifies how many records you want to retrieve per page.
                If not specified we use a default value of 50.
            start_date: A timestamp from which to start listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            subaccount: Provide a subaccount ID to export only settlements for that subaccount.
                Set to ``none`` to export only transactions for the account.
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/settlement?perPage={pagination}")
        query_params = [
            ("subaccount", subaccount),
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Settlement,
        )

    async def get_settlement_transactions(
        self,
        id: str,
        pagination: int = 50,
        page: int = 1,
        start_date: str | None = None,
        end_date: str | None = None,
        alternate_model_class: Type[PaystackDataModel] | None = None,
    ) -> Response[Transaction]:
        """Get the transactions that make up a particular settlement

        Args:
            id: The settlement ID in which you want to fetch its transactions
            pagination: Specifies how many records you want to retrieve per page. If not specified we
                use a default value of 50.
            page: Specifies exactly what page you want to retrieve. If not specified we use a default value of 1.
            start_date: A timestamp from which to start listing settlement transactions
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            end_date: A timestamp at which to stop listing settlement transactions
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
            alternate_model_class: A pydantic model class to use instead of the
                default pydantic model used by the library to present the data in
                the `Response.data`. The default behaviour of the library is to
                set  `Response.data` to `None` if it fails to serialize the data
                returned from paystack with the model provided in the library.
                Providing a pydantic model class via this parameter overrides
                the library default model with the model class you provide.
                This can come in handy when the models in the library do not
                accurately represent the data returned, and you prefer working with the
                data as a pydantic model instead of as a dict of the response returned
                by  paystack before it is serialized with pydantic models, The original
                data can be accessed via `Response.raw`.

        Returns:
            A pydantic model containing the response gotten from paystack's server.
        """

        url = self._full_url(f"/settlement/{id}/transactions?perPage={pagination}")
        query_params = [
            ("page", page),
            ("start_date", start_date),
            ("end_date", end_date),
        ]
        url = append_query_params(query_params, url)
        return await self._handle_request(
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or Transaction,
        )
