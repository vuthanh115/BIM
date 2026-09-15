import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('BSV_BimKetCauVer2.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("'quick-jump-bar' in html?", 'quick-jump-bar' in text)
print("'edit-atool-1' in html?", 'edit-atool-1' in text)
print("'edit-bimspeed-1' in html?", 'edit-bimspeed-1' in text)
print("'edit-atool-2' in html?", 'edit-atool-2' in text)
print("'edit-bimspeed-2' in html?", 'edit-bimspeed-2' in text)

# If quick-jump-bar is not in text, find where <section id="thu-tu-tinh" is
if 'quick-jump-bar' not in text:
    pos = text.find('<section id="thu-tu-tinh"')
    print("<section id='thu-tu-tinh' found at:", pos)
    # Insert before section
    quick_bar = """    <!-- Quick Tool Adjustment Navigator (Điểm Đánh Dấu Can Thiệp Công Cụ) -->
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
    </div>\n\n    """
    text = text[:pos] + quick_bar + text[pos:]
    with open('BSV_BimKetCauVer2.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Inserted quick-jump-bar successfully before section!")

