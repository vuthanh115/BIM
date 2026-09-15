import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check disc-str header
pos = html.find('id="disc-str"')
if pos != -1:
    print("Found disc-str at", pos)
    print(html[pos:pos+500])

