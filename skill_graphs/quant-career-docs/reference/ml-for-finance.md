# Machine Learning for Finance (Months 5–8)

This is where quant and AI intersect. Hedge funds hire people who can do both —
but be honest about what works.

## What actually works
- **Regime detection** (is the market bull or bear?) — Hidden Markov Models.
- **Feature engineering** from financial data — scikit-learn.
- **Predicting direction** (not exact price) — classification models, XGBoost.
- **NLP on earnings calls and news** — sentiment scoring → alpha signal.

## What doesn't work as advertised
- Predicting **exact stock prices with LSTM networks** — finance Twitter oversells
  this enormously.
- Using **raw price as your only feature** — markets are too non-stationary.

## The honest framework
ML in finance is mostly **feature discovery** (finding which signals predict
returns) and **regime identification** (knowing when your strategy should and
shouldn't run). It is not magic price prediction.

## The Markov model that runs hedge funds
**Hidden Markov Models (HMM)** are what quant funds actually use for regime
detection. Markets switch between hidden states (Bull, Bear, Sideways); you can't
observe the state directly but can infer it from returns.

```python
from hmmlearn import hmm
import numpy as np

returns = data['Close'].pct_change().dropna().values.reshape(-1, 1)
model = hmm.GaussianHMM(n_components=3, covariance_type="full", n_iter=100)
model.fit(returns)
hidden_states = model.predict(returns)
```

Three states, fit on returns. The output tells you "right now we're probably in
State 2" (say, the bearish regime). Your strategy turns **off** in bearish regimes
and **on** in bullish ones — regime-conditional investing, in the toolkit of every
serious systematic fund.

## Add this to your stack
- **XGBoost / LightGBM** — gradient-boosted trees. Better than neural nets for
  tabular financial data, faster to train, easier to debug.
- **FinBERT** — a BERT fine-tuned for financial news. Feed it earnings-call
  transcripts, get a sentiment score, use that score as a feature.
- **Prophet / statsmodels** — time-series forecasting and decomposition.
