# Python First. Always.

Python is the language of quant finance. Not MATLAB. Not R. Not C++ (yet).

## The exact stack, in order
1. **NumPy** — numerical computing. Everything is arrays.
2. **Pandas** — data manipulation. You'll use it every single day.
3. **Matplotlib / Plotly** — visualize your data and strategies.
4. **SciPy** — scientific computing: statistics, optimization, signal processing.
5. **scikit-learn** — machine learning: classification, regression, clustering.
6. **yfinance** — free stock data. Your first data source.

## Your first day as a quant (≈20 minutes)
Install them, open a Jupyter notebook, download 5 years of Apple, plot it, and
compute a rolling 30-day mean:

```python
import yfinance as yf
import matplotlib.pyplot as plt

ticker = yf.Ticker("AAPL")
data = ticker.history(period="5y")
data['Close'].rolling(30).mean().plot()
plt.title("AAPL 30-Day Rolling Mean")
plt.show()
```

That's it. You just wrote quant code.
