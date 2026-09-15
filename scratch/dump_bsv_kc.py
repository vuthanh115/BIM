import pymupdf
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = 'BSV_BimKetCauVer2.pdf'
doc = pymupdf.open(pdf_path)
page = doc[0]

text = page.get_text()
print("=== FULL TEXT OF BSV_BimKetCauVer2.pdf ===")
print(text)

# Also extract images to assets/bsv_kc/
img_dir = 'assets/bsv_kc'
os.makedirs(img_dir, exist_ok=True)

images = page.get_images()
print(f"\nTotal images on page: {len(images)}")
for i, img_info in enumerate(images):
    xref = img_info[0]
    base_image = doc.extract_image(xref)
    image_bytes = base_image["image"]
    image_ext = base_image["ext"]
    img_path = os.path.join(img_dir, f"img_{i+1}.{image_ext}")
    with open(img_path, "wb") as f:
        f.write(image_bytes)
    print(f"Saved image {i+1}: {img_path} ({len(image_bytes)} bytes, {base_image.get('width')}x{base_image.get('height')})")

# Render high-resolution page image as reference
pix = page.get_pixmap(dpi=200)
page_img_path = os.path.join(img_dir, "bsv_ketcau_full.png")
pix.save(page_img_path)
print(f"Saved full page render: {page_img_path} ({pix.width}x{pix.height})")

