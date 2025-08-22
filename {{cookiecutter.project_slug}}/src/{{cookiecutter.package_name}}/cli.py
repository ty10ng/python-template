"""
Command-line interface for {{ cookiecutter.project_name }}.

This module provides the CLI entry point and command definitions.
"""

import click
from rich.console import Console
from rich.table import Table

from . import get_logger, get_config, __version__


console = Console()
logger = get_logger(__name__)


@click.group()
@click.version_option(version=__version__)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help="Enable verbose output"
)
@click.option(
    "--config", "-c",
    type=click.Path(exists=True),
    help="Path to configuration file"
)
@click.pass_context
def cli(ctx, verbose, config):
    """
    {{ cookiecutter.project_name }} - {{ cookiecutter.project_description }}
    
    A professional CLI application with comprehensive logging and configuration.
    """
    # Ensure context object exists
    ctx.ensure_object(dict)
    
    # Store options in context
    ctx.obj['verbose'] = verbose
    ctx.obj['config'] = config
    
    if verbose:
        logger.info("Verbose mode enabled")
    
    if config:
        logger.info(f"Using config file: {config}")


@cli.command()
@click.pass_context
def status(ctx):
    """Show application status and configuration."""
    config = get_config()
    
    # Create a status table
    table = Table(title="{{ cookiecutter.project_name }} Status")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Version", __version__)
    table.add_row("App Name", config.get('app.name', 'Unknown'))
    table.add_row("Environment", config.get('app.environment', 'development'))
    table.add_row("Log Level", config.get('logging.level', 'INFO'))
    table.add_row("Verbose Mode", str(ctx.obj.get('verbose', False)))
    
    console.print(table)
    logger.info("Status command executed")


@cli.command()
@click.argument('name', default='World')
@click.option(
    '--count', '-n',
    default=1,
    type=int,
    help='Number of greetings'
)
@click.pass_context
def hello(ctx, name, count):
    """Say hello to NAME."""
    for i in range(count):
        message = f"Hello, {name}!"
        if ctx.obj.get('verbose'):
            message += f" (greeting {i + 1}/{count})"
        console.print(message, style="bold green")
    
    logger.info(f"Greeted {name} {count} time(s)")


@cli.command()
@click.pass_context
def info(ctx):
    """Show detailed application information."""
    config = get_config()
    
    console.print("\n[bold blue]{{ cookiecutter.project_name }}[/bold blue]")
    console.print(f"Version: {__version__}")
    console.print(f"Description: {{ cookiecutter.project_description }}")
    console.print(f"Author: {{ cookiecutter.author_name }}")
    console.print(f"Python Version: {{ cookiecutter.python_version }}+")
    
    console.print("\n[bold blue]Configuration:[/bold blue]")
    for key, value in config.data.items():
        if isinstance(value, dict):
            console.print(f"  {key}:")
            for subkey, subvalue in value.items():
                console.print(f"    {subkey}: {subvalue}")
        else:
            console.print(f"  {key}: {value}")
    
    logger.info("Info command executed")


def main():
    """Main CLI entry point."""
    try:
        cli()
    except Exception as e:
        logger.error(f"CLI error: {e}")
        console.print(f"[red]Error: {e}[/red]")
        raise


if __name__ == "__main__":
    main()
