import os, time

P = "ecogreen.html"
src = open(P, encoding="utf-8").read()
V = str(int(time.time()))          # deploy version = cache-bust key
ok = True

def rep(label, old, new):
    global src, ok
    if new in src and old not in src:
        print(f"skip    {label} (already applied)")
    elif old in src:
        src = src.replace(old, new, 1)
        print(f"ok      {label}")
    else:
        ok = False
        print(f"MISS    {label}")

# 1) cache-bust models-data.js + hero iframe on every deploy
rep("bust models-data",
    '<script src="models-data.js"></script>',
    '<script src="models-data.js?v=' + V + '"></script>')
rep("bust hero iframe",
    "sylvaFrame.src = 'sylva-hero-embed.html';",
    "sylvaFrame.src = 'sylva-hero-embed.html?v=" + V + "';")

# 2) self-healing loader: if ECO_MODELS is missing at boot, re-inject and retry
rep("boot block",
    "  ScrollTrigger.refresh();\n  startModelPipeline();",
    """  ScrollTrigger.refresh();
  if (window.ECO_MODELS){
    startModelPipeline();
  } else {
    console.warn('ECO_MODELS missing — re-injecting models-data.js with cache-bust');
    let tries = 0;
    const bootModels = () => {
      if (window.ECO_MODELS){ startModelPipeline(); return; }
      if (tries++ > 3){
        console.error('models-data.js failed to provide ECO_MODELS after retries');
        return;
      }
      const s = document.createElement('script');
      s.src = 'models-data.js?retry=' + Date.now();
      s.onload = bootModels;
      s.onerror = () => setTimeout(bootModels, 1500);
      document.head.appendChild(s);
      setTimeout(bootModels, 3000);
    };
    bootModels();
  }""")

# 3) Sort: one-shot swaps -> polling swaps (like Deliver already does)
rep("sort swaps",
    """  if (MODELS.conveyor){
    const c = fitModel(MODELS.conveyor, 10);
    c.position.set(-2, -1.54, -6.5); c.rotation.y = .35;
    S.add(c);
  }
  if (MODELS.robot_arm){
    const arm = fitModel(MODELS.robot_arm, 2.7);
    armHolder.add(arm);
    procArm.visible = false;
    const pivots = [];
    (function collect(n, depth){
      if (depth > 5 || pivots.length >= 5) return;
      const kids = n.children.filter(c => {
        let has = false; c.traverse(m => { if (m.isMesh) has = true; });
        return has && c.children.length;
      });
      kids.forEach(k => { pivots.push(k); collect(k, depth + 1); });
    })(arm, 0);
    armPivots = pivots;
  }""",
    """  const trySortModels = () => {
    if (MODELS.conveyor && !S.userData.conveyor){
      S.userData.conveyor = true;
      const c = fitModel(MODELS.conveyor, 10);
      c.position.set(-2, -1.54, -6.5); c.rotation.y = .35;
      S.add(c);
    }
    if (MODELS.robot_arm && !S.userData.arm){
      S.userData.arm = true;
      procArm.visible = false;
      const arm = fitModel(MODELS.robot_arm, 2.7);
      armHolder.add(arm);
      const pivots = [];
      (function collect(n, depth){
        if (depth > 5 || pivots.length >= 5) return;
        const kids = n.children.filter(c => {
          let has = false; c.traverse(m => { if (m.isMesh) has = true; });
          return has && c.children.length;
        });
        kids.forEach(k => { pivots.push(k); collect(k, depth + 1); });
      })(arm, 0);
      armPivots = pivots;
    }
    return !!(S.userData.conveyor && S.userData.arm);
  };
  trySortModels();
  const tSort = setInterval(() => {
    if (trySortModels()) clearInterval(tSort);
  }, 800);
  setTimeout(() => clearInterval(tSort), 90000);""")

open(P, "w", encoding="utf-8").write(src)
print("\nhotfix applied." if ok else "\napplied with MISSes — send them to me.")