import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('00.DESIGN & BIM CAPABILITY GLC.pdf')

target_pages = [3, 6, 7, 16, 17]

for pno in target_pages:
    print(f"\n{'='*30} PAGE {pno} {'='*30}")
    text = doc[pno - 1].get_text()
    print(text)

