import pymupdf
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = 'BSV_BimKetCauVer2.pdf'
doc = pymupdf.open(pdf_path)

print(f"File: {pdf_path}")
print(f"Total pages: {len(doc)}")
print(f"File size: {os.path.getsize(pdf_path)} bytes")

for pno in range(len(doc)):
    page = doc[pno]
    text = page.get_text()
    images = page.get_images()
    print(f"\n--- PAGE {pno + 1} ({len(text)} chars, {len(images)} images) ---")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    print("\n".join(lines[:15]))
    if len(lines) > 15:
        print(f"... and {len(lines) - 15} more lines")

