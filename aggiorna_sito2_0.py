import os
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "img")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")


def crea_backup(file_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}.backup_{timestamp}"
    with open(file_path, "r", encoding="utf-8") as f:
        contenuto = f.read()
    with open(backup_path, "w", encoding="utf-8") as f:
        f.write(contenuto)
    print(f"Backup creato: {os.path.basename(backup_path)}")


def trova_loghi():
    loghi = []
    for file in os.listdir(IMG_DIR):
        nome, est = os.path.splitext(file)
        if nome.lower().endswith("_logo") and est.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            loghi.append(file)
    loghi.sort()
    return loghi


def genera_blocco_loghi(lista_loghi):
    blocco = '    <div class="logoCRA">\n'
    for logo in lista_loghi:
        alt = logo.replace("_logo", "").replace("_", " ").title()
        blocco += f'        <img src="img/{logo}" alt="Logo {alt}">\n'
    blocco += "    </div>"
    return blocco


def aggiorna_css(contenuto):
    nuovo_css = """
        .contatti .logoCRA {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            align-items: center;
            justify-items: center;
        }

        .contatti .logoCRA img {
            max-width: 120px;
            height: auto;
        }
    """

    if ".contatti .logoCRA {" not in contenuto:
        contenuto = contenuto.replace("</style>", nuovo_css + "\n</style>")
        print("CSS loghi a 2 colonne inserito automaticamente")
    else:
        print("CSS già presente")

    return contenuto


def aggiorna_index():
    if not os.path.exists(INDEX_FILE):
        print("ERRORE: index.html non trovato")
        return

    crea_backup(INDEX_FILE)

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        contenuto = f.read()

    loghi = trova_loghi()
    if not loghi:
        print("Nessun logo trovato in img/")
        return

    nuovo_blocco = genera_blocco_loghi(loghi)

    pattern = r'<div class="logoCRA">.*?</div>'
    contenuto = re.sub(pattern, nuovo_blocco, contenuto, flags=re.DOTALL)

    contenuto = aggiorna_css(contenuto)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(contenuto)

    print(f"{len(loghi)} loghi aggiornati automaticamente")
    print("Logo messi in 2 colonne ✅")


if __name__ == "__main__":
    aggiorna_index()