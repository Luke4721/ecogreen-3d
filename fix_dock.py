P = "ecogreen.html"
src = open(P, encoding="utf-8").read()

if "egDockLogic" in src:
    print("already patched")
else:
    JS = """
<script data-egdock-logic>
/* egDockLogic */
(function(){
  const dock = document.getElementById('egDock');
  if (!dock) return;
  const vis = () => dock.classList.toggle('hide', scrollY < innerHeight * .85);
  vis(); addEventListener('scroll', vis, {passive:true});
  dock.addEventListener('click', e => {
    const a = e.target.closest('a'); if (!a) return;
    const t = document.querySelector(a.getAttribute('href'));
    if (t){ e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); }
  });
  const setSec = id => dock.querySelectorAll('.eg-item').forEach(a =>
    a.classList.toggle('on', a.dataset.sec === id));
  [['#types','types'],['#collect','process'],['#sort','process'],['#extrude','process'],
   ['#convert','process'],['#services','services'],['#join','join']].forEach(([sel,id]) => {
    const el = document.querySelector(sel);
    if (el && window.ScrollTrigger){
      ScrollTrigger.create({trigger:sel, start:'top center', end:'bottom center',
        onToggle: s => { if (s.isActive) setSec(id); }});
    }
  });
})();
</script>
"""
    if "</body>" in src:
        src = src.replace("</body>", JS + "\n</body>", 1)
        open(P, "w", encoding="utf-8").write(src)
        print("ok     dock logic appended before </body>")
    else:
        print("MISS   </body> — file may be truncated, tell me")