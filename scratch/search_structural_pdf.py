import fitz  # PyMuPDF
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('00.DESIGN & BIM CAPABILITY GLC.pdf')
print(f"Total pages: {len(doc)}")

keywords = ['kết cấu', 'structure', 'str', 'thép', 'rebar', 'tekla', 'bê tông']

for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()
    found = []
    for kw in keywords:
        matches = re.findall(rf'\b{kw}\b', text, re.IGNORECASE)
        if matches:
            found.append(f"{kw} ({len(matches)})")
    if found:
        print(f"\n--- Page {page_idx + 1} matches: {', '.join(found)} ---")
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for line in lines:
            if any(re.search(rf'\b{kw}\b', line, re.IGNORECASE) for kw in keywords):
                print(f"  * {line}")

