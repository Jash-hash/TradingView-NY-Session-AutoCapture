# TradingView Chart Automation & Flipbook Generator

This project automates TradingView chart screenshots and generates
daily PDFs and flipbook-style trading books for backtesting.

It uses Playwright to load TradingView charts, capture screenshots,
and automatically merge them into organized PDF books.

---

## Features
- Automated TradingView chart capture
- Supports multiple symbols (NQ, ES)
- Multiple timeframes (1m, 5m, 15m, 1h)
- Saves charts by date
- Generates daily PDFs
- Maintains flipbook-style trading books
- Optional parallel execution for faster processing

---

## Setup Instructions

### 1. Install Python
Python 3.10+ recommended

### 2. Install dependencies
```bash
pip install -r requirements.txt

3. Install Playwright browser
python -m playwright install chromium

Authentication

Login session is handled using cookies saved in:

auth/tv_auth.json


You can generate it using:

python auth_setup.py

Run Scripts
Capture charts (single process)
python capture_chart.py

Faster parallel capture (recommended for large data)
python capture_chart_parallel.py

Output

All generated files are saved in:

samples/


Includes:

Daily screenshots

Daily PDFs

Flipbook trading books (auto-updated)

Notes

No TradingView API required

Works with Free or Pro TradingView accounts

Designed for backtesting and strategy review




