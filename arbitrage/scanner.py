"""Arbitrage opportunity scanner stubs."""

from pathlib import Path
import json
import urllib.error

TOKEN_MINTS = {
    "SOL": "So11111111111111111111111111111111111111112",
    "USDC": "EPjFWdd5AufqSSqeM2qP2AMi9kNo6TwL8NXKDxNqGsQ",
    "USDT": "Es9vMFrzaCERj2QTTbkfSUmB7So8yKhvKXgjx6BX3VWn",
}

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

    if config.data_source == "dummy":
        if config.mode == "test":
            # Load opportunities from the bundled JSON dataset.  This simulates
            # fetching real market data while keeping the code self contained.
            data_path = Path(__file__).resolve().parent / "data" / "opportunities.json"
            with data_path.open("r", encoding="utf-8") as f:
                opportunities = json.load(f)

            for item in opportunities:
                yield item
        else:
            # Fallback dummy opportunity for live mode.
            opportunity = {
                "pair": "SOL/USDC",
                "path": ["SOL", "USDC", "SOL"],
                "expected_profit_usd": 1.0,
            }

            if opportunity["expected_profit_usd"] >= config.min_profit_usd:
                yield opportunity
    elif config.data_source == "live":
        # Query Jupiter's public quote API for SOL -> USDC routes.  The
        # response describes multiple swap routes.  For simplicity we pick the
        # first one and convert the output amount to a profit metric.
        #
        # This code path requires network access.  It will raise an exception if
        # the HTTP request fails or if the response structure does not match the
        # expectations.  In offline environments the request will fail.
        import json as _json
        from urllib import parse, request

        base_url = "https://quote-api.jup.ag/v6/quote"
        params = {
            "inputMint": TOKEN_MINTS["SOL"],
            "outputMint": TOKEN_MINTS["USDC"],
            # Quote for one SOL (9 decimals)
            "amount": 1_000_000_000,
            "slippageBps": int(config.max_slippage_pct * 100),
        }

        url = f"{base_url}?{parse.urlencode(params)}"
        try:
            with request.urlopen(url, timeout=10) as resp:
                data = _json.load(resp)
        except urllib.error.HTTPError as exc:
            print(f"HTTP error fetching quote data: {exc}")
            return
        except urllib.error.URLError as exc:
            print(f"Network error fetching quote data: {exc}")
            return

        routes = data.get("data") or data.get("routes", [])
        if not routes:
            return

        best_route = routes[0]
        out_amount = int(best_route.get("outAmount", 0))
        # USDC has 6 decimals
        out_amount_usd = out_amount / 1_000_000

        opportunity = {
            "pair": "SOL/USDC",
            "path": ["SOL", "USDC", "SOL"],
            "expected_profit_usd": out_amount_usd,
        }

        if opportunity["expected_profit_usd"] >= config.min_profit_usd:
            yield opportunity
    else:
        raise ValueError(f"Unknown data source: {config.data_source}")
