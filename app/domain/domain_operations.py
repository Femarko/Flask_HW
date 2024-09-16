import typing, pydantic
from typing import Type, TypeVar

from app.db.db_repository import DBModel
from app.domain.domain_interfaces import StorageInterface, ValidatorInterface

PydanticModel = TypeVar("PydanticModel", bound=pydantic.BaseModel)


class Advertisement:
    def __init__(self, storage_repository: StorageInterface):
        self.storage_repository = storage_repository

    def add(self, validated_data: dict):
        return self.storage_repository.add(validated_data)

    def update(self, advertisement_id: int, new_data: dict) -> DBModel | None:
        modified_advertisement: dict | None = self.storage_repository.update(advertisement_id=advertisement_id,
                                                                             new_data=new_data)
        return modified_advertisement

    def get_one(self, advertisement_id: int, return_dict: bool = True):
        return self.storage_repository.get_one(advertisement_id=advertisement_id)

    def get_sample(self, validated_filter_params: dict):
        return self.storage_repository.get_sample()

    def get_all(self):
        return self.storage_repository.get_all()

    def delete(self):
        return self.storage_repository.delete()

    def validate_input_data(self, validation_model: typing.Type[PydanticModel]):
        return self.validator.validate()


class Validation:
    def __init__(self, validator: ValidatorInterface):
        self.validator = validator

    def validate(self, data_to_validate: dict, validation_model):
        return self.validator.validate(data_to_validate=data_to_validate, validation_model=validation_model)

