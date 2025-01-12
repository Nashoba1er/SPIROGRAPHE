import os
import json


# Construire le chemin vers le fichier JSON
current_dir = os.path.dirname(__file__)  # Répertoire actuel du script
file_path = os.path.join(current_dir, "ressources", "data.json")

if os.path.exists(file_path):
    print("Fichier trouvé :", file_path)
else:
    print("Fichier introuvable :", file_path)

# Charger les données JSON
with open(file_path, "r") as file:
    data = json.load(file)
    print(data)