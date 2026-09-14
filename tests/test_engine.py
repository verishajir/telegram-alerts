from tgalert.config import BotConfig
from tgalert.core.engine import BotEngine
from tgalert.core.risk import RiskManager
from tgalert.data.backtest import run_backtest
from tgalert.data.candles import CandleStore
from tgalert.exchange.client import ExchangeClient
from tgalert.strategy.base import evaluate, next_order


def test_candles_length() -> None:
    assert len(CandleStore("BTCUSDT").window(20)) == 20


def test_candles_stable() -> None:
    a = CandleStore("BTCUSDT").window(8)
    b = CandleStore("BTCUSDT").window(8)
    assert a == b


def test_evaluate_flat_on_short_series() -> None:
    assert evaluate([1.0]) == "flat"


def test_next_order_keys() -> None:
    order = next_order([1.0, 1.1, 1.2], 0.01)
    assert {"side", "qty", "price", "strategy"} <= set(order)


def test_risk_rejects_oversized() -> None:
    risk = RiskManager(BotConfig(max_position=0.1))
    assert risk.allow(50, 100) is False


def test_risk_allows_small() -> None:
    risk = RiskManager(BotConfig(max_position=0.5))
    assert risk.allow(10, 100) is True


def test_backtest_report() -> None:
    report = run_backtest(BotConfig(), bars=32)
    assert report["bars"] == 32
    assert report["equity"] > 0


def test_engine_backtest() -> None:
    engine = BotEngine(BotConfig())
    report = engine.backtest(16)
    assert engine.last == report


def test_paper_tick_records_order() -> None:
    engine = BotEngine(BotConfig())
    engine.paper_tick()
    assert len(engine.client.orders) == 1


def test_ticker_positive() -> None:
    client = ExchangeClient(BotConfig())
    assert client.ticker() > 0
