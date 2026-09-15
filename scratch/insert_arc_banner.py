import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = 'id="disc-arc">\n        <div class="wbs-card-grid">'
if target not in html:
    target = 'id="disc-arc">\r\n        <div class="wbs-card-grid">'

banner = """id="disc-arc">
        <!-- SOP Direct Link Banner for Architecture -->
        <div style="background: linear-gradient(135deg, rgba(14, 165, 233, 0.14), rgba(99, 102, 241, 0.08)); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 16px; padding: 1.5rem 1.8rem; margin-bottom: 2rem; box-shadow: 0 6px 20px rgba(0,0,0,0.3);">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; margin-bottom: 1rem;">
            <div>
              <span style="font-size: 0.75rem; font-weight: 800; color: var(--primary); background: var(--primary-glow); padding: 3px 10px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;">SOP TIÊU CHUẨN REVIT ARCHITECTURE</span>
              <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--text-primary); margin-top: 4px;">
                <i class="fa-solid fa-building-columns" style="color: var(--primary);"></i> Sổ Tay Quy Trình Dựng Hình & Hoàn Thiện: BSV_KIẾN TRÚC (ARC)
              </h4>
              <p style="font-size: 0.875rem; color: var(--text-secondary); margin-top: 4px;">
                Chuẩn hóa 4 bước tiếp cận bản vẽ, tách CAD lệnh BURST, 9 lớp vật liệu tường, tự động hóa ATool, quy trình 7 bước hoàn thiện kết cấu (HTKC) và gán mã code liên kết BOQ.
              </p>
            </div>
            <a href="BSV_BimKienTruc.html" target="_blank" class="btn btn-primary" style="font-weight: 700; white-space: nowrap; padding: 10px 20px; font-size: 0.95rem; box-shadow: 0 0 20px var(--primary-glow);">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> Mở Sổ Tay Kiến Trúc (HTML) &rarr;
            </a>
          </div>

          <!-- Shortcuts -->
          <div style="display: flex; gap: 10px; flex-wrap: wrap; border-top: 1px solid var(--border-color); padding-top: 1rem;">
            <a href="BSV_BimKienTruc.html#step-1" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-folder-tree" style="color: var(--primary);"></i> Step 1: Bản vẽ & Finishing
            </a>
            <a href="BSV_BimKienTruc.html#step-2" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-file-cad" style="color: var(--danger);"></i> Step 2: Lệnh BURST & Cửa
            </a>
            <a href="BSV_BimKienTruc.html#step-3" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-cubes" style="color: var(--accent);"></i> Step 3: Dựng Tường & ATool
            </a>
            <a href="BSV_BimKienTruc.html#step-4" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-barcode" style="color: var(--success);"></i> Step 4: 6 Mã Code HTKC & BOQ
            </a>
            <a href="BSV_BimKienTruc.html#schedules-kt" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-table-cells" style="color: #c084fc;"></i> Thư viện Schedules
            </a>
          </div>
        </div>

        <div class="wbs-card-grid">"""

if target in html and 'BSV_BimKienTruc.html' not in html[html.find('id="disc-arc"'):html.find('id="disc-str"')]:
    html = html.replace(target, banner)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Inserted Architecture banner into #disc-arc successfully!")
else:
    print("Target not found or already inserted.")

