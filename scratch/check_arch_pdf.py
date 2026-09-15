import pymupdf
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

candidates = [
    r'c:\Users\thanhvp\Downloads\BSV_Arch_Working process-1.pdf',
    r'c:\Users\thanhvp\Downloads\BSV_Arch_Working process-2.pdf',
    r'c:\Users\thanhvp\Downloads\Out\01.QuyTrinhLamViec\01.QuyTrinhLamViec_KienTruc\BSV_Arch_Working process.pdf',
    r'c:\Users\thanhvp\Downloads\Out\01.QuyTrinhLamViec\01.QuyTrinhLamViec_KienTruc\BSV_Arch_Working process2.pdf'
]

for c in candidates:
    if os.path.exists(c):
        doc = pymupdf.open(c)
        print(f"File: {c} | Pages: {len(doc)} | Size: {os.path.getsize(c)} bytes")
        for pno in range(len(doc)):
            p = doc[pno]
            print(f"  Page {pno+1}: {len(p.get_text())} chars, {len(p.get_images())} images")

