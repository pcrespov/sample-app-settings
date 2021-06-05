from pydantic import Extra, BaseSettings
from typing import Tuple, List
# https://pydantic-docs.helpmanual.io/usage/model_config/

from contextlib import suppress
from pydantic import ValidationError
class BaseCustomSettings(BaseSettings):
    class Config:
        env_file = '.env'
        case_sensitive = False
        extra = Extra.forbid
        allow_mutation = False
        frozen = True
        validate_all = True

    @classmethod
    def set_defaults(cls,  default_fields: List[ Tuple[str, "BaseCustomSettings"] ]):
        assert issubclass(cls, BaseCustomSettings)
        
        # Builds defaults at this point
        for name, default_cls in default_fields:
            with suppress(ValidationError):
                default = default_cls()
                field_obj = cls.__fields__[name]
                field_obj.default = default
                field_obj.field_info.default = default
                field_obj.required = False