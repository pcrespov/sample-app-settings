import logging
import os
from pprint import pformat

import typer
from pydantic import ValidationError
from pydantic.env_settings import BaseSettings

from app_settings import Settings

log = logging.getLogger()

HEADER = "{:-^50}"


def print_envs(settings_obj):
    for name in settings_obj.__fields__:
        value = getattr(settings_obj, name)
        if isinstance(value, BaseSettings):
            typer.echo(f"\n# {name}")
            print_envs(value)
        else:
            field_info = settings_obj.__fields__[name].field_info
            if field_info.description:
                typer.echo(f"# {field_info.description}")
            typer.echo(f"{name}={value}")


def print_as_json(settings_obj):
    typer.echo(settings_obj.json(indent=2))


def main(
    print_settings_env: bool = typer.Option(
        False,
        "-E",
        "--print-settings-env",
        help="Resolves settings, prints env vars and exits",
    ),
    print_settings_json: bool = False,
    print_settings_json_schema: bool = False,
):
    """A 12-factor app CLI"""

    if print_settings_json_schema:
        typer.echo(Settings.schema_json(indent=2))
        return

    try:
        settings = Settings.create_from_env()

    except ValidationError as err:
        json_schema = Settings.schema_json(indent=2)
        log.error(
            "Invalid application settings. Typically an environment variable is missing or mistyped :\n%s",
            "\n".join(
                [
                    HEADER.format("detail"),
                    str(err),
                    HEADER.format("environment variables"),
                    pformat(
                        {k: v for k, v in dict(os.environ).items() if k.upper() == k}
                    ),
                    HEADER.format("json-schema"),
                    json_schema,
                ]
            ),
            exc_info=False,
        )
        raise

    if print_settings_json:
        print_as_json(settings)
        return

    if print_settings_env:
        print_envs(settings)
        return

    typer.secho("Running app ... ", fg=typer.colors.GREEN)


run = typer.Typer()
run.command()(main)
