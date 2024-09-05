import flask, sqlalchemy
from flask import request, Response
from sqlalchemy.exc import IntegrityError, DatabaseError

from app import adv, db, models, error_handler
from app.db import Session
from app.error_handler import HttpError
from app.models import Adv
from app.type_hints import SQLAlchemySession


@adv.before_request
def before_request() -> None:
    session: SQLAlchemySession = Session()
    request.session = session


@adv.after_request
def after_request(response: Response) -> Response:
    request.session.close()
    return response


def get_adv(adv_id: int) -> Adv:
    adv = flask.request.session.get(Adv, adv_id)
    if adv is None:
        raise HttpError(404, "advertisement not found")
    return adv


def add_adv(adv: Adv) -> Adv:
    try:
        request.session.add(adv)
        request.session.commit()
    except IntegrityError:
        raise HttpError(409, "advertisement already exists")
    return adv


def delete_adv(adv: Adv) -> None:
    try:
        request.session.delete(adv)
        request.session.commit()
    except Exception:
        raise HttpError(500, "unexpacted error occurred")

