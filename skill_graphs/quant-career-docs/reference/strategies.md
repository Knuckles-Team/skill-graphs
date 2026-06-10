# The Three Strategies Every Quant Knows

Learn these three, understand *why* they work, then build them.

## 1. Mean Reversion
Prices that go too far from their average tend to come back. **Pairs trading** is
the classic example: in a correlated pair, buy the cheaper stock and short the
expensive one, betting they re-converge. Relies on cointegration and z-scores.

## 2. Momentum
Assets that have gone up tend to keep going up (for a while). The foundational
factor research is **Jegadeesh & Titman (1993)** — free to read on Google Scholar.

## 3. Factor Models
The **Fama-French 3-factor model** explains stock returns through three exposures:
- **Market** (beta)
- **Size** (small minus big)
- **Value** (high minus low book-to-market)

This is foundational — every portfolio manager knows it. Factor data is free from
**Kenneth French's website**.

## How they map to projects
- Mean reversion → the **Pairs Trading with Cointegration** project.
- Factor models → the **Fama-French 3-factor replication** project.
- Momentum → a natural feature/signal in ML classification work.
