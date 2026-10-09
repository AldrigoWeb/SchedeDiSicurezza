import os, shutil

VECCHIO = "© 2025 Pengo &amp; Zanovello – Tutti i diritti riservati"
NUOVO = "© Andrea Aldrigo &amp; C. SAS – Tutti i diritti riservati"

for root, _, files in os.walk("SCHEDE_FITOSANITARI"):
    if "index.html" in files:
        p = os.path.join(root, "index.html")
        with open(p, encoding="utf-8", newline="") as f:
            html = f.read()
        if VECCHIO in html:
            shutil.copy2(p, p + ".bak")
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(html.replace(VECCHIO, NUOVO))
            print("footer corretto:", p)