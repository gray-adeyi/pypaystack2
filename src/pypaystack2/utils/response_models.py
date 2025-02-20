from pydantic import BaseModel


class ApplePayDomains(BaseModel):
    domain_names: list[str]
