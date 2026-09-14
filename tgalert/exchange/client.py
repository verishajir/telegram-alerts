"""Stub exchange client."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

from tgalert.config import BotConfig


@dataclass
class ExchangeClient:
    """In-memory order book. Nothing leaves the process."""

    config: BotConfig
    orders: list[dict] = field(default_factory=list)

    def ticker(self) -> float:
        raw = hashlib.sha256(
            f"{self.config.exchange}:{self.config.symbol}".encode()
        ).digest()
        return 10_000 + (int.from_bytes(raw[:2], "big") / 100)

    def place(self, side: str, qty: float, price: float) -> dict:
        order = {
            "id": len(self.orders) + 1,
            "side": side,
            "qty": qty,
            "price": price,
            "venue": "binance",
        }
        self.orders.append(order)
        return order
