import os

# Cartella principale dei fornitori
cartella_principale = "SCHEDE_FITOSANITARI"

# File index.html principale
index_file = "index.html"

# Header del file (include la barra di ricerca PDF)
header = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Cerca SDS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 15px; }
        h1 { text-align: center; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        li a { text-decoration: none; color: #007bff; font-weight: bold; }
        li a:hover { text-decoration: underline; }
        #searchBox { width: 100%; padding: 8px; font-size: 16px; margin-bottom: 10px; }
        #searchResults li { margin: 3px 0; }
    </style>
</head>
<body>

<h1>Cerca Schede di Sicurezza (SDS)</h1>

<h2>🔍 Cerca PDF</h2>
<input type="text" id="searchBox" placeholder="Scrivi il nome del prodotto...">
<ul id="searchResults"></ul>

<p>Seleziona il fornitore per vedere le schede dei prodotti:</p>
<ul>
"""

# Footer del file (include script della barra di ricerca)
footer = """
</ul>

<!-- Script di ricerca PDF -->
<script src="pdfList.js"></script>
<script>
const searchBox = document.getElementById("searchBox");
const results = document.getElementById("searchResults");

searchBox.addEventListener("input", function() {
    const query = this.value.toLowerCase();
    results.innerHTML = "";

    if(query === "") return;

    const filtered = pdfList.filter(pdf => pdf.toLowerCase().includes(query));

    if(filtered.length === 0){
        results.innerHTML = "<li>Nessun PDF trovato</li>";
        return;
    }

    filtered.forEach(pdf => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${pdf}" target="_blank">${pdf.split("/").pop()}</a>`;
        results.appendChild(li);
    });
});
</script>

</body>
</html>
"""

# Prende tutte le cartelle dei fornitori
fornitori = [f for f in os.listdir(cartella_principale) if os.path.isdir(os.path.join(cartella_principale, f))]
fornitori.sort()  # ordina alfabeticamente

# Crea i link per i fornitori
links = ""
for f in fornitori:
    links += f'    <li><a href="{cartella_principale}/{f}/index.html">{f}</a></li>\n'

# Scrive il file index.html completo
with open(index_file, "w", encoding="utf-8") as f:
    f.write(header + links + footer)

print("Index aggiornato con tutti i fornitori e barra di ricerca!")
