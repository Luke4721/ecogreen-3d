import base64, os, re, shutil

SRC_OPTIONS = ["sylva-hero.orig.html", "sylva-hero.html"]
ASSETS = "inner-green-assets"
OUT = "sylva-hero-embed.html"
PAGE = "ecogreen.html"

src = next((f for f in SRC_OPTIONS if os.path.exists(f)), None)
if not src:
    raise SystemExit("No sylva-hero.html found — save the full raw file from the ThreeUI repo first.")
if src == "sylva-hero.html" and not os.path.exists("sylva-hero.orig.html"):
    shutil.copy(src, "sylva-hero.orig.html")
    print("backup created: sylva-hero.orig.html")
orig = open("sylva-hero.orig.html" if os.path.exists("sylva-hero.orig.html") else src, encoding="utf-8").read()

out, ok = orig, True
def rep(label, old, new):
    global out, ok
    if old in out:
        out = out.replace(old, new)
        print(f"ok      {label}")
    else:
        print(f"skip    {label} (already applied or not present)")

rep("title", "<title>Sylva — Into the living world</title>",
    "<title>EcoGreen — Every device has a next life</title>")
rep("meta-desc",
    "Restoring wild places through patient design, native planting, and a deeper kind of stewardship.",
    "Circular e-waste renewal — we collect, certify and dismantle electronics, then rebuild them into raw material.")
rep("ghost", ">SYLVA</div>", ">ECOGREEN</div>")
rep("headline-1", ">Step into</i>", ">Every device</i>")
rep("headline-2", ">the living world</i>", ">has a next life</i>")
rep("lede",
    "We restore wild places through patient design, native planting, and a deeper kind of stewardship.",
    "We collect, certify and dismantle electronics — then rebuild them into raw material for the next generation.")
rep("card-1-h", "Let the wild lead.", "Let nothing go to waste.")
rep("card-2-h", "After the Rain", "Back in Circulation")
rep("stat-1", "Canopy restored</dt><dd>282 ha</dd>", "Devices renewed</dt><dd>1.2M kg</dd>")
rep("stat-2", "Native species</dt><dd>43 mapped</dd>", "Materials recovered</dt><dd>96.4%</dd>")
rep("dock-1", "<span>Grove</span>", "<span>What we take</span>")
rep("dock-2", "<span>Habitats</span>", "<span>Process</span>")
rep("dock-3", "<span>Journal</span>", "<span>Services</span>")
rep("home-aria", 'aria-label="Sylva — home"', 'aria-label="EcoGreen — home"')

# ---- inline the Three.js runtime (what ThreeUI's own wrapper does) ----
rt_path = os.path.join(ASSETS, "three.min.js")
tag = '<script src="inner-green-assets/three.min.js"></script>'
if tag in out and os.path.exists(rt_path):
    rt = open(rt_path, encoding="utf-8").read()
    rt = rt.replace("</script", "<\\/script")   # safety for inline embedding
    out = out.replace(tag, "<script data-inline-three-runtime>" + rt + "</script>", 1)
    print(f"ok      three.min.js inlined ({len(rt)//1024} KB)")
elif tag not in out and "data-inline-three-runtime" in out:
    print("skip    three.min.js (already inlined)")
elif not os.path.exists(rt_path):
    ok = False
    print("MISS    inner-green-assets/three.min.js — save the r149 file there")
else:
    ok = False
    print("MISS    script tag anchor")

# ---- base64-inline the two card images ----
for name in ["card-ethos.jpg", "card-ecostove.jpg"]:
    p = os.path.join(ASSETS, name)
    ref = f'inner-green-assets/{name}'
    if f'"{ref}"' not in out:
        print(f"skip    {name} (already inlined)"); continue
    if os.path.exists(p):
        b64 = base64.b64encode(open(p, "rb").read()).decode()
        out = out.replace(f'"{ref}"', f'"data:image/jpeg;base64,{b64}"')
        print(f"ok      {name} inlined ({os.path.getsize(p)//1024} KB)")
    else:
        print(f"WARN    {name} missing — card plate stays dark; copy it into {ASSETS}/")

BRAND = """
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@100..900&display=swap" rel="stylesheet">
<style data-ecogreen-brand>
  .ghost{font-size:calc(190*var(--u))!important;letter-spacing:calc(16*var(--u))!important}
  .stat dd{color:#2CA244}
  .dock-item--enter{background:rgba(69,199,78,.16)!important;color:#d9ffe0!important}
</style>
<script data-ecogreen-bridge>
(function(){
  var targets=['home','types','collect','services','collect'];
  var sc2=document.getElementById('scene'); if(sc2) sc2.setAttribute('aria-label','EcoGreen living world');
  var items=document.querySelectorAll('.dock-item');
  items.forEach(function(a,i){ a.addEventListener('click',function(ev){
    ev.preventDefault(); parent.postMessage({type:'ecogreen-dock',target:targets[i]||'collect'},'*'); });});
  var eb=document.querySelector('.liquid-button--explore');
  if(eb) eb.addEventListener('click',function(){ parent.postMessage({type:'ecogreen-dock',target:'collect'},'*'); });
  var sc=document.querySelector('.scroll');
  if(sc) sc.addEventListener('click',function(ev){ ev.preventDefault(); parent.postMessage({type:'ecogreen-dock',target:'types'},'*'); });
})();
</script>
"""
if "data-ecogreen-bridge" not in out and "</head>" in out:
    out = out.replace("</head>", BRAND + "</head>", 1)
    print("ok      brand-inject")
elif "data-ecogreen-bridge" in out:
    print("skip    brand-inject (already present)")

open(OUT, "w", encoding="utf-8").write(out)
open("sylva-ready.js", "w").write("window.ECO_SYLVA=true;")
print(f"\n{OUT} written ({len(out)//1024} KB), sylva-ready.js written.")

# ---- patch ecogreen.html: iframe src + Lexend link for the dock ----
if os.path.exists(PAGE):
    page = open(PAGE, encoding="utf-8").read()
    changed = False
    if "sylva-hero-embed.html" not in page and "sylvaFrame" in page:
        page = page.replace("sylvaFrame.src = 'sylva-hero.html';",
                            "sylvaFrame.src = 'sylva-hero-embed.html';", 1)
        changed = True; print("ok      ecogreen.html iframe -> sylva-hero-embed.html")
    if "family=Lexend" not in page.split("</head>")[0]:
        page = page.replace("</head>",
            '<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600&display=swap" rel="stylesheet">\n</head>', 1)
        changed = True; print("ok      ecogreen.html Lexend link added (dock font)")
    if changed:
        open(PAGE, "w", encoding="utf-8").write(page)
else:
    print("WARN    ecogreen.html not found — iframe src patch skipped")