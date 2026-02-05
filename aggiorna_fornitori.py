import os

# Percorso della cartella principale dei fornitori
cartella_principale = "SCHEDE_FITOSANITARI"

# Percorso del file index.html principale
index_file = "index.html"

# Legge l'header e lo stile del file esistente
header = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Fornitori</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 15px; }
        h1 { text-align: center; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        li a { text-decoration: none; color: #007bff; font-weight: bold; }
        li a:hover { text-decoration: underline; }
    </style>
</head>
<body>

<h1>Elenco Fornitori</h1>
<ul>
"""

footer = """
</ul>
</body>
</html>
"""

# Prende tutte le cartelle nella cartella principale
fornitori = [f for f in os.listdir(cartella_principale) if os.path.isdir(os.path.join(cartella_principale, f))]
fornitori.sort()  # opzionale, ordina alfabeticamente

# Crea il contenuto dei link
links = ""
for f in fornitori:
    links += f'    <li><a href="{cartella_principale}/{f}/index.html">{f}</a></li>\n'

# Scrive tutto nel file index.html
with open(index_file, "w", encoding="utf-8") as f:
    f.write(header + links + footer)

print("Index aggiornato con tutti i fornitori trovati!")
