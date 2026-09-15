import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find de-muc-bo-mon section
start = text.find('id="de-muc-bo-mon"')
if start != -1:
    print('Found de-muc-bo-mon at index', start)
    # print the next 2000 characters
    print(text[start-100:start+1500])
else:
    print('de-muc-bo-mon NOT found')

# Check script tags and functions
print('\n--- JS Functions ---')
import re
functions = re.findall(r'function\s+([a-zA-Z0-9_]+)', text)
print('Functions:', functions)

# Check all occurrences of switchDiscipline
print('\n--- switchDiscipline occurrences ---')
for line_no, line in enumerate(text.splitlines(), 1):
    if 'switchDiscipline' in line or 'disc-' in line:
        print(f"L{line_no}: {line.strip()[:100]}")
