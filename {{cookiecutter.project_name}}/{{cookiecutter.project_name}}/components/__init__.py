from typing import List

from fastapi import APIRouter

from .meta import COLLECTIONS as META_COLLECTIONS, ROUTER as meta_router

__all__ = ["COLLECTIONS", "get_components_router"]

COLLECTIONS: List[str] = [*META_COLLECTIONS]


def get_components_router() -> APIRouter:
    router = APIRouter()

    router.include_router(meta_router, prefix="/-", tags=["meta"])

    return router
