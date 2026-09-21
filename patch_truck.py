import re

P = "ecogreen.html"
src = open(P, encoding="utf-8").read()

# 1) explicit SVG sizing inside the truck strip
old_css = "#topWrap{width:min(64vw,900px);will-change:transform,width;filter:drop-shadow(0 18px 30px rgba(0,0,0,.45))}"
if "#topSvg{width:100%" in src:
    print("skip   topSvg css (already present)")
elif old_css in src:
    src = src.replace(old_css, old_css + "\n  #topSvg{width:100%;height:auto;display:block}", 1)
    print("ok     topSvg css")
else:
    print("MISS   topSvg css anchor")

# 2) smaller strip -> rotated truck fits fully in view (cab included)
old_sw = "const stripW = () => MOB ? Math.min(innerHeight * .5, 440) : Math.min(innerWidth * .46, innerHeight * .72, 760);"
new_sw = "const stripW = () => MOB ? Math.min(innerHeight * .42, 380) : Math.min(innerWidth * .38, innerHeight * .56, 620);"
if new_sw in src:
    print("skip   stripW (already patched)")
elif old_sw in src:
    src = src.replace(old_sw, new_sw, 1)
    print("ok     stripW")
else:
    print("MISS   stripW anchor")

# 3) dock: hide only over the first viewport, then persist for the whole page
pat = re.compile(
    r"new IntersectionObserver\(\(\[en\]\) => \{.*?\}\), \{threshold:\.?15\}\)\.observe\(document\.getElementById\('hero'\)\);",
    re.S)
new_dock = ("const dockVis = () => dock.classList.toggle('hide', scrollY < innerHeight * .85);\n"
            "  dockVis();\n"
            "  addEventListener('scroll', dockVis, {passive:true});")
if "dockVis" in src:
    print("skip   dock persistence (already patched)")
elif pat.search(src):
    src = pat.sub(new_dock, src, count=1)
    print("ok     dock persistence")
else:
    print("MISS   dock observer anchor")

open(P, "w", encoding="utf-8").write(src)
print("\necogreen.html patched. Hard-refresh next.")