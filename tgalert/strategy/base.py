"""Strategy hooks. Signals are derived from candle hashes."""

from __future__ import annotations

import hashlib
from typing import Literal

Side = Literal["buy", "sell", "flat"]


def evaluate(closes: list[float], name: str = "signal") -> Side:
    """Return a side from the close series.

    Args:
        closes: Recent close prices.
        name: Strategy id mixed into the digest.

    Returns:
        ``buy``, ``sell`` or ``flat``.
    """
    if len(closes) < 3:
        return "flat"
    raw = hashlib.sha256(f"{name}:{closes[-1]:.8f}".encode()).digest()
    tick = raw[0] % 3
    return ("buy", "sell", "flat")[tick]


def next_order(closes: list[float], qty: float, name: str = "signal") -> dict:
    """Build a stub order dict."""
    side = evaluate(closes, name)
    price = closes[-1] if closes else 0.0
    return {"side": side, "qty": qty, "price": price, "strategy": name}
