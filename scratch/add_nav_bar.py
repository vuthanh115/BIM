import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('BSV_BimKetCauVer2.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<!-- SECTION A: THỨ TỰ ƯU TIÊN TÍNH TOÁN -->'

quick_jump_bar = """    <!-- Quick Tool Adjustment Navigator (Điểm Đánh Dấu Can Thiệp Công Cụ) -->
    <div class="quick-jump-bar">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 1.25rem; color: var(--accent);"><i class="fa-solid fa-highlighter"></i></span>
        <div>
          <span style="font-weight: 800; font-size: 0.9rem; color: var(--text-primary); display: block;">VỊ TRÍ ĐÁNH DẤU CHỈNH SỬA CÔNG CỤ (ATOOL & BIMSPEED):</span>
          <span style="font-size: 0.775rem; color: var(--text-muted);">Bấm vào từng nút bên dưới để nhảy trực tiếp đến vị trí cấu hình/thay thế add-in sau này:</span>
        </div>
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <a href="#edit-atool-1" class="jump-btn jump-btn-atool"><i class="fa-solid fa-arrow-down"></i> [1] ATool: Quy ước Join (Mục A)</a>
        <a href="#edit-bimspeed-1" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> [2] BimSpeed: Pick ván khuôn (Mục B)</a>
        <a href="#edit-atool-2" class="jump-btn jump-btn-atool"><i class="fa-solid fa-arrow-down"></i> [3] ATool: Bước 02 Join BOQ</a>
        <a href="#edit-bimspeed-2" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> [4] BimSpeed: Bước 03 Ván khuôn BOQ</a>
      </div>
    </div>
"""

if target in html and 'quick-jump-bar' not in html:
    html = html.replace(target, quick_jump_bar + '\n    ' + target)
    with open('BSV_BimKetCauVer2.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully added Quick Tool Adjustment Navigator bar!")
else:
    print("Already added or target not found.")

