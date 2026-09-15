import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Shop Rebar to Navbar Actions
old_nav_actions = """      <a href="BSV_BimKienTruc.html" target="_blank" class="btn btn-outline" style="border-color: rgba(14, 165, 233, 0.5); color: var(--primary); font-weight: 700;" title="Mở Sổ tay Quy trình BIM Kiến Trúc (ARC)">
        <i class="fa-solid fa-building-columns"></i> Sổ Tay BIM KT
      </a>
      <a href="BSV_BimKetCauVer2.html" target="_blank" class="btn btn-outline" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24; font-weight: 700;" title="Mở Sổ tay Quy trình Dựng hình & Bóc tách Khối lượng BIM Kết Cấu">
        <i class="fa-solid fa-cube"></i> Sổ Tay BIM KC
      </a>"""

new_nav_actions = """      <a href="BSV_BimKienTruc.html" target="_blank" class="btn btn-outline" style="border-color: rgba(14, 165, 233, 0.5); color: var(--primary); font-weight: 700;" title="Mở Sổ tay Quy trình BIM Kiến Trúc (ARC)">
        <i class="fa-solid fa-building-columns"></i> Sổ Tay KT
      </a>
      <a href="BSV_BimKetCauVer2.html" target="_blank" class="btn btn-outline" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24; font-weight: 700;" title="Mở Sổ tay Quy trình Dựng hình & Bóc tách Khối lượng BIM Kết Cấu">
        <i class="fa-solid fa-cube"></i> Sổ Tay KC
      </a>
      <a href="BSV_ShopDrawingRebar.html" target="_blank" class="btn btn-outline" style="border-color: rgba(239, 68, 68, 0.4); color: #f87171; font-weight: 700;" title="Mở Sổ tay Triển khai Shop Drawing Cốt Thép">
        <i class="fa-solid fa-sheet-plastic"></i> Sổ Tay Shop Rebar
      </a>"""

if old_nav_actions in html:
    html = html.replace(old_nav_actions, new_nav_actions)
    print("[1] Updated Navbar in index.html with Shop Rebar button")

# Add Hero pill
old_hero_pills = """          <a href="BSV_BimKetCauVer2.html" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); color: #fbbf24; padding: 8px 18px; border-radius: 30px; font-size: 0.875rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease;">
            <i class="fa-solid fa-cube"></i> Sổ Tay: BSV_KẾT CẤU &rarr;
          </a>"""

new_hero_pills = """          <a href="BSV_BimKetCauVer2.html" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); color: #fbbf24; padding: 8px 18px; border-radius: 30px; font-size: 0.875rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease;">
            <i class="fa-solid fa-cube"></i> Sổ Tay: BSV_KẾT CẤU &rarr;
          </a>
          <a href="BSV_ShopDrawingRebar.html" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.35); color: #f87171; padding: 8px 18px; border-radius: 30px; font-size: 0.875rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease;">
            <i class="fa-solid fa-sheet-plastic"></i> Sổ Tay: SHOP REBAR &rarr;
          </a>"""

if old_hero_pills in html:
    html = html.replace(old_hero_pills, new_hero_pills)
    print("[2] Added Shop Rebar pill in Hero Section")

# Add Shop Rebar Banner in Section #thi-cong
thi_cong_header = '<section id="thi-cong"'
pos_tc = html.find(thi_cong_header)
if pos_tc != -1:
    pos_tc_desc = html.find('</p>\n      </div>', pos_tc)
    if pos_tc_desc != -1 and 'BSV_ShopDrawingRebar.html' not in html[pos_tc:pos_tc+1500]:
        insert_target = html[pos_tc_desc:pos_tc_desc+17]
        shop_banner = """</p>
      </div>

      <!-- Shop Drawing Rebar SOP Banner in Thi Cong Section -->
      <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(245, 158, 11, 0.08)); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 16px; padding: 1.5rem 1.8rem; margin-bottom: 2rem; box-shadow: 0 6px 20px rgba(0,0,0,0.3);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
          <div>
            <span style="font-size: 0.75rem; font-weight: 800; color: #f87171; background: rgba(239, 68, 68, 0.15); padding: 3px 10px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;">SOP THI CÔNG & CHẾ TẠO CỐT THÉP</span>
            <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--text-primary); margin-top: 4px;">
              <i class="fa-solid fa-sheet-plastic" style="color: #f87171;"></i> Sổ Tay Quy Trình Triển Khai: BSV_SHOP DRAWING REBAR
            </h4>
            <p style="font-size: 0.875rem; color: var(--text-secondary); margin-top: 4px;">
              Quy cách đặt tên Partition, nối so le dầm cột móng, kéo hình dạng uốn 2D Bending Detail, Multi-Rebar Annotation (MRA) và xuất bảng thống kê chế tạo thép thi công.
            </p>
          </div>
          <a href="BSV_ShopDrawingRebar.html" target="_blank" class="btn btn-primary" style="background: linear-gradient(135deg, #ef4444, #ea580c); font-weight: 700; white-space: nowrap; padding: 10px 20px; font-size: 0.95rem; box-shadow: 0 0 20px rgba(239, 68, 68, 0.3);">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> Mở Sổ Tay Shop Rebar (HTML) &rarr;
          </a>
        </div>
      </div>"""
        html = html[:pos_tc_desc] + shop_banner + html[pos_tc_desc+17:]
        print("[3] Added Shop Rebar SOP banner in #thi-cong section")

# Add Footer link
old_footer = """          <li><a href="BSV_BimKetCauVer2.html" target="_blank" style="color: #fbbf24; font-weight: 700;">• Sổ Tay BSV_KẾT CẤU (VER 2) <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7rem;"></i></a></li>"""
new_footer = """          <li><a href="BSV_BimKetCauVer2.html" target="_blank" style="color: #fbbf24; font-weight: 700;">• Sổ Tay BSV_KẾT CẤU (VER 2) <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7rem;"></i></a></li>
          <li><a href="BSV_ShopDrawingRebar.html" target="_blank" style="color: #f87171; font-weight: 700;">• Sổ Tay BSV_SHOP DRAWING REBAR <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.7rem;"></i></a></li>"""

if old_footer in html:
    html = html.replace(old_footer, new_footer)
    print("[4] Added Shop Rebar link in Footer")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")

# 2. Update BSV_BimKetCauVer2.html navbar
with open('BSV_BimKetCauVer2.html', 'r', encoding='utf-8') as f:
    kc_html = f.read()

old_kc_btns = """      <a href="BSV_BimKienTruc.html" class="btn btn-outline" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8;" title="Mở Sổ tay Kiến trúc"><i class="fa-solid fa-building-columns"></i> Sang Sổ Tay KT</a>
      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>"""

new_kc_btns = """      <a href="BSV_BimKienTruc.html" class="btn btn-outline" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8;" title="Mở Sổ tay Kiến trúc"><i class="fa-solid fa-building-columns"></i> Sổ Tay KT</a>
      <a href="BSV_ShopDrawingRebar.html" class="btn btn-outline" style="border-color: rgba(239, 68, 68, 0.4); color: #f87171;" title="Mở Sổ tay Shop Rebar"><i class="fa-solid fa-sheet-plastic"></i> Sổ Tay Shop</a>
      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>"""

if old_kc_btns in kc_html:
    kc_html = kc_html.replace(old_kc_btns, new_kc_btns)
    with open('BSV_BimKetCauVer2.html', 'w', encoding='utf-8') as f:
        f.write(kc_html)
    print("[5] Updated Navbar in BSV_BimKetCauVer2.html with Shop Rebar link")

# 3. Update BSV_BimKienTruc.html navbar
with open('BSV_BimKienTruc.html', 'r', encoding='utf-8') as f:
    kt_html = f.read()

old_kt_btns = """      <a href="BSV_BimKetCauVer2.html" class="btn btn-outline" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;" title="Mở Sổ tay Kết cấu"><i class="fa-solid fa-cube"></i> Sang Sổ Tay KC</a>
      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>"""

new_kt_btns = """      <a href="BSV_BimKetCauVer2.html" class="btn btn-outline" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;" title="Mở Sổ tay Kết cấu"><i class="fa-solid fa-cube"></i> Sổ Tay KC</a>
      <a href="BSV_ShopDrawingRebar.html" class="btn btn-outline" style="border-color: rgba(239, 68, 68, 0.4); color: #f87171;" title="Mở Sổ tay Shop Rebar"><i class="fa-solid fa-sheet-plastic"></i> Sổ Tay Shop</a>
      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>"""

if old_kt_btns in kt_html:
    kt_html = kt_html.replace(old_kt_btns, new_kt_btns)
    with open('BSV_BimKienTruc.html', 'w', encoding='utf-8') as f:
        f.write(kt_html)
    print("[6] Updated Navbar in BSV_BimKienTruc.html with Shop Rebar link")

