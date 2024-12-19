# Spirographe: Génération de G-code pour Spirographe

Ce projet est une application graphique interactive écrite en Python avec la bibliothèque Pygame. Elle permet de visualiser et de personnaliser des modèles de spirographes. Vous pouvez ajuster les paramètres des cercles, générer des motifs, zoomer sur le rendu, et préparer des fichiers G-code pour des machines-outils.

---

## Fonctionnalités

### Menu principal
- L'application commence par un menu principal où vous pouvez choisir d'explorer les motifs spirographiques.

### Visualisation des cercles et motifs
- **Affichage du schéma spirographique**:
  - Deux cercles: un grand cercle et un petit cercle tournant à l'intérieur ou à l'extérieur du grand cercle.
  - Un point P, fixé sur le petit cercle, décrit le motif.
- **Zoom sur le schéma**:
  - Vous pouvez agrandir le schéma pour l’observer en détail.
- **Zoom sur le rendu**:
  - Visualisez uniquement le motif dessiné par le point P.

### Modification des paramètres
- Les paramètres du spirographe (r1, r2, p) sont modifiables via des champs de texte.
- Les curseurs permettent d’ajuster les valeurs rapidement et intuitivement.

### Navigation interactive
- **Clics**:
  - Cliquez sur les champs de texte pour les modifier.
  - Cliquez sur le schéma ou le rendu pour passer en mode zoom.
- **Souris**:
  - Survolez les boutons pour les surligner.
  - Faites glisser les curseurs pour ajuster les paramètres.
- **Clavier**:
  - Appuyez sur « Entrée » pour valider les paramètres et visualiser les changements.
  - Utilisez les flèches haut/bas pour ajuster les paramètres numériques.

### Génération de fichiers G-code
- (Fonctionnalité en préparation) Possibilité de générer un fichier G-code pour reproduire le motif avec une machine-outil CNC.

---

## Structure du projet

### Fonctions principales

#### Visualisation
- **`cercles`** : Affiche le schéma du spirographe avec les deux cercles et le point P.
- **`zoom_cercles`** : Affiche une vue agrandie du schéma.
- **`rendu`** : Dessine le motif décrit par le point P.
- **`zoom_rendu`** : Affiche une vue agrandie du motif.

#### Interactions
- **`clic`** : Gère les clics de souris pour changer de mode ou ajuster les paramètres.
- **`bouge_curseur`** : Permet de déplacer un curseur pour ajuster un paramètre.
- **`input_to_text`** : Gère l’entrée clavier pour modifier les champs de texte.

#### Navigation
- **`menu_cercle_dans_cercle_init`** : Initialise le menu pour visualiser le spirographe.
- **`menu_choix`** : Affiche le menu principal.

### Variables globales
- **Paramètres des cercles**:
  - `r1`, `r2`, `p` : Rayons des cercles et distance du point P.
- **Couleurs**:
  - Différentes couleurs pour les éléments graphiques (« ROUGE », « BLEU_FONCÉ », etc.).
- **États de l’application**:
  - Variables comme `run`, `run_visu_2D`, `run_zoom_schema` pour gérer les différents modes d’exécution.

---

## Installation et exécution

### Prérequis
- Python 3.x
- Bibliothèque Pygame

### Installation
1. Clonez le dépôt depuis GitHub :
   ```bash
   git clone <URL_DU_DEPOT>
   ```
2. Installez les dépendances :
   ```bash
   pip install pygame
   ```

### Exécution
Lancez le script principal :
```bash
python main.py
```

---

## Améliorations futures
- Ajout de la fonctionnalité de génération de fichiers G-code.
- Optimisation des performances pour le rendu graphique.
- Support pour différents types de spirographes.
- Interface utilisateur améliorée.

---

## Contributeurs
- **Votre nom ou pseudonyme**

---

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d’informations.

