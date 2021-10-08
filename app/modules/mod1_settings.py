from pydantic import BaseSettings, Field
from settings_library.base import BaseCustomSettings


class MyModuleSettings(BaseCustomSettings):
    """
    Settings for Module 1
    """

    MYMODULE_VALUE: int = Field(..., description="Some value for module 1")
