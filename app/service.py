from typing import Any

# from app.data.db.db_interface import get_adv
import flask

from app.data.schema_and_validation import schema
from app.validation import params_validator_to_create, params_validator_to_edit
from app.data.db import storage_interface
from app.data.db import db_models


# def get_one_adv(adv_id: int) -> Adv:
#     return get_adv(adv_id)
#
#
# def create_new_adv(adv_params: dict) -> Adv.id:
#     return add_adv(adv_params)
#
#
# def update_adv(adv: Adv) -> Adv:
#     return add_adv(adv)

def validate_params_to_create(data_to_validate: Any):
    return params_validator_to_create.validate(data_to_validate)


def validate_params_to_edit(data_to_validate: Any):
    return params_validator_to_edit.validate(data_to_validate)


def save(validated_data):
    object_to_save = db_models.Adv(**validated_data)
    return storage_interface.save(object_to_save)
