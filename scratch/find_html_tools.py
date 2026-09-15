import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('BSV_BimKetCauVer2.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    if any(k in line.lower() for k in ['atool', 'bimspeed']):
        print(f"L{i:04d}: {line.strip()[:100]}")

