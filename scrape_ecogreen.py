import json, re, time, urllib.parse as up
import requests
from bs4 import BeautifulSoup

BASE = "https://ecogreen.eco"
MAX_PAGES = 15
S = requests.Session()
S.headers.update({"User-Agent": "EcoGreenSiteBuild/1.0 (client content audit)"})

def clean(t): return re.sub(r"\s+", " ", t or "").strip()

seen, pages = set(), []
queue = [BASE]
while queue and len(seen) < MAX_PAGES:
    url = queue.pop(0)
    if url in seen: continue
    seen.add(url)
    try:
        r = S.get(url, timeout=15)
    except Exception as e:
        print("fail", url, e); continue
    if "text/html" not in r.headers.get("content-type", ""): continue
    soup = BeautifulSoup(r.text, "html.parser")
    for t in soup(["script", "style", "noscript"]): t.decompose()

    links = []
    for a in soup.find_all("a", href=True):
        h = up.urljoin(url, a["href"].split("#")[0])
        if h.startswith(BASE) and h not in seen:
            queue.append(h)
            label = clean(a.get_text())
            if label: links.append(f"{label} -> {h}")

    blocks = [clean(el.get_text()) for el in soup.find_all(["h1", "h2", "h3", "p", "li"])]
    blocks = [b for b in blocks if len(b) > 2]
    meta = soup.find("meta", attrs={"name": "description"})
    pages.append({
        "url": url,
        "title": clean(soup.title.string) if soup.title else "",
        "meta_description": clean(meta["content"]) if meta else "",
        "copy_blocks": blocks[:100],
        "nav_links": links[:40],
        "emails": sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", r.text))),
        "phones": sorted(set(re.findall(r"\+?\d[\d\s\-()]{7,}\d", soup.get_text())))[:6],
        "images": [(i.get("src", ""), i.get("alt", "")) for i in soup.find_all("img")][:30],
    })
    print("ok", url, f"({len(blocks)} blocks)")
    time.sleep(1)  # be polite

json.dump(pages, open("site-content.json", "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)

md = []
for p in pages:
    md.append(f"\n## {p['title'] or p['url']}\n_{p['url']}_\n")
    if p["meta_description"]: md.append(p["meta_description"] + "\n")
    md += [f"- {b}" for b in p["copy_blocks"]]
    if p["emails"]: md.append("\nEmails: " + ", ".join(p["emails"]))
    if p["phones"]: md.append("Phones: " + ", ".join(p["phones"]))
open("site-content.md", "w", encoding="utf-8").write("\n".join(md))
print("\nsite-content.json + site-content.md written")