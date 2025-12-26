# auth_setup.py
from playwright.sync_api import sync_playwright
import json
import os

# Paths
COOKIES_FILE = "cookies.json"
AUTH_FILE = "auth/tv_auth.json"

if not os.path.exists(COOKIES_FILE):
    print("Error: cookies.json not found. Export cookies from TradingView first.")
    exit()

# Load cookies safely (handles both list or dict with "cookies" key)
with open(COOKIES_FILE, "r") as f:
    data = json.load(f)

if isinstance(data, list):
    cookies = data
else:
    cookies = data.get("cookies", [])

if not cookies:
    print("No cookies found in cookies.json")
    exit()

# Normalize sameSite values for Playwright
for c in cookies:
    if "sameSite" in c:
        val = str(c["sameSite"]).capitalize()
        if val not in ["Strict", "Lax", "None"]:
            val = "Lax"
        c["sameSite"] = val
    else:
        c["sameSite"] = "Lax"

# Make auth folder if not exists
os.makedirs("auth", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # headless for slow laptops
    context = browser.new_context()
    
    # Add cookies to the browser context
    context.add_cookies(cookies)
    
    # Open TradingView chart page (dummy chart)
    page = context.new_page()
    page.goto("https://www.tradingview.com/chart/?symbol=CME_MINI:NQ1!", timeout=180000)
    page.wait_for_timeout(10000)  # wait 10 seconds for chart to load

    # Save session to tv_auth.json
    context.storage_state(path=AUTH_FILE)
    browser.close()
    print(f"tv_auth.json saved successfully at {AUTH_FILE}!")



