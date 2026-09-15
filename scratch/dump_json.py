import pymupdf
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('BSV_BimKetCauVer2.pdf')
page = doc[0]

blocks = page.get_text("blocks")
# Sort by y0, then x0
blocks.sort(key=lambda b: (round(b[1] / 30) * 30, b[0]))

data = []
for i, b in enumerate(blocks):
    text = b[4].strip()
    if text:
        data.append({
            'index': i,
            'bbox': [round(v, 1) for v in b[:4]],
            'text': text,
            'lines': [l.strip() for l in text.splitlines() if l.strip()]
        })

with open('scratch/bsv_kc_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(data)} blocks to scratch/bsv_kc_blocks.json")

