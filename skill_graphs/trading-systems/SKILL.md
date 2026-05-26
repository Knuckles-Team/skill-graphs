---
name: trading-systems
description: >-
  Comprehensive trading systems skill-graph covering exchange backends,
  risk management, algorithmic strategy design, portfolio optimization,
  and market microstructure. Distilled from open-source trading libraries
  (qlib, freqtrade, TradingAgents, FinRL, CCXT) into native agent-utilities patterns.
domain: finance
tags: ['trading', 'finance', 'risk', 'quant', 'crypto', 'equities']
requires: ['emerald-exchange', 'data-science-mcp', 'graph-os']
metadata:
  author: agent-utilities
  version: '1.0.0'
  concepts:
    - 'CONCEPT:KG-2.6'
    - 'CONCEPT:EE-001'
    - 'CONCEPT:EE-007'
---

# Trading Systems Skill Graph

Knowledge distilled from 14+ open-source trading libraries into native
agent-utilities patterns. This skill graph provides structured reference
for all aspects of automated trading.

## 1. Exchange Backend Architecture

### Pattern: Protocol-Based Backend Abstraction (CONCEPT:EE-002)

Every exchange backend implements the `ExchangeBackend` Protocol:

| Method | Purpose |
|--------|---------|
| `connect()` | Initialize connection (API keys, websockets) |
| `submit_order(symbol, side, qty, type, limit_price)` | Submit order with risk guard pre-check |
| `cancel_order(order_id)` | Cancel pending order |
| `get_positions()` | List all open positions |
| `get_account()` | Account summary (equity, cash, buying power) |
| `get_quote(symbol)` | Current bid/ask/last/volume |
| `get_historical(symbol, period, interval)` | OHLCV data |

### Backend Selection

```python
from emerald_exchange.backends import create_backend, TradingMode

# Paper (default, always safe)
backend = create_backend("paper", {}, TradingMode.PAPER)

# Alpaca (FREE paper trading for equities + crypto)
backend = create_backend("alpaca", {
    "api_key": "...", "api_secret": "...",
    "base_url": "https://paper-api.alpaca.markets"
}, TradingMode.PAPER)

# CCXT (100+ crypto exchanges)
backend = create_backend("binance", {
    "api_key": "...", "api_secret": "..."
}, TradingMode.PAPER)
```

## 2. Risk Management (OS-5.1)

### Pre-Trade Validation (CONCEPT:EE-007)

Every order passes through `RiskGuard.pre_trade_check()` before submission:

1. **Kill switch check**: Is trading halted?
2. **Live mode check**: Does live trading require human approval?
3. **Position sizing**: Kelly criterion with configurable cap (default 2%)
4. **Cash sufficiency**: Can the portfolio afford this trade?

### Circuit Breakers (CONCEPT:EE-016)

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Portfolio drawdown | 10% from peak | Auto-halt all trading |
| Daily loss | 3% of equity | Auto-halt all trading |
| Regime shift | KS-test > 0.1 | Auto-halt all trading |

### Kelly Criterion (CONCEPT:EE-015)

```python
# Half-Kelly with 2% cap
f = RiskGuard.kelly_criterion(
    win_rate=0.6,      # 60% win rate
    win_loss_ratio=2.0, # Winners 2x losers
    half_kelly=True,    # Conservative
    max_risk=0.02,      # Never exceed 2%
)
```

## 3. Signal Generation & Fusion

### Alpha Factor Pipeline
1. **Feature Engineering**: Technical indicators, fundamental ratios, alternative data
2. **IC/IR Scoring**: Information Coefficient and Information Ratio ranking
3. **Regime Detection**: HMM-based market state classification (Bull/Bear/Sideways/Crisis)
4. **Bayesian Fusion**: Combine multiple signal sources with uncertainty weighting

### Market Regimes
- **Bull**: Positive momentum, low volatility — increase equity exposure
- **Bear**: Negative momentum, rising volatility — reduce exposure, hedge
- **Sideways**: Range-bound — mean reversion strategies, options selling
- **Crisis**: High correlation, extreme volatility — risk-off, kill switch ready

## 4. Strategy Lifecycle (CONCEPT:EE-013)

```
Draft → Backtest → Paper → Live
         ↑           ↑        ↑
         │           │        └── Human approval REQUIRED
         │           └── Minimum 30-day paper validation
         └── Minimum 2-year backtest with walk-forward
```

### Promotion Gates
| Stage | Requirements |
|-------|-------------|
| Draft → Backtest | Hypothesis documented in KG, debate completed |
| Backtest → Paper | Sharpe > 1.0, max drawdown < 15%, 2yr minimum |
| Paper → Live | 30-day paper profit, risk officer approval, human sign-off |

## 5. Portfolio Optimization

### Supported Optimizers
- **Mean-Variance (MVO)**: Classic Markowitz with shrinkage estimators
- **Risk Parity**: Equal risk contribution across assets
- **Black-Litterman**: Bayesian combination of market equilibrium + views
- **Hierarchical Risk Parity (HRP)**: Cluster-based allocation

### Rebalancing Schedule
- **Tactical**: Weekly (Monday 9AM ET) via `portfolio-rebalance` workflow
- **Strategic**: Monthly review with Brinson attribution analysis
