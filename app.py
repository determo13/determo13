"""Command line interface for the arbitrage trading app."""

import click

from arbitrage.config import AppConfig
from arbitrage.scanner import scan_arbitrage
from arbitrage.executor import execute_trade


@click.command()
@click.option("--mode", type=click.Choice(["test", "live"]), default="test", help="Run mode")
@click.option("--dashboard", is_flag=True, help="Launch dashboard")
def main(mode: str, dashboard: bool) -> None:
    """Entry point for the CLI."""
    config = AppConfig(mode=mode)
    click.echo(f"Running in {config.mode} mode")

    if dashboard:
        click.echo("Dashboard not implemented")

    try:
        for opportunity in scan_arbitrage(config):
            execute_trade(config, opportunity)
    except NotImplementedError as exc:
        click.echo(f"Feature not implemented: {exc}")


if __name__ == "__main__":
    main()
