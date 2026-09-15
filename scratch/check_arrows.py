import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

broken = re.findall(r'(\$\s*[\t\r\n]*rightarrow\$)', text)
print("Broken arrow occurrences:", len(broken))
for b in broken:
    print("Found:", repr(b))

