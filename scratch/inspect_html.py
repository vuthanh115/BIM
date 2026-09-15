import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length:', len(text))
sections = re.findall(r'<section[^>]*id=[\'"]([^\'"]+)[\'"]', text)
print('Section IDs:', sections)
nav_links = re.findall(r'<a\s+href=[\'"]#([^\'"]+)[\'"]', text)
print('Nav links:', nav_links)

headers = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', text)
for h in headers[:15]:
    print('Header:', re.sub(r'<[^>]+>', '', h).strip())
