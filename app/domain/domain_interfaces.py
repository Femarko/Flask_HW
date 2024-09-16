import typing

from app.db.db_interface import DBModel


class StorageInterface(typing.Protocol):
    def add(self, validated_data: dict) -> int | dict:
        pass

    def update(self, advertisement_id: int, new_data: dict) -> dict | None:
        pass

    def get_one(self, advertisement_id: int, return_dict: bool = True) -> dict:
        pass


class ValidatorInterface(typing.Protocol):
    def validate(self, input_data: dict, validation_model) -> dict:
        pass
