---
name: quant-career-docs
description: >-
  Zero-to-hired quantitative finance career roadmap as a structured knowledge
  graph: the math and Python foundations, finance fundamentals, the three
  canonical strategies, leak-free backtesting, ML for finance (HMM/XGBoost/FinBERT),
  the five portfolio projects that get people hired, certifications, and the
  remote quant job search. No PhD required. Distilled from the "Build a Quant
  Career From Zero" roadmap into native agent-utilities reference.
domain: finance
tags: ['quant', 'career', 'finance', 'roadmap', 'backtesting', 'ml-finance', 'portfolio', 'job-search']
requires: ['data-science-mcp', 'emerald-exchange', 'graph-os']
metadata:
  author: agent-utilities
  version: '1.0.0'
  concepts:
    - 'CONCEPT:KG-2.6'
    - 'CONCEPT:EE-001'
---

# Quant Career Skill Graph

A complete, honest roadmap for building a quantitative-finance career from zero
and landing a (often remote) job — no PhD required. Renaissance Technologies'
Medallion Fund returned ~66% annualized for 34 years; the people behind it were
mathematicians, physicists, and programmers who treated markets as datasets.
This skill graph captures every formula, tool, and step to get on that path.

## Quant role tracks

| Role | What they do | PhD needed? | Realistic first target |
|------|--------------|-------------|------------------------|
| **Quant Researcher (QR)** | Find alpha, build predictive models, design strategies | Top firms expect it | Long-term goal |
| **Quant Developer (QD)** | Turn research models into production code (Python/C++) | No — CS background works | Best entry point |
| **Quant Trader (QT)** | Execute strategies in real time; market-making | No | Prop / market-making shops |
| **Risk Analyst** | Measure how much the fund can lose | No | Accessible on-ramp |

For most beginners the realistic first target is **Quant Developer or Risk
Analyst at a mid-tier firm**, with **Quant Researcher** as the long-term goal.

## 📚 Navigation

| Topic | Reference |
|-------|-----------|
| The four quant roles, salaries, first targets | [reference/roles.md](reference/roles.md) |
| Math you actually need + free resources | [reference/math-foundations.md](reference/math-foundations.md) |
| The Python stack (NumPy → yfinance) | [reference/python-stack.md](reference/python-stack.md) |
| Markets, options/Greeks, bonds, hedge funds | [reference/finance-fundamentals.md](reference/finance-fundamentals.md) |
| The three canonical strategies | [reference/strategies.md](reference/strategies.md) |
| Backtesting without lying to yourself | [reference/backtesting.md](reference/backtesting.md) |
| ML for finance (HMM, XGBoost, FinBERT) | [reference/ml-for-finance.md](reference/ml-for-finance.md) |
| The 5 portfolio projects that get you hired | [reference/portfolio-projects.md](reference/portfolio-projects.md) |
| Competitions (Numerai, QuantConnect, Kaggle) | [reference/competitions.md](reference/competitions.md) |
| Certifications that matter (CQF, CFA, EPAT) | [reference/certifications.md](reference/certifications.md) |
| The remote job search + interviews + timeline | [reference/job-search.md](reference/job-search.md) |

## 🤖 Agent Usage Guide

- When the user asks anything about **becoming a quant, learning quant finance,
  building a quant portfolio, or quant interviews**, consult these reference files.
- Pair this knowledge with the personas (`quant_career_mentor`, `quant_developer`,
  `quant_researcher`, `quant_trader`, `risk_analyst`) and the `quant_career_roadmap`
  workflow + the five project workflows under `workflows/finance/`.
- **The one rule that overrides everything: honest analysis.** Always report the
  Sharpe ratio, the max drawdown, and the regimes where a strategy fails — that
  discipline is what separates practitioners from the hopeful.
- Enable this skill-graph with `QUANT_CAREER_DOCS_ENABLE=true`.
