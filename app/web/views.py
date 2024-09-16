from typing import Any, NamedTuple, Type

from flask import jsonify, request, Response
from flask.views import MethodView

import app.db
from app import error_handler
from app.db.db_interface import DBModel
from app.db.db_models import Adv
from app.db.unit_of_work import UnitOfWork
from app.domain import domain_operations
# from app.db import storage_interface
from app.db import StorageInterface, db_interface
from app.domain import domain_models, domain_operations
from app.domain.domain_models import ValidationModel
from app.validation import validation_interface
from app.validation.validation_interface import ValidatorClass


def validate_data(data_to_validate: dict, validation_model: Type[ValidationModel]):
    validator = validation_interface.ValidatorClass()
    domain_validation_instance = domain_operations.Validation(validator=validator)
    validation_result = domain_validation_instance.validate(data_to_validate=data_to_validate,
                                                            validation_model=validation_model)
    if isinstance(validation_result, list):
        raise error_handler.HttpError(status_code=400, description=validation_result)
    return validation_result


class AdvView(MethodView):
    def get(self, advertisement_id: int) -> Response:
        with UnitOfWork() as unit_of_work:
            db_repository = db_interface.StorageInterface(session=unit_of_work.session)
            domain_advertisement_instance = domain_operations.Advertisement(storage_repository=db_repository)
            fetched_adv_params: dict | None = domain_advertisement_instance.get_one(advertisement_id)
            if fetched_adv_params is None:
                raise error_handler.HttpError(description="advertisement not found", status_code=404)
            return jsonify(fetched_adv_params)

    def post(self) -> tuple[Response, int]:
        validated_data = validate_data(data_to_validate=request.json,
                                       validation_model=domain_models.validation_models.create_adv)
        with UnitOfWork() as unit_of_work:
            db_repository = db_interface.StorageInterface(session=unit_of_work.session)
            domain_operations_advertisement = domain_operations.Advertisement(storage_repository=db_repository)
            new_adv: DBModel = domain_operations_advertisement.add(validated_data=validated_data)
            unit_of_work.commit()
            return jsonify({'id': new_adv.id}), 201

    def patch(self, advertisement_id: int) -> tuple[Response, int]:
        data_validation_result = validate_data(data_to_validate=request.json,
                                               validation_model=domain_models.validation_models.edit_adv)
        with UnitOfWork() as unit_of_work:
            db_repository = db_interface.StorageInterface(unit_of_work.session)
            domain_operations_advertisement = domain_operations.Advertisement(storage_repository=db_repository)
            domain_operation_result: dict | None = domain_operations_advertisement.update(
                advertisement_id=advertisement_id, new_data=data_validation_result
            )
            if domain_operation_result is None:
                raise error_handler.HttpError(description="advertisement not found", status_code=404)
            unit_of_work.commit()
            return jsonify({"modified advertisement parameters": domain_operation_result}), 200

    # def delete(self, adv_id: int) -> tuple[Response, int]:
    #     adv = get_adv(adv_id)
    #     adv_params = {
    #         "id": adv.id,
    #         "title": adv.title,
    #         "description": adv.description,
    #         "creation_date": adv.creation_date,
    #         "author": adv.author
    #     }
    #     delete_adv(adv)
    #     return jsonify({"deleted": adv_params}), 200
