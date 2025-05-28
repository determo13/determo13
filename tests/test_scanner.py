import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from arbitrage.config import AppConfig
from arbitrage.scanner import scan_arbitrage


def test_scanner_returns_dummy_data():
    cfg = AppConfig(mode="test", data_source="dummy")
    opportunities = list(scan_arbitrage(cfg))
    assert len(opportunities) > 0
    assert "pair" in opportunities[0]
    assert "expected_profit_usd" in opportunities[0]


def test_scanner_handles_live_errors_gracefully():
    cfg = AppConfig(mode="live", data_source="live")
    opportunities = list(scan_arbitrage(cfg))
    assert opportunities == []
