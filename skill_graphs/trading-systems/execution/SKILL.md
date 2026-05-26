---
name: trading-execution
description: Order execution patterns, exchange backend abstraction, and routing for the trading ecosystem.
---

# Execution Skill-Graph — CONCEPT:EE-002 / EE-009

Exchange backend abstraction and order execution patterns.

## Exchange Backend Protocol — CONCEPT:EE-002

All backends implement the `ExchangeBackend` Protocol with a unified interface:

```python
class ExchangeBackend(Protocol):
    @property
    def name(self) -> str: ...
    @property
    def mode(self) -> TradingMode: ...  # paper | live
    @property
    def supported_assets(self) -> list[str]: ...

    def connect(self) -> bool: ...
    def disconnect(self) -> None: ...
    def submit_order(self, symbol, side, qty, order_type, limit_price) -> ExecutionResult: ...
    def cancel_order(self, order_id) -> bool: ...
    def get_order_status(self, order_id) -> ExecutionResult: ...
    def get_positions(self) -> list[Position]: ...
    def get_account(self) -> AccountInfo: ...
    def get_quote(self, symbol) -> Quote: ...
    def get_historical(self, symbol, period, interval) -> list[OHLCV]: ...
```

## Backend Implementations

### PaperBackend (Default) — CONCEPT:EE-003
- Local simulation, no external dependencies
- In-memory position tracking
- Default for all new deployments
- Assets: equity, crypto, forex (simulated)

### AlpacaBackend — CONCEPT:EE-004
- **Free**: Paper trading with real market data
- US equities + crypto
- Library: `alpaca-py`
- Config: `exchanges.alpaca` in config.json

### CCXTBackend — CONCEPT:EE-005
- **100+ crypto exchanges** via unified CCXT library
- Pre-registered shortcuts: `binance`, `coinbase`, `kraken`
- Supports sandbox mode for paper trading
- Library: `ccxt`

### FreqtradeBackend — CONCEPT:EE-006
- Algorithmic crypto trading bot
- REST API integration
- Strategy execution managed by Freqtrade engine
- Library: REST client (no Python dependency)

## Backend Registry & Factory

```python
BACKEND_REGISTRY = {
    "paper": PaperBackend,
    "alpaca": AlpacaBackend,
    "ccxt": CCXTBackend,
    "binance": CCXTBackend,     # Shortcut
    "coinbase": CCXTBackend,    # Shortcut
    "kraken": CCXTBackend,      # Shortcut
    "freqtrade": FreqtradeBackend,
}

# Switch backends at runtime:
backend = create_backend("alpaca", config, TradingMode.PAPER)
```

## Order Lifecycle — CONCEPT:EE-009

```
submit → risk_guard.pre_trade_check() → backend.submit_order() → KG audit
  │              │                              │                    │
  │              └── REJECTED if limits exceeded │                    │
  │                                              └── ExecutionResult  │
  │                                                                   └── VersionedOrder node
```

## Data Classes

| Class | Purpose |
|-------|---------|
| `ExecutionResult` | Order fill result (id, status, qty, price, fees) |
| `Position` | Active portfolio position |
| `AccountInfo` | Account equity, cash, buying power |
| `Quote` | Real-time bid/ask/last/volume |
| `OHLCV` | Historical candle data |

## Adding a New Backend

1. Create class implementing `ExchangeBackend` Protocol
2. Register in `BACKEND_REGISTRY` dict
3. Add config section under `trading.exchanges` in config.json
4. Add infrastructure blueprint YAML in `infrastructure-blueprints/trading/`
5. Register `CONCEPT:EE-0XX` ID in `docs/concepts.md`
