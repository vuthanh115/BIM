import sys

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BSV_KẾT CẤU (Ver 2) - Quy Trình Chuẩn Hóa Dựng Hình & Bóc Tách Khối Lượng BIM Kết Cấu</title>
  
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
      background: linear-gradient(135deg, #0284c7, #2563eb);
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
      color: var(--primary);
      background: var(--primary-glow);
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
      background: linear-gradient(135deg, var(--primary), #2563eb);
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

    .theme-toggle-btn:hover {
      border-color: var(--accent);
      transform: rotate(15deg);
    }

    /* Container */
    .main-container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 2.5rem 2rem 5rem 2rem;
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.08), rgba(37, 99, 235, 0.04));
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 2.5rem;
      margin-bottom: 3rem;
      position: relative;
      overflow: hidden;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--primary-glow);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }

    .hero-title {
      font-size: 2.4rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 0.75rem;
      line-height: 1.25;
    }

    .hero-title span {
      background: linear-gradient(135deg, var(--primary), #60a5fa);
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
      color: var(--primary);
    }

    /* Section Headers */
    .section-header {
      margin-bottom: 2rem;
    }

    .section-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      color: var(--primary);
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

    /* Priority Chain Card */
    .priority-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 2rem;
      margin-bottom: 3.5rem;
      box-shadow: var(--box-shadow);
    }

    .priority-chain {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin: 1.5rem 0 2rem 0;
      overflow-x: auto;
      padding-bottom: 10px;
    }

    .chain-node {
      background: var(--bg-surface);
      border: 2px solid var(--border-color);
      border-radius: 14px;
      padding: 1rem 1.4rem;
      text-align: center;
      min-width: 140px;
      flex-shrink: 0;
      transition: all 0.25s ease;
      cursor: default;
    }

    .chain-node:hover {
      border-color: var(--primary);
      transform: translateY(-3px);
      box-shadow: 0 8px 20px var(--primary-glow);
    }

    .chain-node.rank-1 { border-color: #38bdf8; background: rgba(56, 189, 248, 0.08); }
    .chain-node.rank-2 { border-color: #3b82f6; }
    .chain-node.rank-3 { border-color: #6366f1; }
    .chain-node.rank-4 { border-color: #a855f7; }
    .chain-node.rank-5 { border-color: #ec4899; }
    .chain-node.rank-6 { border-color: #f59e0b; }

    .chain-rank {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
    }

    .chain-title {
      font-size: 1.15rem;
      font-weight: 800;
      margin: 4px 0;
    }

    .chain-rule {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .chain-arrow {
      font-size: 1.3rem;
      color: var(--text-muted);
      flex-shrink: 0;
    }

    .tool-callout {
      background: rgba(56, 189, 248, 0.07);
      border-left: 4px solid var(--primary);
      border-radius: 0 10px 10px 0;
      padding: 1rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 15px;
      font-size: 0.9rem;
    }

    .tool-badge {
      background: var(--primary);
      color: #000;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
    }

    /* Rules Table */
    .rules-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1.5rem;
      font-size: 0.9rem;
    }

    .rules-table th {
      background: var(--bg-surface);
      color: var(--text-primary);
      padding: 12px 16px;
      text-align: left;
      border: 1px solid var(--border-color);
      font-weight: 700;
    }

    .rules-table td {
      padding: 12px 16px;
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
    }

    .rules-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    .badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }

    .badge-cyan { background: var(--primary-glow); color: var(--primary); border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-amber { background: var(--accent-glow); color: var(--accent); border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-green { background: var(--success-glow); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-rose { background: var(--danger-glow); color: var(--danger); border: 1px solid rgba(244, 63, 94, 0.3); }

    /* 7-Step Workflow */
    .workflow-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
      margin-bottom: 3.5rem;
    }

    .wf-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.4rem;
      position: relative;
      transition: all 0.25s ease;
    }

    .wf-card:hover {
      border-color: var(--primary);
      transform: translateY(-2px);
    }

    .wf-num {
      position: absolute;
      top: 1.2rem;
      right: 1.2rem;
      font-size: 2rem;
      font-weight: 900;
      font-family: 'JetBrains Mono', monospace;
      color: rgba(255, 255, 255, 0.05);
      line-height: 1;
    }

    .wf-title {
      font-size: 1.05rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .wf-desc {
      font-size: 0.85rem;
      color: var(--text-secondary);
      line-height: 1.6;
    }

    .wf-warning {
      margin-top: 0.75rem;
      padding: 8px 12px;
      border-radius: 8px;
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.25);
      color: var(--accent);
      font-size: 0.775rem;
      font-weight: 600;
    }

    /* Component Tabs & Cards */
    .comp-container {
      margin-bottom: 4rem;
    }

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
      border-color: var(--primary);
      color: var(--text-primary);
    }

    .comp-tab-btn.active {
      background: var(--primary);
      color: #000;
      border-color: var(--primary);
    }

    .comp-detail-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 2.25rem;
      box-shadow: var(--box-shadow);
    }

    .comp-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 1.25rem;
      margin-bottom: 1.5rem;
    }

    .comp-header-left h3 {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .comp-header-left p {
      font-size: 0.875rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .comp-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }

    .sub-panel {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.4rem;
    }

    .sub-panel-title {
      font-size: 0.95rem;
      font-weight: 800;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text-primary);
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
      color: var(--primary);
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
      color: var(--primary);
      cursor: pointer;
    }

    .code-tag:hover {
      background: var(--primary);
      color: #000;
    }

    /* Schedules Gallery */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
      margin-bottom: 3.5rem;
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
      border-color: var(--primary);
      transform: translateY(-3px);
      box-shadow: 0 10px 25px var(--primary-glow);
    }

    .sched-img-box {
      height: 220px;
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

    .sched-zoom-hint {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      color: #fff;
      font-size: 0.75rem;
      padding: 4px 8px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .sched-info {
      padding: 1rem;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
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

    /* Mindmap Full Canvas Preview */
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

    .mindmap-text h3 {
      font-size: 1.35rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
    }

    .mindmap-text p {
      font-size: 0.9rem;
      color: var(--text-secondary);
      max-width: 680px;
    }

    .mindmap-preview-btn {
      padding: 12px 24px;
      font-size: 0.95rem;
      font-weight: 700;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--primary), #2563eb);
      color: #fff;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 0 20px var(--primary-glow);
      white-space: nowrap;
    }

    .mindmap-preview-btn:hover {
      opacity: 0.95;
      transform: translateY(-1px);
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
      .gallery-grid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 768px) {
      .navbar { padding: 0.8rem 1.25rem; }
      .nav-links { display: none; }
      .hero-title { font-size: 1.8rem; }
      .hero-meta-grid { grid-template-columns: 1fr; }
      .gallery-grid { grid-template-columns: 1fr; }
      .mindmap-banner { flex-direction: column; align-items: flex-start; }
    }

    @media print {
      .navbar, .theme-toggle-btn, .nav-actions, .mindmap-preview-btn, .image-modal { display: none !important; }
      body { background: white !important; color: black !important; }
      .hero-banner, .priority-card, .wf-card, .comp-detail-box { border: 1px solid #ccc !important; box-shadow: none !important; background: white !important; }
    }
  </style>
</head>
<body>

  <!-- Sticky Top Navbar -->
  <nav class="navbar">
    <a href="index.html" class="brand" title="Quay lại Trang chủ BIM Management Platform">
      <div class="brand-badge"><i class="fa-solid fa-cube"></i> BIM KC</div>
      <div class="brand-text">
        <h1>BSV_KẾT CẤU (VER 2)</h1>
        <p>Quy Trình Chuẩn Hóa Dựng Hình & Bóc Tách Khối Lượng</p>
      </div>
    </a>

    <ul class="nav-links">
      <li><a href="#thu-tu-tinh"><i class="fa-solid fa-layer-group"></i> 1. Ưu Tiên QS</a></li>
      <li><a href="#quy-trinh-7-buoc"><i class="fa-solid fa-list-check"></i> 2. Gán Biến BOQ</a></li>
      <li><a href="#14-cau-kien"><i class="fa-solid fa-sitemap"></i> 3. 14 Cấu Kiện</a></li>
      <li><a href="#bang-thong-ke"><i class="fa-solid fa-table-cells"></i> 4. Bảng Thống Kê</a></li>
      <li><a href="#mindmap-view"><i class="fa-solid fa-diagram-project"></i> 5. Sơ Đồ Gốc</a></li>
    </ul>

    <div class="nav-actions">
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" title="Chuyển chế độ Sáng / Tối">
        <i class="fa-solid fa-sun" id="themeIcon"></i>
      </button>
      <a href="index.html" class="btn btn-outline"><i class="fa-solid fa-arrow-left"></i> Về Portal BIM</a>
      <button class="btn btn-primary" onclick="window.print()"><i class="fa-solid fa-print"></i> In Sổ Tay</button>
    </div>
  </nav>

  <div class="main-container">

    <!-- Hero Banner -->
    <header class="hero-banner">
      <div class="hero-badge"><i class="fa-solid fa-book-bookmark"></i> Standard Operating Procedure (SOP) • Revit Structure</div>
      <h1 class="hero-title">SỔ TAY QUY TRÌNH <span>BSV_KẾT CẤU (VER 2)</span></h1>
      <p class="hero-subtitle">
        Chuẩn hóa toàn diện quy tắc mô hình hóa, gán biến tham số dự án (Project Parameters), liên kết dữ liệu với bộ phận Dự toán (QS/BOQ), tự động hóa tính ván khuôn – bê tông – cốt thép và triệt tiêu sai số trong suốt vòng đời dự án.
      </p>

      <div class="hero-meta-grid">
        <div class="meta-box">
          <div class="meta-label">Chuẩn Ưu Tiên Join</div>
          <div class="meta-val"><i class="fa-solid fa-arrows-split-up-and-left"></i> Sàn > Móng > Cột...</div>
        </div>
        <div class="meta-box">
          <div class="meta-label">Bộ Công Cụ Add-in</div>
          <div class="meta-val"><i class="fa-solid fa-screwdriver-wrench"></i> Atool, BimSpeed...</div>
        </div>
        <div class="meta-box">
          <div class="meta-label">Cấu Kiện Chuẩn Hóa</div>
          <div class="meta-val"><i class="fa-solid fa-cubes"></i> 14 Hạng Mục Cốt Lõi</div>
        </div>
        <div class="meta-box">
          <div class="meta-label">Khối Lượng Tự Động</div>
          <div class="meta-val"><i class="fa-solid fa-chart-pie"></i> Bê tông, Ván khuôn, Diện tích</div>
        </div>
      </div>
    </header>

    <!-- SECTION A: THỨ TỰ ƯU TIÊN TÍNH TOÁN -->
    <section id="thu-tu-tinh" style="scroll-margin-top: 90px; margin-bottom: 3.5rem;">
      <div class="section-header">
        <span class="section-tag">PHẦN A</span>
        <h2 class="section-title">Thứ Tự Ưu Tiên Tính Toán & Quy Ước Khấu Trừ Với QS</h2>
        <p class="section-desc">
          Thứ tự ưu tiên cắt giao giữa các cấu kiện chịu lực nhằm bảo đảm khối lượng bóc tách từ mô hình Revit trùng khớp 100% với nguyên tắc lập dự toán của QS.
        </p>
      </div>

      <div class="priority-card">
        <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--text-primary);">
          <i class="fa-solid fa-arrow-down-wide-short" style="color: var(--primary);"></i> Chuỗi Ưu Tiên Join Cấu Kiện:
        </div>

        <div class="priority-chain">
          <div class="chain-node rank-1">
            <div class="chain-rank">Ưu tiên 1</div>
            <div class="chain-title">SÀN / NỀN</div>
            <div class="chain-rule">Tính Full diện tích</div>
          </div>
          <div class="chain-arrow"><i class="fa-solid fa-chevron-right"></i></div>

          <div class="chain-node rank-2">
            <div class="chain-rank">Ưu tiên 2</div>
            <div class="chain-title">MÓNG</div>
            <div class="chain-rule">Trừ phần giao Sàn</div>
          </div>
          <div class="chain-arrow"><i class="fa-solid fa-chevron-right"></i></div>

          <div class="chain-node rank-3">
            <div class="chain-rank">Ưu tiên 3</div>
            <div class="chain-title">CỘT</div>
            <div class="chain-rule">Trừ phần giao Sàn</div>
          </div>
          <div class="chain-arrow"><i class="fa-solid fa-chevron-right"></i></div>

          <div class="chain-node rank-4">
            <div class="chain-rank">Ưu tiên 4</div>
            <div class="chain-title">DẦM</div>
            <div class="chain-rule">Trừ Sàn, Móng, Cột</div>
          </div>
          <div class="chain-arrow"><i class="fa-solid fa-chevron-right"></i></div>

          <div class="chain-node rank-5">
            <div class="chain-rank">Ưu tiên 5</div>
            <div class="chain-title">VÁCH</div>
            <div class="chain-rule">Trừ Sàn, Móng, Cột, Dầm</div>
          </div>
          <div class="chain-arrow"><i class="fa-solid fa-chevron-right"></i></div>

          <div class="chain-node rank-6">
            <div class="chain-rank">Ưu tiên 6</div>
            <div class="chain-title">CẦU THANG</div>
            <div class="chain-rule">Trừ hết cấu kiện trên</div>
          </div>
        </div>

        <div class="tool-callout">
          <div>
            <strong><i class="fa-solid fa-robot"></i> Tự động hóa xử lý:</strong> Sử dụng add-in <span class="tool-badge">Atool</span> để nạp chuỗi quy ước trên và tự động Join hàng loạt cấu kiện 3D trong Revit mà không cần join thủ công.
          </div>
          <div>
            <span class="badge badge-amber"><i class="fa-solid fa-triangle-exclamation"></i> Chú ý khe cô lập</span> để tách riêng dầm và cột khỏi sàn chống lún.
          </div>
        </div>

        <!-- Detail table -->
        <table class="rules-table">
          <thead>
            <tr>
              <th style="width: 22%;">Cấu kiện</th>
              <th style="width: 20%;">Nguyên tắc tính</th>
              <th>Quy tắc khấu trừ chi tiết</th>
              <th style="width: 25%;">Lưu ý kỹ thuật</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Nền & Sàn</strong></td>
              <td><span class="badge badge-cyan">Full 100% diện tích</span></td>
              <td>Tính trọn vẹn khối tích sàn, không bị trừ bởi các cấu kiện khác đâm xuyên.</td>
              <td>Phân biệt rõ vùng có khe cô lập (Isolation joint) quanh cổ cột và móng máy.</td>
            </tr>
            <tr>
              <td><strong>Móng (Đài & Giằng)</strong></td>
              <td><span class="badge badge-green">Tính đủ</span></td>
              <td>Chỉ trừ phần bê tông giao cắt với bản sàn tầng trệt (nếu có).</td>
              <td>Phần dầm móng (đà kiềng) giao với đài móng sẽ được tính theo cấp ưu tiên.</td>
            </tr>
            <tr>
              <td><strong>Cột & Cổ cột</strong></td>
              <td><span class="badge badge-green">Tính đủ</span></td>
              <td>Tính từ đỉnh móng tới đáy dầm sàn, trừ phần giao sàn tầng.</td>
              <td>Cổ cột có khe cô lập sàn được tính thẳng lên tới mặt trên hoàn thiện của sàn.</td>
            </tr>
            <tr>
              <td><strong>Dầm (Beam)</strong></td>
              <td><span class="badge badge-amber">Trừ giao cắt</span></td>
              <td>Khối lượng bê tông dầm trừ phần giao với Sàn, Móng và Cột.</td>
              <td><strong>Ván khuôn:</strong> Ván đáy dầm tính gộp vào Ván khuôn Sàn; ván 2 bên hông tính cho Dầm.</td>
            </tr>
            <tr>
              <td><strong>Vách (Wall)</strong></td>
              <td><span class="badge badge-amber">Trừ giao cắt</span></td>
              <td>Trừ toàn bộ phần giao nhau với Sàn, Móng, Cột và Dầm.</td>
              <td>Vách bê tông chịu lực tầng hầm cần gắn tham số trám lỗ ti xuyên vách <span class="code-tag">BSV_LoTi</span>.</td>
            </tr>
            <tr>
              <td><strong>Cầu thang (Stair)</strong></td>
              <td><span class="badge badge-rose">Trừ tất cả</span></td>
              <td>Bị trừ bởi toàn bộ các cấu kiện kết cấu nêu trên.</td>
              <td>Mô hình dạng <em>Model-in-place (Structural Framing)</em>; thép thang tính kiểm tra bằng bảng tính Excel.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION B: 7 BƯỚC QUY TRÌNH GÁN BIẾN & ĐỐI CHIẾU BOQ -->
    <section id="quy-trinh-7-buoc" style="scroll-margin-top: 90px; margin-bottom: 3.5rem;">
      <div class="section-header">
        <span class="section-tag">PHẦN B</span>
        <h2 class="section-title">Quy Trình 7 Bước Chuẩn Hóa Gán Biến & Đối Chiếu BOQ</h2>
        <p class="section-desc">
          Các bước bắt buộc kỹ sư BIM phải thực hiện tuần tự để kiểm soát dữ liệu đầu vào, chạy ván khuôn tự động và liên kết chính xác với bảng dự toán BOQ.
        </p>
      </div>

      <div class="workflow-grid">
        <div class="wf-card">
          <div class="wf-num">01</div>
          <div class="wf-title"><i class="fa-solid fa-tags" style="color: var(--primary);"></i> Gán Biến Bê Tông Theo BOQ</div>
          <div class="wf-desc">
            Nhập tham số <span class="code-tag">Comments</span> và <span class="code-tag">BSV_PhanLoai</span> phân tách theo từng phân khu / tầng (VD: <code>02.Mong-PK1</code>, <code>05.1.CoCot</code>).
          </div>
          <div class="wf-warning"><i class="fa-solid fa-triangle-exclamation"></i> Gán thật kỹ biến bê tông trước khi chạy ván khuôn!</div>
        </div>

        <div class="wf-card">
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
        </div>

        <div class="wf-card">
          <div class="wf-num">04</div>
          <div class="wf-title"><i class="fa-solid fa-shield-halved" style="color: var(--primary);"></i> Kiểm Tra Trùng Lặp Cấu Kiện</div>
          <div class="wf-desc">
            Chạy tool <strong>BSV_KiemTraTrungNhau</strong> để phát hiện các đối tượng ván khuôn hoặc bê tông bị vẽ đè lên nhau, xem xét xóa bỏ phần dư thừa.
          </div>
        </div>

        <div class="wf-card">
          <div class="wf-num">05</div>
          <div class="wf-title"><i class="fa-solid fa-file-excel" style="color: var(--primary);"></i> Đối Chiếu Model 3D & Xuất Excel</div>
          <div class="wf-desc">
            Mở đồng thời bảng thống kê (Revit Schedules) và khung nhìn 3D để highlight đối chiếu số lượng, sau đó xuất bảng tính ra định dạng Excel chuẩn.
          </div>
        </div>

        <div class="wf-card">
          <div class="wf-num">06</div>
          <div class="wf-title"><i class="fa-solid fa-link" style="color: var(--primary);"></i> Link Khối Lượng Vào BOQ</div>
          <div class="wf-desc">
            Liên kết trực tiếp các cell khối lượng từ file xuất Revit vào bảng BOQ dự toán của dự án.
          </div>
          <div class="wf-warning"><i class="fa-solid fa-ban"></i> Tuyệt đối không cộng trừ thủ công trong bảng để tránh sai lệch khi cập nhật!</div>
        </div>

        <div class="wf-card" style="grid-column: 1 / -1;">
          <div class="wf-num">07</div>
          <div class="wf-title"><i class="fa-solid fa-calculator" style="color: var(--primary);"></i> Sum Tổng Khối Lượng Đối Soát Hai Chiều</div>
          <div class="wf-desc">
            Thực hiện hàm Sum kiểm tra tổng khối lượng: <strong>Bê tông lót, ván khuôn lót, bê tông chính, ván khuôn thành, thép...</strong> giữa số liệu nhập vào từ bản vẽ thiết kế với số liệu đo bóc tự động trên máy tính. Đặt mã code phân loại đồng nhất để dễ dàng lọc và lọc chéo khi kiểm toán.
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION C: 14 CẤU KIỆN KẾT CẤU (WBS 01 -> 14) -->
    <section id="14-cau-kien" class="comp-container" style="scroll-margin-top: 90px;">
      <div class="section-header">
        <span class="section-tag">PHẦN C</span>
        <h2 class="section-title">Hệ Thống 14 Hạng Mục Cấu Kiện Kết Cấu Chi Tiết</h2>
        <p class="section-desc">
          Quy định chi tiết cho từng cấu kiện: Quy ước đặt tên Type, mác bê tông, bóc tách cốt thép, phân loại ván khuôn và công cụ add-in thực hiện.
        </p>
      </div>

      <!-- Component Navigation Tabs -->
      <div class="comp-tabs" id="compTabs">
        <button class="comp-tab-btn active" onclick="showComponent('c01', this)"><i class="fa-solid fa-bore-hole"></i> 01. Cọc</button>
        <button class="comp-tab-btn" onclick="showComponent('c02', this)"><i class="fa-solid fa-cubes-stacked"></i> 02. Móng</button>
        <button class="comp-tab-btn" onclick="showComponent('c03', this)"><i class="fa-solid fa-grip-lines"></i> 03. Đà Kiềng</button>
        <button class="comp-tab-btn" onclick="showComponent('c04', this)"><i class="fa-solid fa-border-all"></i> 04. Nền</button>
        <button class="comp-tab-btn" onclick="showComponent('c05', this)"><i class="fa-solid fa-monument"></i> 05. Cột & Cổ Cột</button>
        <button class="comp-tab-btn" onclick="showComponent('c06', this)"><i class="fa-solid fa-table-columns"></i> 06. Vách</button>
        <button class="comp-tab-btn" onclick="showComponent('c07', this)"><i class="fa-solid fa-bars"></i> 07. Dầm</button>
        <button class="comp-tab-btn" onclick="showComponent('c08', this)"><i class="fa-solid fa-layer-group"></i> 08. Sàn</button>
        <button class="comp-tab-btn" onclick="showComponent('c09', this)"><i class="fa-solid fa-stairs"></i> 09. Cầu Thang</button>
        <button class="comp-tab-btn" onclick="showComponent('c10', this)"><i class="fa-solid fa-ellipsis"></i> 10. Tam Cấp</button>
        <button class="comp-tab-btn" onclick="showComponent('c11', this)"><i class="fa-solid fa-arrow-trend-up"></i> 11. Ramp</button>
        <button class="comp-tab-btn" onclick="showComponent('c12', this)"><i class="fa-solid fa-box-archive"></i> 12. Pit Thang Máy</button>
        <button class="comp-tab-btn" onclick="showComponent('c13', this)"><i class="fa-solid fa-truck-ramp-box"></i> 13. Dock Hàng</button>
        <button class="comp-tab-btn" onclick="showComponent('c14', this)"><i class="fa-solid fa-wrench"></i> 14. Cấu Kiện Phụ</button>
      </div>

      <!-- COMPONENT PANELS CONTAINER -->
      <div id="compPanels">

        <!-- 01. COC -->
        <div class="comp-detail-box" id="panel-c01">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-bore-hole" style="color: var(--primary);"></i> 01. Cọc Ly Tâm & Xử Lý Đầu Cọc</h3>
              <p>Mô hình hóa hệ thống cọc ép/khoan nhồi, tính toán cắt đầu cọc và chiều sâu ép âm</p>
            </div>
            <span class="badge badge-cyan">SCHEDULE: 01.1.CỌC</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-calculator"></i> Phân loại & Số lượng</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Tổng số cọc:</strong> Thống kê tự động từ mô hình 3D.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Cọc đại trà:</strong> <code>Cọc đại trà = (Tổng số cọc - Số cọc thí nghiệm)</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Cọc thí nghiệm:</strong> Gán biến <span class="code-tag">BSV_CocThiNghiem</span>, <span class="code-tag">BSV_TaiCocToiDa</span>.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-scissors"></i> Xử lý & Cắt đầu cọc</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Đập đầu cọc:</strong> Theo bản vẽ chi tiết ngàm cốt thép vào đài móng.</li>
                <li><i class="fa-solid fa-check"></i> <strong>TH1 (Cos tự nhiên > Cos san lấp):</strong><br><code>Chiều sâu = Cos san lấp - Cos đầu cọc</code></li>
                <li><i class="fa-solid fa-check"></i> <strong>TH2 (Cos tự nhiên < Cos san lấp):</strong><br><code>Chiều sâu = Cos tự nhiên - Cos đầu cọc</code> (Chỉ tính âm).</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-screwdriver-wrench"></i> Ép âm & Add-in Tool</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Chạy Tool tự động: <span class="tool-badge">BSV_EpAm</span>.</li>
                <li><i class="fa-solid fa-check"></i> Gán dữ liệu vào parameter: <span class="code-tag">BSV_CaoDoEpAm</span>.</li>
                <li><i class="fa-solid fa-check"></i> Đưa vào bảng khối lượng cọc để đối chiếu chiều sâu ép thực tế.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 02. MONG -->
        <div class="comp-detail-box" id="panel-c02" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-cubes-stacked" style="color: var(--primary);"></i> 02. Đài Móng & Bê Tông Lót</h3>
              <p>Móng đơn, móng băng, móng vát và các lớp lót đầm chặt đáy móng</p>
            </div>
            <span class="badge badge-green">SCHEDULE: 00.1.2.KL BÊ TÔNG</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Móng & BTL</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Bê tông móng (B25):</strong> Gán <code>Comments: 02.Mong</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Bê tông lót móng (B7.5):</strong> Chiều dày <code>h = 100mm</code>, độ mở rộng <code>a = 100mm</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Diện tích đầm chặt:</strong> <code>DT = Thể tích BTL / Chiều dày lót</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Tính sửa đất:</strong> Khối lượng sửa thủ công đáy hố móng.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-bars-staggered"></i> Cốt Thép Móng</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Thép theo mặt cắt thiết kế (thép lớp dưới, lớp trên nếu đài dày).</li>
                <li><i class="fa-solid fa-check"></i> Thép đai giằng liên kết cổ móng.</li>
                <li><i class="fa-solid fa-check"></i> Chiều dài bẻ móc neo và đoạn lap nối theo quy chuẩn kết cấu.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn & Phân loại</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn lót:</strong> <span class="code-tag">BSV_PhanLoai: VK_LotMong</span> (không tính phần giao sàn/đà).</li>
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn móng:</strong> <span class="code-tag">BSV_PhanLoai: VK_Mong</span>.</li>
                <li><i class="fa-solid fa-check"></i> Phân biệt móng có thành (móng thường) vs không thành (móng vát ngược).</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 03. DA KIENG -->
        <div class="comp-detail-box" id="panel-c03" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-grip-lines" style="color: var(--primary);"></i> 03. Đà Kiềng (Giằng Móng)</h3>
              <p>Dầm giằng móng BTCT liên kết các đài cọc và chân cột</p>
            </div>
            <span class="badge badge-amber">SCHEDULE: 00.2.2.KL VÁN KHUÔN</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông & Quy ước Type</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Quy ước đặt Type:</strong> <code>Rộng x Cao</code> (Ví dụ: <code>300x500</code>).</li>
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 03.DaKieng</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Bê tông lót đà kiềng (B7.5):</strong> Chiều dày h, độ mở rộng a.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Đầm chặt:</strong> Gán biến <span class="code-tag">BSV_PhanLoai: DT_DamChat</span>.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-bars-staggered"></i> Cốt thép Đà Kiềng</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Thép lớp trên + tăng cường gối.</li>
                <li><i class="fa-solid fa-check"></i> Thép lớp dưới + tăng cường bụng.</li>
                <li><i class="fa-solid fa-check"></i> Thép đai, thép giá, thép vai bò (nếu có).</li>
                <li><i class="fa-solid fa-check"></i> Đọc kỹ spec kết cấu về chiều dài neo, lap, vị trí cắt thép sole.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn & Trám lỗ ti</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn lót:</strong> <span class="code-tag">VK_LotDaKieng</span> (trừ phần giao móng).</li>
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn đà kiềng:</strong> <span class="code-tag">VK_DaKieng</span> (trừ giao móng, cột).</li>
                <li><i class="fa-solid fa-check"></i> <strong>Trám lỗ ti:</strong> Tham số <span class="code-tag">BSV_LoTi</span>, chạy Tool <span class="tool-badge">TramLoTi</span>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 04. NEN -->
        <div class="comp-detail-box" id="panel-c04" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-border-all" style="color: var(--primary);"></i> 04. Nền Nhà Xưởng (Slab on Grade)</h3>
              <p>Các lớp cấu tạo nền xưởng chịu tải trọng nặng, khe co giãn và lưới thép hàn</p>
            </div>
            <span class="badge badge-cyan">SCHEDULE: 00.3.1.KL DIỆN TÍCH</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Các lớp cấu tạo nền</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Tấm PVC lót chống ẩm:</strong> <span class="code-tag">BSV_PhanLoai: DT_Nen</span>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Lớp đá base:</strong> <code>DT_Nen * ChieuDayBase</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Diện tích đầm chặt:</strong> <code>(DT Nền) - (Giao đà kiềng, cổ cột, móng)</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Xử lý chống mối:</strong> Đo bóc theo diện tích nền xưởng.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Bê tông lót nền:</strong> <code>DT_Nen * ChieuDayLot</code> (Type đặt <code>50_BTL</code>).</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông & Cốt thép nền</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Quy ước đặt Type:</strong> Ghi chiều dày H sàn (VD: <code>150</code>, <code>200</code>, <code>300</code>). Gán <code>Comments: 04.Nen</code>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Bê tông nền đàn hồi:</strong> Không liên kết với đà, cột.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Cốt thép:</strong> Cốt sợi ($kg/m^3$) HOẶC Thép thường (thép trên, dưới, chân kê) HOẶC Lưới thép hàn (lap chồng).</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-arrows-split-up-and-left"></i> Hệ thống Khe & Ván khuôn</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn thành xung quanh:</strong> <span class="code-tag">BSV_PhanLoai: VK_Nen</span>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn khe thi công:</strong> Chạy dọc tuyến đổ bê tông.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Các loại khe:</strong> Khe cắt (Saw-cut), Khe co giãn nhiệt (Expansion), Khe cô lập (Isolation), Khe thi công (Construction). Tính chiều dài m và vật liệu chèn khe.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 05. COT -->
        <div class="comp-detail-box" id="panel-c05" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-monument" style="color: var(--primary);"></i> 05. Cột & Cổ Cột Bê Tông Cốt Thép</h3>
              <p>Quy cách mô hình cột theo tầng, cao độ ngắt đổ bê tông và tool tự động</p>
            </div>
            <span class="badge badge-green">TOOL: BSV_Str_TaoCot_Ver4</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Cổ Cột & Thân Cột</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Quy ước Type:</strong> <code>Ngắn x Dài</code> (Ví dụ: <code>500x800</code>).</li>
                <li><i class="fa-solid fa-check"></i> Chạy Tool tự động: <span class="tool-badge">BSV_Str_TaoCot_Ver4</span>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Cổ cột:</strong> Gán <code>Comments: 05.1.CoCot</code>.
                  <br>- Cột không cô lập sàn: Tính tới <em>đáy sàn</em>.
                  <br>- Cột cô lập sàn: Tính tới <em>mặt trên sàn</em>.
                </li>
                <li><i class="fa-solid fa-check"></i> <strong>Cột tầng 1, 2... mái:</strong> Gán <code>Comments: 05.2.Cot-T1-Xuong</code>... tính tới đáy dầm sàn lầu.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-bars-staggered"></i> Cốt thép Cột</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Dựng theo mặt cắt chi tiết thiết kế.</li>
                <li><i class="fa-solid fa-check"></i> Chiều dài bẻ móc ngàm móng, đoạn nối sole so le tầng.</li>
                <li><i class="fa-solid fa-check"></i> Thép đai dày vùng chân/đầu cột, đai thường vùng giữa.</li>
                <li><i class="fa-solid fa-check"></i> Thống kê hàm lượng thép ($\%$ hoặc $kg/m^3$).</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn Cột</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn cổ cột:</strong> <span class="code-tag">BSV_PhanLoai: VK_CoCot</span>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn cột tầng:</strong> <span class="code-tag">BSV_PhanLoai: VK_Cot</span>.</li>
                <li><i class="fa-solid fa-check"></i> Tự động trừ phần giao dầm sàn theo thứ tự ưu tiên.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 06. VACH -->
        <div class="comp-detail-box" id="panel-c06" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-table-columns" style="color: var(--primary);"></i> 06. Vách Bê Tông Cốt Thép</h3>
              <p>Vách thang máy, vách bể nước, vách hầm và công tác trám lỗ ti</p>
            </div>
            <span class="badge badge-amber">TOOL: TI VÁCH</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Vách</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Quy ước Type:</strong> Ghi chiều dày vách (VD: <code>100</code>, <code>200</code>, <code>300</code>).</li>
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 06.Vach</code>.</li>
                <li><i class="fa-solid fa-check"></i> Bê tông mác B25, trừ phần giao sàn, móng, dầm, cột.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-bars-staggered"></i> Cốt thép Vách</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Thép 2 lớp theo mặt cắt thiết kế.</li>
                <li><i class="fa-solid fa-check"></i> Cốt đai liên kết 2 lớp thép vách, móc C.</li>
                <li><i class="fa-solid fa-check"></i> Chiều dài neo ngàm vào móng và sàn trên.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn & Lỗ ti</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> <strong>Ván khuôn vách:</strong> <span class="code-tag">BSV_PhanLoai: VK_Vach</span>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Trám lỗ ti vách:</strong> Gán biến <span class="code-tag">BSV_LoTi</span>, chạy <strong>Tool ti vách</strong>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 07. DAM -->
        <div class="comp-detail-box" id="panel-c07" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-bars" style="color: var(--primary);"></i> 07. Dầm Tầng & Dầm Mái (Beams)</h3>
              <p>Quy ước tách ván khuôn hông dầm vs ván đáy dầm chuyển sang sàn</p>
            </div>
            <span class="badge badge-rose">QUY ƯỚC QUAN TRỌNG VÁN KHUÔN</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Dầm</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 07.Dam</code> (Dầm tầng 2, 3... mái, tum).</li>
                <li><i class="fa-solid fa-check"></i> Bê tông B25, trừ phần giao sàn, cột, dầm chính.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-bars-staggered"></i> Cốt thép Dầm</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Thép lớp trên + thép tăng cường gối.</li>
                <li><i class="fa-solid fa-check"></i> Thép lớp dưới + thép tăng cường nhịp bụng.</li>
                <li><i class="fa-solid fa-check"></i> Thép đai (vùng dày đầu dầm & thưa giữa dầm).</li>
                <li><i class="fa-solid fa-check"></i> Thép giá dọc hông dầm, thép vai bò chống cắt (nếu có).</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn Dầm</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Gán <span class="code-tag">BSV_PhanLoai: VK_Dam</span>.</li>
                <li><i class="fa-solid fa-check"></i> <strong>Quy ước đo bóc QS:</strong> Chỉ tính <em>Ván khuôn 2 bên hông dầm</em>!</li>
                <li><i class="fa-solid fa-check"></i> <strong>Lưu ý:</strong> Ván đáy dầm được tính chuyển vào ván khuôn Sàn.</li>
                <li><i class="fa-solid fa-check"></i> Trám lỗ ti dầm bằng Tool chuyên dụng.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 08. SAN -->
        <div class="comp-detail-box" id="panel-c08" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-layer-group" style="color: var(--primary);"></i> 08. Sàn Lầu, Sàn Mái & Tum</h3>
              <p>Nguyên tắc tính full ván khuôn đáy dầm + đáy sàn + thành sàn</p>
            </div>
            <span class="badge badge-cyan">SCHEDULE: 00.2.2.KL VÁN KHUÔN</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Sàn</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 08.1.San-T2-Xuong</code>, <code>08.2.San-T3-Xuong</code>...</li>
                <li><i class="fa-solid fa-check"></i> Bê tông tính full khối tích, ăn đứt các cấu kiện bên dưới.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-bars-staggered"></i> Cốt thép Sàn</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Tính trực tiếp trên Revit.</li>
                <li><i class="fa-solid fa-check"></i> Cốt thép thường: Thép lớp trên, lớp dưới, thép tăng cường, con kê sàn.</li>
                <li><i class="fa-solid fa-check"></i> Lưới thép hàn: Tính chiều dài từng tấm, chiều rộng và tỷ lệ lap chồng.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn Sàn Toàn Diện</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Gán <span class="code-tag">BSV_PhanLoai: VK_San</span> (không tính phần giao cột).</li>
                <li><i class="fa-solid fa-check"></i> <strong>Công thức chuẩn QS:</strong><br><code>Ván khuôn sàn = Ván đáy sàn + Ván thành sàn + Ván đáy dầm</code>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 09. CAU THANG -->
        <div class="comp-detail-box" id="panel-c09" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-stairs" style="color: var(--primary);"></i> 09. Cầu Thang Bộ (Stairs)</h3>
              <p>Model in place (Structural Framing), đo bóc kết cấu & hoàn thiện kiến trúc bậc</p>
            </div>
            <span class="badge badge-amber">MODEL IN PLACE</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông & Ván khuôn</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Dựng bằng <em>Model in place (Structural Framing)</em> gồm bản thang, dầm thang, cối thang.</li>
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 09.1.CauThang-ST1-Xuong</code>...</li>
                <li><i class="fa-solid fa-check"></i> Ván khuôn đáy bản thang: <span class="code-tag">VK_CauThang</span>.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-bars-staggered"></i> Thép Cầu Thang</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Tính toán bóc tách qua bảng tính <strong>Excel</strong>.</li>
                <li><i class="fa-solid fa-check"></i> Thép lớp trên, lớp dưới, thép tăng cường chiếu nghỉ, thép đai bậc tam giác.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-paint-roller"></i> Hoàn thiện bậc thang</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Đá ốp mặt bậc: <span class="code-tag">DT_MatTren</span>.</li>
                <li><i class="fa-solid fa-check"></i> Đá ốp cổ bậc: <span class="code-tag">DT_MatTruoc</span>.</li>
                <li><i class="fa-solid fa-check"></i> Sơn thang: <code>VK_CauThang + DT_MatHong</code>.</li>
                <li><i class="fa-solid fa-check"></i> Lan can, tay vịn: Đo Pline từ bản vẽ CAD.</li>
                <li><i class="fa-solid fa-check"></i> Mũi chống trượt: <code>(Số bậc) x (Chiều rộng bậc)</code>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 10. TAM CAP -->
        <div class="comp-detail-box" id="panel-c10" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-ellipsis" style="color: var(--primary);"></i> 10. Bậc Tam Cấp Ngoài Nhà</h3>
              <p>Model in place, cấu tạo nền đầm chặt và bê tông bậc tam cấp</p>
            </div>
            <span class="badge badge-cyan">MODEL IN PLACE</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Tam Cấp</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Dựng <em>Model in place by Structural Framing</em>.</li>
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 10.1.TamCap-ST1-Xuong</code>.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Lớp lót & Đầm chặt</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Lớp đá base đầm chặt bên dưới tam cấp.</li>
                <li><i class="fa-solid fa-check"></i> Bê tông lót mác B7.5.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn & Hoàn thiện</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Ván khuôn thành các bậc tam cấp.</li>
                <li><i class="fa-solid fa-check"></i> Gạch / đá granite ốp lát bề mặt.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 11. RAMP -->
        <div class="comp-detail-box" id="panel-c11" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-arrow-trend-up" style="color: var(--primary);"></i> 11. Đường Dốc (Ramp)</h3>
              <p>Đường dốc lên xuống xưởng, dốc tầng hầm và hoàn thiện mặt ram dốc</p>
            </div>
            <span class="badge badge-green">RAMP STRUCTURE</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Lớp cấu tạo Ramp</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Màng PVC, bê tông lót, đá base đầm chặt.</li>
                <li><i class="fa-solid fa-check"></i> Gán biến: <span class="code-tag">BSV_PhanLoai: DT_NenRamp</span>.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Ramp</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 11.Ramp</code>.</li>
                <li><i class="fa-solid fa-check"></i> Bê tông mác B25, kẻ rãnh quả trám hoặc sơn epoxy chống trượt.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn Ramp</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Ván khuôn mặt bên ramp: <span class="code-tag">VK_Ramp</span>.</li>
                <li><i class="fa-solid fa-check"></i> Ván khuôn vách bo biên ramp: <span class="code-tag">VK_VachRamp</span>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 12. PIT -->
        <div class="comp-detail-box" id="panel-c12" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-box-archive" style="color: var(--primary);"></i> 12. Hố Pit Thang Máy & Hố Kỹ Thuật</h3>
              <p>Kết cấu hố âm, chống thấm đáy pit và ván khuôn hố pit</p>
            </div>
            <span class="badge badge-amber">SUBSTRUCTURE PIT</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Lớp cấu tạo Pit</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Lớp lót chống ẩm, đầm chặt đáy pit.</li>
                <li><i class="fa-solid fa-check"></i> Gán biến: <span class="code-tag">BSV_PhanLoai: DT_NenPit</span>.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Pit</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 12.Pit</code>.</li>
                <li><i class="fa-solid fa-check"></i> Bê tông B25 có phụ gia chống thấm W6/W8.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn Pit</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Ván khuôn đáy hố pit: <span class="code-tag">VK_Pit</span>.</li>
                <li><i class="fa-solid fa-check"></i> Ván khuôn thành vách hố: <span class="code-tag">VK_VachPit</span>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 13. DOCK -->
        <div class="comp-detail-box" id="panel-c13" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-truck-ramp-box" style="color: var(--primary);"></i> 13. Hố Pit Dock Leveler (Bốc Dỡ Hàng)</h3>
              <p>Hệ thống sàn nâng hạ container công nghiệp và dầm đỡ cơ khí</p>
            </div>
            <span class="badge badge-rose">LOGISTICS DOCK</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-layer-group"></i> Cấu tạo nền Dock</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> PVC, lót, đá base, đầm chặt.</li>
                <li><i class="fa-solid fa-check"></i> Gán biến: <span class="code-tag">BSV_PhanLoai: DT_NenDock</span>.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-cube"></i> Bê tông Dock</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Gán <code>Comments: 13.Dock</code>.</li>
                <li><i class="fa-solid fa-check"></i> Đặt thép chờ, thanh thép góc V bo viền chống sứt mẻ mép bê tông.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-table-cells-large"></i> Ván khuôn Dock</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Ván khuôn hố dock: <span class="code-tag">VK_Dock</span>.</li>
                <li><i class="fa-solid fa-check"></i> Ván khuôn dầm dock: <span class="code-tag">VK_DamDock</span>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 14. CAU KIEN PHU -->
        <div class="comp-detail-box" id="panel-c14" style="display: none;">
          <div class="comp-header">
            <div class="comp-header-left">
              <h3><i class="fa-solid fa-wrench" style="color: var(--primary);"></i> 14. Cấu Kiện Phụ (Mương Nước, Bệ Máy...)</h3>
              <p>Mương cáp điện, rãnh thoát nước ngầm và bệ móng máy thiết bị</p>
            </div>
            <span class="badge badge-cyan">MISCELLANEOUS</span>
          </div>
          <div class="comp-grid">
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-water"></i> Mương kỹ thuật</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Bê tông mương: Gán <code>Comments: 14.1.Muong</code>.</li>
                <li><i class="fa-solid fa-check"></i> Ván khuôn mương: <span class="code-tag">BSV_PhanLoai: VK_Muong</span>.</li>
                <li><i class="fa-solid fa-check"></i> Nắp đan bê tông hoặc grating thép mạ kẽm.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-gear"></i> Bệ máy thiết bị</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Bê tông bệ máy: Gán <code>Comments: 14.2.BeMay</code>.</li>
                <li><i class="fa-solid fa-check"></i> Ván khuôn bệ máy: <span class="code-tag">BSV_PhanLoai: VK_BeMay</span>.</li>
                <li><i class="fa-solid fa-check"></i> Bulong móng neo chân máy và bản mã thép chôn sẵn.</li>
              </ul>
            </div>
            <div class="sub-panel">
              <div class="sub-panel-title"><i class="fa-solid fa-list-check"></i> Quản lý khối lượng</div>
              <ul class="sub-list">
                <li><i class="fa-solid fa-check"></i> Đặt mã code phân nhóm rõ ràng để không lẫn vào kết cấu chính.</li>
                <li><i class="fa-solid fa-check"></i> Tách riêng dự toán phần xây lắp phụ trợ.</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION D: HỆ THỐNG BẢNG BIỂU REVIT SCHEDULES -->
    <section id="bang-thong-ke" style="scroll-margin-top: 90px; margin-bottom: 3.5rem;">
      <div class="section-header">
        <span class="section-tag">PHẦN D</span>
        <h2 class="section-title">Hệ Thống Bảng Biểu Thống Kê Chuẩn (Revit Schedules)</h2>
        <p class="section-desc">
          Trích xuất 7 biểu mẫu thống kê thực tế từ file PDF, thể hiện cách gom nhóm, phân tầng và tính toán khối lượng tự động trên Revit. Nhấp vào từng ảnh để phóng to.
        </p>
      </div>

      <div class="gallery-grid">
        <!-- Image 1 -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/img_1.png', '00.1.2.KL BÊ TÔNG - Thống kê Bê tông Cột, Móng, Dầm theo Phân Khu')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/img_1.png" alt="Bảng khối lượng bê tông">
            <div class="sched-zoom-hint"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem Bảng 01</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">00.1.2.KL BÊ TÔNG (Phần 1)</div>
            <div class="sched-desc">Phân loại bê tông theo Comments & Phân khu dự án</div>
          </div>
        </div>

        <!-- Image 2 -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/img_2.png', '00.1.2.KL BÊ TÔNG - Thống kê Bê tông Sàn, Vách & Cấu kiện Phụ')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/img_2.png" alt="Bảng khối lượng bê tông 2">
            <div class="sched-zoom-hint"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem Bảng 02</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">00.1.2.KL BÊ TÔNG (Phần 2)</div>
            <div class="sched-desc">Tổng hợp thể tích m³ dầm, sàn tầng và mác bê tông</div>
          </div>
        </div>

        <!-- Image 3 -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/img_3.png', '00.2.2.KL VÁN KHUÔN - Bảng thống kê diện tích ván khuôn m² theo BSV_PhanLoai')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/img_3.png" alt="Bảng ván khuôn 1">
            <div class="sched-zoom-hint"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem Bảng 03</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">00.2.2.KL VÁN KHUÔN (Phần 1)</div>
            <div class="sched-desc">Thống kê diện tích ván khuôn móng, cổ cột, đà kiềng</div>
          </div>
        </div>

        <!-- Image 4 -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/img_4.png', '00.2.2.KL VÁN KHUÔN - Bảng thống kê ván khuôn dầm sàn và vách')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/img_4.png" alt="Bảng ván khuôn 2">
            <div class="sched-zoom-hint"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem Bảng 04</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">00.2.2.KL VÁN KHUÔN (Phần 2)</div>
            <div class="sched-desc">Tự động trừ giao và tính ván khuôn thành dầm, sàn</div>
          </div>
        </div>

        <!-- Image 5 -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/img_5.png', '00.3.1.KL DIỆN TÍCH - Bảng đo bóc diện tích nền, đầm chặt và tấm PVC')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/img_5.png" alt="Bảng khối lượng diện tích">
            <div class="sched-zoom-hint"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem Bảng 05</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">00.3.1.KL DIỆN TÍCH</div>
            <div class="sched-desc">Đo bóc diện tích nền m², diện tích đầm chặt, chống thấm</div>
          </div>
        </div>

        <!-- Image 6 -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/img_6.png', '01.1.CỌC - Bảng thống kê cọc ly tâm, số lượng, chiều sâu và ép âm')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/img_6.png" alt="Bảng thống kê cọc">
            <div class="sched-zoom-hint"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem Bảng 06</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">01.1.CỌC</div>
            <div class="sched-desc">Quản lý tim cọc, tải trọng, cọc thí nghiệm và cao độ ép âm</div>
          </div>
        </div>

        <!-- Image 7 -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/img_7.png', '00.2.1.KL VÁN KHUÔN LÓT - Thống kê ván khuôn bê tông lót móng và đà kiềng')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/img_7.png" alt="Bảng ván khuôn lót">
            <div class="sched-zoom-hint"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem Bảng 07</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">00.2.1.KL VÁN KHUÔN LÓT</div>
            <div class="sched-desc">Lọc riêng ván khuôn be thành bê tông lót móng đá 4x6</div>
          </div>
        </div>

        <!-- Mindmap Card -->
        <div class="sched-card" onclick="openModal('assets/bsv_kc/bsv_ketcau_full.png', 'BSV_KẾT CẤU (VER 2) - Toàn bộ Sơ Đồ Tư Duy Gốc Siêu Nét (Full Canvas Resolution)')">
          <div class="sched-img-box">
            <img src="assets/bsv_kc/bsv_ketcau_full.png" alt="Toàn bộ Sơ đồ tư duy">
            <div class="sched-zoom-hint"><i class="fa-solid fa-expand"></i> Phóng to Mindmap</div>
          </div>
          <div class="sched-info">
            <div class="sched-title">SƠ ĐỒ GỐC (FULL CANVAS)</div>
            <div class="sched-desc">Bản vẽ đồ họa gốc độ phân giải cực cao 6120 x 17875 px</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION E: MINDMAP VIEWER BANNER -->
    <section id="mindmap-view">
      <div class="mindmap-banner">
        <div class="mindmap-text">
          <h3><i class="fa-solid fa-diagram-project" style="color: var(--primary);"></i> Khám Phá Sơ Đồ Tư Duy Đồ Họa Gốc</h3>
          <p>
            Bạn có thể mở và phóng to toàn màn hình bản vẽ Mindmap nguyên bản của <strong>BSV_BimKetCauVer2.pdf</strong> để tra cứu cấu trúc phân nhánh trực quan từ Root Node đến từng Parameter chi tiết.
          </p>
        </div>
        <button class="mindmap-preview-btn" onclick="openModal('assets/bsv_kc/bsv_ketcau_full.png', 'BSV_KẾT CẤU (VER 2) - Bản đồ tư duy gốc')">
          <i class="fa-solid fa-magnifying-glass-plus"></i> Mở Sơ Đồ Full Canvas
        </button>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <p>&copy; 2026 BIM Management Platform • Bộ môn Kết Cấu (BSV_KẾT CẤU VER 2)</p>
      <p style="margin-top: 4px; font-size: 0.775rem;">Được số hóa từ tài liệu kỹ thuật <code>BSV_BimKetCauVer2.pdf</code> phục vụ công tác chuẩn hóa quy trình BIM.</p>
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

    // Component Tab Switching
    function showComponent(compId, btn) {
      document.querySelectorAll('.comp-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.comp-detail-box').forEach(p => p.style.display = 'none');

      if (btn) btn.classList.add('active');
      const targetPanel = document.getElementById('panel-' + compId);
      if (targetPanel) {
        targetPanel.style.display = 'block';
      }
    }

    // Image Modal
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

    // Load Theme State
    window.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('bim_theme_preference') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);
    });
  </script>
</body>
</html>
"""

with open('BSV_BimKetCauVer2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created BSV_BimKetCauVer2.html successfully!")
