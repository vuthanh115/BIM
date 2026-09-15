import os

files = ['index.html', 'BSV_BimKetCauVer2.html', 'BSV_BimKienTruc.html', 'BSV_ShopDrawingRebar.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    print(f"\n=== {f} ({len(text)} chars) ===")
    for t in ['script', 'style', 'div', 'section', 'a']:
        o = text.count(f'<{t}')
        c = text.count(f'</{t}>')
        print(f"  Tag <{t}>: open={o}, close={c}")
    
    # Check links
    for target in files:
        if target != f:
            print(f"  Has link to {target}? {target in text}")

