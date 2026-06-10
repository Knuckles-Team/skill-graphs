# Finance Fundamentals (Months 2–5)

Code without finance context is just noise. You need to know what you're modeling.

## Markets 101
- **How stocks work** — price discovery, bid-ask spread, order types (market,
  limit, stop). Read *A Random Walk Down Wall Street* (Malkiel) — free with most
  library cards.
- **How options work** — calls, puts, strike price, expiry, and the Greeks
  (**Delta, Gamma, Theta, Vega**). The **Black-Scholes** model is the first real
  quant formula most people learn.
- **How bonds work** — duration, yield curves, interest-rate sensitivity. Risk
  models are built on this.
- **What a hedge fund actually does** — long/short equity, market neutral,
  statistical arbitrage, HFT. Read *More Money Than God* (Sebastian Mallaby) for
  the history and culture.

## Black-Scholes
The canonical options-pricing model and the first real quant formula. Requires
calculus (derivatives, integrals, differential equations) — which is why the
calculus foundation matters. Its sensitivities are the Greeks above.

## Why this comes before the modeling
Every strategy and risk model downstream assumes you understand price discovery,
the spread, optionality, and rate sensitivity. Build the vocabulary first.
