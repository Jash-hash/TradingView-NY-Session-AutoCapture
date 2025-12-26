# capture_chart.py
from playwright.sync_api import sync_playwright
from datetime import datetime
from reportlab.pdfgen import canvas
from PIL import Image
import os

AUTH_FILE = "auth/tv_auth.json"
OUTPUT_DIR = "samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# SYMBOL CONFIG (easy to extend)
SYMBOLS = {
    "NQ": "CME_MINI:NQ1!",
    "ES": "CME_MINI:ES1!",
    "CL": "NYMEX:CL1!",
    "BTC": "BINANCE:BTCUSDT"
}

today = datetime.now().strftime("%Y-%m-%d")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        storage_state=AUTH_FILE,
        viewport={"width": 1600, "height": 900}
    )
    page = context.new_page()

    for name, symbol in SYMBOLS.items():
        print(f"\n📊 Capturing {name}...")

        png_path = f"{OUTPUT_DIR}/{name}_NY_Session_{today}.png"
        pdf_path = f"{OUTPUT_DIR}/{name}_NY_Session_{today}.pdf"

        page.goto(
            f"https://www.tradingview.com/chart/?symbol={symbol}",
            timeout=180000
        )

        page.wait_for_timeout(15000)

        # Force 1-minute timeframe
        page.keyboard.press("1")
        page.keyboard.press("m")
        page.wait_for_timeout(3000)

        # Zoom in
        for _ in range(5):
            page.keyboard.press("Control+-")
            page.wait_for_timeout(300)

        # Scroll to NY session visually
        page.mouse.wheel(0, -3000)
        page.wait_for_timeout(3000)

        # Screenshot
        page.screenshot(path=png_path)
        print(f"Saved screenshot → {png_path}")

        # Convert to PDF
        img = Image.open(png_path)
        c = canvas.Canvas(pdf_path, pagesize=(img.width, img.height))
        c.drawImage(png_path, 0, 0, img.width, img.height)
        c.showPage()
        c.save()

        print(f"Saved PDF → {pdf_path}")

    browser.close()

print("\n✅ All symbols captured successfully.")




