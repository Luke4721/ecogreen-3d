import base64, json, os

SLOTS = [
    ("robot_arm", ["robot", "axis"],                     []),
    ("conveyor",  ["conveyor", "belt"],                  []),
    ("truck",     ["truck", "semi", "trailer", "lorry"], []),
    ("washer",    ["wash", "fridge", "appliance"],       []),
]
MAX_MB = 12

found = {}
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not d.startswith((".", "_"))]
    for fn in files:
        if not fn.lower().endswith(".glb"):
            continue
        p = os.path.join(root, fn)
        mb = os.path.getsize(p) / 1e6
        low = fn.lower()
        for slot, kws, not_kw in SLOTS:
            if slot in found:
                continue
            if any(k in low for k in kws) and not any(x in low for x in not_kw):
                if mb > MAX_MB:
                    print(f"SKIP (too big {mb:.1f} MB): {fn} -> {slot}")
                    break
                found[slot] = p
                break

out = {}
for slot, path in found.items():
    with open(path, "rb") as f:
        out[slot] = "data:model/gltf-binary;base64," + base64.b64encode(f.read()).decode()
    print(f"packed: {slot:<10} <- {path}")

for name, _, _ in SLOTS:
    if name not in found:
        print(f"missing (page will use built-in fallback): {name}")

with open("models-data.js", "w") as f:
    f.write("window.ECO_MODELS=" + json.dumps(out) + ";")
print(f"\nmodels-data.js written - {len(found)}/{len(SLOTS)} models")