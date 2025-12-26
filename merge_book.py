# merge_book.py
from PyPDF2 import PdfMerger
import os

SAMPLES_DIR = "samples"
OUTPUT_FILE = "Trading_Book.pdf"

merger = PdfMerger()

# Collect PDFs
pdf_files = [
    f for f in os.listdir(SAMPLES_DIR)
    if f.endswith(".pdf") and f.startswith("NQ_")
]

# Sort by filename (date-based)
pdf_files.sort()

if not pdf_files:
    print("No PDFs found to merge.")
    exit()

for pdf in pdf_files:
    merger.append(os.path.join(SAMPLES_DIR, pdf))
    print(f"Added: {pdf}")

merger.write(OUTPUT_FILE)
merger.close()

print(f"\n📘 Trading book created: {OUTPUT_FILE}")
