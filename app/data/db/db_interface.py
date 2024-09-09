from typing import TypeVar

from sqlalchemy.exc import IntegrityError

from app import adv
from app.data.db import db_models
from app.data.db.db_models import Adv
from app.error_handler import HttpError
from app.type_hints import SQLAlchemySession

DBModel = TypeVar("DBModel", bound=db_models.Base)


# @adv.before_request
# def before_request() -> None:
#     session: SQLAlchemySession = Session()
#     request.session = session
#
#
# @adv.after_request
# def after_request(response: Response) -> Response:
#     request.session.close()
#     return response


class StorageInterface:

    def __init__(self, session: SQLAlchemySession):
        self.session = session

    def save(self, object_to_save: DBModel):
        try:
            self.session.add(object_to_save)
            self.session.commit()
            new_adv_id = object_to_save.id
            return new_adv_id
        except IntegrityError:
            raise HttpError(409, "advertisement already exists")
        finally:
            self.session.close()

    # def modify(self):
    #     raise NotImplementedError
    #
    # def retrieve_one(self):
    #     raise NotImplementedError
    #
    # def retrieve_all(self):
    #     raise NotImplementedError
    #
    # def delete(self):
    #     raise NotImplementedError

# def get_adv(adv_id: int) -> Adv:
#     adv = flask.request.session.get(Adv, adv_id)
#     if adv is None:
#         raise HttpError(404, "advertisement not found")
#     return adv
#
#
# def delete_adv(adv: Adv) -> None:
#     try:
#         request.session.delete(adv)
#         request.session.commit()
#     except Exception:
#         raise HttpError(500, "unexpacted error occurred")
