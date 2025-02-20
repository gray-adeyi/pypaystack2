from _operator import add
from functools import reduce
from typing import Any


def add_to_payload(
    optional_params: list[tuple[str, Any]], payload: dict[str, Any]
) -> dict[str, Any]:
    """Adds more parameters to an existing payload.

    This is a utility is used in the generation of payloads
    for a request body. It helps to add more parameters to
    a payload if it is not None.
    e.g. say you want to send a payload which is currently
    ``{"amount": 20000}`` and you want to include an additional
    data such as ``currency`` if provided in the ``optional_params``
    to send this ``{"amount": 20000,"currency":"ngn"}`` if only
    the currency is available otherwise send the initial payload.
    This functions takes a list of optional parameters
    which is added to the payload is they are available and
    returns the payload.

    Args:
        optional_params: A list of additional data to be added to the payload if it is
            available. It follows the format ``[("name-on-payload","value")].``
            e.g ``[("currency","ngn"),("amount",2000)]``
        payload: A dictionary containing the data to be sent in the request body.

    Returns:
        A dictionary of the payload updated with additional data in the
            optional_params that are not `None`.
    """
    [
        payload.update({item[0]: item[1]})
        for item in optional_params
        if item[1] is not None
    ]
    return payload


def append_query_params(query_params: list[tuple[str, Any]], url: str) -> str:
    """Adds more queries to url that already have query parameters in its suffix

    This function should only be used with urls that already have a
    query parameter suffixed to it because it makes that assumption
    that the url supplied is of the state ``http://example-url.com?firstQuery=1``
    and it adds more query parameters delimited by & to the end of the provided
    url ``http://example-url.com?firstQuery=1&otherQuery=2&...``

    Args:
        query_params: A list of other query parameters that should be appended to the url
            if it is not None. e.g ``[("page",2),("pagination",50),("currency",None)]`` ->
            ``url&page=2&pagination=50``
        url: The url to which additional query parameters are added.

    Returns:
        The new url with padded query parameters.
    """
    params = [
        f"&{param[0]}={param[1]}" for param in query_params if param[1] is not None
    ]
    if len(params) == 0:
        return url
    return url + reduce(add, params)
