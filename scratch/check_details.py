import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/bsv_kc_blocks.json', 'r', encoding='utf-8') as f:
    blocks = json.load(f)

print(f"Loaded {len(blocks)} blocks")

# Let's inspect block 15: 01. Gán biến bê tông theo BOQ
for b in blocks:
    t = b['text']
    if 'BOQ' in t or '01.Gán' in t or 'Khối lượng' in t or 'TH1:' in t or 'Atool' in t:
        print(f"\n--- Block {b['index']} (y={b['bbox'][1]}): ---")
        print(t)

