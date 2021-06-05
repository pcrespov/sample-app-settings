
from modules.mod1_settings import MyModuleSettings
from modules.mod2_settings import AnotherModuleSettings
from settingslib.base_settings import BaseCustomSettings
from settingslib.postgres import PostgresSettings

from pydantic import Field

class Settings(BaseCustomSettings):
    APP_HOST: str
    APP_PORT: int = 3

    APP_POSTGRES: PostgresSettings
    APP_MODULE_1: MyModuleSettings = Field(None, description="Some Module Example")
    APP_MODULE_2: AnotherModuleSettings

    @classmethod
    def create_from_env(cls) -> "Settings":
        cls.set_defaults(
            [
                ("APP_POSTGRES", PostgresSettings),
                ("APP_MODULE_1", MyModuleSettings),
                ("APP_MODULE_2", AnotherModuleSettings),
            ]
        )
        return cls()
