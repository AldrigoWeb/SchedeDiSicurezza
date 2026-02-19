import shutil
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("SCHEDE_FITOSANITARI")
PDFLIST_FILE = Path("pdfList.js")
INDEX_FILE = Path("index.html")

# =========================
# BACKUP AUTOMATICO
# =========================
def backup_file(file_path):
    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = file_path.with_suffix(file_path.suffix + f".backup_{timestamp}")
        shutil.copy(file_path, backup_name)
        print(f"Backup creato: {backup_name.name}")

# =========================
# GENERA pdfList.js
# =========================
def genera_pdf_list():
    pdf_paths = []

    for fornitore in sorted(BASE_DIR.iterdir(), key=lambda x: x.name):
        if fornitore.is_dir():
            for file in sorted(fornitore.iterdir(), key=lambda x: x.name):
                if file.is_file() and file.suffix.lower() == ".pdf":
                    pdf_paths.append(file.as_posix())

    backup_file(PDFLIST_FILE)

    with open(PDFLIST_FILE, "w", encoding="utf-8") as f:
        f.write("const pdfList = [\n")
        for path in pdf_paths:
            f.write(f'    "{path}",\n')
        f.write("];\n")

    print(f"pdfList.js aggiornato ({len(pdf_paths)} PDF trovati)")

# =========================
# AGGIORNA BLOCCO FORNITORI
# =========================
def aggiorna_index_principale():
    if not INDEX_FILE.exists():
        print("index.html non trovato.")
        return

    fornitori_html = []

    for fornitore in sorted(BASE_DIR.iterdir(), key=lambda x: x.name):
        if fornitore.is_dir():
            nome_visibile = fornitore.name.replace("_", " ")
            link = f"SCHEDE_FITOSANITARI/{fornitore.name}/index.html"
            fornitori_html.append(
                f'    <a class="fornitore" href="{link}">{nome_visibile}</a>'
            )

    nuovo_blocco = "<div class=\"fornitori\">\n" + "\n".join(fornitori_html) + "\n</div>"

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        contenuto = f.read()

    contenuto_nuovo = re.sub(
        r"<div class=\"fornitori\">.*?</div>",
        nuovo_blocco,
        contenuto,
        flags=re.DOTALL
    )

    backup_file(INDEX_FILE)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(contenuto_nuovo)

    print("Blocco fornitori aggiornato in index.html")

# =========================
# CREA index.html FORNITORE
# =========================
def crea_index_fornitore():
    for fornitore in sorted(BASE_DIR.iterdir(), key=lambda x: x.name):
        if fornitore.is_dir():
            index_path = fornitore / "index.html"

            pdf_links = []
            for file in sorted(fornitore.iterdir(), key=lambda x: x.name):
                if file.is_file() and file.suffix.lower() == ".pdf":
                    pdf_links.append(
                        f'<li><a href="{file.name}" target="_blank">{file.name}</a></li>'
                    )

            html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>{fornitore.name}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{ font-family: Arial; max-width: 800px; margin: 40px auto; }}
h1 {{ color: #1f3a5f; }}
a {{ text-decoration: none; color: #1f3a5f; }}
li {{ margin-bottom: 8px; }}
</style>
</head>
<body>
<h1>{fornitore.name.replace("_"," ")}</h1>
<ul>
{''.join(pdf_links)}
</ul>
<p><a href="../../index.html">← Torna alla home</a></p>
</body>
</html>"""

            with open(index_path, "w", encoding="utf-8") as f:
                f.write(html)

    print("Index dei fornitori rigenerati")

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    if not BASE_DIR.exists():
        print("Cartella SCHEDE_FITOSANITARI non trovata.")
    else:
        genera_pdf_list()
        aggiorna_index_principale()
        crea_index_fornitore()
        print("\nSITO AGGIORNATO CORRETTAMENTE ✅")
