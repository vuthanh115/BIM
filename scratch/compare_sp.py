import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

file1 = 'BSV_KC_ShareParameter.txt'
file2 = 'MEGA-BP3_2026.04.21.ifc.sharedparameters.txt'

def read_shared_param_file(filepath):
    # Try utf-16 first, then utf-8, then latin1
    for enc in ['utf-16', 'utf-16-le', 'utf-8-sig', 'utf-8', 'cp1252']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
                # Verify header
                if '# This is a Revit shared parameter file' in content or '*META' in content or '*PARAM' in content:
                    return content, enc
        except Exception:
            continue
    raise ValueError(f"Could not read {filepath}")

content1, enc1 = read_shared_param_file(file1)
content2, enc2 = read_shared_param_file(file2)

print(f"File 1: {file1} (Encoding: {enc1}, Size: {os.path.getsize(file1)} bytes)")
print(f"File 2: {file2} (Encoding: {enc2}, Size: {os.path.getsize(file2)} bytes)")

def parse_sp(content):
    groups = {} # id -> name
    params = {} # name -> dict(guid, type, group_id, group_name, visible, desc, modifiable, hide)
    
    current_section = None
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('*'):
            current_section = line[1:].split()[0]
            continue
        
        parts = line.split('\t')
        if current_section == 'GROUP' and len(parts) >= 3:
            # GROUP <ID> <NAME>
            gid = parts[1].strip()
            gname = parts[2].strip()
            groups[gid] = gname
        elif current_section == 'PARAM' and len(parts) >= 4:
            # PARAM <GUID> <NAME> <DATATYPE> <DATACATEGORY> <GROUP> ...
            guid = parts[1].strip()
            name = parts[2].strip()
            dtype = parts[3].strip()
            group_id = parts[5].strip() if len(parts) > 5 else ''
            visible = parts[6].strip() if len(parts) > 6 else '1'
            desc = parts[7].strip() if len(parts) > 7 else ''
            
            params[name] = {
                'guid': guid,
                'name': name,
                'datatype': dtype,
                'group_id': group_id,
                'group_name': groups.get(group_id, f"Group_{group_id}"),
                'visible': visible,
                'description': desc
            }
    return groups, params

groups1, params1 = parse_sp(content1)
groups2, params2 = parse_sp(content2)

print(f"\n--- GROUPS ---")
print(f"File 1 Groups ({len(groups1)}):", groups1)
print(f"File 2 Groups ({len(groups2)}):", groups2)

print(f"\n--- PARAMETERS COUNT ---")
print(f"File 1 Parameters: {len(params1)}")
print(f"File 2 Parameters: {len(params2)}")

names1 = set(params1.keys())
names2 = set(params2.keys())

common = names1.intersection(names2)
only1 = names1 - names2
only2 = names2 - names1

print(f"\nCommon parameters ({len(common)}): {sorted(list(common))}")
print(f"Only in File 1 ({len(only1)}): {sorted(list(only1))}")
print(f"Only in File 2 ({len(only2)}): {sorted(list(only2))}")

# Check data types distribution
def get_type_dist(params):
    dist = {}
    for p in params.values():
        t = p['datatype']
        dist[t] = dist.get(t, 0) + 1
    return dist

print(f"\nData types in File 1:", get_type_dist(params1))
print(f"Data types in File 2:", get_type_dist(params2))

