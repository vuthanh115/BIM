import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for i, line in enumerate(text.splitlines(), 1):
    if any(k in line.lower() for k in ['atool', 'bimspeed']):
        print(f"index.html L{i}: {line.strip()[:100]}")

