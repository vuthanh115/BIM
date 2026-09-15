import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add scroll spy and navbar active update in DOMContentLoaded
scroll_spy_js = """
      // Smooth Scroll & Active Nav State on Click
      const navLinks = document.querySelectorAll('.nav-links a');
      navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
          const targetId = this.getAttribute('href');
          if (targetId && targetId.startsWith('#') && targetId.length > 1) {
            const targetEl = document.querySelector(targetId);
            if (targetEl) {
              e.preventDefault();
              navLinks.forEach(l => l.classList.remove('active'));
              this.classList.add('active');
              targetEl.scrollIntoView({ behavior: 'smooth' });
              history.pushState(null, null, targetId);
            }
          }
        });
      });

      // Scroll Spy for Nav Highlighting
      window.addEventListener('scroll', () => {
        const sections = document.querySelectorAll('section[id]');
        let currentSection = '';
        const scrollPosition = window.pageYOffset + 120;

        sections.forEach(section => {
          const sectionTop = section.offsetTop;
          const sectionHeight = section.offsetHeight;
          if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            currentSection = section.getAttribute('id');
          }
        });

        if (currentSection) {
          navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + currentSection) {
              link.classList.add('active');
            }
          });
        }
      });
"""

if 'Scroll Spy for Nav Highlighting' not in content:
    content = content.replace("loadState();", "loadState();\n" + scroll_spy_js)
    print("Added scroll spy and nav click handler")

# 2. Add direct link in Stage 2 Checklist
stage2_target = """<span class="check-tag">BIM 3D</span>
              </div>
            </label>"""

stage2_replacement = """<span class="check-tag">BIM 3D</span>
                <div style="margin-top: 10px;">
                  <a href="#de-muc-bo-mon" onclick="event.stopPropagation();" style="color: var(--primary); font-size: 0.82rem; font-weight: 700; text-decoration: underline; display: inline-flex; align-items: center; gap: 5px;">
                    <i class="fa-solid fa-sitemap"></i> Xem chi tiết Đề mục 4 Bộ môn (WBS) & Ma trận va chạm &rarr;
                  </a>
                </div>
              </div>
            </label>"""

if 'Xem chi tiết Đề mục 4 Bộ môn (WBS)' not in content and stage2_target in content:
    content = content.replace(stage2_target, stage2_replacement)
    print("Added direct WBS link inside Stage 2 Checklist")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html with nav spy & Stage 2 link!")
