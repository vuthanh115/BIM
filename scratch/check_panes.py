import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

buttons = re.findall(r'<button[^>]*class=[\'"]disc-btn[^\'"]*[\'"][^>]*>.*?</button>', html, re.DOTALL)
print(f"Total disc-btn: {len(buttons)}")
for b in buttons:
    onclick = re.search(r'onclick=[\'"]([^\'"]+)[\'"]', b)
    text = re.sub(r'<[^>]+>', ' ', b).strip()
    print(f" - {text} -> {onclick.group(1) if onclick else 'none'}")

panes = re.findall(r'<div[^>]*class=[\'"]disc-pane[^\'"]*[\'"][^>]*id=[\'"]([^\'"]+)[\'"]', html)
print(f"\nTotal disc-panes: {len(panes)}")
for p in panes:
    print(f" - Pane id: {p}")

