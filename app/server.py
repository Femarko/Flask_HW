import flask
import pydantic
from flask import jsonify, request, Response
from flask.views import MethodView
from flask import Response
from sqlalchemy.exc import IntegrityError

from app.error_handler import HttpError
from app.db import Session
from app.models import Adv
from app.schema import CreateAdv
from app import adv


@adv.before_request
def before_request():
    session = Session()
    request.session = session


@adv.after_request
def after_request(response: Response):
    request.session.close()
    return response


def get_adv(adv_id: int):
    adv = request.session.get(Adv, adv_id)
    if adv is None:
        raise HttpError(404, "advertisement not found")
    return adv


def add_adv(adv: Adv):
    try:
        request.session.add(adv)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "advertisement already exists")
    return adv


def validate_data(model, data):
    try:
        return model.model_validate(data).model_dump(exclude_unset=True)
    except pydantic.ValidationError as err:
        error = err.errors()[0]
        error.pop("ctx", None)
        raise HttpError(400, error)



class AdvView(MethodView):

    @property
    def session(self) -> Session:
        return request.session

    def get(self, adv_id: int):
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

    def post(self):
        adv_data = validate_data(model=CreateAdv, data=request.json)
        new_adv = Adv(**adv_data)
        self.session.add(new_adv)
        self.session.commit()
        return jsonify({'id': new_adv.id}), 201

    def patch(self, adv_id: int):
        adv = get_adv(adv_id)
        adv_data = request.json
        for key, value in adv_data.items():
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

    def delete(self, adv_id: int):
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


