---
name: trading-risk-management
description: Risk management patterns, circuit breakers, and compliance controls for the trading ecosystem.
---

# Risk Management Skill-Graph — CONCEPT:EE-011 / OS-5.1

Comprehensive risk management patterns enforced by the Emerald Exchange RiskGuard engine.

## P0 Risk Controls

### Circuit Breakers
| Control | Threshold | Action | Recovery |
|---------|-----------|--------|----------|
| Portfolio Drawdown | > 10% from peak | HALT all trading | Manual resume only |
| Daily Loss Limit | > 3% of equity | HALT new orders | Next trading day |
| Regime Shift | KS-test p < 0.05 | HALT + alert | Manual review |
| Kill Switch | Manual trigger | HALT immediately | `emerald_orders(action='resume')` |

### Position Sizing — Kelly Criterion
```
Kelly fraction = W - (1-W)/R
Where:
  W = historical win rate
  R = win/loss ratio (avg win / avg loss)

Capped at: min(kelly, max_position_pct=2%)
```

### Pre-Trade Validation
Every order passes through `RiskGuard.pre_trade_check()`:
1. **Halt check**: Is trading halted?
2. **Position size**: Does this exceed 2% equity limit?
3. **Concentration**: Portfolio exposure to single asset?
4. **Cash availability**: Sufficient buying power?
5. **Live gate**: If live mode, require human approval (OS-5.1)

## Regime Detection — CONCEPT:EE-012

### Hidden Markov Model (HMM)
- 3-state model: Bull, Bear, Neutral
- Trained on rolling 252-day windows
- State transitions trigger portfolio adjustments

### KS-Test Regime Shift
- Kolmogorov-Smirnov test on recent vs historical prediction distributions
- Detects distribution drift before traditional drawdown signals
- p-value < 0.05 triggers circuit breaker

## Monitoring Schedule
| Check | Interval | MCP Tool |
|-------|----------|----------|
| Drawdown | 5 minutes | `emerald_risk(action='drawdown_check')` |
| Daily P&L | 5 minutes | `emerald_risk(action='daily_loss_check')` |
| Regime | 15 minutes | `emerald_signals(action='regime')` |
| Portfolio snapshot | 15 minutes | `emerald_portfolio(action='positions')` |

## Human-in-the-Loop — OS-5.1
- **Paper → Live promotion**: Requires explicit human approval via `graph_orchestrate.request_approval`
- **Kill switch**: Any agent can halt; only human can resume live trading
- **Audit trail**: All risk events persisted as `RiskSnapshot` nodes in KG

## Integration Points
- **Risk MCP**: `emerald_risk` — status, drawdown, daily loss, Kelly, limits
- **Orders MCP**: `emerald_orders` — halt/resume kill switch
- **KG Ontology**: `RiskSnapshot`, `regimeState`, `isHalted` OWL classes
- **Workflow**: `risk-monitoring` cron (every 5 min)
