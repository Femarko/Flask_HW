from typing import TypeVar, Type, Generic

from sqlalchemy.exc import IntegrityError

from app.db.db_models import Base, Adv
from app.error_handler import HttpError
from app.type_hints import SQLAlchemySession
DBModel = TypeVar("DBModel", bound=Base)


class StorageInterface:
    def __init__(self, session: SQLAlchemySession, return_db_model: bool = False):
        self.session = session

    def get_one(self, advertisement_id: int, return_dict: bool = True) -> dict | DBModel | None:
        db_model: DBModel | None = self.session.get(Adv, advertisement_id)
        if db_model is None:
            return
        if return_dict is False:
            return db_model
        return db_model.db_model_to_dict()

    def add(self, validated_data: dict) -> DBModel:
        db_model_instance: DBModel = Adv(**validated_data)
        self.session.add(db_model_instance)
        return db_model_instance

    def update(self, advertisement_id: int, new_data: dict) -> dict | None:
        advertisement: DBModel | None = self.get_one(db_model_instance_id=advertisement_id, return_dict=False)
        if advertisement is None:
            return
        for key, value in new_data.items():
            setattr(advertisement, key, value)
        self.session.add(advertisement)
        advertisement_added_to_session_params: dict = advertisement.db_model_to_dict()
        return advertisement_added_to_session_params

    def get_sample(self, **validated_filter_params: dict): ...
        # sample = self.session.query(**validated_filter_params)



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
