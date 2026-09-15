import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<div class="disc-pane" id="disc-str">\n        <div class="wbs-card-grid">'

banner = """<div class="disc-pane" id="disc-str">
        <!-- SOP Direct Link Banner -->
        <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.12), rgba(37, 99, 235, 0.06)); border: 1px solid var(--border-highlight); border-radius: 14px; padding: 1.25rem 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
          <div>
            <h4 style="font-size: 1.05rem; font-weight: 800; color: var(--text-primary); margin-bottom: 4px;">
              <i class="fa-solid fa-book-bookmark" style="color: var(--primary);"></i> Sổ Tay Kỹ Thuật Chi Tiết: BSV_KẾT CẤU (VER 2)
            </h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">
              Chuẩn hóa quy ước tính khối lượng với QS, chuỗi ưu tiên Join Atool, quy trình 7 bước gán biến BOQ, chi tiết 14 cấu kiện & bảng thống kê Revit Schedules.
            </p>
          </div>
          <a href="BSV_BimKetCauVer2.html" target="_blank" class="btn btn-primary" style="font-weight: 700; white-space: nowrap; padding: 8px 16px;">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> Mở Sổ Tay BSV_KẾT CẤU (HTML) &rarr;
          </a>
        </div>

        <div class="wbs-card-grid">"""

if 'BSV_BimKetCauVer2.html' not in html and target in html:
    html = html.replace(target, banner)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added SOP banner to index.html successfully!")
else:
    print("Already added or target not found.")

