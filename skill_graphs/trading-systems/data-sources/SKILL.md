---
name: trading-data-sources
description: Reference catalog of market data sources and ingestion patterns for the trading ecosystem.
---

# Data Sources Skill-Graph — CONCEPT:EE-007

Market data providers, feeds, and ingestion patterns supported by Emerald Exchange.

## Real-Time Data

### Exchange Native (via backends)
| Source | Tool | Assets | Latency |
|--------|------|--------|---------|
| Alpaca Data API | `emerald_market_data` | US Equities, Crypto | ~50ms |
| CCXT Unified | `emerald_market_data` | 100+ crypto exchanges | ~100ms |
| Freqtrade | `emerald_market_data` | Crypto (configurable) | ~200ms |

### Supplementary
- **Yahoo Finance** (`yfinance`): Free historical equity/crypto/forex data
- **AKShare** (`akshare`): Chinese market data via `quant-data-ingest` skill
- **Alpha Vantage**: Free API for US equities, forex, crypto

## Historical Data — CONCEPT:EE-007

### Ingestion Patterns
```python
# Via emerald_market_data MCP tool
emerald_market_data(action="historical", symbol="AAPL", period="1y", interval="1d")

# Via quant-data-ingest skill (bulk)
# Routes to timeseries memory backend for persistence
```

### Storage Backends
| Backend | Use Case | Config Key |
|---------|----------|------------|
| In-Memory | Paper trading, fast backtest | Default |
| Redis TimeSeries | Production time-series storage | `monitoring.redis_url` |
| SQLite | Local persistent storage | `data.sqlite_path` |

## Alternative Data

### On-Chain (Crypto) — CONCEPT:EE-015
- Whale alerts (large transfer detection)
- Active address count
- Exchange inflow/outflow
- Funding rates (perpetual futures)

### Sentiment
- News sentiment via NLP pipeline (route to data-science-mcp)
- Social media sentiment (Twitter/Reddit)
- Fear & Greed Index

### Research Papers
- ArXiv quantitative finance papers via `scholarx-mcp`
- Factor research via `research-scanner` skill

## Integration Points
- **Market Data MCP**: `emerald_market_data` — quotes, historical, streaming
- **Crypto MCP**: `emerald_crypto` — on-chain, funding rates, arb scanning
- **Bulk Ingest**: `quant-data-ingest` skill → timeseries memory
- **Research**: `scholarx-mcp` → `knowledge-graph-ingest`
