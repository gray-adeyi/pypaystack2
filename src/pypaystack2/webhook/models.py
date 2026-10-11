from pydantic import BaseModel


class EndpointAddress(BaseModel):
    host: str | None = None
    port: int | None = None
