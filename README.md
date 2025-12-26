Overview

This project automates the process of capturing daily New York (NY) session charts from TradingView and generating PDF reports for multiple market symbols. The system is fully automated using Python and Playwright, ensuring you never miss a trading day’s snapshots.

Multi-symbol support: NQ, ES, CL, BTC

Automated PDF generation for each symbol

Daily scheduling via Windows Task Scheduler

Headless browser automation (no manual clicks required)

Features

✅ Automated Chart Capture

Captures charts from TradingView for predefined symbols

Saves both screenshots and PDFs in the samples/ folder

✅ Multi-Symbol Support

Easily configurable to capture any symbols you want

Currently includes: NQ, ES, CL, BTC

✅ Daily Automation

Task Scheduler triggers the script daily at NY session close

Fully hands-free workflow

✅ Portfolio-Ready

Demonstrates professional automation skills

Ready for freelance or professional applications

Installation

Clone the project to your local machine

Install dependencies:

pip install playwright PyPDF2
playwright install


Set up authentication:

python auth/auth_setup.py


This will save tv_auth.json with TradingView login cookies

Usage
Capture Charts
python capture_chart.py


Captures all configured symbols

Saves screenshots and PDFs to samples/

Merge PDFs into One Book
python merge_book.py


Combines all symbol PDFs into Trading_Book.pdf

Automation

Use Windows Task Scheduler to run capture_chart.py daily

Set the trigger at NY session close (7:45 PM NPT for Nepal)

Optional: Add a second trigger 10 minutes later for backup

Notes

Works on Windows with Python ≥3.10

Requires internet connection to access TradingView

Headless browser ensures minimal interference

Easily extensible for additional symbols or sessions

Skills Demonstrated

Python scripting and automation

Web automation with Playwright

PDF handling and image processing

Task Scheduler automation

Professional project documentation

Output Example
samples/
├── NQ_NY_Session_2025-12-26.png
├── NQ_NY_Session_2025-12-26.pdf
├── ES_NY_Session_2025-12-26.pdf
├── CL_NY_Session_2025-12-26.pdf
├── BTC_NY_Session_2025-12-26.pdf
└── Trading_Book.pdf
