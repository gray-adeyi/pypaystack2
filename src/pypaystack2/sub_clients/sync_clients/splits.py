from http import HTTPMethod

from pypaystack2.base_clients import (
    BaseAPIClient,
    add_to_payload,
    append_query_params,
)
from pypaystack2.enums import Bearer, Currency, Split
from pypaystack2.models import Response
from pypaystack2.models.payload_models import SplitAccount
from pypaystack2.models.response_models import TransactionSplit
from pypaystack2.types import PaystackDataModel


class TransactionSplitClient(BaseAPIClient):
    """Provides a wrapper for paystack Transaction Splits API

    The Transaction Splits API enables merchants split the settlement for a transaction
    across their payout account, and one or more Subaccounts.
    https://paystack.com/docs/api/split/
    """

    def create(
        self,
        name: str,
        type_: Split,
        currency: Currency,
        subaccounts: list[SplitAccount],
        bearer_type: Bearer,
        bearer_subaccount: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransactionSplit] | Response[PaystackDataModel]:
        """Create a split payment on your integration

        Args:
            name: Name of the transaction split
            type_: The type of transaction split you want to create.
                Any value from the ``SplitType`` enum
            currency: Any value from the ``Currency`` enum
            subaccounts: A list of dictionaries containing subaccount code and
                number of shares: ``[{subaccount: 'ACT_xxxxxxxxxx', share: xxx},{...}]``
            bearer_type: Any value from the ``Bearer`` enum
            bearer_subaccount: Subaccount code
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
        _subaccounts = [account.model_dump() for account in subaccounts]

        url = self._full_url("/split")
        payload = {
            "name": name,
            "type": type_,
            "currency": currency,
            "subaccounts": _subaccounts,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount,
        }
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or TransactionSplit,
        )

    def get_splits(
        self,
        name: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        active: bool = True,
        pagination: int = 50,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[list[TransactionSplit]] | Response[PaystackDataModel]:
        """Get/search for the transaction splits available on your integration.

        Args:
            name: The name of the split
            sort_by: Sort by name, defaults to createdAt date
            page: Page number to view. If not specify we use a default value of 1.
            start_date: A timestamp from which to start listing splits e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
            end_date: A timestamp at which to stop listing splits e.g. 2019-09-24T00:00:05.000Z, 2019-09-21
            active: Flag to filter by active
            pagination: Number of splits per page. If not specified we use a default value of 50.
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

        url = self._full_url(f"/split?perPage={pagination}")
        query_params = [
            ("name", name),
            ("sort_by", sort_by),
            ("page", page),
            ("from", start_date),
            ("to", end_date),
            ("active", str(active).lower()),
        ]
        url = append_query_params(query_params, url)

        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TransactionSplit,
        )

    def get_split(
        self,
        id_or_code: int | str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransactionSplit] | Response[PaystackDataModel]:
        """Get details of a split on your integration.

        Args:
            id_or_code: The id of the split
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
        url = self._full_url(f"/split/{id_or_code}/")
        return self._handle_request(  # type: ignore
            HTTPMethod.GET,
            url,
            response_data_model_class=alternate_model_class or TransactionSplit,
        )

    def update(
        self,
        id_: int | str,
        name: str,
        active: bool,
        bearer_type: Bearer | None = None,
        bearer_subaccount: str | None = None,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransactionSplit] | Response[PaystackDataModel]:
        """Update a transaction split details on your integration

        Args:
            id_: Split ID
            name: Name of the transaction split
            active: Flag for active
            bearer_type: Any value from the Bearer enum
            bearer_subaccount: Subaccount code of a subaccount in the split group.
                This should be specified only if the bearer_type
                is ``Bearer.subaccount``
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

        if bearer_subaccount:
            if bearer_type != Bearer.SUB_ACCOUNT:
                raise ValueError(
                    "`bearer_subaccount` can only have a value if `bearer_type` is `Bearer.SUBACCOUNT`"
                )

        payload = {
            "name": name,
            "active": active,
        }
        optional_params = [
            ("bearer_type", bearer_type),
            ("bearer_subaccount", bearer_subaccount),
        ]
        payload = add_to_payload(optional_params, payload)
        url = self._full_url(f"/split/{id_}/")
        return self._handle_request(  # type: ignore
            HTTPMethod.PUT,
            url,
            payload,
            response_data_model_class=alternate_model_class or TransactionSplit,
        )

    def add_or_update(
        self,
        id_: int | str,
        subaccount: str,
        share: int | float,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[TransactionSplit] | Response[PaystackDataModel]:
        """
        Add a Subaccount to a Transaction Split, or update
        the share of an existing Subaccount in a Transaction Split

        Args:
         id_: Split ID
         subaccount: This is the subaccount code
         share: This is the transaction share for the subaccount
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

        payload = {"subaccount": subaccount, "share": share}
        url = self._full_url(f"/split/{id_}/subaccount/add")
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class or TransactionSplit,
        )

    def remove(
        self,
        id_: int | str,
        subaccount: str,
        alternate_model_class: type[PaystackDataModel] | None = None,
    ) -> Response[None] | Response[PaystackDataModel]:
        """Remove a subaccount from a transaction split

        Args:
            id_: Split ID
            subaccount: This is the subaccount code
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

        payload = {"subaccount": subaccount}
        url = self._full_url(f"/split/{id_}/subaccount/remove")
        return self._handle_request(  # type: ignore
            HTTPMethod.POST,
            url,
            payload,
            response_data_model_class=alternate_model_class,
        )
