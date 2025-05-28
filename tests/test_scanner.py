import sys
import pathlib
import json
import io
from unittest.mock import patch

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import io
import json
from pathlib import Path
from arbitrage.config import AppConfig
from arbitrage.scanner import scan_arbitrage
import urllib.request


    # Convert the expected_profit_usd entries to the format returned by the
    # live API ("outAmount" in atomic units)
    mock_payload = {
        "data": [
            {"outAmount": int(item["expected_profit_usd"] * 1_000_000)}
            for item in dataset
        ]
    }

    class MockHTTPResponse(io.StringIO):
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            pass

    def mock_urlopen(url, timeout=10):
        return MockHTTPResponse(json.dumps(mock_payload))

    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)


def test_scanner_returns_data(monkeypatch):
    """scan_arbitrage should yield opportunities from a mocked HTTP response."""

    # Load the bundled opportunities dataset to build the mock API response
    data_path = Path(__file__).resolve().parents[1] / "arbitrage" / "data" / "opportunities.json"
    with data_path.open("r", encoding="utf-8") as f:
        dataset = json.load(f)

    # Convert the expected_profit_usd entries to the format returned by the
    # live API ("outAmount" in atomic units)
    mock_payload = {
        "data": [
            {"outAmount": int(item["expected_profit_usd"] * 1_000_000)}
            for item in dataset
        ]
    }

    class MockHTTPResponse(io.StringIO):
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            pass

    def mock_urlopen(url, timeout=10):
        return MockHTTPResponse(json.dumps(mock_payload))

    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)


    cfg = AppConfig(mode="live", data_source="live")
    opportunities = list(scan_arbitrage(cfg))

    # scan_arbitrage yields the first route as an opportunity
    expected = dataset[0]
    assert opportunities == [expected]
