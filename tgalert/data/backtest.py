"""Walk a close series and accumulate paper PnL."""

from __future__ import annotations

from tgalert.config import BotConfig
from tgalert.core.risk import RiskManager
from tgalert.data.candles import CandleStore
from tgalert.strategy.base import next_order


def run_backtest(config: BotConfig, bars: int = 64, qty: float = 0.01) -> dict:
    """Replay stub candles and return a summary dict."""
    closes = CandleStore(config.symbol).window(bars)
    risk = RiskManager(config)
    equity = 10_000.0
    fills = 0
    for i in range(3, len(closes)):
        order = next_order(closes[: i + 1], qty, config.strategy)
        if order["side"] == "flat":
            continue
        notional = order["qty"] * order["price"]
        if not risk.allow(notional, equity):
            continue
        fee = notional * config.fee_bps / 10_000
        pnl = (1 if order["side"] == "buy" else -1) * 0.0 - fee
        risk.mark(pnl)
        equity -= fee
        fills += 1
    return {"equity": round(equity, 4), "fills": fills, "bars": bars}
