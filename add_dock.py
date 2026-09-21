src = open("ecogreen.html", encoding="utf-8").read()
if "egdock" in src:
    raise SystemExit("dock already injected")

CSS = """
  /* ---- EcoGreen prime dock (Sylva-consistent) ---- */
  @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600&display=swap');
  .egdock{position:fixed;z-index:60;top:18px;left:50%;transform:translateX(-50%);
    display:flex;align-items:center;gap:4px;padding:5px;border-radius:14px;
    border:1px solid rgba(255,255,255,.11);
    background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,0) 42%),rgba(24,32,24,.78);
    box-shadow:0 8px 22px rgba(6,12,6,.35),inset 0 1px rgba(255,255,255,.06);
    font-family:'Lexend',sans-serif;
    transition:transform .5s cubic-bezier(.22,.61,.36,1),opacity .5s;}
  .egdock.hide{transform:translateX(-50%) translateY(-160%);opacity:0;pointer-events:none}
  .eg-item{display:inline-flex;align-items:center;justify-content:center;gap:8px;
    height:36px;padding:0 14px;border-radius:10px;border:1px solid transparent;
    background:rgba(255,255,255,.04);color:rgba(255,255,255,.62);
    text-decoration:none;font-size:11px;font-weight:500;letter-spacing:1.5px;
    text-transform:uppercase;white-space:nowrap;
    transition:color .18s,border-color .2s,background .2s}
  .eg-item:hover{color:#fff;border-color:rgba(255,255,255,.19);background:rgba(31,37,28,.94)}
  .eg-item.on{background:#F7F4ED;border-color:#F7F4ED;color:#23261f}
  .eg-item .g{width:14px;height:14px;flex:none;opacity:.66}
  .eg-item .g svg{display:block;width:100%;height:100%;fill:none;stroke:currentColor;
    stroke-width:1.25;stroke-linecap:round;stroke-linejoin:round}
  .eg-mark{width:36px;padding:0;background:#eef1e7;border-color:#eef1e7;color:#23261f}
  .eg-mark svg{width:58%;height:58%;display:block;fill:currentColor;stroke:none}
  .eg-enter{background:rgba(69,199,78,.16)!important;color:#d9ffe0!important}
  .eg-enter:hover{background:rgba(69,199,78,.28)!important}
  @media (max-width:900px){
    .egdock{padding:6px;gap:4px;border-radius:17px}
    .eg-item{width:44px;height:44px;padding:0;border-radius:12px}
    .eg-item .l{display:none}
    .eg-item .g{width:19px;height:19px;opacity:1}
  }
"""
HTML = """
<!-- EcoGreen prime dock -->
<nav id="egDock" class="egdock hide" aria-label="EcoGreen primary">
  <a class="eg-item eg-mark" href="#hero" aria-label="EcoGreen — home">
    <svg viewBox="0 0 24 24"><path d="M12 2C7 7 4 11 4 15a8 8 0 0 0 16 0c0-4-3-8-8-13z"/></svg>
  </a>
  <a class="eg-item" href="#types" data-sec="types">
    <span class="g"><svg viewBox="0 0 16 16"><path d="M8 14V9"/><path d="M8 9c0-2.4 1.7-4.3 4-4.3.2 2.6-1.6 4.6-4 4.3Z"/><path d="M8 10.5C7.9 8.4 6.4 6.8 4.4 6.8 4.3 8.9 5.9 10.6 8 10.5Z"/></svg></span>
    <span class="l">What we take</span></a>
  <a class="eg-item" href="#collect" data-sec="process">
    <span class="g"><svg viewBox="0 0 16 16"><path d="M1.6 12.4c2.4-3.4 4.3-5.1 5.7-5.1 2 0 3 3.6 5 3.6 1.1 0 1.9-.5 2.4-1.4"/><path d="M4.3 6.2C5.5 4.4 6.6 3.5 7.6 3.5c1.5 0 2.2 2.4 3.7 2.4"/></svg></span>
    <span class="l">Process</span></a>
  <a class="eg-item" href="#services" data-sec="services">
    <span class="g"><svg viewBox="0 0 16 16"><path d="M4 2.4h5.3L12 5.1v8.5H4z"/><path d="M9.2 2.4V5h2.7"/><path d="M6 8.4h4M6 10.8h2.8"/></svg></span>
    <span class="l">Services</span></a>
  <a class="eg-item eg-enter" href="#join" data-sec="join">
    <span class="g"><svg viewBox="0 0 16 16"><path d="M6.6 2.5h5.1a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H6.6"/><path d="M2.6 8h6.6"/><path d="m7 5.6 2.4 2.4L7 10.4"/></svg></span>
    <span class="l">Enter</span></a>
</nav>
"""
JS = """
/* ================= prime dock ================= */
(function(){
  const dock = document.getElementById('egDock');
  if (!dock) return;
  dock.addEventListener('click', e => {
    const a = e.target.closest('a'); if (!a) return;
    const t = document.querySelector(a.getAttribute('href'));
    if (t){ e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); }
  });
  /* hide while the hero (and its own dock) is on screen */
  new IntersectionObserver(([en]) => {
    dock.classList.toggle('hide', en.isIntersecting);
  }, {threshold:.15}).observe(document.getElementById('hero'));
  /* active-section highlight */
  const setSec = id => {
    dock.querySelectorAll('.eg-item').forEach(a =>
      a.classList.toggle('on', a.dataset.sec === id));
  };
  [['#types','types'],['#collect','process'],['#sort','process'],['#extrude','process'],
   ['#convert','process'],['#services','services'],['#join','join']].forEach(([sel, id]) => {
    const el = document.querySelector(sel); if (!el) return;
    ScrollTrigger.create({trigger:sel, start:'top center', end:'bottom center',
      onToggle: s => { if (s.isActive) setSec(id); }});
  });
})();
"""

css_anchor = "  @media (prefers-reduced-motion:reduce){.flake,.wave,#sideSvg{animation:none!important}}"
html_anchor = "<!-- ============ PRELOADER ============ -->"
js_anchor = "/* ================= model status pill"

for label, anchor, block in [("css", css_anchor, CSS), ("html", html_anchor, HTML), ("js", js_anchor, JS)]:
    if anchor not in src:
        print(f"MISS {label} anchor — tell me"); continue
    src = src.replace(anchor, anchor + block if label != "css" else block + "\n" + anchor, 1)
    print(f"ok {label}")

open("ecogreen.html", "w", encoding="utf-8").write(src)
print("prime dock injected.")