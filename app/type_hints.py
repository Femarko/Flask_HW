import typing
from typing import TypeVar
import pydantic

PydanticModel = TypeVar("PydanticModel", bound=pydantic.BaseModel)


class SQLAlchemySession(typing.Protocol):
    def commit(self, *args, **kwargs):
        pass

    def add(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def close(self):
        pass
