import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('BSV_BimKetCauVer2.pdf')
page = doc[0]

blocks = page.get_text("blocks")
print(f"Total blocks: {len(blocks)}")

# Sort blocks top-to-bottom, left-to-right
blocks.sort(key=lambda b: (round(b[1] / 100) * 100, b[0]))

for i, b in enumerate(blocks):
    text = b[4].strip()
    if text:
        bbox = f"({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f})"
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        first_line = lines[0] if lines else ""
        print(f"Block {i:02d} {bbox}: {first_line[:45]} | {len(lines)} lines")

