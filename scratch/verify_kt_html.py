import os

html_path = 'BSV_BimKienTruc.html'
print(f"File size: {os.path.getsize(html_path)} bytes")

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

for t in ['script', 'style', 'div', 'section', 'a']:
    o = text.count(f'<{t}')
    c = text.count(f'</{t}>')
    print(f"Tag <{t}>: open={o}, close={c}")

# Check image files
img_dir = 'assets/bsv_kt'
imgs = os.listdir(img_dir)
print(f"Total images in {img_dir}: {len(imgs)}")

