from typing import List, Type

from ...core.database.crud import BaseMongoCRUD


CRUDS: List[Type[BaseMongoCRUD]] = []
