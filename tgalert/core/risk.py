"""Position and daily-loss checks."""

from __future__ import annotations

from tgalert.config import BotConfig


class RiskManager:
    """Rejects size that exceeds the configured caps."""

    def __init__(self, config: BotConfig) -> None:
        self.config = config
        self.realized = 0.0

    def allow(self, notional: float, equity: float) -> bool:
        """Return False when size or daily loss is too large."""
        if equity <= 0:
            return False
        if notional / equity > self.config.max_position:
            return False
        if self.realized < 0 and abs(self.realized) / equity >= self.config.daily_loss:
            return False
        return True

    def mark(self, pnl: float) -> None:
        self.realized += pnl
