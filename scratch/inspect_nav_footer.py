import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('=== NAVBAR ACTIONS ===')
m = re.search(r'<div class="nav-actions">(.*?)</div>', text, re.DOTALL)
if m:
    print(m.group(1).strip())

print('\n=== CHECKLIST STAGE 2 ===')
pos2 = text.find('id="stage-2"')
if pos2 != -1:
    print(text[pos2:pos2+1200])

print('\n=== FOOTER ===')
posf = text.find('<footer')
if posf != -1:
    print(text[posf:posf+1200])

