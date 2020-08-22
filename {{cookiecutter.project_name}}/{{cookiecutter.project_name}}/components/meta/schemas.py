from enum import Enum

from pydantic import Field

from ...core.schemas import BaseSchema


class HealthCheckStatus(Enum):
    ok = "ok"
    error = "error"


class HealthCheckResponse(BaseSchema):
    status: HealthCheckStatus = Field(...)
