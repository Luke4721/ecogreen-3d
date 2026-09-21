src = open("sylva-hero.html", encoding="utf-8").read()
anchor = "var targets=['home','types','collect','services','collect'];"
add = anchor + "\n  var sc2=document.getElementById('scene'); if(sc2) sc2.setAttribute('aria-label','EcoGreen living world');"
if "aria-label','EcoGreen living world'" not in src:
    open("sylva-hero.html", "w", encoding="utf-8").write(src.replace(anchor, add, 1))
    print("aria-label added")
else:
    print("already patched")