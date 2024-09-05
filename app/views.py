from flask import jsonify, request, Response
from flask.views import MethodView
from typing import Any

from app.data_validation import validate_data
from app.models import Adv
from app.schema import CreateAdv, EditAdv
from app.type_hints import SQLAlchemySession
from app.service import get_adv, add_adv, delete_adv


class AdvView(MethodView):

    def get(self, adv_id: int) -> Response:
        adv = get_adv(adv_id)
        return jsonify(
            {
                "id": adv.id,
                "title": adv.title,
                "description": adv.description,
                "creation_date": adv.creation_date.isoformat(),
                "author": adv.author
            }
        )

    def post(self) -> tuple[Response, int]:
        validated_adv_data: dict[str, str] = validate_data(model=CreateAdv, data=request.json)
        adv_to_create = Adv(**validated_adv_data)
        new_adv: Adv = add_adv(adv_to_create)
        return jsonify({'id': new_adv.id}), 201

    def patch(self, adv_id: int) -> tuple[Response, int]:
        adv: Adv = get_adv(adv_id)
        validated_data: dict[str, Any] = validate_data(model=EditAdv, data=request.json)
        for key, value in validated_data.items():
            setattr(adv, key, value)
        modified_adv: Adv = add_adv(adv)
        modified_adv_fields: dict[str, str | int] = {
            "id": modified_adv.id,
            "title": modified_adv.title,
            "description": modified_adv.description,
            "creation_date": modified_adv.creation_date.isoformat(),
            "author": modified_adv.author
        }
        return jsonify({"modified_advertisement": modified_adv_fields}), 200

    def delete(self, adv_id: int) -> tuple[Response, int]:
        adv = get_adv(adv_id)
        adv_params = {
            "id": adv.id,
            "title": adv.title,
            "description": adv.description,
            "creation_date": adv.creation_date,
            "author": adv.author
        }
        delete_adv(adv)
        return jsonify({"deleted": adv_params}), 200
