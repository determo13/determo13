"""Trade execution stubs."""

from .config import AppConfig


def execute_trade(config: AppConfig, opportunity: dict) -> str:
    """Execute a trade based on the provided opportunity.

    This function does not perform any real blockchain interaction.  Instead
    it prints a short description of the trade and returns a mock transaction
    signature.  The behaviour differs slightly based on whether the
    application is running in ``test`` or ``live`` mode so that downstream
    consumers can react accordingly.

    Parameters
    ----------
    config:
        Application configuration.
    opportunity:
        Arbitrage opportunity details.

    Returns
    -------
    str
        Transaction signature placeholder.
    """

    if config.is_live:
        print(f"Executing trade in live mode: {opportunity}")
        return "LIVE_TX_SIGNATURE"

    print(f"Simulated trade: {opportunity}")
    return "TEST_TX_SIGNATURE"
