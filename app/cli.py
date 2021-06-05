import logging
import os
import sys
from pathlib import Path
from pprint import pformat
from typing import Optional

import typer
from pydantic import ValidationError
from pydantic.env_settings import BaseSettings

from app_settings import Settings

log = logging.getLogger()


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

        HEADER = "{:-^50}"
        log.error(
            "Invalid settings. %s:",
            err,
            # HEADER.format("schema"),
            # Settings.schema_json(indent=2),
            # HEADER.format("environment variables"),
            # pformat(dict(os.environ)),
            exc_info=False,
        )
        raise RuntimeError(os.EX_DATAERR)

    if print_settings_json:
        print_as_json(settings)

    if print_settings_env:
        print_envs(settings)


if __name__ == "__main__":
    typer.run(main)
