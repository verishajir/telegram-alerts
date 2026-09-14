"""Deterministic OHLCV series."""

from __future__ import annotations

import hashlib


class CandleStore:
    """Build a synthetic candle window from a symbol seed."""

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def window(self, bars: int = 64) -> list[float]:
        """Return ``bars`` close prices."""
        closes: list[float] = []
        price = 100.0
        for i in range(bars):
            raw = hashlib.sha256(f"{self.symbol}:{i}".encode()).digest()
            delta = (raw[0] - 128) / 50
            price = max(1.0, price + delta)
            closes.append(round(price, 4))
        return closes
