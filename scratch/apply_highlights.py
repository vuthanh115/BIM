import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('BSV_BimKetCauVer2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for high-visibility highlights and pulsers
highlight_css = """
    /* Highlight Styles for Tool Customization */
    .tool-highlight {
      position: relative;
      border: 2px dashed #f59e0b !important;
      background: rgba(245, 158, 11, 0.08) !important;
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      margin: 1.25rem 0;
      transition: all 0.3s ease;
      box-shadow: 0 0 20px rgba(245, 158, 11, 0.15);
    }

    .tool-highlight:hover {
      background: rgba(245, 158, 11, 0.14) !important;
      border-color: #fbbf24 !important;
      box-shadow: 0 0 30px rgba(245, 158, 11, 0.3);
    }

    .tool-highlight-bimspeed {
      border-color: #10b981 !important;
      background: rgba(16, 185, 129, 0.08) !important;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.15);
    }

    .tool-highlight-bimspeed:hover {
      background: rgba(16, 185, 129, 0.14) !important;
      border-color: #34d399 !important;
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.3);
    }

    .edit-marker {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }

    .marker-atool {
      background: #f59e0b;
      color: #000;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
    }

    .marker-bimspeed {
      background: #10b981;
      color: #000;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
    }

    .quick-jump-bar {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 2rem;
    }

    .jump-btn {
      font-size: 0.8rem;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .jump-btn-atool {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
    }

    .jump-btn-atool:hover {
      background: #f59e0b;
      color: #000;
    }

    .jump-btn-bimspeed {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
    }

    .jump-btn-bimspeed:hover {
      background: #10b981;
      color: #000;
    }
"""

# Insert CSS before </style>
if '.tool-highlight {' not in html:
    html = html.replace('</style>', highlight_css + '\n  </style>')
    print("[1] Injected highlight CSS styles")

# 2. Add Quick Jump Bar right after Hero Banner
quick_jump_html = """    <!-- Quick Tool Adjustment Navigator -->
    <div class="quick-jump-bar">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.1rem; color: var(--accent);"><i class="fa-solid fa-highlighter"></i></span>
        <span style="font-weight: 800; font-size: 0.85rem; color: var(--text-primary);">ĐIỂM ĐÁNH DẤU CHỈNH SỬA CÔNG CỤ (ATOOL & BIMSPEED):</span>
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <a href="#edit-atool-1" class="jump-btn jump-btn-atool"><i class="fa-solid fa-arrow-down"></i> ATool: Ưu tiên Join (Mục A)</a>
        <a href="#edit-bimspeed-1" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> BimSpeed: Pick ván khuôn (Mục B)</a>
        <a href="#edit-atool-2" class="jump-btn jump-btn-atool"><i class="fa-solid fa-arrow-down"></i> ATool: Bước 02 BOQ</a>
        <a href="#edit-bimspeed-2" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> BimSpeed: Bước 03 BOQ</a>
      </div>
    </div>
"""

hero_end = '</header>'
if 'quick-jump-bar' not in html and hero_end in html:
    html = html.replace(hero_end, hero_end + '\n\n' + quick_jump_html)
    print("[2] Added Quick Tool Adjustment Navigator bar")

# 3. Highlight Location 1: ATool in Section A (Priority Chain Callout)
old_atool_1 = """        <div class="tool-callout">
          <div>
            <strong><i class="fa-solid fa-robot"></i> Tự động hóa xử lý:</strong> Sử dụng add-in <span class="tool-badge">Atool</span> để nạp chuỗi quy ước trên và tự động Join hàng loạt cấu kiện 3D trong Revit mà không cần join thủ công.
          </div>
          <div>
            <span class="badge badge-amber"><i class="fa-solid fa-triangle-exclamation"></i> Chú ý khe cô lập</span> để tách riêng dầm và cột khỏi sàn chống lún.
          </div>
        </div>"""

new_atool_1 = """        <!-- EDIT LOCATION 1: ATOOL JOIN GEOMETRY -->
        <div class="tool-highlight" id="edit-atool-1" style="scroll-margin-top: 120px;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 8px;">
            <span class="edit-marker marker-atool"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ CHỈNH SỬA 1: ATOOL - JOIN CẤU KIỆN]</span>
            <span style="font-size: 0.75rem; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">PDF Block 03 • (537.8, 131.8)</span>
          </div>
          <div style="font-size: 0.92rem; color: var(--text-primary); line-height: 1.6;">
            <strong><i class="fa-solid fa-robot" style="color: #f59e0b;"></i> Văn bản gốc trong tài liệu:</strong> 
            <code style="background: rgba(0,0,0,0.4); padding: 3px 8px; border-radius: 5px; color: #fbbf24; font-weight: 700;">(Sử dụng Atool để join cấu kiện)</code> theo thứ tự: 
            <strong>Sàn &gt; Móng &gt; Cột &gt; Dầm &gt; Vách &gt; Cầu thang</strong>.
          </div>
          <div style="margin-top: 8px; font-size: 0.8rem; color: var(--accent); background: rgba(245, 158, 11, 0.1); padding: 8px 12px; border-radius: 6px;">
            <i class="fa-solid fa-pen-to-square"></i> <strong>Ghi chú điều chỉnh sau này:</strong> Nếu bạn chuyển sang dùng công cụ khác (như Dynamo Script, BIM One, hoặc tool tự phát triển), hãy thay thế tên add-in và cấu hình thứ tự Join tại vị trí này.
          </div>
        </div>"""

if old_atool_1 in html:
    html = html.replace(old_atool_1, new_atool_1)
    print("[3] Highlighted ATool Location 1 in Section A")

# 4. Highlight Location 2: BimSpeed in Section B Parameters
old_sec_b_header = """    <!-- SECTION B: 7 BƯỚC QUY TRÌNH GÁN BIẾN & ĐỐI CHIẾU BOQ -->
    <section id="quy-trinh-7-buoc" style="scroll-margin-top: 90px; margin-bottom: 3.5rem;">
      <div class="section-header">
        <span class="section-tag">PHẦN B</span>
        <h2 class="section-title">Quy Trình 7 Bước Chuẩn Hóa Gán Biến & Đối Chiếu BOQ</h2>
        <p class="section-desc">
          Các bước bắt buộc kỹ sư BIM phải thực hiện tuần tự để kiểm soát dữ liệu đầu vào, chạy ván khuôn tự động và liên kết chính xác với bảng dự toán BOQ.
        </p>
      </div>"""

new_sec_b_header = """    <!-- SECTION B: PROJECT PARAMETERS & 7 BƯỚC QUY TRÌNH GÁN BIẾN -->
    <section id="quy-trinh-7-buoc" style="scroll-margin-top: 90px; margin-bottom: 3.5rem;">
      <div class="section-header">
        <span class="section-tag">PHẦN B</span>
        <h2 class="section-title">Project Parameters & Quy Trình 7 Bước Đối Chiếu BOQ</h2>
        <p class="section-desc">
          Các quy ước thiết lập tham số dự án (Revit) và các bước kỹ sư BIM bắt buộc thực hiện tuần tự để kiểm soát dữ liệu đầu vào, chạy ván khuôn tự động và liên kết chính xác với bảng dự toán BOQ.
        </p>
      </div>

      <!-- Core 3 Parameter Groups from PDF with BIMSPEED Highlight -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 1.5rem;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem;">
          <div style="font-size: 0.75rem; color: var(--primary); font-weight: 800; text-transform: uppercase;">Nhóm 01</div>
          <h4 style="font-size: 1rem; font-weight: 800; margin: 4px 0 8px 0; color: var(--text-primary);"><i class="fa-solid fa-cube"></i> Khối Lượng Bê Tông</h4>
          <p style="font-size: 0.825rem; color: var(--text-secondary); line-height: 1.5;">
            Gán biến thật kỹ theo BOQ rồi mới chạy ván khuôn. Tham số <code>Comments</code>: Nhập kiểu phân loại - Phân khu.
          </p>
        </div>

        <!-- EDIT LOCATION 2: BIMSPEED FORMWORK PARAMETERS -->
        <div class="tool-highlight tool-highlight-bimspeed" id="edit-bimspeed-1" style="margin: 0; scroll-margin-top: 120px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <div style="font-size: 0.75rem; color: #10b981; font-weight: 800; text-transform: uppercase;">Nhóm 02</div>
            <span class="edit-marker marker-bimspeed" style="margin-bottom: 0; font-size: 0.68rem;"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 2: BIMSPEED]</span>
          </div>
          <h4 style="font-size: 1rem; font-weight: 800; margin: 4px 0 8px 0; color: var(--text-primary);"><i class="fa-solid fa-clone" style="color: #10b981;"></i> Khối Lượng Ván Khuôn</h4>
          <p style="font-size: 0.825rem; color: var(--text-primary); line-height: 1.5;">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #34d399; font-weight: 700;">(Chạy tool bimspeed cho toàn bộ cấu kiện - pick đáy + mặt bên)</code>.
          </p>
          <div style="margin-top: 6px; font-size: 0.75rem; color: #10b981;">
            <i class="fa-solid fa-pen-to-square"></i> <em>Điểm chỉnh sửa: Tùy chỉnh chế độ phủ ván hoặc add-in ván khuôn thay thế.</em>
          </div>
        </div>

        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem;">
          <div style="font-size: 0.75rem; color: var(--accent); font-weight: 800; text-transform: uppercase;">Nhóm 03</div>
          <h4 style="font-size: 1rem; font-weight: 800; margin: 4px 0 8px 0; color: var(--text-primary);"><i class="fa-solid fa-border-all"></i> Khối Lượng Diện Tích</h4>
          <p style="font-size: 0.825rem; color: var(--text-secondary); line-height: 1.5;">
            Thường sử dụng ván gán diện tích nền, đầm chặt... Biến <code>BSV_PhanLoai</code>: <code>DT_Nen</code>, <code>DT_DamChat</code>.
          </p>
        </div>
      </div>"""

if old_sec_b_header in html:
    html = html.replace(old_sec_b_header, new_sec_b_header)
    print("[4] Added Parameter Groups and Highlighted BimSpeed Location 2")

# 5. Highlight Location 3 & 4: Step 02 (ATool) and Step 03 (BimSpeed) in 7-Step Workflow
old_step_2_3 = """        <div class="wf-card">
          <div class="wf-num">02</div>
          <div class="wf-title"><i class="fa-solid fa-object-ungroup" style="color: var(--primary);"></i> Chạy Join Bê Tông Tự Động</div>
          <div class="wf-desc">
            Mở add-in <strong>Atool</strong>, nạp đúng thứ tự ưu tiên <code>Sàn > Móng > Cột > Dầm > Vách > Cầu thang</code> và chạy quét join toàn bộ mô hình 3D.
          </div>
        </div>

        <div class="wf-card">
          <div class="wf-num">03</div>
          <div class="wf-title"><i class="fa-solid fa-clone" style="color: var(--primary);"></i> Chạy Ván Khuôn (BimSpeed)</div>
          <div class="wf-desc">
            Chạy tool <strong>BimSpeed</strong> (pick đáy + mặt bên), sau đó chạy tool <strong>BSV_PhanLoaiVanKhuon</strong> để tự động kế thừa Comments từ bê tông.
          </div>
          <div class="wf-warning"><i class="fa-solid fa-magnifying-glass"></i> Kiểm tra kỹ các diện ván bị lỗi hoặc bị trùng!</div>
        </div>"""

new_step_2_3 = """        <!-- EDIT LOCATION 3: STEP 02 ATOOL JOIN -->
        <div class="wf-card tool-highlight" id="edit-atool-2" style="scroll-margin-top: 120px; border-width: 2px !important;">
          <div class="wf-num">02</div>
          <span class="edit-marker marker-atool"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 3: BƯỚC 02 - ATOOL]</span>
          <div class="wf-title"><i class="fa-solid fa-object-ungroup" style="color: #f59e0b;"></i> Chạy Join Bê Tông Tự Động (ATool)</div>
          <div class="wf-desc">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #fbbf24; font-weight: 700;">02. Chạy join bê tông theo quy ước (Load thứ tự trong Atool)</code>.
            Mở add-in <strong>Atool</strong>, nạp file config thứ tự ưu tiên <code>Sàn &gt; Móng &gt; Cột &gt; Dầm &gt; Vách &gt; Cầu thang</code> và kích hoạt quét join toàn bộ công trình 3D.
          </div>
          <div style="margin-top: 8px; font-size: 0.775rem; color: #fbbf24;">
            <i class="fa-solid fa-pen-to-square"></i> <em>Điểm chỉnh sửa: Tùy chỉnh quy trình gọi add-in Join sau này.</em>
          </div>
        </div>

        <!-- EDIT LOCATION 4: STEP 03 BIMSPEED FORMWORK -->
        <div class="wf-card tool-highlight tool-highlight-bimspeed" id="edit-bimspeed-2" style="scroll-margin-top: 120px; border-width: 2px !important;">
          <div class="wf-num">03</div>
          <span class="edit-marker marker-bimspeed"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 4: BƯỚC 03 - BIMSPEED]</span>
          <div class="wf-title"><i class="fa-solid fa-clone" style="color: #10b981;"></i> Chạy Ván Khuôn (BimSpeed)</div>
          <div class="wf-desc">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #34d399; font-weight: 700;">03. Chạy ván khuôn (Bim Speed), gán biến ván khuôn (Tool BSV_PhanLoaiVanKhuon)</code>.
            Chạy tool <strong>BimSpeed</strong> (chọn pick đáy + mặt bên), kế tiếp chạy tool <strong>BSV_PhanLoaiVanKhuon</strong> để tự động sao chép giá trị Comments từ Bê tông sang Ván khuôn.
          </div>
          <div class="wf-warning" style="background: rgba(16, 185, 129, 0.15); border-color: rgba(16, 185, 129, 0.3); color: #34d399;">
            <i class="fa-solid fa-magnifying-glass"></i> Kiểm tra kỹ các diện ván bị lỗi hoặc bị trùng!
          </div>
          <div style="margin-top: 8px; font-size: 0.775rem; color: #34d399;">
            <i class="fa-solid fa-pen-to-square"></i> <em>Điểm chỉnh sửa: Tùy chỉnh công cụ dựng ván khuôn & tool gán mã code.</em>
          </div>
        </div>"""

if old_step_2_3 in html:
    html = html.replace(old_step_2_3, new_step_2_3)
    print("[5] Highlighted Step 02 (ATool) and Step 03 (BimSpeed) in 7-Step Workflow")

with open('BSV_BimKetCauVer2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully saved highlighted version of BSV_BimKetCauVer2.html!")
