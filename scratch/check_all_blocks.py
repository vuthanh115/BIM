import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/bsv_kc_blocks.json', 'r', encoding='utf-8') as f:
    blocks = json.load(f)

for b in blocks[16:]:
    lines = [l.strip() for l in b['lines'] if l.strip()]
    if lines:
        print(f"[{b['index']}] {lines[0]} (lines: {len(lines)}) -> {' // '.join(lines[1:3])}")

