from typing import TypeVar

from pydantic import BaseModel

from pypaystack2.enums import SupportedCountryRelationshipType

PaystackDataModel = TypeVar("PaystackDataModel", bound=BaseModel)

# FIXME: I was having issues constraining this generic type to the types
#   `PaystackDataModel`, `list[PaystackDataModel]` or `None`. it's why it's left as is.
PaystackResponseData = TypeVar("PaystackResponseData")
T = TypeVar("T", SupportedCountryRelationshipType, str)
D = TypeVar("D")
