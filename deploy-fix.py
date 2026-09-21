import os, shutil, time

# copy ecogreen.html -> index.html (Vercel needs index.html at the root)
if not os.path.exists("ecogreen.html"):
    raise SystemExit("ecogreen.html not found")

st_e = os.path.getmtime("ecogreen.html")
st_i = os.path.getmtime("index.html") if os.path.exists("index.html") else 0

if st_e > st_i or not os.path.exists("index.html"):
    shutil.copy("ecogreen.html", "index.html")
    print("ok     index.html refreshed from ecogreen.html")
else:
    print("skip   index.html is already newer than ecogreen.html")
    print("       (did you forget to re-copy after a patch? delete index.html and re-run if unsure)")