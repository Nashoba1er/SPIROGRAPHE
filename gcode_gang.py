from json import dump, load
from os import path


def couleur(color):
    match color:
        case "BLACK":
            return (0, 0, 0)
        case "GRAY":
            return (150, 127, 127)
        case "WHITE":
            return (255, 255, 255)
        case "RED":
            return (255, 0, 0)
        case "GREEN":
            return (0, 255, 0)
        case "BLUE":
            return (0, 0, 255)
        case "YELLOW":
            return (255, 255, 0)
        case "CYAN":
            return (0, 255, 255)
        case "MAGENTA":
            return (255, 0, 255)
        case "PINK":
            return (255, 0, 128)
        case "PINK2":
            return (255, 20, 147)
        case "PINK3":
            return (255, 192, 203)
        case "C1_GREEN":
            return (204, 255, 204)
        case "C1_BLUE":
            return (153, 204, 255)
        case "BG_COLOR":
            return (127, 127, 255)
        case "VERT":
            return (0, 200, 0)
        case "ORANGE":
            return (255, 130, 0)
        case "MARRON":
            return (110, 42, 42)
        case "ROSE_CLAIR":
            return (255, 182, 193)
        case "VIOLET_FONCE":
            return (148, 0, 211)
        case "BLEU_FONCE":
            return (0, 0, 150)
        case "GRIS_CLAIR":
            return (200, 200, 200)
        case "VERT_CLAIR":
            return (150, 255, 150)
        case "SAUGE_LOANN":
            return (146, 166, 157)
        case "ROSE_POUDREE":
            return (204, 153, 159)
        case "BLEU_JOLI":
            return (169, 184, 204)
        case _:
            raise ValueError(f"Unknown color name: {color}")



# Set les couleurs et valeurs rempli lors de la dernière utilisation
# Construire le chemin vers le fichier JSON
current_dir = path.dirname(__file__)  # Répertoire actuel du script
file_path = path.join(current_dir, "ressources", "data.json")
try:
  with open(file_path, "r") as file:
      data = load(file)
      couleur_param = data.get("couleur_param", "(255,255,255)")  # Valeur par défaut 0 si "x" n'existe pas
      couleur_fond = data.get("couleur_fond", "(153, 204, 255)")  # Valeur par défaut 0 si "x" n'existe pas
      couleur_rendu = data.get("couleur_rendu", "(169, 184, 204)")  # Valeur par défaut 0 si "x" n'existe pas

except FileNotFoundError:
    couleur_rendu = (255,255,255)
    couleur_fond = couleur("C1_BLUE")
    couleur_param = couleur("BLEU_JOLI")

print(f"La valeur actuelle de couleur_param est : {couleur_param}")



data = {
    "couleur_fond" : str(couleur_fond),
    "couleur_param": str(couleur_param),
    "couleur_rendu": str(couleur_rendu)}

with open(file_path, "w") as file:
    dump(data, file)