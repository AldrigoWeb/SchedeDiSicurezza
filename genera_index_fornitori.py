import os

FORNITORI_DIR = "SCHEDE_FITOSANITARI"
INDEX_PRINCIPALE = "../index.html"  # link torna all'elenco

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>{fornitore}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 15px;
        }}
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
{links}
</ul>

<p><a href="{indice_principale}">⬅ Torna all'elenco fornitori</a></p>
</body>
</html>
"""

for fornitore in sorted(os.listdir(FORNITORI_DIR)):
    cartella = os.path.join(FORNITORI_DIR, fornitore)
    if not os.path.isdir(cartella):
        continue

    # Trova tutti i PDF nella cartella
    pdf_files = sorted(f for f in os.listdir(cartella) if f.lower().endswith(".pdf"))
    if not pdf_files:
        print(f"⚠️ Nessun PDF per {fornitore}, index non creato")
        continue  # Salta cartelle vuote

    # Genera i link HTML
    links_html = "\n".join([f'    <li><a href="{f}">{f}</a></li>' for f in pdf_files])

    # Scrivi nuovo index.html
    index_path = os.path.join(cartella, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(
            fornitore=fornitore,
            links=links_html,
            indice_principale=INDEX_PRINCIPALE
        ))

    print(f"✔ index.html creato per {fornitore}")
