# telegram-alerts

> telegram · alert · paper

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

Telegram alert hook — evaluate() is what a relay would call.

## Features

- Default venue binance / BTCUSDT
- Built-in signal strategy plus paper mode
- Risk manager with daily-loss kill switch
- OHLCV store and SHA-256 stub candles
- Backtester with fill + fee model
- Click CLI: backtest, paper, status, orders

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd telegram-alerts
python -m pip install -e .
python -m tgalert --help
```

## CLI Usage

```bash
tgalert backtest --bars 200
# Replay stub candles

tgalert paper
# Start a paper session

tgalert status
# Print engine state

tgalert orders
# List simulated fills
```

## Project Structure

```
tgalert/
  core/        engine + risk
  strategy/    grid / dca / ema hooks
  exchange/    stub order client
  data/        candles + backtest
  cli.py
tests/
```

## Configuration

See `tgalert/config.py`.

| Setting | Default | Description |
|---------|---------|-------------|
| `exchange` | `binance` | Venue id |
| `symbol` | `BTCUSDT` | Default pair |
| `strategy` | `signal` | Active strategy |
| `mode` | `paper` | paper or backtest |

## Tests

```bash
python -m pytest -q
```

## Background

Signal groups bookmark telegram-alerts, not telegram-crypto-bot.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![telegram](https://img.shields.io/badge/telegram-111827?style=flat-square) ![alerts](https://img.shields.io/badge/alerts-111827?style=flat-square) ![telegram-alerts](https://img.shields.io/badge/telegram%20alerts-111827?style=flat-square) ![trading-bot](https://img.shields.io/badge/trading%20bot-111827?style=flat-square) ![crypto-trading](https://img.shields.io/badge/crypto%20trading-111827?style=flat-square) ![binance](https://img.shields.io/badge/binance-111827?style=flat-square) ![defi](https://img.shields.io/badge/defi-111827?style=flat-square) ![algorithmic-trading](https://img.shields.io/badge/algorithmic%20trading-111827?style=flat-square)

`telegram` `alerts` `telegram-alerts` `trading-bot` `crypto-trading` `binance` `defi` `algorithmic-trading` `quantitative-finance` `open-source` `python`

Search: telegram-alerts · telegram · alert · paper · Telegram alert hook — evaluate() is what a relay would call.

---

<sub>Telegram alert hook — evaluate() is what a relay would call.</sub>
