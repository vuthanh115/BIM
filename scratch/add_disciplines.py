# -*- coding: utf-8 -*-
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS before </style>
css_addition = """
    /* Discipline Section Styles */
    .discipline-nav {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 12px;
      margin-bottom: 2rem;
    }

    .disc-btn {
      padding: 14px 16px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      cursor: pointer;
      color: var(--text-secondary);
      font-weight: 700;
      font-size: 0.9rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
      text-align: center;
    }

    .disc-btn i {
      font-size: 1.35rem;
      color: var(--primary);
    }

    .disc-btn:hover {
      border-color: var(--border-highlight);
      color: var(--text-primary);
      transform: translateY(-2px);
    }

    .disc-btn.active {
      background: var(--bg-accent);
      color: var(--primary);
      border-color: var(--primary);
      box-shadow: 0 0 20px var(--primary-glow);
    }

    .disc-pane {
      display: none;
      animation: fadeIn 0.3s ease;
    }

    .disc-pane.active {
      display: block;
    }

    .wbs-card-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .wbs-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.6rem;
      box-shadow: var(--box-shadow);
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
    }

    .wbs-box:hover {
      border-color: var(--border-highlight);
      transform: translateY(-2px);
    }

    .wbs-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid var(--border-color);
    }

    .wbs-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      background: var(--primary-glow);
      color: var(--primary);
      padding: 3px 8px;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .lod-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(245, 158, 11, 0.15);
      color: var(--accent);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .wbs-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--text-primary);
      margin-bottom: 0.5rem;
    }

    .wbs-body {
      font-size: 0.875rem;
      color: var(--text-secondary);
      line-height: 1.6;
      flex-grow: 1;
    }

    .wbs-deliverables {
      margin-top: 1rem;
      background: var(--bg-surface);
      padding: 0.85rem 1rem;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      font-size: 0.825rem;
    }

    .wbs-deliverables strong {
      color: var(--text-primary);
    }

    .clash-matrix-table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.875rem;
    }

    .clash-matrix-table th, .clash-matrix-table td {
      padding: 12px 14px;
      border: 1px solid var(--border-color);
      text-align: left;
    }

    .clash-matrix-table th {
      background: var(--table-header);
      color: var(--text-primary);
      font-weight: 700;
    }

    .clash-priority-high {
      color: var(--danger);
      font-weight: 700;
    }

    .clash-priority-med {
      color: var(--accent);
      font-weight: 700;
    }

    .clash-priority-low {
      color: var(--primary);
      font-weight: 700;
    }
"""

if '.discipline-nav' not in content:
    content = content.replace('    /* Print & Responsive */', css_addition + '\n    /* Print & Responsive */')

# 2. Update navbar
if '#de-muc-bo-mon' not in content:
    target_nav = '<li><a href="#quy-trinh" class="active"><i class="fa-solid fa-list-check"></i> Quy trình BIM</a></li>'
    replacement_nav = target_nav + '\n      <li><a href="#de-muc-bo-mon"><i class="fa-solid fa-sitemap"></i> Đề mục 4 Bộ môn</a></li>'
    content = content.replace(target_nav, replacement_nav)

# 3. Add Section before #thiet-ke
section_html = """
    <!-- SECTION: HỆ THỐNG ĐỀ MỤC CÁC BỘ MÔN (DISCIPLINE BREAKDOWN STRUCTURE) -->
    <section id="de-muc-bo-mon" style="scroll-margin-top: 90px; margin-bottom: 4.5rem;">
      <div class="section-header">
        <span class="section-tag">CHUẨN HÓA PHẠM VI MÔ HÌNH HÓA (WBS)</span>
        <h2 class="section-title">Hệ Thống Đề Mục & Quy Trình 4 Bộ Môn Cốt Lõi</h2>
        <p class="section-desc">
          Phân rã chi tiết phạm vi kỹ thuật cho từng bộ môn: Kiến trúc, Kết cấu, Cơ điện (MEPF) và Hạ tầng kỹ thuật xuyên suốt các mốc LOD 200 $\rightarrow$ LOD 500 phục vụ bóc tách khối lượng 5D, tiến độ 4D và bàn giao số.
        </p>
      </div>

      <!-- Discipline Tabs -->
      <div class="discipline-nav">
        <button class="disc-btn active" onclick="switchDiscipline('disc-arc', this)">
          <i class="fa-solid fa-building-columns"></i>
          <span>1. BIM Kiến Trúc<br><small style="color: var(--text-muted); font-size: 0.75rem;">(Architecture - ARC)</small></span>
        </button>
        <button class="disc-btn" onclick="switchDiscipline('disc-str', this)">
          <i class="fa-solid fa-cubes-stacked"></i>
          <span>2. BIM Kết Cấu<br><small style="color: var(--text-muted); font-size: 0.75rem;">(Structure - STR)</small></span>
        </button>
        <button class="disc-btn" onclick="switchDiscipline('disc-mep', this)">
          <i class="fa-solid fa-bolt"></i>
          <span>3. BIM Cơ Điện<br><small style="color: var(--text-muted); font-size: 0.75rem;">(MEPF Systems)</small></span>
        </button>
        <button class="disc-btn" onclick="switchDiscipline('disc-inf', this)">
          <i class="fa-solid fa-road"></i>
          <span>4. BIM Hạ Tầng<br><small style="color: var(--text-muted); font-size: 0.75rem;">(Infrastructure - INF)</small></span>
        </button>
        <button class="disc-btn" onclick="switchDiscipline('disc-matrix', this)">
          <i class="fa-solid fa-shuffle"></i>
          <span>5. Ma Trận Phối Hợp<br><small style="color: var(--text-muted); font-size: 0.75rem;">(Clash Matrix & SOP)</small></span>
        </button>
      </div>

      <!-- PANE 1: ARC (KIẾN TRÚC) -->
      <div class="disc-pane active" id="disc-arc">
        <div class="wbs-card-grid">
          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: ARC-01</span>
              <span class="lod-badge">LOD 200 - 300</span>
            </div>
            <h4 class="wbs-title">Khối Tích Không Gian & Phân Vùng Chức Năng</h4>
            <div class="wbs-body">
              Thiết lập lưới trục định vị, cao độ tầng (Levels). Mô hình hóa khối tích Massing, tạo lập Room & Area Space phân định rõ: Khu vực sản xuất, Kho xưởng, Văn phòng điều hành, Khu vực phụ trợ kỹ thuật.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bảng thống kê diện tích tự động (Area Schedule), Room Count, Sơ đồ công năng mặt bằng.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: ARC-02</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Hệ Thống Vỏ Bao Che & Tường Ngăn</h4>
            <div class="wbs-body">
              Mô hình hóa tường ngoại thất (Panel tôn cách nhiệt sandwich, tường gạch), vách kính mặt dựng (Curtain Wall), vách thạch cao chống ẩm/ngăn cháy nội thất. Gắn mã vật liệu phục vụ dự toán chi phí.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Khối lượng diện tích tường m², bảng bóc tách tấm panel, chi tiết liên kết chân tường & giằng đỉnh.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: ARC-03</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Cửa Đi, Cửa Sổ & Lam Thông Gió (Louvers)</h4>
            <div class="wbs-body">
              Mô hình hóa chuẩn kích thước lỗ mở thô (Rough Opening), loại cửa đi (cửa trượt công nghiệp, cửa thép thoát hiểm ngăn cháy, cửa cuốn), cửa sổ kính và hệ thống louver lấy gió tươi nhà xưởng.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bảng thống kê cửa đi / cửa sổ (Door/Window Schedule) gắn phụ kiện bản lề, khóa, giới hạn chịu lửa.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: ARC-04</span>
              <span class="lod-badge">LOD 300 - 400</span>
            </div>
            <h4 class="wbs-title">Hoàn Thiện Sàn, Trần & Hệ Mái Thoát Nước</h4>
            <div class="wbs-body">
              Mô hình hóa lớp tăng cứng sàn xưởng (Sika Hardener, sơn Epoxy), trần thạch cao văn phòng, mái tôn sóng kèm xốp cách nhiệt EPS/PU, máng xối (gutter), ống thu nước mưa rulo và độ dốc mái tối thiểu 10%.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bảng khối lượng sơn sàn Epoxy m², diện tích tôn mái kèm phụ kiện diềm mè, úp nóc, máng xối.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: ARC-05</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Giao Thông Trục Đứng (Thang Bộ, Thang Máy, Ram Dốc)</h4>
            <div class="wbs-body">
              Mô hình hóa cầu thang thoát hiểm (BTCT hoặc thang thép), lan can bảo vệ an toàn cao 1.1m, buồng thang máy chở hàng/chở người, hố pit, phòng máy và ram dốc bốc dỡ hàng hóa xe container (Loading Dock).
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bản vẽ chi tiết thang bộ, cao độ bậc, độ dốc ram hàng và phối hợp chừa lỗ mở sàn kết cấu.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: ARC-06</span>
              <span class="lod-badge">LOD 350 - 500</span>
            </div>
            <h4 class="wbs-title">Nội Thất, Thiết Bị Vệ Sinh & Hoàn Công As-built</h4>
            <div class="wbs-body">
              Bố trí bàn ghế văn phòng, thiết bị phòng lab, tủ locker công nhân, vách vệ sinh compact, chậu rửa, bồn cầu. Cập nhật hiện trạng hoàn công 100% ngoài công trường để bàn giao số.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Danh mục tài sản nội thất (Asset List) gắn mã ID tra cứu phục vụ quản lý cơ sở vật chất (FM).
            </div>
          </div>
        </div>
      </div>

      <!-- PANE 2: STR (KẾT CẤU) -->
      <div class="disc-pane" id="disc-str">
        <div class="wbs-card-grid">
          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: STR-01</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Kết Cấu Phần Ngầm (Substructure)</h4>
            <div class="wbs-body">
              Mô hình hóa hệ cọc ép / cọc khoan nhồi, đài cọc, móng đơn, móng băng, dầm giằng móng BTCT, nền nhà xưởng chịu tải trọng động xe nâng/xe tải, hố pit bốc dỡ hàng (Dock Leveler) và bể nước ngầm.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Khối lượng bê tông móng m³, diện tích ván khuôn, bảng thống kê tọa độ tim cọc.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: STR-02</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Kết Cấu Thân Bê Tông Cốt Thép (Superstructure)</h4>
            <div class="wbs-body">
              Mô hình hóa hệ cột, vách thang máy, dầm sàn các tầng lầu khu văn phòng. Gắn kết thuộc tính mác bê tông (B25, B30), cấp độ bền và mô hình hóa cốt thép 3D (Rebar) tại các vị trí nút khung phức tạp.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Khối lượng bê tông thân, bảng bóc tách cốt thép kg/tấn theo đường kính (phi 10 - phi 32).
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: STR-03</span>
              <span class="lod-badge">LOD 350 - 400</span>
            </div>
            <h4 class="wbs-title">Kết Cấu Thép Nhà Tiền Chế (Pre-Engineered Steel)</h4>
            <div class="wbs-body">
              Mô hình hóa hệ bu lông neo móng (Anchor Bolts), cột thép chữ H, vì kèo thép (Rafter), dầm cầu trục (Crane Beam), hệ giằng mái cáp thép, giằng cột và xà gồ tường/mái (C/Z Purlin).
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bảng khối lượng thép hình tấn, bản vẽ chế tạo gia công xưởng (Fabrication Shop Drawings), bảng chi tiết bulong.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: STR-04</span>
              <span class="lod-badge">LOD 350 - 400</span>
            </div>
            <h4 class="wbs-title">Khẩu Độ Chôn Sẵn & Lỗ Xuyên Cấu Kiện (Opening & Sleeve)</h4>
            <div class="wbs-body">
              Định vị và khoét các lỗ mở kỹ thuật trên sàn BTCT, đục lỗ trên dầm cho ống cơ điện xuyên qua (Sleeve Pipe), bản mã thép chôn sẵn (Embedded Plate) phục vụ neo đỡ thang máng cáp và ống PCCC.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bản vẽ định vị Sleeve & Lỗ mở trước khi đổ bê tông, triệt tiêu 100% việc đục phá dầm sàn sau này.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: STR-05</span>
              <span class="lod-badge">LOD 300 - 4D</span>
            </div>
            <h4 class="wbs-title">Biện Pháp Thi Công & Kết Cấu Tạm (Temporary Works)</h4>
            <div class="wbs-body">
              Mô hình hóa hệ cốp pha giàn giáo, cẩu tháp vận thăng, đường vận chuyển nội bộ cho xe cẩu lắp dựng vì kèo thép, vùng sàn thao tác trên cao phục vụ mô phỏng tiến độ thi công 4D an toàn.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Video mô phỏng lắp dựng kết cấu thép theo ngày, kiểm soát bán kính cẩu hàng không va chạm.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: STR-06</span>
              <span class="lod-badge">LOD 500</span>
            </div>
            <h4 class="wbs-title">Mô Hình Hoàn Công Kết Cấu (As-built Structural)</h4>
            <div class="wbs-body">
              Cập nhật cao độ đỉnh bu lông, độ lệch tim cột sau khi lắp dựng, vị trí cốt thép nghiệm thu thực tế, biên bản kiểm tra siêu âm mối hàn đường nối để phục vụ hồ sơ cấp phép nghiệm thu công trình.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bộ bản vẽ hoàn công kết cấu số, dữ liệu nghiệm thu liên kết với mô hình số hóa GLCONS.
            </div>
          </div>
        </div>
      </div>

      <!-- PANE 3: MEPF (CƠ ĐIỆN) -->
      <div class="disc-pane" id="disc-mep">
        <div class="wbs-card-grid">
          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: MEP-01 (HVAC)</span>
              <span class="lod-badge">LOD 300 - 400</span>
            </div>
            <h4 class="wbs-title">Thông Gió & Điều Hòa Không Khí (HVAC System)</h4>
            <div class="wbs-body">
              Mô hình hóa thiết bị trung tâm: Chiller giải nhiệt gió/nước, AHU phòng sạch/xưởng may, quạt hút khí thải, đường ống gió (Supply/Return/Exhaust Duct), van dập lửa (FD/VAV), miệng gió cấp/hút và đường ống nước lạnh Chilled Water.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Diện tích tôn ống gió m², bảng kích thước miệng gió, bản vẽ định vị ty treo giá đỡ (Hangers).
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: MEP-02 (ELE)</span>
              <span class="lod-badge">LOD 300 - 400</span>
            </div>
            <h4 class="wbs-title">Hệ Thống Điện & Chiếu Sáng (Electrical & Lighting)</h4>
            <div class="wbs-body">
              Trạm biến áp trung thế, máy phát điện dự phòng, tủ điện chính MSB/MDB, đường thang máng cáp (Cable Tray / Trunking / Ladder), ống luồn dây điện (Conduit), đèn led chiếu sáng xưởng/văn phòng, công tắc ổ cắm, tiếp địa chống sét.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Chiều dài thang máng cáp (mét), số lượng máng phụ kiện (Co, Tê, Giảm), bảng tải phụ tải điện.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: MEP-03 (PLUMB)</span>
              <span class="lod-badge">LOD 300 - 400</span>
            </div>
            <h4 class="wbs-title">Hệ Thống Cấp Thoát Nước (Plumbing & Drainage)</h4>
            <div class="wbs-body">
              Bể chứa nước ngầm, trạm máy bơm cấp nước áp lực (như thiết bị PWP-01), ống cấp nước PPR/HDPE, mạng lưới thoát nước thải sinh hoạt/sản xuất (uPVC), ống thoát nước mưa gom từ mái, hố thu sàn, bẫy mùi và hệ thống xử lý nước thải.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Chiều dài ống theo đường kính (D20 - D250), bảng thống kê van chặn, van một chiều, đồng hồ đo lưu lượng.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: MEP-04 (FIRE)</span>
              <span class="lod-badge">LOD 300 - 400</span>
            </div>
            <h4 class="wbs-title">Phòng Cháy Chữa Cháy (Fire Protection & Alarm)</h4>
            <div class="wbs-body">
              Máy bơm PCCC động cơ điện & Diesel, đường ống chữa cháy vách tường, mạng lưới đầu phun tự động Sprinkler (Upright/Pendant), họng tiếp nước xe chữa cháy, đầu báo khói/nhiệt địa chỉ, nút nhấn khẩn, chuông còi báo động.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Cao độ đầu phun Sprinkler so với trần và máng cáp, bảng thống kê van tràn ngập Deluge Valve, bình chữa cháy.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: MEP-05 (ELV/BMS)</span>
              <span class="lod-badge">LOD 300 - 400</span>
            </div>
            <h4 class="wbs-title">Điện Nhẹ & Quản Trị Tòa Nhà (ELV, Camera AI & BMS)</h4>
            <div class="wbs-body">
              Hệ thống Camera AI giám sát công trường/nhà xưởng 24/7 (kết nối dữ liệu BIM Core), mạng LAN cáp quang nội bộ, tổng đài thoại, hệ thống kiểm soát cửa vào ra vân tay/thẻ từ (Access Control), loa âm trần thông báo PA và cảm biến BMS.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bản vẽ sơ đồ nguyên lý hạ tầng mạng viễn thông, tọa độ vị trí lắp đặt camera AI không điểm mù.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: MEP-06 (FM)</span>
              <span class="lod-badge">LOD 500</span>
            </div>
            <h4 class="wbs-title">Gắn Thuộc Tính Vận Hành Tài Sản Thiết Bị (COBie & FM)</h4>
            <div class="wbs-body">
              Số hóa toàn bộ thông số kỹ thuật (Model, Serial Number, công suất kW, lưu lượng m³/h, ngày lắp đặt, đơn vị cung cấp, hạn bảo hành) vào từng phần tử 3D thiết bị. Đính kèm liên kết file PDF Catalogue và sổ tay O&M Manual.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bảng cơ sở dữ liệu tài sản số xuất chuẩn Excel/COBie, sẵn sàng tích hợp trực tiếp vào phần mềm bảo trì FM.
            </div>
          </div>
        </div>
      </div>

      <!-- PANE 4: INF (HẠ TẦNG KỸ THUẬT) -->
      <div class="disc-pane" id="disc-inf">
        <div class="wbs-card-grid">
          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: INF-01</span>
              <span class="lod-badge">LOD 200 - 300</span>
            </div>
            <h4 class="wbs-title">San Nền & Khối Lượng Đào Đắp (Earthwork Cut & Fill)</h4>
            <div class="wbs-body">
              Dựng mô hình bề mặt địa hình tự nhiên từ số liệu trắc địa/drone bay quét Point Cloud. Mô hình hóa mặt bằng thiết kế hoàn thiện, tính toán khối lượng đào đắp (Cut & Fill) theo ô lưới và đường đồng mức cao độ.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Báo cáo cân bằng đào đắp m³, sơ đồ hướng dốc thoát nước bề mặt khu đất dự án.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: INF-02</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Giao Thông Nội Khu & Sân Bãi Bốc Dỡ Hàng</h4>
            <div class="wbs-body">
              Mô hình hóa kết cấu áo đường bê tông nhựa/bê tông xi măng, bó vỉa, vỉa hè cho người đi bộ, vạch kẻ sơn giao thông, biển báo, bán kính quay xe tải nặng/container và sân đỗ xe container chờ giao nhận hàng.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Diện tích thảm bê tông nhựa m², chiều dài bó vỉa mét, mô phỏng góc quay xe tải (Swept Path Analysis).
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: INF-03</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Thoát Nước Mưa & Nước Thải Ngoài Nhà</h4>
            <div class="wbs-body">
              Hệ thống mương hở/mương kín thu nước mặt, hố ga lắng cát, ống cống tròn BTCT ly tâm (D400 - D1500), trạm xử lý nước thải tập trung nội khu, tuyến ống thoát nước thải sau xử lý đấu nối ra mạng lưới khu công nghiệp.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Trắc dọc tuyến cống, cao độ đáy hố ga (Invert Level), khối lượng đất đào đặt cống và số lượng hố ga.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: INF-04</span>
              <span class="lod-badge">LOD 300 - 350</span>
            </div>
            <h4 class="wbs-title">Mạng Lưới Cấp Điện & Cấp Nước Ngoài Nhà</h4>
            <div class="wbs-body">
              Tuyến cáp ngầm trung/hạ thế, mương cáp kỹ thuật, hệ thống cột đèn chiếu sáng sân vườn và đường giao thông nội khu, trụ tiếp nước chữa cháy ngoài nhà (Fire Hydrant), đường ống cấp nước sạch từ nguồn KCN vào nhà máy.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bản vẽ mặt bằng tổng thể mạng lưới kỹ thuật ngầm ngoài nhà, tránh xung đột với hố móng công trình.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: INF-05</span>
              <span class="lod-badge">LOD 300 - 400</span>
            </div>
            <h4 class="wbs-title">Hàng Rào, Cổng Bảo Vệ & Cảnh Quan Cây Xanh</h4>
            <div class="wbs-body">
              Hệ thống tường rào bao quanh khu đất (tường gạch kết hợp lưới B40/thép hoa), nhà bảo vệ trực cổng, cổng xếp tự động barrier, bồn hoa cảnh quan, cây xanh bóng mát cách ly đảm bảo mật độ cây xanh theo quy chuẩn KCN.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Chiều dài mét hàng rào, diện tích thảm cỏ cây xanh m², phối cảnh tổng thể toàn khu dự án.
            </div>
          </div>

          <div class="wbs-box">
            <div class="wbs-header">
              <span class="wbs-code">WBS: INF-06</span>
              <span class="lod-badge">LOD 500</span>
            </div>
            <h4 class="wbs-title">Hoàn Công Hạ Tầng & Tọa Độ Đấu Nối Kỹ Thuật Số</h4>
            <div class="wbs-body">
              Định vị tọa độ thực tế (VN-2000) các hố ga ngầm, van chặn nước ngoài nhà, tuyến cáp ngầm. Đảm bảo khi sửa chữa hoặc mở rộng nhà máy trong tương lai (30 - 50 năm) không bị khoan trúng đường cáp ống ngầm.
            </div>
            <div class="wbs-deliverables">
              <strong>Đầu ra:</strong> Bản đồ số hạ tầng ngầm GIS/BIM, hỗ trợ công tác duy tu bảo dưỡng đường sá và hạ tầng.
            </div>
          </div>
        </div>
      </div>

      <!-- PANE 5: MA TRẬN PHỐI HỢP & XỬ LÝ XUNG ĐỘT (CLASH MATRIX) -->
      <div class="disc-pane" id="disc-matrix">
        <div style="background: var(--bg-card); padding: 2rem; border-radius: 14px; border: 1px solid var(--border-color); box-shadow: var(--box-shadow); margin-bottom: 2rem;">
          <h4 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-bottom: 1rem;">
            <i class="fa-solid fa-table-cells" style="color: var(--primary);"></i> Ma Trận Kiểm Soát Xung Đột Đa Bộ Môn (Clash Detection Matrix)
          </h4>
          <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
            Quy định các cặp bộ môn cần chạy kiểm tra xung đột tự động trên phần mềm Navisworks / Solibri và mức độ ưu tiên xử lý:
          </p>

          <table class="clash-matrix-table">
            <thead>
              <tr>
                <th>Cặp bộ môn phối hợp</th>
                <th>Loại xung đột thường gặp</th>
                <th>Mức độ ưu tiên</th>
                <th>Quy tắc phân xử & Giải pháp tiêu chuẩn</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>STR vs MEPF</strong><br><small style="color: var(--text-muted);">(Dầm sàn vs Ống cơ điện)</small></td>
                <td>Ống gió lớn, ống thoát nước đâm xuyên qua dầm, sàn hoặc móng BTCT</td>
                <td><span class="clash-priority-high"><i class="fa-solid fa-triangle-exclamation"></i> Bắt buộc xử lý (High)</span></td>
                <td>Ưu tiên giữ an toàn chịu lực của Kết cấu. MEP dịch chuyển tuyến hoặc xin cấp phép mở Sleeve theo vùng cho phép của kỹ sư Kết cấu.</td>
              </tr>
              <tr>
                <td><strong>MEPF vs MEPF</strong><br><small style="color: var(--text-muted);">(Các hệ cơ điện giao nhau)</small></td>
                <td>Máng cáp điện đâm ống gió, ống chữa cháy va chạm ống thoát nước tự chảy</td>
                <td><span class="clash-priority-high"><i class="fa-solid fa-triangle-exclamation"></i> Bắt buộc xử lý (High)</span></td>
                <td>
                  <strong>Quy tắc ưu tiên không gian:</strong><br>
                  1. Ống thoát nước tự chảy có độ dốc (Gravity)<br>
                  2. Ống gió kích thước lớn (Duct)<br>
                  3. Máng cáp điện & điện nhẹ (Cable Tray)<br>
                  4. Ống áp lực nhỏ (Cấp nước, PCCC) uốn lượn tránh.
                </td>
              </tr>
              <tr>
                <td><strong>ARC vs MEPF</strong><br><small style="color: var(--text-muted);">(Kiến trúc vs Thiết bị)</small></td>
                <td>Đáy ống gió / máng cáp vi phạm cao độ thông thủy trần hoàn thiện (Clearance)</td>
                <td><span class="clash-priority-med"><i class="fa-solid fa-circle-exclamation"></i> Trung bình (Medium)</span></td>
                <td>Đổi tiết diện ống gió từ vuông sang dẹt hoặc Kiến trúc hạ cao độ trần giả cục bộ (giật cấp trang trí).</td>
              </tr>
              <tr>
                <td><strong>INF vs STR/MEP</strong><br><small style="color: var(--text-muted);">(Hạ tầng vs Nhà xưởng)</small></td>
                <td>Tuyến cống ngoài nhà va chạm móng tường rào hoặc ống ngầm xuyên tường tầng hầm</td>
                <td><span class="clash-priority-med"><i class="fa-solid fa-circle-exclamation"></i> Trung bình (Medium)</span></td>
                <td>Đồng bộ cao độ đáy hố ga ngoài sân với điểm ra của hộp gen kỹ thuật trong nhà (Invert Level alignment).</td>
              </tr>
              <tr>
                <td><strong>ARC vs STR</strong><br><small style="color: var(--text-muted);">(Kiến trúc vs Kết cấu)</small></td>
                <td>Cột kết cấu nhô ra khỏi tường kiến trúc, vị trí cửa sổ đâm vào thanh giằng cột</td>
                <td><span class="clash-priority-low"><i class="fa-solid fa-info-circle"></i> Điều chỉnh TK (Low)</span></td>
                <td>Kiến trúc điều chỉnh bề dày vách bao hoặc dịch chuyển vị trí cửa sổ tránh thanh giằng thép xưởng.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""

if 'id="de-muc-bo-mon"' not in content:
    target_section = '<!-- SECTION 2: GIAI ĐOẠN THIẾT KẾ (BIM 3D - 4D - 5D) -->'
    content = content.replace(target_section, section_html + '\n    ' + target_section)

# 4. Add JS function before </script>
js_addition = """
    // Switch Discipline Tabs
    function switchDiscipline(paneId, btn) {
      document.querySelectorAll('.disc-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.disc-pane').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const targetPane = document.getElementById(paneId);
      if (targetPane) {
        targetPane.classList.add('active');
      }
    }
"""

if 'switchDiscipline' not in content:
    content = content.replace('    window.addEventListener(\'DOMContentLoaded\', () => {', js_addition + '\n    window.addEventListener(\'DOMContentLoaded\', () => {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully integrated 4 disciplines into index.html!')
