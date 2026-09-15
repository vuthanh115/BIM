import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navbar Actions
nav_actions_old = """    <div class="nav-actions">
      <!-- Dark/Light Mode Switcher -->
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" title="Chuyển chế độ Sáng / Tối">
        <i class="fa-solid fa-sun" id="themeIcon"></i>
      </button>

      <button class="btn btn-outline" onclick="window.print()"><i class="fa-solid fa-print"></i> In SOP</button>
      <a href="#quy-trinh" class="btn btn-primary"><i class="fa-solid fa-bolt"></i> Thực thi Quy trình</a>
    </div>"""

nav_actions_new = """    <div class="nav-actions">
      <!-- Direct SOP Structural Handbook Link -->
      <a href="BSV_BimKetCauVer2.html" target="_blank" class="btn btn-outline" style="border-color: rgba(56, 189, 248, 0.4); color: var(--primary); font-weight: 700;" title="Mở Sổ tay Quy trình Dựng hình & Bóc tách Khối lượng BIM Kết Cấu">
        <i class="fa-solid fa-book-bookmark"></i> Sổ Tay BIM KC
      </a>

      <!-- Dark/Light Mode Switcher -->
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" title="Chuyển chế độ Sáng / Tối">
        <i class="fa-solid fa-sun" id="themeIcon"></i>
      </button>

      <button class="btn btn-outline" onclick="window.print()"><i class="fa-solid fa-print"></i> In SOP</button>
      <a href="#quy-trinh" class="btn btn-primary"><i class="fa-solid fa-bolt"></i> Thực thi Quy trình</a>
    </div>"""

if nav_actions_old in html:
    html = html.replace(nav_actions_old, nav_actions_new)
    print("[1] Updated Navbar Actions with Sổ Tay BIM KC button")

# 2. Add Quick Pill in Hero Section
hero_target = """        <div class="hero-stats">"""
hero_pill = """        <div style="margin-bottom: 1.5rem; display: flex; gap: 12px; flex-wrap: wrap;">
          <a href="BSV_BimKetCauVer2.html" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35); color: var(--primary); padding: 8px 18px; border-radius: 30px; font-size: 0.875rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease; box-shadow: 0 0 15px var(--primary-glow);">
            <i class="fa-solid fa-book-bookmark"></i> Sổ Tay Chuẩn Hóa: BSV_KẾT CẤU (VER 2) &rarr;
          </a>
          <span style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.8rem; color: var(--text-muted);">
            <i class="fa-solid fa-circle-check" style="color: var(--success);"></i> Đã tích hợp Atool, BimSpeed & 14 Cấu kiện
          </span>
        </div>

        <div class="hero-stats">"""

if hero_target in html and 'Sổ Tay Chuẩn Hóa: BSV_KẾT CẤU (VER 2)' not in html:
    html = html.replace(hero_target, hero_pill)
    print("[2] Added Quick Pill in Hero Section")

# 3. Add Link in Checklist Stage 2 Task 3 (BIM 5D Cost)
cost_task_old = """                <h4>Bóc tách khối lượng tự động & Đánh giá chi phí (BIM 5D)</h4>
                <p>Liên kết khối lượng bóc tách từ mô hình với đơn giá để lập dự toán và so sánh biến động chi phí khi có thay đổi phương án.</p>
                <span class="check-tag">BIM 5D Cost</span>
              </div>"""

cost_task_new = """                <h4>Bóc tách khối lượng tự động & Đánh giá chi phí (BIM 5D)</h4>
                <p>Liên kết khối lượng bóc tách từ mô hình với đơn giá để lập dự toán và so sánh biến động chi phí khi có thay đổi phương án.</p>
                <span class="check-tag">BIM 5D Cost</span>
                <div style="margin-top: 10px;">
                  <a href="BSV_BimKetCauVer2.html" target="_blank" onclick="event.stopPropagation();" style="color: var(--primary); font-size: 0.82rem; font-weight: 700; text-decoration: underline; display: inline-flex; align-items: center; gap: 5px;">
                    <i class="fa-solid fa-file-invoice-dollar"></i> Xem Quy trình 7 bước gán biến BOQ & Khấu trừ QS (BSV_KẾT CẤU) &rarr;
                  </a>
                </div>
              </div>"""

if cost_task_old in html:
    html = html.replace(cost_task_old, cost_task_new)
    print("[3] Added link inside Stage 2 BIM 5D Task")

# 4. Enhance the banner in #disc-str with quick anchors to sections in BSV_BimKetCauVer2.html
disc_str_old_banner = """<div class="disc-pane" id="disc-str">
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
        </div>"""

disc_str_new_banner = """<div class="disc-pane" id="disc-str">
        <!-- SOP Direct Link Banner with Section Shortcuts -->
        <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.14), rgba(37, 99, 235, 0.08)); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 16px; padding: 1.5rem 1.8rem; margin-bottom: 2rem; box-shadow: 0 6px 20px rgba(0,0,0,0.3);">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; margin-bottom: 1rem;">
            <div>
              <span style="font-size: 0.75rem; font-weight: 800; color: var(--primary); background: var(--primary-glow); padding: 3px 10px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;">SOP TIÊU CHUẨN REVIT STRUCTURE</span>
              <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--text-primary); margin-top: 4px;">
                <i class="fa-solid fa-book-bookmark" style="color: var(--primary);"></i> Sổ Tay Quy Trình Dựng Hình & Bóc Tách: BSV_KẾT CẤU (VER 2)
              </h4>
              <p style="font-size: 0.875rem; color: var(--text-secondary); margin-top: 4px;">
                Chuẩn hóa quy ước tính khối lượng với QS, thứ tự ưu tiên Join cấu kiện (Atool), quy trình 7 bước gán biến BOQ, chi tiết 14 cấu kiện & 7 bảng biểu mẫu Revit Schedules.
              </p>
            </div>
            <a href="BSV_BimKetCauVer2.html" target="_blank" class="btn btn-primary" style="font-weight: 700; white-space: nowrap; padding: 10px 20px; font-size: 0.95rem; box-shadow: 0 0 20px var(--primary-glow);">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> Mở Toàn Bộ Sổ Tay (HTML) &rarr;
            </a>
          </div>

          <!-- Quick Navigation Pills to BSV_BimKetCauVer2.html sections -->
          <div style="display: flex; gap: 10px; flex-wrap: wrap; border-top: 1px solid var(--border-color); padding-top: 1rem;">
            <a href="BSV_BimKetCauVer2.html#thu-tu-tinh" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-arrows-split-up-and-left" style="color: var(--primary);"></i> 1. Thứ tự Join QS (Atool)
            </a>
            <a href="BSV_BimKetCauVer2.html#quy-trinh-7-buoc" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-list-check" style="color: var(--accent);"></i> 2. Quy trình 7 bước gán biến BOQ
            </a>
            <a href="BSV_BimKetCauVer2.html#14-cau-kien" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-sitemap" style="color: var(--success);"></i> 3. 14 Hạng mục Cấu kiện
            </a>
            <a href="BSV_BimKetCauVer2.html#bang-thong-ke" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-table-cells" style="color: var(--primary);"></i> 4. 7 Bảng Revit Schedules
            </a>
            <a href="BSV_BimKetCauVer2.html#mindmap-view" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
              <i class="fa-solid fa-diagram-project" style="color: var(--accent);"></i> 5. Sơ đồ Mindmap gốc
            </a>
          </div>
        </div>"""

if disc_str_old_banner in html:
    html = html.replace(disc_str_old_banner, disc_str_new_banner)
    print("[4] Enhanced banner in #disc-str with direct section shortcuts")

# 5. Add Link in Footer
footer_col_old = """      <div class="footer-col">
        <h4>Năng Lực Cốt Lõi</h4>
        <ul>
          <li><a href="#thiet-ke">• Architecture & Structure Modeling</a></li>
          <li><a href="#thiet-ke">• MEP Systems & Clash Detection</a></li>
          <li><a href="#thiet-ke">• 4D Scheduling & 5D Quantity Takeoff</a></li>
          <li><a href="#thi-cong">• Site Management & Inspection QA/QC</a></li>
          <li><a href="#van-hanh">• Digital Handover & Asset Management</a></li>
        </ul>
      </div>"""

footer_col_new = """      <div class="footer-col">
        <h4>Năng Lực Cốt Lõi</h4>
        <ul>
          <li><a href="#thiet-ke">• Architecture & Structure Modeling</a></li>
          <li><a href="BSV_BimKetCauVer2.html" target="_blank" style="color: var(--primary); font-weight: 700;">• Sổ Tay BSV_KẾT CẤU (VER 2) <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7rem;"></i></a></li>
          <li><a href="#thiet-ke">• MEP Systems & Clash Detection</a></li>
          <li><a href="#thiet-ke">• 4D Scheduling & 5D Quantity Takeoff</a></li>
          <li><a href="#thi-cong">• Site Management & Inspection QA/QC</a></li>
          <li><a href="#van-hanh">• Digital Handover & Asset Management</a></li>
        </ul>
      </div>"""

if footer_col_old in html:
    html = html.replace(footer_col_old, footer_col_new)
    print("[5] Added direct link to BSV_BimKetCauVer2.html in Footer")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished updating index.html!")
