import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('BSV_BimKetCauVer2.pdf')
page = doc[0]

img_list = page.get_images()
print("Images count:", len(img_list))

for i, img in enumerate(img_list):
    xref = img[0]
    rects = page.get_image_rects(xref)
    for r in rects:
        print(f"Image {i+1} (xref {xref}) at bbox: ({r.x0:.1f}, {r.y0:.1f}, {r.x1:.1f}, {r.y1:.1f}) | size: {r.width:.1f} x {r.height:.1f}")

# Also inspect blocks from y = 5000 to end
blocks = page.get_text("blocks")
bottom_blocks = [b for b in blocks if b[1] >= 5200]
bottom_blocks.sort(key=lambda b: (round(b[1] / 50) * 50, b[0]))
print(f"\n--- Bottom blocks (>= 5200) count: {len(bottom_blocks)} ---")
for b in bottom_blocks:
    lines = [l.strip() for l in b[4].splitlines() if l.strip()]
    print(f"B ({b[0]:.1f}, {b[1]:.1f}): {' | '.join(lines[:4])}")

