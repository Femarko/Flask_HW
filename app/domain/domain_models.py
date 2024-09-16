from dataclasses import dataclass

import pydantic
from typing import NamedTuple, Type, TypeVar


class ValidationBaseClass:
    pass


class CreateAdv(pydantic.BaseModel, ValidationBaseClass):
    title: str
    description: str
    author: str


class EditAdv(pydantic.BaseModel, ValidationBaseClass):
    title: str | None = None
    description: str | None = None
    author: str | None = None


class ValidationModels(NamedTuple):
    create_adv: Type[CreateAdv]
    edit_adv: Type[EditAdv]


def get_validation_models() -> ValidationModels:
    return ValidationModels(CreateAdv, EditAdv)


validation_models = get_validation_models()

ValidationModel = TypeVar("ValidationModel", bound=ValidationBaseClass)

