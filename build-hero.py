import os, shutil

SRC = "sylva-hero.html"
BAK = "sylva-hero.orig.html"

if not os.path.exists(SRC):
    raise SystemExit("sylva-hero.html not found — save the full raw file from the ThreeUI repo first.")

# always rebrand from the pristine original so re-runs are clean
if not os.path.exists(BAK):
    shutil.copy(SRC, BAK)
orig = open(BAK, encoding="utf-8").read()

out = orig
ok = True

def rep(label, old, new, expect=1):
    global out, ok
    n = out.count(old)
    if n >= expect:
        out = out.replace(old, new)
        print(f"ok      {label} ({n}x)")
    else:
        ok = False
        print(f"MISS    {label} (found {n}, expected >= {expect})")

rep("title",
    "<title>Sylva — Into the living world</title>",
    "<title>EcoGreen — Every device has a next life</title>")
rep("meta-desc",
    'Restoring wild places through patient design, native planting, and a deeper kind of stewardship.',
    'Circular e-waste renewal — we collect, certify and dismantle electronics, then rebuild them into raw material.')

# v2: global phrase swap — covers canvas aria, any other aria/alt, however long the string is
rep("sylva-phrase", "Sylva Living Green", "EcoGreen living world")

rep("ghost",
    '>SYLVA</div>',
    '>ECOGREEN</div>')
rep("headline-1",
    '>Step into</i>',
    '>Every device</i>')
rep("headline-2",
    '>the living world</i>',
    '>has a next life</i>')
rep("lede",
    "We restore wild places through patient design, native planting, and a deeper kind of stewardship.",
    "We collect, certify and dismantle electronics — then rebuild them into raw material for the next generation.")
rep("card-1-h",
    "Let the wild lead.",
    "Let nothing go to waste.")
rep("card-2-h",
    "After the Rain",
    "Back in Circulation")

# v2: full dd swap — no stray closing tags
rep("stat-1",
    "Canopy restored</dt><dd>282 ha</dd>",
    "Devices renewed</dt><dd>1.2M kg</dd>")     # placeholder — set real figures
rep("stat-2",
    "Native species</dt><dd>43 mapped</dd>",
    "Materials recovered</dt><dd>96.4%</dd>")

rep("dock-1", "<span>Grove</span>",    "<span>What we take</span>")
rep("dock-2", "<span>Habitats</span>", "<span>Process</span>")
rep("dock-3", "<span>Journal</span>",  "<span>Services</span>")
rep("dock-mark-1",
    'd="M11 1.3c-2.1 0-3.95 1.2-4.75 2.95C3.95 4.55 2.3 6.25 2.3 8.35c0 2.3 1.9 4.2 4.3 4.2h8.8c2.4 0 4.3-1.9 4.3-4.2 0-2.1-1.65-3.8-4-4.1C14.95 2.5 13.1 1.3 11 1.3Z"',
    'd="M11 1.5C6.7 6.8 4 10.6 4 14a7 7 0 0 0 14 0c0-3.4-2.7-7.2-7-12.5Z"')
rep("dock-mark-2",
    'd="M9.6 12.55h2.8v4.2c1.35.3 2.45 1.15 3.15 2.4-1.35.4-2.4.15-3.15-.4v4.15H9.6v-4.15c-.75.55-1.8.8-3.15.4.7-1.25 1.8-2.1 3.15-2.4v-4.2Z"',
    'd="M11 13.2c0-3 2.1-5.2 5-5.2.2 3.2-2 5.5-5 5.2Z"')
rep("home-aria",
    'aria-label="Sylva — home"',
    'aria-label="EcoGreen — home"')

BRAND_INJECT = """
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@100..900&display=swap" rel="stylesheet">
<style data-ecogreen-brand>
  .ghost{font-size:calc(190*var(--u))!important;letter-spacing:calc(16*var(--u))!important}
  .stat dd{color:#2CA244}
  .dock-item--enter{background:rgba(69,199,78,.16)!important;color:#d9ffe0!important}
</style>
<script data-ecogreen-bridge>
(function(){
  var targets=['home','types','collect','services','collect'];
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
if "</head>" in out:
    out = out.replace("</head>", BRAND_INJECT + "</head>", 1)
    print("ok      brand-inject")
else:
    ok = False
    print("MISS    </head>")

open(SRC, "w", encoding="utf-8").write(out)
open("sylva-ready.js", "w").write("window.ECO_SYLVA=true;")
print("\nsylva-hero.html rebranded (v2), sylva-ready.js written.")
if not ok:
    print("Some anchors missed — send me the MISS lines and I'll adjust.")
missing = [p for p in ["inner-green-assets/three.min.js",
                       "inner-green-assets/card-ethos.jpg",
                       "inner-green-assets/card-ecostove.jpg"] if not os.path.exists(p)]
if missing:
    print("WARNING missing assets:", ", ".join(missing),
          "- cards render as dark plates until copied.")
    







    