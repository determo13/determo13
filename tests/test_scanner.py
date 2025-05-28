import sys
import pathlib
import json
import io
from unittest.mock import patch

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from arbitrage.config import AppConfig
from arbitrage.scanner import scan_arbitrage


def test_scanner_returns_data():
    """scan_arbitrage should parse live API responses."""

    def mock_urlopen(url, timeout=10):
        """Return a context-managed BytesIO with dummy JSON."""
        data_path = (
            pathlib.Path(__file__).resolve().parents[1]
            / "arbitrage"
            / "data"
            / "opportunities.json"
        )
        with data_path.open("r", encoding="utf-8") as f:
            opportunities = json.load(f)

        out_amount = int(opportunities[0]["expected_profit_usd"] * 1_000_000)
        payload = json.dumps({"data": [{"outAmount": out_amount}]}).encode("utf-8")

        resp = io.BytesIO(payload)
        resp.__enter__ = lambda self=resp: resp
        resp.__exit__ = lambda *args: None
        return resp

    with patch("urllib.request.urlopen", new=mock_urlopen):
        cfg = AppConfig(mode="live", data_source="live")
        opportunities = list(scan_arbitrage(cfg))

    assert len(opportunities) > 0
    # Ensure the first opportunity has expected keys
    assert "pair" in opportunities[0]
    assert "expected_profit_usd" in opportunities[0]
