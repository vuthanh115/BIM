import pymupdf
import sys
import os
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'c:\Users\thanhvp\Downloads\BIM\SHOP DRAWING REBAR.pdf'
doc = pymupdf.open(pdf_path)
print(f"Total pages: {len(doc)}")
page = doc[0]
print(f"Page rect: {page.rect}")
text = page.get_text()
print(f"Total text chars: {len(text)}")

img_dir = r'c:\Users\thanhvp\Downloads\BIM\assets\bsv_shop'
os.makedirs(img_dir, exist_ok=True)

# Extract images
images = page.get_images()
print(f"Total images: {len(images)}")
for i, img_info in enumerate(images):
    xref = img_info[0]
    base_image = doc.extract_image(xref)
    image_bytes = base_image["image"]
    image_ext = base_image["ext"]
    img_path = os.path.join(img_dir, f"shop_img_{i+1}.{image_ext}")
    with open(img_path, "wb") as f:
        f.write(image_bytes)
    print(f"Saved {img_path} ({base_image.get('width')}x{base_image.get('height')})")

# Render high-res full canvas
pix = page.get_pixmap(dpi=150)
full_img = os.path.join(img_dir, "bsv_shop_rebar_full.png")
pix.save(full_img)
print(f"Saved full canvas render: {full_img} ({pix.width}x{pix.height})")

# Dump text blocks
blocks = page.get_text("blocks")
blocks.sort(key=lambda b: (round(b[1] / 30) * 30, b[0]))

data = []
for i, b in enumerate(blocks):
    t = b[4].strip()
    if t:
        data.append({
            'index': i,
            'bbox': [round(v, 1) for v in b[:4]],
            'text': t,
            'lines': [l.strip() for l in t.splitlines() if l.strip()]
        })

with open('scratch/bsv_shop_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(data)} blocks to scratch/bsv_shop_blocks.json")

