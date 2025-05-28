import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from arbitrage.config import AppConfig
from arbitrage.scanner import scan_arbitrage


def test_scanner_returns_data():
    cfg = AppConfig(mode="test")
    opportunities = list(scan_arbitrage(cfg))
    assert len(opportunities) > 0
    # Ensure the first opportunity has expected keys
    assert "pair" in opportunities[0]
    assert "expected_profit_usd" in opportunities[0]
