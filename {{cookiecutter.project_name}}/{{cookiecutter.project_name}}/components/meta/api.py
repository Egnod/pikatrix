from fastapi import APIRouter, HTTPException, Path
from starlette.requests import Request

from .schemas import HealthCheckResponse, HealthCheckStatus

router = APIRouter()


@router.post("/check", response_model=HealthCheckResponse)
async def create_link(request: Request) -> HealthCheckResponse:
    return HealthCheckResponse(status=HealthCheckStatus.ok)

