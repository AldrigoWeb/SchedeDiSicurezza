import os
from datetime import datetime

# Cartella dei loghi
logo_folder = "img"
output_file = "loghi.html"

# Trova tutti i file _logo.png nella cartella img
loghi = [f for f in os.listdir(logo_folder) if f.endswith("_logo.png")]
loghi.sort()  # ordinati alfabeticamente

# Backup del vecchio file HTML se esiste
if os.path.exists(output_file):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.rename(output_file, f"{output_file}.backup_{timestamp}")
    print(f"Backup creato: {output_file}.backup_{timestamp}")

# Inizio HTML
html = """
<section id="loghi">
  <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:15px;">
"""

# Genera il blocco per ciascun logo
for logo in loghi:
    nome = os.path.splitext(logo)[0].replace("_logo","")
    html += f'''
    <div style="flex:1 1 45%; text-align:center; min-width:120px; max-width:200px;">
        <img src="{logo_folder}/{logo}" alt="{nome}" style="width:100%; height:auto; max-height:100px;">
    </div>
    '''

# Chiusura HTML
html += """
  </div>
</section>
"""

# Scrivi su file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"{len(loghi)} loghi generati in {output_file} ✅")