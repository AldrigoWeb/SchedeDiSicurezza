import os
import json

cartella_principale = "SCHEDE_FITOSANITARI"
output_file = "pdflist.js"

pdf_list = []

# Scansiona tutte le cartelle dei fornitori
for fornitore in os.listdir(cartella_principale):
    percorso_fornitore = os.path.join(cartella_principale, fornitore)
    if os.path.isdir(percorso_fornitore):
        for file in os.listdir(percorso_fornitore):
            if file.lower().endswith(".pdf"):
                # Salva percorso relativo
                percorso_relativo = f"{cartella_principale}/{fornitore}/{file}"
                pdf_list.append(percorso_relativo)

# Scrive il file pdflist.js
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const pdflist = ")
    json.dump(pdf_list, f, ensure_ascii=False, indent=2)
    f.write(";")

print(f"{len(pdf_list)} PDF registrati in {output_file}")
