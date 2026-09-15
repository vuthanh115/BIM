import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/bsv_kc_blocks.json', 'r', encoding='utf-8') as f:
    blocks = json.load(f)

keywords = ['atool', 'bimspeed', 'tool']

print(f"=== SEARCHING IN BSV_BimKetCauVer2.pdf BLOCKS ===")
matches = []

for b in blocks:
    text = b['text']
    for kw in keywords:
        if re.search(rf'\b{kw}\b', text, re.IGNORECASE):
            matches.append((kw, b))
            break

print(f"Total blocks matching keywords: {len(matches)}\n")

for kw, b in matches:
    print(f"--- Block {b['index']} (Bbox: {b['bbox']}) [Matched: '{kw}'] ---")
    print(b['text'].strip())
    print()

