"""Arbitrage opportunity scanner stubs."""

from pathlib import Path
import json

from .config import AppConfig


def scan_arbitrage(config: AppConfig):
    """Yield arbitrage opportunities.

    This implementation reads opportunities from a JSON file when running in
    ``test`` mode.  The file provides a simple stand in for real market data
    so the rest of the application can operate on realistic input without
    requiring network access.  In a production system the scanner would query
    external services such as Jupiter's API and evaluate the routes returned
    for profit potential.
    """

    if config.mode == "test":
        # Load opportunities from the bundled JSON dataset.  This simulates
        # fetching real market data while keeping the code self contained.
        data_path = Path(__file__).resolve().parent / "data" / "opportunities.json"
        with data_path.open("r", encoding="utf-8") as f:
            opportunities = json.load(f)

        for item in opportunities:
            yield item
    else:
        # Fallback dummy opportunity for live mode. In a real implementation
        # this branch would query external services.
        opportunity = {
            "pair": "SOL/USDC",
            "path": ["SOL", "USDC", "SOL"],
            "expected_profit_usd": 1.0,
        }

        if opportunity["expected_profit_usd"] >= config.min_profit_usd:
            yield opportunity
