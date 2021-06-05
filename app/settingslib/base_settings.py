from contextlib import suppress
from typing import List, Tuple

from pydantic import BaseSettings, Extra, ValidationError


class BaseCustomSettings(BaseSettings):
    class Config:
        # MORE in: https://pydantic-docs.helpmanual.io/usage/model_config/

        env_file = '.env' # This is convenient to set .env for demo purposes but should not be there in the final version
        case_sensitive = False
        extra = Extra.forbid
        allow_mutation = False
        frozen = True
        validate_all = True

    @classmethod
    def set_defaults_with_default_constructors(cls,  default_fields: List[ Tuple[str, "BaseCustomSettings"] ]):
        assert issubclass(cls, BaseCustomSettings)
        
        # Builds defaults at this point
        for name, default_cls in default_fields:
            with suppress(ValidationError):
                default = default_cls()
                field_obj = cls.__fields__[name]
                field_obj.default = default
                field_obj.field_info.default = default
                field_obj.required = False
