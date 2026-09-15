import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add responsive CSS for .discipline-nav & .wbs-card-grid if not present
responsive_css = """
    @media (max-width: 1024px) {
      .discipline-nav {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    @media (max-width: 768px) {
      .discipline-nav {
        grid-template-columns: repeat(2, 1fr);
      }
      .wbs-card-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 520px) {
      .discipline-nav {
        grid-template-columns: 1fr;
      }
    }
"""

if '.discipline-nav {' in content and '@media (max-width: 1024px)' not in content:
    # insert before @media (max-width: 900px)
    if '@media (max-width: 900px)' in content:
        content = content.replace('@media (max-width: 900px)', responsive_css.strip() + '\n\n    @media (max-width: 900px)')
    else:
        content = content.replace('</style>', responsive_css + '\n  </style>')
    print("Added responsive CSS for discipline-nav")

# 2. Add switchDiscipline function and tab handler into <script>
js_functions = """
    // Switch Discipline Tabs (4 Bo Mon & Clash Matrix)
    function switchDiscipline(paneId, btn) {
      // Deactivate all discipline tab buttons
      document.querySelectorAll('.disc-btn').forEach(function(b) {
        b.classList.remove('active');
      });
      // Deactivate all discipline panes
      document.querySelectorAll('.disc-pane').forEach(function(p) {
        p.classList.remove('active');
      });

      // Activate selected button
      if (btn) {
        btn.classList.add('active');
      } else {
        var matchedBtn = document.querySelector('.disc-btn[onclick*="' + paneId + '"]');
        if (matchedBtn) matchedBtn.classList.add('active');
      }

      // Activate selected pane
      var targetPane = document.getElementById(paneId);
      if (targetPane) {
        targetPane.classList.add('active');
      }
    }
    window.switchDiscipline = switchDiscipline;

    // Handle hash links for direct discipline tab navigation
    function checkHashForDiscipline() {
      var hash = window.location.hash;
      if (hash) {
        var id = hash.replace('#', '');
        var validPanes = ['disc-arc', 'disc-str', 'disc-mep', 'disc-inf', 'disc-matrix'];
        if (validPanes.indexOf(id) !== -1) {
          switchDiscipline(id);
          var sec = document.getElementById('de-muc-bo-mon');
          if (sec) {
            sec.scrollIntoView({ behavior: 'smooth' });
          }
        }
      }
    }
"""

# Check if switchDiscipline is already in content
if 'function switchDiscipline' not in content:
    # Put it right after toggleTheme / updateThemeIcon or before switchStage
    target_pos = '    // Tab switching for stages'
    if target_pos in content:
        content = content.replace(target_pos, js_functions.strip() + '\n\n' + target_pos)
        print("Successfully injected switchDiscipline before 'Tab switching for stages'")
    else:
        # put before window.addEventListener('DOMContentLoaded'
        target_pos_alt = "window.addEventListener('DOMContentLoaded'"
        content = content.replace(target_pos_alt, js_functions.strip() + '\n\n    ' + target_pos_alt)
        print("Successfully injected switchDiscipline before DOMContentLoaded")
else:
    print("switchDiscipline already present in script")

# Also ensure checkHashForDiscipline is called on load and hashchange
hash_listener = """
    window.addEventListener('hashchange', checkHashForDiscipline);
"""

if 'hashchange' not in content:
    content = content.replace("window.addEventListener('DOMContentLoaded', () => {", hash_listener + "\n    window.addEventListener('DOMContentLoaded', () => {\n      checkHashForDiscipline();")
    print("Added hashchange listener")

# Ensure html tag has smooth scrolling
if 'html {' not in content and 'scroll-behavior: smooth;' in content:
    content = content.replace('body {', 'html { scroll-behavior: smooth; }\n    body {')
    print("Added html smooth scroll")

# Clean any literal tab in LOD 200 $	rightarrow$ LOD 500
content = content.replace('$\trightarrow$', '&rarr;')
content = content.replace('$\rightarrow$', '&rarr;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")
