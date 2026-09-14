"""Top-level paper engine."""

from __future__ import annotations

from tgalert.config import BotConfig
from tgalert.data.backtest import run_backtest
from tgalert.exchange.client import ExchangeClient


class BotEngine:
    """Owns config, client and last report."""

    def __init__(self, config: BotConfig | None = None) -> None:
        self.config = config or BotConfig()
        self.client = ExchangeClient(self.config)
        self.last: dict | None = None

    def backtest(self, bars: int = 64) -> dict:
        self.last = run_backtest(self.config, bars=bars)
        return self.last

    def paper_tick(self) -> dict:
        price = self.client.ticker()
        order = self.client.place("buy", 0.01, price)
        self.last = {"mode": "paper", "order": order}
        return self.last
