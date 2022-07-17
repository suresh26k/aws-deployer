import os.path
import typer
import yaml

CONFIG_FILE = ".aws_deployer.yaml"

if not os.path.exists(CONFIG_FILE):
    typer.echo("Please provide a valid config file")
    raise typer.Exit()

with open(CONFIG_FILE, "r") as file_:
    config = yaml.safe_load(file_)
