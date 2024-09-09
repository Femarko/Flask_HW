from app.validation.validation_models import CreateAdv, EditAdv
from app.validation.validation_interface import AdvParamsValidator, create_validator

params_validator_to_create = create_validator(AdvParamsValidator, "create")
params_validator_to_edit = create_validator(AdvParamsValidator, "edit")