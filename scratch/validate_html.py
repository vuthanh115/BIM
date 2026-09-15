import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check script syntax
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
print(f"Number of script tags: {len(scripts)}")
for i, s in enumerate(scripts):
    print(f"Script {i} length: {len(s)} chars")
    # Quick check for obvious JS syntax issues
    open_braces = s.count('{')
    close_braces = s.count('}')
    open_parens = s.count('(')
    close_parens = s.count(')')
    print(f"  Braces: {open_braces} open, {close_braces} close")
    print(f"  Parens: {open_parens} open, {close_parens} close")

# Check all IDs referenced in onclick
onclicks = re.findall(r'onclick=[\'"]([^\'"]+)[\'"]', content)
print(f"Total onclicks: {len(onclicks)}")
missing_fns = set()
for oc in onclicks:
    m = re.match(r'([a-zA-Z0-9_]+)\(', oc.strip())
    if m:
        fn_name = m.group(1)
        if fn_name not in ['toggleTheme', 'switchStage', 'toggleTask', 'updateProgress', 'resetTasks', 'exportChecklistReport', 'openModal', 'closeModal', 'switchDiscipline'] and not oc.startswith('window.'):
            missing_fns.add(fn_name)
print("Missing or unhandled functions in onclick:", missing_fns)

