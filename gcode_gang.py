import os
import json

# Données JSON
data = {
    "nom": "Alice",
    "âge": 30,
    "langages": ["Python", "JavaScript"],
    "actif": True,
    "note": None
}

# Définir le chemin du dossier et du fichier
dossier = "prout"
fichier_json = os.path.join(dossier, "data.json")

# Créer le dossier s'il n'existe pas
os.makedirs(dossier, exist_ok=True)

# Écrire les données dans le fichier JSON
with open(fichier_json, "w") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Fichier JSON créé à : {fichier_json}")
