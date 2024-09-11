from flask import jsonify, request, Response
from flask.views import MethodView

import app.db
from app.domain import domain_model, domain_service
from app.db import storage_interface
from app.validation import params_validator_to_create

class AdvView(MethodView):

    # def get(self, adv_id: int) -> Response:
    #     adv = get_adv(adv_id)
    #     return jsonify(
    #         {
    #             "id": adv.id,
    #             "title": adv.title,
    #             "description": adv.description,
    #             "creation_date": adv.creation_date.isoformat(),
    #             "author": adv.author
    #         }
    #     )

    def post(self) -> tuple[Response, int]:
        # validated_adv_data: dict[str, str] = service.validate_params_to_create(request.json)
        # new_adv_id = service.save(validated_adv_data)
        validated_adv_data = params_validator_to_create.validate(data_to_validate=request.json)
        adv_service_instance = domain_model.Advertisement(storage_repository=app.db.storage_interface)
        new_adv_id = adv_service_instance.add_new(validated_adv_data)
        return jsonify({'id': new_adv_id}), 201

    # def patch(self, adv_id: int) -> tuple[Response, int]:
    #     adv: Adv = get_adv(adv_id)
    #     validated_data: dict[str, Any] = validate_data(model=EditAdv, data=request.json)
    #     for key, value in validated_data.items():
    #         setattr(adv, key, value)
    #     modified_adv: Adv = add_adv(adv)
    #     modified_adv_fields: dict[str, str | int] = {
    #         "id": modified_adv.id,
    #         "title": modified_adv.title,
    #         "description": modified_adv.description,
    #         "creation_date": modified_adv.creation_date.isoformat(),
    #         "author": modified_adv.author
    #     }
    #     return jsonify({"modified_advertisement": modified_adv_fields}), 200

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
