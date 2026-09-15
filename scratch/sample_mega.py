import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('MEGA-BP3_2026.04.21.ifc.sharedparameters.txt', 'r', encoding='utf-16') as f:
    lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]

for line in lines[:30]:
    print(line)

