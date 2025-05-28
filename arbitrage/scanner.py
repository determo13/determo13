"""Arbitrage opportunity scanner stubs."""

from .config import AppConfig


def scan_arbitrage(config: AppConfig):
    """Yield arbitrage opportunities.

    This stubbed implementation creates a fake opportunity when running in
    ``test`` mode.  In a production system the scanner would query external
    services such as Jupiter's API and evaluate the routes returned for
    profit potential.
    """

    opportunity = {
        "pair": "SOL/USDC",
        "path": ["SOL", "USDC", "SOL"],
        "expected_profit_usd": 1.0,
    }

    if config.mode == "test":
        # In test mode always yield a single synthetic opportunity so the rest
        # of the system has something to act upon.
        yield opportunity
    else:
        # In live mode only yield the opportunity when the expected profit is
        # above the configured minimum.  This keeps the example implementation
        # simple while demonstrating how the configuration might be used.
        if opportunity["expected_profit_usd"] >= config.min_profit_usd:
            yield opportunity
