from typing import Any

from app.validation import params_validator_to_create, params_validator_to_edit
from app.data.db import storage_interface


def validate_params_to_create(data_to_validate: Any):
    return params_validator_to_create.validate(data_to_validate)


def validate_params_to_edit(data_to_validate: Any):
    return params_validator_to_edit.validate(data_to_validate)


def save(validated_data: dict):
    return storage_interface.save(validated_data)
