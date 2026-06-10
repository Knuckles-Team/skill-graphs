# Backtesting: The Art of Not Lying to Yourself (Months 3–6)

A backtest simulates how your strategy would have performed on historical data.
It's how every quant tests an idea before risking real money. This is where most
people quit — don't.

## The most important rule: don't look at the future
**Lookahead bias** is when your model accidentally uses tomorrow's data to make
today's decision. It's the most common beginner mistake, and it makes every
strategy look like a genius. Audit every feature and join for future leakage.

## Tools
- **Backtrader** — free, Python.
- **Zipline Reloaded** — free, Python.

## "Hello World": SMA Crossover
When the 50-day moving average crosses above the 200-day, buy; when it crosses
below, sell.

```python
import backtrader as bt

class SMACrossover(bt.Strategy):
    def __init__(self):
        self.sma50 = bt.indicators.SMA(period=50)
        self.sma200 = bt.indicators.SMA(period=200)

    def next(self):
        if self.sma50 > self.sma200 and not self.position:
            self.buy()
        elif self.sma50 < self.sma200 and self.position:
            self.sell()
```

Run it on 10 years of data and compute your **Sharpe Ratio** (return divided by
volatility):
- **> 1.0** — a decent strategy.
- **< 0.5** — back to the drawing board.

Most first strategies are terrible. That's not failure — that's the point. The
backtest told you not to risk real money.

## Then: Pairs Trading with Cointegration
Find two stocks that move together historically (e.g. Coca-Cola and Pepsi). When
they diverge, bet on convergence. This single project forces you to learn
statistical hypothesis testing, z-scores, position sizing, and risk management all
at once — the best single learning project in quant finance. Put it on GitHub with
a README explaining what you did and what the results were.
