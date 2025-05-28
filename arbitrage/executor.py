"""Trade execution stubs."""

from .config import AppConfig


def execute_trade(config: AppConfig, opportunity: dict) -> str:
    """Execute a trade based on the provided opportunity.

    Parameters
    ----------
    config:
        Application configuration.
    opportunity:
        Arbitrage opportunity details.

    Returns
    -------
    str
        Transaction signature.
    """
    raise NotImplementedError("Trade execution not implemented")
