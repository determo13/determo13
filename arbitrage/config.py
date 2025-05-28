from dataclasses import dataclass, field
from typing import List

@dataclass
class AppConfig:
    """Configuration for the trading app."""
    mode: str = "test"  # "test" or "live"
    min_profit_usd: float = 0.5
    max_slippage_pct: float = 0.3
    trade_cooldown_sec: int = 15
    watchlist_tokens: List[str] = field(default_factory=lambda: ["SOL", "USDC", "USDT"])

    @property
    def is_live(self) -> bool:
        return self.mode == "live"
