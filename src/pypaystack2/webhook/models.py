from typing import Any

from pydantic import BaseModel

from pypaystack2.enums import Country, Identification
from pypaystack2.webhook.enums import PaystackWebhookEvent


class EndpointAddress(BaseModel):
    host: str | None = None
    port: int | None = None


class PaystackWebhookPayload(BaseModel):
    event: PaystackWebhookEvent
    data: dict[str, Any]


class CustomerIdentificationFailedDataIdentification(BaseModel):
    country: Country
    type: Identification
    bvn: str
    account_number: str
    bank_code: str


class CustomerIdentificationFailedData(BaseModel):
    customer_id: int
    customer_code: str
    email: str
    identification: CustomerIdentificationFailedDataIdentification  # I really don't know what to name this atm 😭
    reason: str


class CustomerIdentificationSuccessDataIdentification(BaseModel):
    country: Country
    type: Identification
    value: str


class CustomerIdentificationSuccessData(BaseModel):
    customer_id: int
    customer_code: str
    email: str
    identification: CustomerIdentificationSuccessDataIdentification
