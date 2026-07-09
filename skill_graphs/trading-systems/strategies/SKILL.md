---
name: trading-strategies
skill_type: graph
description: Reference catalog of trading strategy patterns available in the Emerald Exchange ecosystem.
---

# Trading Strategies Skill-Graph — CONCEPT:EE-013

Reference catalog of strategy archetypes supported by the Emerald Exchange strategy lifecycle.

## Strategy Types

### Momentum
- **Trend Following**: EMA crossover, Bollinger breakout, ADX-filtered
- **Relative Strength**: Sector rotation, pair momentum, cross-sectional momentum
- **Time-Series Momentum**: TSMOM 1M/3M/12M look-back

### Mean Reversion
- **Statistical Arbitrage**: Pairs trading via cointegration (Engle-Granger)
- **Bollinger Mean Reversion**: Z-score entry/exit on Bollinger bands
- **Ornstein-Uhlenbeck**: Mean-reversion speed estimation

### Factor-Based
- **Multi-Factor**: Value + Momentum + Quality + Low-Vol composite
- **Alpha Factors**: IC/IR scoring via QLib factor pipeline
- **Fama-French**: 3-factor and 5-factor model decomposition

### Machine Learning
- **Regime Detection**: HMM-based (Hidden Markov Model) state classification
- **Signal Prediction**: LightGBM/XGBoost on engineered features
- **Deep Learning**: Transformer-based price prediction (route to GPU via data-science-mcp)

### Crypto-Native
- **Funding Rate Arbitrage**: Long spot / short perp when funding > threshold
- **Cross-Exchange Arbitrage**: Bid-ask spread exploitation across CCXT backends
- **DeFi Yield**: Liquidity provision optimization (requires on-chain integration)

## Strategy Lifecycle — CONCEPT:EE-013

```
draft → backtest → paper → live
  │        │         │       │
  │        │         │       └── Requires human approval (OS-5.1)
  │        │         └── 30-day minimum paper trading
  │        └── Sharpe > 1.5, MaxDD < 15%
  └── Hypothesis documented in KG
```

## Integration Points
- **Backtest Engine**: Routes to `data-science-mcp` on GPU hardware
- **Signal Generation**: `emerald_signals` MCP tool
- **Risk Validation**: `emerald_risk` pre-trade checks
- **Export**: PineScript, MQL5, TDX via `emerald_strategy(action='export')`
