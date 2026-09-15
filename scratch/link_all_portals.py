import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add to Navbar Actions
old_nav_actions = """      <a href="BSV_BimKetCauVer2.html" target="_blank" class="btn btn-outline" style="border-color: rgba(56, 189, 248, 0.4); color: var(--primary); font-weight: 700;" title="Mở Sổ tay Quy trình Dựng hình & Bóc tách Khối lượng BIM Kết Cấu">
        <i class="fa-solid fa-book-bookmark"></i> Sổ Tay BIM KC
      </a>"""

new_nav_actions = """      <a href="BSV_BimKienTruc.html" target="_blank" class="btn btn-outline" style="border-color: rgba(14, 165, 233, 0.5); color: var(--primary); font-weight: 700;" title="Mở Sổ tay Quy trình BIM Kiến Trúc (ARC)">
        <i class="fa-solid fa-building-columns"></i> Sổ Tay BIM KT
      </a>
      <a href="BSV_BimKetCauVer2.html" target="_blank" class="btn btn-outline" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24; font-weight: 700;" title="Mở Sổ tay Quy trình Dựng hình & Bóc tách Khối lượng BIM Kết Cấu">
        <i class="fa-solid fa-cube"></i> Sổ Tay BIM KC
      </a>"""

if old_nav_actions in html:
    html = html.replace(old_nav_actions, new_nav_actions)
    print("[1] Updated Navbar actions in index.html with BIM KT button")

# Add Hero pill
old_hero_pill = """<a href="BSV_BimKetCauVer2.html" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35); color: var(--primary); padding: 8px 18px; border-radius: 30px; font-size: 0.875rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease; box-shadow: 0 0 15px var(--primary-glow);">
            <i class="fa-solid fa-book-bookmark"></i> Sổ Tay Chuẩn Hóa: BSV_KẾT CẤU (VER 2) &rarr;
          </a>"""

new_hero_pill = """<a href="BSV_BimKienTruc.html" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(14, 165, 233, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: var(--primary); padding: 8px 18px; border-radius: 30px; font-size: 0.875rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease; box-shadow: 0 0 15px var(--primary-glow);">
            <i class="fa-solid fa-building-columns"></i> Sổ Tay: BSV_KIẾN TRÚC &rarr;
          </a>
          <a href="BSV_BimKetCauVer2.html" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); color: #fbbf24; padding: 8px 18px; border-radius: 30px; font-size: 0.875rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease;">
            <i class="fa-solid fa-cube"></i> Sổ Tay: BSV_KẾT CẤU &rarr;
          </a>"""

if old_hero_pill in html:
    html = html.replace(old_hero_pill, new_hero_pill)
    print("[2] Updated Hero pills in index.html with BIM KT")

# Add Architecture Banner in #disc-arc
arc_pane_target = """      <!-- PANE 1: ARC (KIẾN TRÚC) -->
      <div class="disc-pane active" id="disc-arc">
        <div class="wbs-card-grid">"""

arc_pane_banner = """      <!-- PANE 1: ARC (KIẾN TRÚC) -->
      <div class="disc-pane active" id="disc-arc">
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

if arc_pane_target in html and 'BSV_BimKienTruc.html' not in html:
    html = html.replace(arc_pane_target, arc_pane_banner)
    print("[3] Added Architecture SOP banner in #disc-arc")

# Add in Footer
old_footer_links = """        <ul>
          <li><a href="#thiet-ke">• Architecture & Structure Modeling</a></li>
          <li><a href="BSV_BimKetCauVer2.html" target="_blank" style="color: var(--primary); font-weight: 700;">• Sổ Tay BSV_KẾT CẤU (VER 2) <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7rem;"></i></a></li>"""

new_footer_links = """        <ul>
          <li><a href="#thiet-ke">• Architecture & Structure Modeling</a></li>
          <li><a href="BSV_BimKienTruc.html" target="_blank" style="color: var(--primary); font-weight: 700;">• Sổ Tay BSV_KIẾN TRÚC (ARC) <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7rem;"></i></a></li>
          <li><a href="BSV_BimKetCauVer2.html" target="_blank" style="color: #fbbf24; font-weight: 700;">• Sổ Tay BSV_KẾT CẤU (VER 2) <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7rem;"></i></a></li>"""

if old_footer_links in html:
    html = html.replace(old_footer_links, new_footer_links)
    print("[4] Added BIM KT link to Footer in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")

# 2. Update BSV_BimKetCauVer2.html to link with BSV_BimKienTruc.html
with open('BSV_BimKetCauVer2.html', 'r', encoding='utf-8') as f:
    kc_html = f.read()

old_kc_nav_btn = """      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>"""
new_kc_nav_btn = """      <a href="BSV_BimKienTruc.html" class="btn btn-outline" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8;" title="Mở Sổ tay Kiến trúc"><i class="fa-solid fa-building-columns"></i> Sang Sổ Tay KT</a>
      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>"""

if old_kc_nav_btn in kc_html and 'BSV_BimKienTruc.html' not in kc_html:
    kc_html = kc_html.replace(old_kc_nav_btn, new_kc_nav_btn)
    with open('BSV_BimKetCauVer2.html', 'w', encoding='utf-8') as f:
        f.write(kc_html)
    print("[5] Linked BSV_BimKienTruc.html in BSV_BimKetCauVer2.html navbar!")

