"""Arbitrage opportunity scanner stubs."""

from .config import AppConfig


def scan_arbitrage(config: AppConfig):
    """Yield arbitrage opportunities.

    This is a placeholder implementation. A real version would query
    Jupiter's API and evaluate token routes for profit potential.
    """
    raise NotImplementedError("Arbitrage scanning not implemented")
