import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Verify all buttons have corresponding panes
buttons = re.findall(r"switchDiscipline\('([^']+)',\s*this\)", html)
print("Buttons target IDs:", buttons)
for bid in buttons:
    pane_match = re.search(r'id=[\'"]' + bid + r'[\'"]', html)
    if pane_match:
        print(f"  [OK] Pane '{bid}' exists.")
    else:
        print(f"  [ERROR] Pane '{bid}' does not exist!")

# Verify script contains switchDiscipline definition
if "function switchDiscipline" in html and "window.switchDiscipline = switchDiscipline" in html:
    print("[OK] switchDiscipline function is defined and globally exported to window.")
else:
    print("[ERROR] switchDiscipline definition issue!")

# Verify dark mode compatibility
if 'data-theme="dark"' in html:
    print("[OK] Dark mode default attribute is set on <html>.")

# Verify nav link
if '<a href="#de-muc-bo-mon">' in html or 'href="#de-muc-bo-mon"' in html:
    print("[OK] Nav link to #de-muc-bo-mon exists.")
