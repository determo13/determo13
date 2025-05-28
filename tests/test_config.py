import sys, pathlib; sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from arbitrage.config import AppConfig

def test_default_config():
    cfg = AppConfig()
    assert cfg.mode == "test"
    assert cfg.is_live is False
    assert "SOL" in cfg.watchlist_tokens
