from typing import List

from fastapi import APIRouter

from .api import router
from .crud import CRUDS

COLLECTIONS: List[str] = [crud.collection for crud in CRUDS]
ROUTER: APIRouter = router
