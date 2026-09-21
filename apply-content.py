P = "ecogreen.html"
HERO = "sylva-hero-embed.html"
src = open(P, encoding="utf-8").read()

def rep(s, label, old, new):
    if new in s and old not in s:
        print(f"skip    {label} (already applied)"); return s, True
    if old in s:
        print(f"ok      {label}"); return s.replace(old, new, 1), True
    print(f"MISS    {label}"); return s, False

all_ok = True

# ---------- 1. intro paragraph: multi-material story ----------
src, ok = rep(src, "intro",
"""Most electronics serve us for a few years, then get buried. We built a better loop:
      devices are collected, data is destroyed, materials are recovered — and fed back into
      new products, over and over.""",
"""Every year, electronics, plastics, paper and metals are used once, then buried.
      Eco Green built a better loop: we collect, certify and dismantle — recovering
      metal, plastic and fibre, and feeding it all back into new products, over and over.""")
all_ok &= ok

# ---------- 2. impact paragraph, grounded in their claims ----------
src, ok = rep(src, "impact",
"""One laptop kept out of a landfill comes back as recovered aluminium, copper and
      engineering plastic — feeding new devices instead of digging new ore. Multiply that
      by a city.""",
"""Recycling aluminium uses a fraction of the energy of smelting it from ore. Recovered
      copper, steel and paper cut mining and logging pressure alike. Multiply one load by a
      city, a state, an industry — that is the scale of the difference.""")
all_ok &= ok

# ---------- 3. carousel: 5 streams per their site ----------
cards = [
("card-1", """<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 100 70" fill="none" stroke="currentColor" stroke-width="2"><rect x="18" y="8" width="64" height="42" rx="3"/><path d="M8 62h84l-6-10H14z"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">PHONES &amp; LAPTOPS</p>""",
"""<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 100 70" fill="none" stroke="currentColor" stroke-width="2"><rect x="18" y="8" width="64" height="42" rx="3"/><path d="M8 62h84l-6-10H14z"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">E-WASTE · ALL DEVICES</p>"""),
("card-2", """<svg class="h-32 text-neutral-600 group-hover:scale-105 transition" viewBox="0 0 40 80" fill="none" stroke="currentColor" stroke-width="2"><rect x="8" y="14" width="24" height="52" rx="3"/><rect x="14" y="8" width="12" height="6"/><path d="M14 26h12M14 38h12M14 50h12"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">BATTERIES</p>""",
"""<svg class="h-32 text-neutral-600 group-hover:scale-105 transition" viewBox="0 0 40 80" fill="none" stroke="currentColor" stroke-width="2"><rect x="8" y="14" width="24" height="52" rx="3"/><rect x="14" y="8" width="12" height="6"/><path d="M14 26h12M14 38h12M14 50h12"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">LITHIUM BATTERIES</p>"""),
("card-3", """<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 80 80" fill="none" stroke="currentColor" stroke-width="2"><path d="M30 10v14M50 10v14"/><path d="M22 24h36v12c0 12-8 20-18 20S22 48 22 36z"/><path d="M40 56v12M28 74h24"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">CABLES &amp; CHARGERS</p>""",
"""<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 80 80" fill="none" stroke="currentColor" stroke-width="2"><path d="M26 14h28v14l-6 8v30a8 8 0 0 1-16 0V36l-6-8z"/><path d="M26 22h28"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">PLASTIC</p>"""),
("card-4", """<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 100 80" fill="none" stroke="currentColor" stroke-width="2"><rect x="10" y="10" width="80" height="50" rx="3"/><path d="M40 74h20M50 60v14"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">MONITORS &amp; TVs</p>""",
"""<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 100 80" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 52l14-24h44l14 24z"/><path d="M14 52v14h72V52M32 52V40h16v12M60 40v12"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">METALS · ALU · CU · IRON</p>"""),
("card-5", """<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 80 90" fill="none" stroke="currentColor" stroke-width="2"><rect x="12" y="8" width="56" height="74" rx="5"/><circle cx="40" cy="48" r="16"/><circle cx="40" cy="48" r="7"/><path d="M22 18h12"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">APPLIANCES</p>""",
"""<svg class="h-32 text-neutral-500 group-hover:scale-105 transition" viewBox="0 0 80 90" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 10h40v70H16zM24 22h24M24 34h24M24 46h18"/><path d="M62 30h8v50h-8z"/></svg>
          </div><p class="mt-3 text-xs font-semibold tracking-[0.2em]">PAPER &amp; BOOKS</p>"""),
]
for label, old, new in cards:
    src, ok = rep(src, label, old, new); all_ok &= ok

# ---------- 4. services: their real six ----------
svc = [
("svc-1", ">IT asset disposition</h4>",
         ">E-Waste recycling</h4>"),
("svc-1p", "Full decommissioning at scale — audit, wipe, refurbish or recycle, with reporting at every step.",
           "Secure collection and responsible dismantling of end-of-life electronics — hazardous parts handled safely, valuable components recovered."),
("svc-2", ">Certified data destruction</h4>",
          ">Lithium battery recycling</h4>"),
("svc-2p", "Drive wiping and shredding with certificates you can file — nothing leaves recoverable.",
           "Safe discharge, shredding and chemical separation that recovers up to 95% of battery components while neutralising fire and toxicity risk."),
("svc-3", ">Bulk &amp; event collection</h4>",
          ">Plastic recycling</h4>"),
("svc-3p", "Office clear-outs, campus drives and pop-up events — we plan, crew and haul, end to end.",
           "Sorted, cleaned and regranulated into reusable feedstock — diverting plastic waste from landfill and oceans at scale."),
("svc-4", ">Battery &amp; peripherals</h4>",
          ">Paper recycling</h4>"),
("svc-4p", "Safe, compliant channels for lithium batteries, cables, chargers and accessories.",
           "High-efficiency pulping and baling that returns paper and books to fibre — conserving forests and cutting virgin pulp demand."),
("svc-5", ">ESG &amp; compliance reporting</h4>",
          ">Metal recycling</h4>"),
("svc-5p", "Weights, diversion rates and certificates — formatted for your sustainability reports.",
           "Advanced magnetic separation and granulation for aluminium, copper and iron — feeding industry without opening new mines."),
("svc-6", ">Drop-off hubs</h4>",
          ">EPR compliance</h4>"),
("svc-6p", "Bring devices to a hub near you — open to households and small businesses alike.",
           "Extended Producer Responsibility handled end to end — collection targets, documentation and filings, audit-ready."),
]
for label, old, new in svc:
    src, ok = rep(src, label, old, new); all_ok &= ok

# ---------- 5. CTA: real contact ----------
src, ok = rep(src, "cta-link",
'<a href="#" class="inline-block mt-10 bg-[#08130C] text-white text-xs tracking-[0.25em] uppercase px-12 py-5 rounded-full hover:scale-105 transition shadow-xl">Get involved</a>',
'''<a href="mailto:operation@ecogreen.eco" class="inline-block mt-10 bg-[#08130C] text-white text-xs tracking-[0.25em] uppercase px-12 py-5 rounded-full hover:scale-105 transition shadow-xl">Start a pickup</a>
    <p class="mt-6 text-white/70 text-sm"><a href="tel:+919319253708" class="underline hover:text-white">+91 93192 53708</a> · <a href="mailto:operation@ecogreen.eco" class="underline hover:text-white">operation@ecogreen.eco</a><br>
    <span class="text-white/50 text-xs">Eco Green Recyclers (P) Ltd · Plot 479, Habibpur, Dadri Road, Greater Noida 201306</span></p>''')
all_ok &= ok

# ---------- 6. hero stats (sylva embed): verifiable, no invented tonnage ----------
if __import__('os').path.exists(HERO):
    h = open(HERO, encoding="utf-8").read()
    h, ok = rep(h, "hero-stat-1",
        "Devices renewed</dt><dd>1.2M kg</dd>", "Recycling streams</dt><dd>5 + EPR</dd>")
    all_ok &= ok
    h, ok = rep(h, "hero-stat-2",
        "Materials recovered</dt><dd>96.4%</dd>", "Materials recovered</dt><dd>Metal · Plastic · Paper</dd>")
    all_ok &= ok
    open(HERO, "w", encoding="utf-8").write(h)
else:
    print("WARN    sylva-hero-embed.html not found — hero stats not patched")

open(P, "w", encoding="utf-8").write(src)
print("\nDONE — content pass applied." if all_ok else "\nDONE with MISSes — send me the MISS lines.")