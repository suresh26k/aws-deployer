import typer
from aws_deployer import settings


app = typer.Typer()


@app.command()
def show_config():
    config = settings.config

    typer.echo("Function Name : ", config.get("function_name"))
    typer.echo("AWS Region : ", config.get("aws_region"))