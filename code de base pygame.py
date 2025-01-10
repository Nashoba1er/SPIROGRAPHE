import numpy as np
from math import *
from pygame import *
import tkinter as tk
from tkinter import filedialog

def points_3d (theta_max, N, petit_r, grand_r, p, Rsphere) :
  #retourne la liste des points en 3D de coordonée z qui varie selon le rayon Rsphere si (grand_r-petit_r+p)<=Rpshere
  #retourne la liste des points en 3D de coordonée z fixe égale à 0 si Rsphere = 0
    theta = np.linspace(0.0, theta_max, N)
    diff_r = grand_r - petit_r
    q = 1.0 - (grand_r/petit_r) #arrangez vous pour que ce rapport soit différent de 1/2
    max_dist = diff_r + p
    res = []
    if (Rsphere == 0) :
      for i in range (N) :
        new_x = diff_r*np.cos(theta[i]) + p * np.cos(q*theta[i])
        new_y = diff_r*np.sin(theta[i]) + p * np.sin(q*theta[i])
        z = 0
        res.append((new_x, new_y, z))
    elif (max_dist<=Rsphere) :
      for i in range (N) :
        new_x = diff_r*np.cos(theta[i]) + p * np.cos(q*theta[i])
        new_y = diff_r*np.sin(theta[i]) + p * np.sin(q*theta[i])
        z = sqrt(Rsphere*Rsphere - new_x*new_x - new_y*new_y) - sqrt (Rsphere*Rsphere - max_dist*max_dist)
        res.append((new_x, new_y, z))
    else :
        print("le motif est trop grand pour la sphere")
    return res

def generate_gcode_points(points, extrusion_rate=0.05, layer_height=0.2):
  #genere le gcode à partir d'une liste de points
    gcode = []
    gcode.append("; Début du fichier G-code")
    gcode.append("G21 ; Unités en millimètres")
    gcode.append("G90 ; Mode de positionnement absolu")
    gcode.append("G28 ; Aller à l'origine")
    gcode.append("G92 E0 ; Réinitialiser l'extrusion")
    gcode.append("G1 Z0.2 F300 ; Début à la window_height de couche initiale")
    extrusion = 0
    for i, point in enumerate(points):
        x, y, z = point
        if i == 0:
            gcode.append(f"G0 X{x:.6f} Y{y:.6f} Z{z:.6f} ; Déplacement initial")
        else:
            distance = ((points[i][0] - points[i - 1][0]) ** 2 +
                        (points[i][1] - points[i - 1][1]) ** 2 +
                        (points[i][2] - points[i - 1][2]) * 2) * 0.5
            extrusion += distance * extrusion_rate
            gcode.append(f"G1 X{x:.6f} Y{y:.6f} Z{z:.6f} E{extrusion:.4f}")
    gcode.append("G1 E-1 F300 ; Rétractation")
    gcode.append("G28 ; Retour à l'origine")
    gcode.append("M104 S0 ; Arrêt de l'extrudeur")
    gcode.append("M140 S0 ; Arrêt du plateau")
    gcode.append("; Fin du fichier G-code")
    return "\n".join(gcode)

def write_gcode (theta_max, N, petit_r, grand_r, p, Rsphere) :
  points = points_3d (theta_max, N, petit_r, grand_r, p, Rsphere)
  gcode = generate_gcode_points (points)
  if (Rsphere>=(grand_r - petit_r + p)) :
    gcode_name = f"{theta_max:.0f}_{N}_{petit_r:.0f}_{grand_r:.0f}_{p:.0f}_{Rsphere:.0f}.gcode"
  elif (Rsphere==0) :
    gcode_name = f"{theta_max:.0f}_{N}_{petit_r:.0f}_{grand_r:.0f}_{p:.0f}_a_plat.gcode"
  return gcode_name, gcode

def sauvegarde_fichier_gcode(name, content):
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale Tkinter
    fichier = filedialog.asksaveasfilename(
        title="Enregistrer sous",
        initialfile=name,
        filetypes=[("Fichiers GCODE", ".gcode"), ("Tous les fichiers", ".*")]
    )

    if fichier:  # Si un chemin est sélectionné
        # S'assurer que l'extension ".gcode" est ajoutée si non fournie
        if not fichier.endswith(".gcode"):
            fichier += ".gcode"

        # Créer ou écraser le fichier
        try:
            with open(fichier, 'w') as f:
                f.write(content)  # remplacer par le code génére en fonction des parametres
            print(f"Fichier créé : {fichier}")
        except Exception as e:
            print(f"Erreur lors de la création du fichier : {e}")
    return fichier

#Sélection des valeurs

theta_max = 6000.0
N = 100000
petit_r = 39
grand_r = 100
p = 35
Rsphere = 175

# Initialiser Pygame
init()

# Paramètres de la fenêtre Pygame
window_width, window_height = 800, 600
screen = display.set_mode((window_width, window_height))
display.set_caption("Exemple avec Pygame et Tkinter")

# Fonction pour afficher un texte
def ecriture(phrase,color,taille,position):
    '''
    entrée :
        phrase : le texte
        color : la couleur du texte
        taille : la taille de la police
        position = (x,y) : la position du centre du texte
    effet : 
        ecrit la phrase en color à position   
    '''
    police = font.SysFont("Courier New", taille) #donner une forme à la police d'écriture
    string_rendu = police.render(phrase, True,color)     # Rendu du texte avec la police choisie
    position_string = string_rendu.get_rect(center=position) #positionement du texte dans la fenêtre.
    screen.blit(string_rendu, position_string) #texte début de question
 

# Mise à jour de l'écran Pygame

def menu_g_code():
    screen.fill((0, 0, 0))  # Fond noir
    i = 1
    ecriture("Vous vous appretez à sauvegarder un fichier gcode" , (255,255,255), 25, (window_width/2, i*window_height/12))
    ecriture("généré selon les paramètres suivants" , (255,255,255), 25, (window_width/2, (2*i+1)*window_height/24))
    i = i+1.5
    ecriture("theta max = " + str(theta_max), (255,255,255), 25, (window_width/2, i*window_height/12))
    i = i+1
    ecriture("appuyez sur Entrée pour poursuivre", (255,255,255), 25 ,(window_width/2, i*window_height/12))
    i = i+1
    ecriture("sinon, fermez la fenêtre", (255,255,255), 25, (window_width/2, i*window_height/12))
    display.flip()

menu_g_code()

# Boucle principale
run_g_code = True
while run_g_code:
    for Pyevent in event.get():
        if Pyevent.type == QUIT:
            run_g_code = False
        elif Pyevent.type == KEYDOWN and Pyevent.key == K_RETURN:  # Appuyer sur Entrée pour sauvegarder
            gcode_name, gcode = write_gcode (theta_max, N, petit_r, grand_r, p, Rsphere)
            run_g_code = False
            chemin_fichier = sauvegarde_fichier_gcode(gcode_name, gcode)
            if chemin_fichier:
                print(f"Fichier enregistré à : {chemin_fichier}")
# Quitter Pygame
quit()