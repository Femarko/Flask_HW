from typing import Type, Any

import pydantic

from app.error_handler import HttpError
from app.type_hints import PydanticModel


def validate_data(model: Type[PydanticModel], data: dict[str, Any] | Any) -> dict[str, Any]:
    try:
        return model.model_validate(data).model_dump(exclude_unset=True)
    except pydantic.ValidationError as err:
        errors_list: list = err.errors()
        raise HttpError(400, errors_list)
