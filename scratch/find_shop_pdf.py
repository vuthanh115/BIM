import os

for root, dirs, files in os.walk(r'c:\Users\thanhvp\Downloads'):
    for f in files:
        if f.lower().endswith('.pdf'):
            full_path = os.path.join(root, f)
            if any(k in f.lower() for k in ['shop', 'rebar', 'thep']):
                print("FOUND:", full_path)

