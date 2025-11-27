# Ecaflip

Research project exploring whether **insider trading declarations** on French markets carry a predictive signal on stock returns.

## Goal

Company executives must declare their trades to the AMF (French market regulator). Ecaflip collects these declarations, turns them into features and trains a model to decide which trades are worth following, then backtests the resulting strategies against the CAC 40.

The approach is inspired by [Quiver Quant's Corporate Insider Model](https://quiverquant.medium.com/quiver-quants-corporate-insider-model-752382b9dfd), adapted from US SEC filings to French AMF declarations.

## How it works

| Component | Role | Stack |
|---|---|---|
| `worker/` | Fetches declarations from the AMF BDIF API, parses the PDFs, retrieves tickers and historical prices | Python, Celery, Redis, yfinance |
| `database/` | Schema and migrations for companies, insiders, transactions, quotes and strategies | PostgreSQL, SQLModel, Alembic |
| `model.py` / `model.ipynb` | Feature engineering (insider Elo rating, buy/sell consensus, holdings ratio, momentum) and classification | pandas, LightGBM, Optuna |
| `app/` | Web dashboard: strategy returns vs. benchmark, drawdowns, monthly returns, trade history | FastAPI, Jinja2, Chart.js |

## Run locally

```bash
cp .env.example .env   # fill in Postgres / Redis settings
docker compose up --build
```

The dashboard is served on http://localhost:8000.
