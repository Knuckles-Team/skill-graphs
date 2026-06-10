# The Portfolio That Gets You Hired (Months 6–12)

Nobody hires a resume. They hire demonstrated ability. **Your GitHub profile is
your quant resume.**

## The GitHub rule — every project needs:
1. A clear **README**: what the strategy is and why it should *theoretically* work.
2. **Performance metrics**: Sharpe ratio, max drawdown, CAGR vs benchmark.
3. **Clean, commented code.**
4. An honest **"what didn't work"** section.

Recruiters at mid-tier funds actually look at this. One prop-shop recruiter has
hired candidates with zero finance experience because their GitHub showed rigorous
thinking and honest analysis.

## The 5 projects that move the needle (need ≥3, 5 is better)

### Project 1 — Pairs Trading Strategy
Backtest a cointegration-based strategy on two correlated stocks. Show full stats.
→ workflow `pairs_trading_project`.

### Project 2 — Factor Model
Replicate the **Fama-French 3-factor model**. Download factor data from Kenneth
French's website (free). Regress your returns against the factors.
→ workflow `factor_model_project`.

### Project 3 — Volatility Forecasting
Use **GARCH** models to forecast daily volatility. Compare forecast vs realized
volatility. This is literally what risk desks do.
→ workflow `volatility_forecast_project`.

### Project 4 — Sentiment Alpha
Scrape financial news headlines (NewsAPI free tier). Run **FinBERT** on them. Build
a signal from sentiment. Backtest it.
→ workflow `sentiment_alpha_project`.

### Project 5 — ML Classification
Build a model that predicts whether the S&P 500 will be up or down tomorrow, using
technical indicators as features. **Benchmark against a coin flip.**
→ workflow `ml_classification_project`.

## Metrics glossary
- **Sharpe ratio** — return ÷ volatility. > 1.0 is decent; < 0.5 is weak.
- **Max drawdown** — largest peak-to-trough loss; how bad it got.
- **CAGR vs benchmark** — compound annual growth vs (e.g.) buy-and-hold S&P 500.
