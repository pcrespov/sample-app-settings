from modules.mod1_settings import MyModuleSettings
from modules.mod2_settings import AnotherModuleSettings

from pydantic import Field
from settings_library.base import BaseCustomSettings
from settings_library.postgres import PostgresSettings

class Settings(BaseCustomSettings):
    """The app settings"""

    APP_HOST: str
    APP_PORT: int = 3

    APP_POSTGRES: PostgresSettings
    APP_MODULE_1: MyModuleSettings = Field(..., description="Some Module Example")
    APP_MODULE_2: AnotherModuleSettings
