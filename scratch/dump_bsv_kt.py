import pymupdf
import sys
import os
import shutil
import json

sys.stdout.reconfigure(encoding='utf-8')

src_pdf = r'c:\Users\thanhvp\Downloads\BSV_Arch_Working process-1.pdf'
dst_pdf = r'c:\Users\thanhvp\Downloads\BIM\BSV_Arch_Working_process.pdf'
shutil.copyfile(src_pdf, dst_pdf)
print(f"Copied {src_pdf} to {dst_pdf}")

doc = pymupdf.open(dst_pdf)
page = doc[0]

img_dir = r'c:\Users\thanhvp\Downloads\BIM\assets\bsv_kt'
os.makedirs(img_dir, exist_ok=True)

# 1. Extract all images
images = page.get_images()
print(f"Total images on page: {len(images)}")
for i, img_info in enumerate(images):
    xref = img_info[0]
    base_image = doc.extract_image(xref)
    image_bytes = base_image["image"]
    image_ext = base_image["ext"]
    img_path = os.path.join(img_dir, f"kt_img_{i+1}.{image_ext}")
    with open(img_path, "wb") as f:
        f.write(image_bytes)
    print(f"Saved {img_path} ({base_image.get('width')}x{base_image.get('height')})")

# 2. Render high-res full page
pix = page.get_pixmap(dpi=150)
full_img = os.path.join(img_dir, "bsv_kientruc_full.png")
pix.save(full_img)
print(f"Saved full render: {full_img} ({pix.width}x{pix.height})")

# 3. Dump text blocks
blocks = page.get_text("blocks")
# Sort top-to-bottom, left-to-right
blocks.sort(key=lambda b: (round(b[1] / 30) * 30, b[0]))

data = []
for i, b in enumerate(blocks):
    text = b[4].strip()
    if text:
        data.append({
            'index': i,
            'bbox': [round(v, 1) for v in b[:4]],
            'text': text,
            'lines': [l.strip() for l in text.splitlines() if l.strip()]
        })

with open('scratch/bsv_kt_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(data)} text blocks to scratch/bsv_kt_blocks.json")

