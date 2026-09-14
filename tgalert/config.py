"""Bot configuration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BotConfig:
    """Paper-trading defaults. No API secrets are required."""

    exchange: str = "binance"
    symbol: str = "BTCUSDT"
    strategy: str = "signal"
    mode: str = "paper"
    max_position: float = 0.25
    daily_loss: float = 0.03
    fee_bps: float = 8.0
