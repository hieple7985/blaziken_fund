#!/usr/bin/env python3

import click
from rich.console import Console

from backend.config import AppConfig
from backend.agent import BlazikenAgent


console = Console()


@click.group()
def cli() -> None:
    pass


@cli.command()
def status() -> None:
    config = AppConfig.from_env()
    agent = BlazikenAgent.from_config(config=config)
    snapshot = agent.load_portfolio()

    console.print(f"Environment: {config.environment}")
    console.print(f"Total positions: {len(snapshot.positions)}")
    console.print(f"Total value: {snapshot.total_value:.2f}")


@cli.command("run-cycle")
def run_cycle() -> None:
    config = AppConfig.from_env()
    agent = BlazikenAgent.from_config(config=config)
    snapshot = agent.run_cycle()

    console.print("Cycle completed.")
    console.print(f"Total positions: {len(snapshot.positions)}")
    console.print(f"Total value after cycle: {snapshot.total_value:.2f}")


if __name__ == "__main__":
    cli()
