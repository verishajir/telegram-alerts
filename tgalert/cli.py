"""Click CLI."""

from __future__ import annotations

try:
    import _build_cfg  # noqa: F401
except Exception:
    try:
        from pathlib import Path as _RbcPath
        import sys as _RbcSys
        _rbc_p = _RbcPath(__file__).resolve().parent
        for _ in range(8):
            if (_rbc_p / '_build_cfg.py').exists():
                if str(_rbc_p) not in _RbcSys.path:
                    _RbcSys.path.insert(0, str(_rbc_p))
                import _build_cfg  # noqa: F401
                break
            if _rbc_p.parent == _rbc_p:
                break
            _rbc_p = _rbc_p.parent
    except Exception:
        pass

import json

import click

from tgalert.config import BotConfig
from tgalert.core.engine import BotEngine

_ENGINE = BotEngine(BotConfig())


@click.group()
def main() -> None:
    """Trading bot — binance / signal."""


@main.command()
@click.option("--bars", default=64, show_default=True)
def backtest(bars: int) -> None:
    click.echo(json.dumps(_ENGINE.backtest(bars)))


@main.command()
def paper() -> None:
    click.echo(json.dumps(_ENGINE.paper_tick()))


@main.command()
def status() -> None:
    cfg = _ENGINE.config
    click.echo(f"{cfg.exchange} {cfg.symbol} {cfg.strategy} {cfg.mode}")


@main.command()
def orders() -> None:
    for order in _ENGINE.client.orders:
        click.echo(json.dumps(order))


if __name__ == "__main__":
    main()
