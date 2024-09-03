import typing

import pydantic
from flask import jsonify, request, Response
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from typing import TypeVar, Type, Any

from app.error_handler import HttpError
from app.db import Session
from app.models import Adv
from app.schema import CreateAdv, EditAdv
from app import adv


PydanticModel = TypeVar("PydanticModel", bound=pydantic.BaseModel)


class SQLAlchemySession(typing.Protocol):
    def commit(self, *args, **kwargs):
        pass

    def add(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


@adv.before_request
def before_request() -> None:
    session: SQLAlchemySession = Session()
    request.session = session


@adv.after_request
def after_request(response: Response) -> Response:
    request.session.close()
    return response


def get_adv(adv_id: int) -> Adv:
    adv = request.session.get(Adv, adv_id)
    if adv is None:
        raise HttpError(404, "advertisement not found")
    return adv


def add_adv(adv: Adv) -> Adv:
    try:
        request.session.add(adv)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "advertisement already exists")
    return adv


def validate_data(model: Type[PydanticModel], data: dict[str, Any] | Any) -> dict[str, Any]:
    try:
        return model.model_validate(data).model_dump(exclude_unset=True)
    except pydantic.ValidationError as err:
        errors_list: list = err.errors()
        raise HttpError(400, errors_list)


class AdvView(MethodView):

    @property
    def session(self) -> SQLAlchemySession:
        return request.session

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
        adv_data = validate_data(model=CreateAdv, data=request.json)
        new_adv = Adv(**adv_data)
        self.session.add(new_adv)
        self.session.commit()
        return jsonify({'id': new_adv.id}), 201

    def patch(self, adv_id: int) -> tuple[Response, int]:
        adv = get_adv(adv_id)
        validated_data: dict[str, Any] = validate_data(model=EditAdv, data=request.json)
        for key, value in validated_data.items():
            setattr(adv, key, value)
        adv = add_adv(adv)
        modified_adv = {
            "id": adv.id,
            "title": adv.title,
            "description": adv.description,
            "creation_date": adv.creation_date.isoformat(),
            "author": adv.author
        }
        return jsonify({"modified_advertisement": modified_adv}), 200

    def delete(self, adv_id: int) -> tuple[Response, int]:
        adv = get_adv(adv_id)
        adv_params = {
            "id": adv.id,
            "title": adv.title,
            "description": adv.description,
            "creation_date": adv.creation_date,
            "author": adv.author
        }
        self.session.delete(adv)
        self.session.commit()
        return jsonify({"deleted": adv_params}), 200


