from typing import Type, Any, TypeVar, Literal
import pydantic

from app.error_handler import HttpError
from app.domain.domain_models import CreateAdv, EditAdv, ValidationModel


class BaseValidator:
    pass


# class AdvParamsValidator(BaseValidator):
#     def __init__(self, validation_goal: Literal["create", "edit"]):
#         self.validation_goal = validation_goal
#
#     def _get_validation_models(self) -> dict[Literal["create"] | Literal["edit"], Type[ValidationModel]]:
#         return {"create": CreateAdv, "edit": EditAdv}
#
#     def validate(self, data_to_validate: dict[str, Any] | Any) -> dict[str, Any] | list:
#         validation_models = self._get_validation_models()
#         validation_model: Type[ValidationModel] = validation_models.get(self.validation_goal)
#         try:
#             return validation_model.model_validate(data_to_validate).model_dump(exclude_unset=True)
#         except pydantic.ValidationError as err:
#             errors_list: list = err.errors()
#             return errors_list
            # raise HttpError(400, errors_list)


class ValidatorClass(BaseValidator):

    def validate(self, data_to_validate: dict, validation_model: Type[ValidationModel]):
        try:
            return validation_model.model_validate(data_to_validate).model_dump(exclude_unset=True)
        except pydantic.ValidationError as err:
            errors_list: list = err.errors()
            raise HttpError(400, errors_list)



Validator = TypeVar("Validator", bound=BaseValidator)


def create_validator(validator_class: Type[Validator], validation_goal: Literal["create", "edit"]) -> Validator:
    validator = validator_class(validation_goal)
    return validator
