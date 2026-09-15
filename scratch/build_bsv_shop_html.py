import sys

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BSV_SHOP DRAWING REBAR - Quy Trình Chuẩn Hóa Triển Khai Bản Vẽ Thép Revit</title>
  
  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    :root[data-theme="dark"] {
      --bg-body: #080c14;
      --bg-surface: #0f172a;
      --bg-card: #141e33;
      --bg-card-hover: #192640;
      --bg-accent: #1e293b;
      --border-color: #202d45;
      --border-highlight: #334668;
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --primary-glow: rgba(56, 189, 248, 0.15);
      
      --accent: #f59e0b;
      --accent-glow: rgba(245, 158, 11, 0.15);
      
      --success: #10b981;
      --success-glow: rgba(16, 185, 129, 0.15);
      
      --danger: #f43f5e;
      --danger-glow: rgba(244, 63, 94, 0.15);
      
      --purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.15);
      
      --box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }

    :root[data-theme="light"] {
      --bg-body: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f5f9;
      --bg-accent: #f1f5f9;
      --border-color: #e2e8f0;
      --border-highlight: #cbd5e1;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-glow: rgba(2, 132, 199, 0.12);
      
      --accent: #d97706;
      --accent-glow: rgba(217, 119, 6, 0.12);
      
      --success: #16a34a;
      --success-glow: rgba(22, 163, 74, 0.12);
      
      --danger: #e11d48;
      --danger-glow: rgba(225, 29, 72, 0.12);
      
      --purple: #7e22ce;
      --purple-glow: rgba(126, 34, 206, 0.12);
      
      --box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-body);
      color: var(--text-primary);
      line-height: 1.6;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Top Sticky Navigation */
    .navbar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.85rem 2.5rem;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }

    .brand-badge {
      background: linear-gradient(135deg, #f59e0b, #ef4444);
      color: white;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 6px 12px;
      border-radius: 8px;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .brand-text h1 {
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: var(--text-primary);
    }

    .brand-text p {
      font-size: 0.75rem;
      color: var(--text-secondary);
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      list-style: none;
    }

    .nav-links a {
      text-decoration: none;
      color: var(--text-secondary);
      font-weight: 600;
      font-size: 0.85rem;
      padding: 8px 12px;
      border-radius: 8px;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .nav-links a:hover, .nav-links a.active {
      color: var(--accent);
      background: var(--accent-glow);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 14px;
      font-size: 0.85rem;
      font-weight: 600;
      border-radius: 8px;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }

    .btn-outline {
      background: transparent;
      border-color: var(--border-color);
      color: var(--text-secondary);
    }

    .btn-outline:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--accent), #ea580c);
      color: white;
    }

    .theme-toggle-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--accent);
      width: 38px;
      height: 38px;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.05rem;
      transition: all 0.2s ease;
    }

    /* Container */
    .main-container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 2.5rem 2rem 5rem 2rem;
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(239, 68, 68, 0.05));
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 20px;
      padding: 2.5rem;
      margin-bottom: 2rem;
      position: relative;
      overflow: hidden;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--accent-glow);
      color: var(--accent);
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }

    .hero-title {
      font-size: 2.3rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 0.75rem;
      line-height: 1.25;
    }

    .hero-title span {
      background: linear-gradient(135deg, var(--accent), #f97316);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
      font-size: 1.05rem;
      color: var(--text-secondary);
      max-width: 950px;
      margin-bottom: 1.8rem;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
      border-top: 1px solid var(--border-color);
      padding-top: 1.5rem;
    }

    .meta-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1rem 1.25rem;
    }

    .meta-label {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 700;
      margin-bottom: 4px;
    }

    .meta-val {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .meta-val i {
      color: var(--accent);
    }

    /* Quick Tool Adjustment Navigator */
    .quick-jump-bar {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 2.5rem;
      box-shadow: var(--box-shadow);
    }

    .jump-btn {
      font-size: 0.8rem;
      font-weight: 700;
      padding: 7px 14px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
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

    .jump-btn-atool {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
    }

    .jump-btn-atool:hover {
      background: #f59e0b;
      color: #000;
    }

    /* Tool Highlights */
    .tool-highlight {
      position: relative;
      border: 2px dashed #10b981 !important;
      background: rgba(16, 185, 129, 0.08) !important;
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      margin: 1.25rem 0;
      transition: all 0.3s ease;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.15);
    }

    .tool-highlight:hover {
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

    .marker-bimspeed {
      background: #10b981;
      color: #000;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
    }

    .marker-atool {
      background: #f59e0b;
      color: #000;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
    }

    /* Section Headers */
    .section-header {
      margin-bottom: 2rem;
    }

    .section-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      color: var(--accent);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 1px;
    }

    .section-title {
      font-size: 1.75rem;
      font-weight: 800;
      color: var(--text-primary);
      margin-top: 4px;
    }

    .section-desc {
      color: var(--text-secondary);
      font-size: 0.95rem;
      margin-top: 6px;
    }

    /* Component Tabs */
    .comp-tabs {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 12px;
      margin-bottom: 1.5rem;
    }

    .comp-tab-btn {
      padding: 10px 16px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      color: var(--text-secondary);
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }

    .comp-tab-btn:hover {
      border-color: var(--accent);
      color: var(--text-primary);
    }

    .comp-tab-btn.active {
      background: var(--accent);
      color: #000;
      border-color: var(--accent);
    }

    /* Component Content Box */
    .comp-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 2.25rem;
      box-shadow: var(--box-shadow);
      margin-bottom: 3.5rem;
    }

    .comp-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
      margin-top: 1.25rem;
    }

    .sub-panel {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.4rem;
    }

    .sub-panel-title {
      font-size: 1rem;
      font-weight: 800;
      color: var(--text-primary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 8px;
    }

    .sub-list {
      list-style: none;
      font-size: 0.85rem;
      color: var(--text-secondary);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .sub-list li {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      line-height: 1.5;
    }

    .sub-list li i {
      color: var(--accent);
      font-size: 0.75rem;
      margin-top: 5px;
      flex-shrink: 0;
    }

    .code-tag {
      font-family: 'JetBrains Mono', monospace;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-color);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.78rem;
      color: var(--accent);
    }

    .tool-badge {
      background: #10b981;
      color: #000;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
    }

    /* Schedules Gallery */
    .sched-gallery {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
      margin-top: 1.5rem;
    }

    .sched-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
    }

    .sched-card:hover {
      border-color: var(--accent);
      transform: translateY(-3px);
      box-shadow: 0 10px 25px var(--accent-glow);
    }

    .sched-img-box {
      height: 180px;
      background: #000;
      overflow: hidden;
      position: relative;
    }

    .sched-img-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      transition: transform 0.3s ease;
    }

    .sched-card:hover .sched-img-box img {
      transform: scale(1.05);
    }

    .sched-info {
      padding: 1rem;
      flex-grow: 1;
    }

    .sched-title {
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--text-primary);
      margin-bottom: 4px;
    }

    .sched-desc {
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    /* Mindmap Banner */
    .mindmap-banner {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
      margin-bottom: 3rem;
    }

    /* Modal Image Lightbox */
    .image-modal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.9);
      backdrop-filter: blur(10px);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }

    .image-modal.active {
      display: flex;
    }

    .modal-content-box {
      max-width: 95vw;
      max-height: 90vh;
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .modal-content-box img {
      max-width: 100%;
      max-height: 85vh;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
      object-fit: contain;
    }

    .modal-close-btn {
      position: absolute;
      top: -40px;
      right: 0;
      color: white;
      font-size: 1.8rem;
      cursor: pointer;
      background: none;
      border: none;
    }

    .modal-caption {
      color: var(--text-secondary);
      font-size: 0.85rem;
      margin-top: 10px;
      text-align: center;
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border-color);
      padding: 2.5rem 0 1.5rem 0;
      margin-top: 4rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      text-align: center;
    }

    /* Responsive */
    @media (max-width: 1100px) {
      .hero-meta-grid { grid-template-columns: repeat(2, 1fr); }
      .comp-grid { grid-template-columns: 1fr; }
      .sched-gallery { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 768px) {
      .navbar { padding: 0.8rem 1.25rem; }
      .nav-links { display: none; }
      .hero-title { font-size: 1.8rem; }
      .hero-meta-grid { grid-template-columns: 1fr; }
      .sched-gallery { grid-template-columns: 1fr; }
      .mindmap-banner { flex-direction: column; align-items: flex-start; }
    }
  </style>
</head>
<body>

  <!-- Sticky Top Navbar -->
  <nav class="navbar">
    <a href="index.html" class="brand" title="Quay lại Trang chủ BIM Management Platform">
      <div class="brand-badge"><i class="fa-solid fa-layer-group"></i> SHOP REBAR</div>
      <div class="brand-text">
        <h1>BSV_SHOP DRAWING REBAR</h1>
        <p>Quy Trình Chuẩn Hóa Triển Khai Bản Vẽ Thép Revit</p>
      </div>
    </a>

    <ul class="nav-links">
      <li><a href="#quy-tac-join"><i class="fa-solid fa-arrows-split-up-and-left"></i> 01. Join Cấu Kiện</a></li>
      <li><a href="#comp-section"><i class="fa-solid fa-cubes"></i> Các Cấu Kiện Shop</a></li>
      <li><a href="#schedules-shop"><i class="fa-solid fa-table-cells"></i> Biểu Mẫu Shop</a></li>
      <li><a href="#mindmap-shop"><i class="fa-solid fa-diagram-project"></i> Mindmap Gốc</a></li>
    </ul>

    <div class="nav-actions">
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" title="Chuyển chế độ Sáng / Tối">
        <i class="fa-solid fa-sun" id="themeIcon"></i>
      </button>
      <a href="BSV_BimKetCauVer2.html" class="btn btn-outline" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;" title="Mở Sổ tay Kết cấu"><i class="fa-solid fa-cube"></i> Sổ Tay KC</a>
      <a href="BSV_BimKienTruc.html" class="btn btn-outline" style="border-color: rgba(14, 165, 233, 0.4); color: #38bdf8;" title="Mở Sổ tay Kiến trúc"><i class="fa-solid fa-building-columns"></i> Sổ Tay KT</a>
      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>
      <button class="btn btn-primary" onclick="window.print()"><i class="fa-solid fa-print"></i> In Sổ Tay</button>
    </div>
  </nav>

  <div class="main-container">

    <!-- Hero Banner -->
    <header class="hero-banner">
      <div class="hero-badge"><i class="fa-solid fa-sheet-plastic"></i> Standard Operating Procedure (SOP) • Revit Rebar Shop Drawing</div>
      <h1 class="hero-title">SỔ TAY QUY TRÌNH <span>SHOP DRAWING REBAR</span></h1>
      <p class="hero-subtitle">
        Chuẩn hóa toàn diện quy cách đặt tên Partition, quy ước cắt gọt thép dầm/cột/móng/sàn, kỹ thuật kéo hình dạng thép 2D Bending Detail, Multi-Rebar Annotation (MRA), quản lý View Template và tự động hóa xuất bảng thống kê cốt thép thi công.
      </p>

      <div class="hero-meta-grid">
        <div class="meta-box">
          <div class="meta-label">Nguyên Tắc Join Đầu Tiên</div>
          <div class="meta-val"><i class="fa-solid fa-arrows-split-up-and-left"></i> Sàn > Móng > Cột...</div>
        </div>
        <div class="meta-box">
          <div class="meta-label">Công Cụ Dựng Thép</div>
          <div class="meta-val"><i class="fa-solid fa-screwdriver-wrench"></i> BimSpeed Rebar Tool</div>
        </div>
        <div class="meta-box">
          <div class="meta-label">Chi Tiết Uốn Thép 2D</div>
          <div class="meta-val"><i class="fa-solid fa-bezier-curve"></i> Rebar Bending Detail</div>
        </div>
        <div class="meta-box">
          <div class="meta-label">Quản Lý Thép Bản Vẽ</div>
          <div class="meta-val"><i class="fa-solid fa-tags"></i> Partition & BSV_PhanLoai</div>
        </div>
      </div>
    </header>

    <!-- Quick Tool Adjustment Navigator -->
    <div class="quick-jump-bar">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 1.25rem; color: #10b981;"><i class="fa-solid fa-highlighter"></i></span>
        <div>
          <span style="font-weight: 800; font-size: 0.9rem; color: var(--text-primary); display: block;">VỊ TRÍ ĐÁNH DẤU CHỈNH SỬA CÔNG CỤ (BIMSPEED REBAR & 2D BENDING):</span>
          <span style="font-size: 0.775rem; color: var(--text-muted);">Bấm vào từng nút bên dưới để nhảy trực tiếp đến vị trí cấu hình add-in dựng thép từng cấu kiện:</span>
        </div>
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <a href="#edit-bimspeed-mong" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> [1] BimSpeed Móng (02)</a>
        <a href="#edit-bimspeed-dakieng" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> [2] BimSpeed Đà Kiềng (03)</a>
        <a href="#edit-bimspeed-nen" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> [3] BimSpeed Nền Sàn (04)</a>
        <a href="#edit-bimspeed-cot" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> [4] BimSpeed Cột (05)</a>
        <a href="#edit-bimspeed-vach" class="jump-btn jump-btn-bimspeed"><i class="fa-solid fa-arrow-down"></i> [5] BimSpeed Vách (06)</a>
      </div>
    </div>

    <!-- SECTION 01: NGUYÊN TẮC JOIN ĐẦU TIÊN -->
    <section id="quy-tac-join" class="comp-box" style="scroll-margin-top: 90px;">
      <div class="section-header">
        <span class="section-tag">NGUYÊN TẮC BẮT BUỘC 01</span>
        <h2 class="section-title">01. Join Cấu Kiện Trước Khi Triển Khai Shop Rebar</h2>
        <p class="section-desc">
          Bắt buộc thực hiện Join toàn bộ mô hình kết cấu theo đúng quy ước để bê tông được khấu trừ chuẩn xác trước khi rải cốt thép:
        </p>
      </div>

      <div style="background: rgba(245, 158, 11, 0.08); border: 2px dashed var(--accent); border-radius: 14px; padding: 1.5rem; margin-bottom: 1rem;">
        <div style="font-size: 1.2rem; font-weight: 800; color: #fbbf24; display: flex; align-items: center; gap: 10px;">
          <i class="fa-solid fa-shield-halved"></i> QUY TẮC JOIN: SÀN &gt; MÓNG &gt; CỘT &gt; DẦM &gt; VÁCH &gt; CẦU THANG
        </div>
        <p style="font-size: 0.875rem; color: var(--text-secondary); margin-top: 6px;">
          Đảm bảo lớp bê tông bảo vệ (Concrete Cover) của cấu kiện ưu tiên không bị cắt lẹm, cốt thép được đặt chính xác vào vùng neo chịu lực.
        </p>
      </div>
    </section>

    <!-- SECTION 02 - 14: CÁC CẤU KIỆN SHOP DRAWING REBAR -->
    <section id="comp-section" style="scroll-margin-top: 90px;">
      <div class="section-header">
        <span class="section-tag">QUY TRÌNH TỪNG CẤU KIỆN</span>
        <h2 class="section-title">Hệ Thống Triển Khai Shop Drawing Từng Hạng Mục (02 &rarr; 14)</h2>
        <p class="section-desc">
          Chọn cấu kiện để xem chi tiết quy cách vẽ thép (BimSpeed), quy cách đặt tên Partition, View Template, Tag Rebar Bending Detail và bảng thống kê.
        </p>
      </div>

      <!-- Component Tabs -->
      <div class="comp-tabs" id="shopTabs">
        <button class="comp-tab-btn active" onclick="showShopTab('s02', this)"><i class="fa-solid fa-cubes-stacked"></i> 02. Móng</button>
        <button class="comp-tab-btn" onclick="showShopTab('s03', this)"><i class="fa-solid fa-grip-lines"></i> 03. Đà Kiềng</button>
        <button class="comp-tab-btn" onclick="showShopTab('s04', this)"><i class="fa-solid fa-border-all"></i> 04. Nền Xưởng</button>
        <button class="comp-tab-btn" onclick="showShopTab('s05', this)"><i class="fa-solid fa-monument"></i> 05. Cột</button>
        <button class="comp-tab-btn" onclick="showShopTab('s06', this)"><i class="fa-solid fa-table-columns"></i> 06. Vách</button>
        <button class="comp-tab-btn" onclick="showShopTab('s07', this)"><i class="fa-solid fa-bars"></i> 07. Dầm Tầng</button>
        <button class="comp-tab-btn" onclick="showShopTab('s08', this)"><i class="fa-solid fa-layer-group"></i> 08. Sàn Tầng</button>
        <button class="comp-tab-btn" onclick="showShopTab('s09', this)"><i class="fa-solid fa-stairs"></i> 09. Cầu Thang</button>
        <button class="comp-tab-btn" onclick="showShopTab('s11', this)"><i class="fa-solid fa-arrow-trend-up"></i> 11. Ramp</button>
      </div>

      <!-- TAB 02: MÓNG -->
      <div class="comp-box shop-panel" id="shop-s02">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-cubes-stacked" style="color: var(--accent);"></i> 02. Shop Drawing Cốt Thép Móng</h3>
          <span class="code-tag">VIEW TEMPLATE: BSV_02.1_Detail_Foudation</span>
        </div>

        <!-- Highlight BimSpeed -->
        <div class="tool-highlight" id="edit-bimspeed-mong" style="scroll-margin-top: 120px;">
          <span class="edit-marker marker-bimspeed"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 1: BIMSPEED - DỰNG THÉP MÓNG]</span>
          <div style="font-size: 0.9rem; color: var(--text-primary); margin-top: 4px;">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #34d399; font-weight: 700;">(Chạy tool Bimspeed vẽ móng)</code>: Móng đơn & các loại móng khác &rarr; Nhập lớp bê tông bảo vệ (btbv), vẽ lớp thép trên, lớp thép dưới, lớp giữa, cốt thép dọc, cốt thép ngang.
          </div>
          <div style="margin-top: 6px; font-size: 0.775rem; color: #34d399;">
            <i class="fa-solid fa-pen-to-square"></i> <em>Điểm chỉnh sửa: Cấu hình bảng thông số dựng thép móng hoặc đổi add-in rải thép móng tự động.</em>
          </div>
        </div>

        <div class="comp-grid">
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-tags"></i> Quy Cách Đặt Tên Thép</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <strong>Partition:</strong> Gán tên móng, VD: <span class="code-tag">F1</span>, <code>F2</code>...</li>
              <li><i class="fa-solid fa-check"></i> <strong>BSV_PhanLoai:</strong> <span class="code-tag">02.ThepMong_VP</span>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>BSV_SoCauKien:</strong> Số lượng đài móng cùng loại trong dự án.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-eye"></i> Quy Ước Thể Hiện Bản Vẽ</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <strong>Mặt bằng:</strong> Nhìn từ trên xuống, từ trái qua phải.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Section:</strong> <span class="code-tag">BSV_02_Sec_Foudation</span>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Kéo thép 2D:</strong> Công cụ <span class="tool-badge">Rebar bending detail</span> (tắt leader).</li>
              <li><i class="fa-solid fa-check"></i> <strong>Tag mặt bằng:</strong> <span class="code-tag">BSV_02.0_TagRebar_Fou_SL_D_a</span>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Mặt cắt:</strong> Dùng Multi-Rebar Annotation <span class="code-tag">BSV_02.2_TagRebar_Fou_Opendot_Sl_D_a</span>.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-table"></i> Bảng Thống Kê Thép Móng</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <strong>Tiêu đề:</strong> THỐNG KÊ THÉP MÓNG F1.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Các cột bắt buộc:</strong> Partitions (Số hiệu), Bending detail (Hình dạng thanh thép), Bar Diameter ($\Phi$), Quantities (SL), BSV_SoCauKien, Tổng chiều dài (mm), Tổng khối lượng (Kg).</li>
              <li><i class="fa-solid fa-check"></i> <strong>Key Plan:</strong> Gán View template <span class="code-tag">BSV_02_KP_Foudation</span>.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 03: ĐÀ KIỀNG -->
      <div class="comp-box shop-panel" id="shop-s03" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-grip-lines" style="color: var(--accent);"></i> 03. Shop Drawing Cốt Thép Đà Kiềng (Giằng Móng)</h3>
          <span class="code-tag">VIEW TEMPLATE: BSV_03.2_Detail_GroundBeam</span>
        </div>

        <!-- Highlight BimSpeed -->
        <div class="tool-highlight" id="edit-bimspeed-dakieng" style="scroll-margin-top: 120px;">
          <span class="edit-marker marker-bimspeed"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 2: BIMSPEED - DỰNG THÉP ĐÀ KIỀNG / DẦM]</span>
          <div style="font-size: 0.9rem; color: var(--text-primary); margin-top: 4px;">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #34d399; font-weight: 700;">(Chạy tool Bimspeed vẽ dầm)</code>: Theo mặt cắt chi tiết hoặc theo Spec &rarr; Nhập/kiểm tra lớp btbv, thép lớp dưới + tăng cường dưới, thép lớp trên + tăng cường trên, thép giá + thép đai.
          </div>
        </div>

        <div class="comp-grid">
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-ruler-horizontal"></i> Quy Tắc Nối Cắt & Đường Gióng</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <strong>Neo & Lap:</strong> Neo 40d, Lap 40d nối so le.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Thép tăng cường:</strong> Đoạn vươn $L/4$ nhịp.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Đường gióng nối cắt (Hidden line):</strong>
                <br>• Vùng nối thép trên: $L/4$ ở nhịp bụng.
                <br>• Vùng nối thép dưới: $L/6$ ở vùng gối dầm.
              </li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-scissors"></i> Kéo Bending Detail 2D</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Kéo thép chủ, tăng cường, thép giá, vai bò 2D từ trên xuống dưới.</li>
              <li><i class="fa-solid fa-check"></i> Thép chủ Bending detail: <span class="code-tag">BSV_03.4_Tag Rebar_Beam_Sl_D_L</span>.</li>
              <li><i class="fa-solid fa-check"></i> Thép đai, thép C Bending detail: <span class="code-tag">BSV_03.6_Tag Rebar_Beam_Sl_D_a_L</span>.</li>
              <li><i class="fa-solid fa-check"></i> Ghi chú Dim khoảng cách nối thép rõ ràng.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-table"></i> Viewport & Bảng Thống Kê</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <strong>Mặt cắt dọc:</strong> <code>BSV_Title_Large_Sec_Beam</code> &rarr; <code>[ B2a_(SL=2)_(L=12220) ]</code>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Mặt cắt ngang:</strong> <code>BSV_Title_Medium_Sec_Beam</code> &rarr; <code>[ MẶT CẮT 1-1 ]</code>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Key Plan:</strong> View template <span class="code-tag">BSV_03.1_KP_GroundBeam</span>.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 04: NỀN XƯỞNG -->
      <div class="comp-box shop-panel" id="shop-s04" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-border-all" style="color: var(--accent);"></i> 04. Shop Drawing Cốt Thép Nền Nhà Xưởng (Slab on Grade)</h3>
          <span class="code-tag">VIEW TEMPLATE: BSV_04.2_PlanSlabTop / Bot</span>
        </div>

        <!-- Highlight BimSpeed -->
        <div class="tool-highlight" id="edit-bimspeed-nen" style="scroll-margin-top: 120px;">
          <span class="edit-marker marker-bimspeed"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 3: BIMSPEED - DỰNG THÉP SÀN NỀN]</span>
          <div style="font-size: 0.9rem; color: var(--text-primary); margin-top: 4px;">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #34d399; font-weight: 700;">(Chạy tool Bimspeed vẽ sàn)</code>: Thép lớp trên + tăng cường trên, thép lớp dưới + tăng cường dưới. Công thức móc bẻ chân chó: <code>L1 = Chiều dày sàn - 2 lớp btbv</code>, <code>L2 = Chiều dày sàn - 2 lớp btbv</code>.
          </div>
        </div>

        <div class="comp-grid">
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Tách Mặt Bằng Lớp Trên / Dưới</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Mặt bằng thép lớp trên: <span class="code-tag">BSV_04.2_PlanSlabTop</span>.</li>
              <li><i class="fa-solid fa-check"></i> Mặt bằng thép lớp dưới: <span class="code-tag">BSV_04.3_PlanSlabBot</span>.</li>
              <li><i class="fa-solid fa-check"></i> Mặt cắt thép sàn: <span class="code-tag">BSV_04.4__Sec_Slab</span>.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-arrows-left-right"></i> Ký Hiệu Rải & Tag Thép</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <strong>Detail Component khoảng rải:</strong> Sử dụng family <span class="tool-badge">BSV_Symbol_RaiThep</span>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>Thép song song mặt cắt:</strong> <span class="code-tag">BSV_04.2_Tag Rebar_Slab_SL_D_a</span> (thể hiện leader).</li>
              <li><i class="fa-solid fa-check"></i> <strong>Thép vuông góc mặt cắt:</strong> <span class="code-tag">BSV_04.3_Tag Rebar_Slab_OpenDot_Sl_D_a</span>.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-table"></i> Quản Lý Partition & Bảng Biểu</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <strong>Partition:</strong> <span class="code-tag">Slab_Caodo_VP</span>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>BSV_PhanLoai:</strong> <span class="code-tag">04.ThepNen_VP</span>.</li>
              <li><i class="fa-solid fa-check"></i> Bảng thống kê thép Sàn Vp2 (Partitions, Bending detail, $\Phi$, SL, Chiều dài, Khối lượng).</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 05: CỘT -->
      <div class="comp-box shop-panel" id="shop-s05" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-monument" style="color: var(--accent);"></i> 05. Shop Drawing Cốt Thép Cột & Cổ Cột</h3>
          <span class="code-tag">VIEW TEMPLATE: BSV_05.2_Detail_Column</span>
        </div>

        <!-- Highlight BimSpeed -->
        <div class="tool-highlight" id="edit-bimspeed-cot" style="scroll-margin-top: 120px;">
          <span class="edit-marker marker-bimspeed"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 4: BIMSPEED - DỰNG THÉP CỘT]</span>
          <div style="font-size: 0.9rem; color: var(--text-primary); margin-top: 4px;">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #34d399; font-weight: 700;">(Chạy tool Bimspeed vẽ Cột)</code>: Hiệu chỉnh cốt thép theo phương cạnh x, y; tiết diện & loại đai, thép chờ móng, cài đặt cốt đai chính, cốt đai bổ sung, chiều dài neo và nối so le cột qua tầng.
          </div>
        </div>

        <div class="comp-grid">
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-up-down"></i> Mặt Cắt Dọc Cột</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Đoạn nối thép so le 40d theo Spec, tránh nối 100% tại 1 mặt cắt.</li>
              <li><i class="fa-solid fa-check"></i> Đai dày chân cột và đầu cột (khoảng cách $a100$), đai thường thân cột ($a200$).</li>
              <li><i class="fa-solid fa-check"></i> <strong>Kéo Bending Detail 2D:</strong> Kéo từ trái sang phải <span class="code-tag">BSV_05.3_TagRebar_Column_SL_2D</span>.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-circle-dot"></i> Mặt Cắt Ngang Cột</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Tag thép chủ: <span class="code-tag">BSV_05.4_Tag Rebar_Column_Sl_D</span>.</li>
              <li><i class="fa-solid fa-check"></i> Tag đai lồng kín, thép C: <span class="code-tag">BSV_05.2_TagRebarShear_Column_SL_D_a</span>.</li>
              <li><i class="fa-solid fa-check"></i> Kéo Bending detail đai: <span class="code-tag">BSV_05.4_TagRebar_Column_SL_D_a_L</span>.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-table"></i> Viewport & Key Plan</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Viewport: <code>BSV_Title_Large_Sec_Column</code> &rarr; <code>[ CHI TIẾT CỘT C5 ]</code>.</li>
              <li><i class="fa-solid fa-check"></i> Key Plan: <span class="code-tag">BSV_05.1_KP_Column</span>.</li>
              <li><i class="fa-solid fa-check"></i> Bảng thống kê thép Cột C5.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 06: VÁCH -->
      <div class="comp-box shop-panel" id="shop-s06" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-table-columns" style="color: var(--accent);"></i> 06. Shop Drawing Cốt Thép Vách Bê Tông</h3>
          <span class="code-tag">VIEW TEMPLATE: BSV_06.2_Detail_StrWall</span>
        </div>

        <!-- Highlight BimSpeed -->
        <div class="tool-highlight" id="edit-bimspeed-vach" style="scroll-margin-top: 120px;">
          <span class="edit-marker marker-bimspeed"><i class="fa-solid fa-highlighter"></i> [VỊ TRÍ 5: BIMSPEED - DỰNG THÉP VÁCH]</span>
          <div style="font-size: 0.9rem; color: var(--text-primary); margin-top: 4px;">
            <strong>Văn bản gốc:</strong> <code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #34d399; font-weight: 700;">(Chạy tool Bimspeed vẽ vách)</code>: Thép lớp dưới + tăng cường dưới, thép lớp trên + tăng cường trên, thép giá + thép đai C giằng 2 lớp thép vách.
          </div>
        </div>

        <div class="comp-grid">
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Quy Cách Thép Vách</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> <code>Partition: B1_Caodo_VP</code>, <code>BSV_PhanLoai: 06.ThepVach_VP</code>.</li>
              <li><i class="fa-solid fa-check"></i> Thép chủ neo 40d, lap 40d so le, tăng cường $L/4$.</li>
              <li><i class="fa-solid fa-check"></i> Thép đai C liên kết 2 lớp lưới thép vách.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-bezier-curve"></i> Kéo Bending Detail 2D Vách</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Thép chủ Bending detail: <span class="code-tag">BSV_06.2_Tag Rebar_StrWall_Sl_D_L</span>.</li>
              <li><i class="fa-solid fa-check"></i> Thép đai/C Bending detail: <span class="code-tag">BSV_06.3_Tag Reabar Shear_StrWall_Sl_D_a</span>.</li>
            </ul>
          </div>

          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-table"></i> Bảng Thống Kê Thép Vách</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Key Plan: <span class="code-tag">BSV_06.1_KP_StrWall</span>.</li>
              <li><i class="fa-solid fa-check"></i> Bảng thống kê khối lượng thép vách toàn dự án.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 07: DẦM TẦNG -->
      <div class="comp-box shop-panel" id="shop-s07" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-bars" style="color: var(--accent);"></i> 07. Shop Drawing Cốt Thép Dầm Tầng & Dầm Mái</h3>
          <span class="code-tag">QUY TRÌNH: TƯƠNG TỰ 03. ĐÀ KIỀNG</span>
        </div>
        <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
          Cốt thép Dầm các tầng lầu và dầm mái tuân thủ 100% theo quy cách của <strong>03. Đà Kiềng</strong>: Chạy BimSpeed vẽ dầm, neo 40d, lap 40d so le bụng (thép trên $L/4$) và gối (thép dưới $L/6$), kéo 2D Bending Detail từ trên xuống và quản lý qua View Template.
        </p>
      </div>

      <!-- TAB 08: SÀN TẦNG -->
      <div class="comp-box shop-panel" id="shop-s08" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-layer-group" style="color: var(--accent);"></i> 08. Shop Drawing Cốt Thép Sàn Tầng & Sàn Mái</h3>
          <span class="code-tag">QUY TRÌNH: TƯƠNG TỰ 04. NỀN</span>
        </div>
        <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
          Cốt thép Sàn các tầng lầu áp dụng quy cách của <strong>04. Nền</strong>: Chạy BimSpeed vẽ sàn, tách riêng Mặt bằng thép lớp trên (Top) và Mặt bằng thép lớp dưới (Bottom), dùng ký hiệu rải <code>BSV_Symbol_RaiThep</code> và MRA tag thép.
        </p>
      </div>

      <!-- TAB 09: CẦU THANG -->
      <div class="comp-box shop-panel" id="shop-s09" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-stairs" style="color: var(--accent);"></i> 09. Shop Drawing Cốt Thép Cầu Thang Bộ</h3>
          <span class="code-tag">VIEW TEMPLATE: BSV_09.1_Detail_Stair</span>
        </div>
        <div class="comp-grid">
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-bezier-curve"></i> Bố Trí Thép Bản Thang</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Dựng bằng công cụ Structure Rebar chuẩn.</li>
              <li><i class="fa-solid fa-check"></i> Thép lớp trên + tăng cường trên.</li>
              <li><i class="fa-solid fa-check"></i> Thép lớp dưới + tăng cường dưới, thép đai bẻ bậc thang.</li>
              <li><i class="fa-solid fa-check"></i> <code>Partition: Slab_Caodo_VP</code>, <code>BSV_PhanLoai: 09.ThepCauThang_VP</code>.</li>
            </ul>
          </div>
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-eye"></i> Kéo Bending Detail Thang</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Kéo thép chủ 2D Bending Detail từ trên xuống dưới.</li>
              <li><i class="fa-solid fa-check"></i> Tag Bending detail: <span class="code-tag">BSV_09.4_TagRebar_Stair_SL_D_a_L</span>.</li>
              <li><i class="fa-solid fa-check"></i> Mặt bằng cầu thang tầng 1-2: <span class="code-tag">BSV_09.1_Title_Large_Plan_Stair</span>.</li>
            </ul>
          </div>
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-table"></i> Thống Kê & 10. Tam Cấp</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Bảng thống kê thép Cầu thang (Số hiệu, hình dạng uốn, $\Phi$, SL, chiều dài, khối lượng).</li>
              <li><i class="fa-solid fa-check"></i> Key Plan: <span class="code-tag">BSV_09.1_KP_Stair</span>.</li>
              <li><i class="fa-solid fa-check"></i> <strong>10. Tam Cấp:</strong> Quy cách triển khai tương tự Cầu thang.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 11: RAMP -->
      <div class="comp-box shop-panel" id="shop-s11" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary);"><i class="fa-solid fa-arrow-trend-up" style="color: var(--accent);"></i> 11. Shop Drawing Cốt Thép Đường Dốc (Ramp)</h3>
          <span class="code-tag">VIEW TEMPLATE: BSV_11.2_PlanSlabTop</span>
        </div>
        <div class="comp-grid">
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Thép Ramp Dốc</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Thép lớp trên + tăng cường trên.</li>
              <li><i class="fa-solid fa-check"></i> Thép lớp dưới + tăng cường dưới theo độ dốc ramp.</li>
              <li><i class="fa-solid fa-check"></i> <code>Partition: Slab_Caodo_VP</code>, <code>BSV_PhanLoai: 11.ThepRamp_VP</code>.</li>
            </ul>
          </div>
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-bezier-curve"></i> Kéo Bending Detail Ramp</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Kéo thép chủ 2D Bending Detail từ trên xuống.</li>
              <li><i class="fa-solid fa-check"></i> Tag Bending detail: <span class="code-tag">BSV_11.4_TagRebar_Ramp_SL_D_a_L</span>.</li>
            </ul>
          </div>
          <div class="sub-panel">
            <div class="sub-panel-title"><i class="fa-solid fa-table"></i> 12. Pit, 13. Dock, 14. Phụ</div>
            <ul class="sub-list">
              <li><i class="fa-solid fa-check"></i> Bảng thống kê thép Ramp.</li>
              <li><i class="fa-solid fa-check"></i> <strong>12. Pit thang máy</strong> & <strong>13. Dock hàng</strong> & <strong>14. Cấu kiện phụ</strong>: Triển khai theo cấu tạo dầm sàn móng tương ứng.</li>
            </ul>
          </div>
        </div>
      </div>

    </section>

    <!-- SECTION: THƯ VIỆN BIỂU MẪU SHOP DRAWING -->
    <section id="schedules-shop" class="comp-box" style="scroll-margin-top: 90px;">
      <div class="section-header">
        <span class="section-tag">THƯ VIỆN BIỂU MẪU SHOP</span>
        <h2 class="section-title">Hệ Thống Biểu Mẫu Thống Kê & Chi Tiết Shop Rebar Mẫu</h2>
        <p class="section-desc">
          Trích xuất 35 hình ảnh bản vẽ chi tiết thép, bảng uốn Bending Detail 2D và khung tên bản vẽ thực tế. Nhấp vào từng ảnh để phóng to.
        </p>
      </div>

      <div class="sched-gallery">
        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_1.png', 'Mặt bằng thép móng & Bảng thống kê F1')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_1.png" alt="Móng Shop 1"></div>
          <div class="sched-info">
            <div class="sched-title">01. Mặt Bằng Thép Móng</div>
            <div class="sched-desc">Chi tiết bố trí thép đài F1</div>
          </div>
        </div>

        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_4.png', 'Mặt cắt dọc & Bending Detail Dầm Đà Kiềng')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_4.png" alt="Dầm Shop 4"></div>
          <div class="sched-info">
            <div class="sched-title">02. Bending Detail Dầm B2</div>
            <div class="sched-desc">Kéo hình dạng thép chủ & đai 2D</div>
          </div>
        </div>

        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_7.png', 'Mặt bằng thép sàn lớp trên & dưới')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_7.png" alt="Sàn Shop 7"></div>
          <div class="sched-info">
            <div class="sched-title">03. Thép Sàn Nền (Top & Bot)</div>
            <div class="sched-desc">Ký hiệu khoảng rải BSV_Symbol_RaiThep</div>
          </div>
        </div>

        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_9.png', 'Chi tiết thép Cột C5 & Đai lồng')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_9.png" alt="Cột Shop 9"></div>
          <div class="sched-info">
            <div class="sched-title">04. Chi Tiết Thép Cột C5</div>
            <div class="sched-desc">Nối so le & đai lồng kín</div>
          </div>
        </div>

        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_12.png', 'Mặt cắt thép Vách bể & Vách hầm')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_12.png" alt="Vách Shop 12"></div>
          <div class="sched-info">
            <div class="sched-title">05. Thép Vách Bê Tông</div>
            <div class="sched-desc">Thép 2 lớp & đai C liên kết</div>
          </div>
        </div>

        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_13.png', 'Mặt cắt chi tiết thép Cầu Thang')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_13.png" alt="Thang Shop 13"></div>
          <div class="sched-info">
            <div class="sched-title">06. Thép Cầu Thang Bộ</div>
            <div class="sched-desc">Bending detail thép bản & bậc thang</div>
          </div>
        </div>

        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_16.png', 'Bảng thống kê thép Dầm B2')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_16.png" alt="Thống kê Dầm 16"></div>
          <div class="sched-info">
            <div class="sched-title">07. Thống Kê Thép Dầm</div>
            <div class="sched-desc">Hình dạng uốn, đường kính, trọng lượng</div>
          </div>
        </div>

        <div class="sched-card" onclick="openModal('assets/bsv_shop/shop_img_25.png', 'Bảng thống kê thép Cột C5')">
          <div class="sched-img-box"><img src="assets/bsv_shop/shop_img_25.png" alt="Thống kê Cột 25"></div>
          <div class="sched-info">
            <div class="sched-title">08. Thống Kê Thép Cột</div>
            <div class="sched-desc">Partitions, thanh uốn, chiều dài mm</div>
          </div>
        </div>
      </div>
    </section>

    <!-- MINDMAP FULL CANVAS BANNER -->
    <div class="mindmap-banner" id="mindmap-shop">
      <div>
        <h3 style="font-size: 1.35rem; font-weight: 800; margin-bottom: 0.5rem;"><i class="fa-solid fa-diagram-project" style="color: var(--accent);"></i> Bản Đồ Tư Duy Gốc SHOP DRAWING REBAR (Full Canvas)</h3>
        <p style="font-size: 0.9rem; color: var(--text-secondary);">
          Xem bản vẽ đồ họa gốc siêu nét độ phân giải cực lớn <strong>6448 x 25779 px</strong> bao quát toàn bộ 14 hạng mục cấu kiện và hướng dẫn chi tiết từng công cụ.
        </p>
      </div>
      <button class="btn btn-primary" onclick="openModal('assets/bsv_shop/bsv_shop_rebar_full.png', 'SHOP DRAWING REBAR - Bản đồ tư duy gốc siêu nét')" style="padding: 12px 24px; font-weight: 700; white-space: nowrap;">
        <i class="fa-solid fa-expand"></i> Mở Mindmap Gốc Full
      </button>
    </div>

    <!-- Footer -->
    <footer>
      <p>&copy; 2026 BIM Management Platform • Bộ môn Shop Drawing Cốt Thép (BSV_SHOP DRAWING REBAR)</p>
      <p style="margin-top: 4px; font-size: 0.775rem;">Được số hóa từ tài liệu kỹ thuật <code>SHOP DRAWING REBAR.pdf</code> phục vụ công tác chuẩn hóa thi công.</p>
    </footer>

  </div>

  <!-- Lightbox Image Modal -->
  <div class="image-modal" id="imageModal" onclick="closeModal()">
    <div class="modal-content-box" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeModal()">&times;</button>
      <img id="modalImg" src="" alt="Schedule Preview">
      <div class="modal-caption" id="modalCaption"></div>
    </div>
  </div>

  <script>
    // Theme Toggle
    function toggleTheme() {
      const html = document.documentElement;
      const currentTheme = html.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('bim_theme_preference', newTheme);
      updateThemeIcon(newTheme);
    }

    function updateThemeIcon(theme) {
      const icon = document.getElementById('themeIcon');
      if (icon) {
        icon.className = theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
      }
    }

    // Shop Component Tab Switching
    function showShopTab(tabId, btn) {
      document.querySelectorAll('.comp-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.shop-panel').forEach(p => p.style.display = 'none');

      if (btn) btn.classList.add('active');
      const targetPanel = document.getElementById('shop-' + tabId);
      if (targetPanel) {
        targetPanel.style.display = 'block';
      }
    }

    // Image Modal Lightbox
    function openModal(imgSrc, caption) {
      const modal = document.getElementById('imageModal');
      const modalImg = document.getElementById('modalImg');
      const modalCap = document.getElementById('modalCaption');
      modalImg.src = imgSrc;
      modalCap.innerText = caption || '';
      modal.classList.add('active');
    }

    function closeModal() {
      const modal = document.getElementById('imageModal');
      modal.classList.remove('active');
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });

    // Load Theme Preference
    window.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('bim_theme_preference') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);
    });
  </script>
</body>
</html>
"""

with open('BSV_ShopDrawingRebar.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created BSV_ShopDrawingRebar.html successfully!")
