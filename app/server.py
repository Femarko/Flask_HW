import flask
from flask import jsonify, request, Response
from flask.views import MethodView
from flask import Response

from app.error_handler import HttpError
from models import Session, Adv
from sqlalchemy.exc import IntegrityError
from __init__ import adv

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
        adv_data = request.json
        new_adv = Adv(**adv_data)
        self.session.add(new_adv)
        self.session.commit()
        return jsonify({'id': new_adv.id})

    def patch(self, adv_id: int):
        adv = get_adv(adv_id)
        adv_data = request.json
        for key, value in adv_data.items():
            setattr(adv, key, value)
        adv = add_adv(adv)
        return jsonify(
            {
                "modified data":
                    {
                        "id": adv.id,
                        "title": adv.title,
                        "description": adv.description,
                        "creation_date": adv.creation_date.isoformat(),
                        "author": adv.author
                    }
            }
        )

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
        return jsonify({"deleted": adv_params})


if __name__ == "__main__":
    adv.run(debug=True)
