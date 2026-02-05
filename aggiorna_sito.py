import os

# ============================
# CONFIGURAZIONE
# ============================

cartella_principale = "SCHEDE_FITOSANITARI"
pdfList_file = "pdfList.js"

# ============================
# FUNZIONI
# ============================

def rinomina_pdf(percorso_fornitore):
    """Rinomina tutti i PDF della cartella sostituendo spazi con underscore"""
    for file in os.listdir(percorso_fornitore):
        if file.lower().endswith(".pdf"):
            nuovo_nome = "_".join(file.split())
            if nuovo_nome != file:
                vecchio = os.path.join(percorso_fornitore, file)
                nuovo = os.path.join(percorso_fornitore, nuovo_nome)
                os.rename(vecchio, nuovo)
                print(f"[RINOMINATO] {file} → {nuovo_nome}")

def genera_index(percorso_fornitore, fornitore):
    """Genera index.html nella cartella del fornitore"""
    pdf_files = [f for f in os.listdir(percorso_fornitore) if f.lower().endswith(".pdf")]
    pdf_files.sort()

    content = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>{fornitore}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 15px; }}
        h1 {{ text-align: center; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 5px 0; }}
        li a {{ text-decoration: none; color: #007bff; font-weight: bold; }}
        li a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>

<h1>{fornitore}</h1>
<ul>
"""
    for pdf in pdf_files:
        content += f'    <li><a href="{pdf}">{pdf}</a></li>\n'

    content += f"""</ul>
<p><a href="../index.html">⬅ Torna all'elenco fornitori</a></p>
</body>
</html>
"""
    index_path = os.path.join(percorso_fornitore, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[INDEX GENERATO] {fornitore}/index.html")

def genera_pdfList_js(cartella_principale, output_file):
    """Genera pdfList.js con tutti i PDF di tutti i fornitori"""
    pdf_entries = []
    for fornitore in os.listdir(cartella_principale):
        percorso_fornitore = os.path.join(cartella_principale, fornitore)
        if os.path.isdir(percorso_fornitore):
            for file in os.listdir(percorso_fornitore):
                if file.lower().endswith(".pdf"):
                    path_relativo = f"{cartella_principale}/{fornitore}/{file}"
                    pdf_entries.append(path_relativo.replace("\\", "/"))

    pdf_entries.sort()
    js_content = "const pdfList = [\n"
    for pdf in pdf_entries:
        js_content += f'    "{pdf}",\n'
    js_content += "];\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"[PDFLIST GENERATO] {output_file} ({len(pdf_entries)} PDF)")

# ============================
# SCRIPT PRINCIPALE
# ============================

for fornitore in os.listdir(cartella_principale):
    percorso_fornitore = os.path.join(cartella_principale, fornitore)
    if os.path.isdir(percorso_fornitore):
        rinomina_pdf(percorso_fornitore)
        genera_index(percorso_fornitore, fornitore)

genera_pdfList_js(cartella_principale, pdfList_file)
print("\nTUTTO AGGIORNATO ✅")
