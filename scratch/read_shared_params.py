import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('BSV_KC_ShareParameter.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for line in lines[:50]:
    print(line.rstrip())

