from typing import Optional

import typer

from aws_deployer import __app_name__, __version__
from aws_deployer import lambda_function
from aws_deployer import settings

app = typer.Typer()
app.add_typer(lambda_function.app, name="lambda-function")
# app.add_typer(show_config.app, name="show-config")


@app.command()
def show_config():
    config = settings.config

    typer.echo("Function Name : " + config.get("function_name"))
    typer.echo("AWS Region : " + config.get("aws_region"))


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
