import typing
from datetime import datetime

import pydantic


class StorageService(typing.Protocol):
    def save(self, object_to_save):
        raise NotImplementedError


class ValidationTool(typing.Protocol):
    def validate(self, *args, **kwargs):
        raise NotImplementedError


    # def modify(self):
    #     raise NotImplementedError
    #
    # def retrieve_one(self):
    #     raise NotImplementedError
    #
    # def retrieve_all(self):
    #     raise NotImplementedError
    #
    # def delete(self):
    #     raise NotImplementedError


class Adv(pydantic.BaseModel):
    id: int
    title: str
    description: str
    author: str
    creation_date: datetime
