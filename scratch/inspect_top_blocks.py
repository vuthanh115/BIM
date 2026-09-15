import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('BSV_BimKetCauVer2.pdf')
page = doc[0]

blocks = page.get_text("blocks")
# Sort by y0, then x0
blocks.sort(key=lambda b: (round(b[1] / 50) * 50, b[0]))

print(f"Total blocks: {len(blocks)}")
for i in range(min(50, len(blocks))):
    b = blocks[i]
    text = b[4].strip()
    if text:
        bbox = f"({b[0]:.1f}, {b[1]:.1f})"
        first_line = text.splitlines()[0]
        print(f"B{i:02d} {bbox}: {first_line[:50]} ({len(text.splitlines())} lines)")

