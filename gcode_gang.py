import numpy as np
from math import *

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
    else:
      max_dist_opp = 2*Rsphere - max_dist
      for i in range (N) :
        new_x = diff_r*np.cos(theta[i]) + p * np.cos(q*theta[i])
        new_y = diff_r*np.sin(theta[i]) + p * np.sin(q*theta[i])
        if (new_x*new_x + new_y*new_y <= Rsphere*Rsphere) :
          z = sqrt(Rsphere*Rsphere - new_x*new_x - new_y*new_y) + sqrt (Rsphere*Rsphere - max_dist_opp*max_dist_opp)
        else :
          norm = sqrt(new_x*new_x + new_y*new_y)
          new_x_opp = 2*Rsphere*new_x/norm - new_x
          new_y_opp = 2*Rsphere*new_y/norm - new_y
          z = -sqrt(Rsphere*Rsphere - new_x_opp*new_x_opp - new_y_opp*new_y_opp) + sqrt (Rsphere*Rsphere - max_dist_opp*max_dist_opp)
        res.append((new_x_opp, new_y_opp, z))
    return res

def generate_gcode_points(points, extrusion_rate=0.05, layer_height=0.2):
  #genere le gcode à partir d'une liste de points
    gcode = []
    gcode.append("; Début du fichier G-code")
    gcode.append("G21 ; Unités en millimètres")
    gcode.append("G90 ; Mode de positionnement absolu")
    gcode.append("G28 ; Aller à l'origine")
    gcode.append("G92 E0 ; Réinitialiser l'extrusion")
    gcode.append("G1 Z0.2 F300 ; Début à la hauteur de couche initiale")
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
  gcode_name = f"{theta_max:.0f}_{N}_{petit_r:.0f}_{grand_r:.0f}_{p:.0f}_{Rsphere:.0f}.gcode"
  with open(gcode_name, "w") as file:
    file.write(gcode)

# Générer le G-code

theta_max = 10000.0
N = 100000
petit_r = 65
grand_r = 100
p = 65
Rsphere = 100
write_gcode (theta_max, N, petit_r, grand_r, p, Rsphere)
