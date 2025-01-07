; Début du fichier G-code
G21 ; Unités en millimètres
G90 ; Mode de positionnement absolu
M104 S200 ; Chauffer l'extrudeur à 200°C
M140 S60 ; Chauffer le plateau à 60°C
G28 ; Aller à l'origine
G92 E0 ; Réinitialiser l'extrusion
G1 Z0.2 F300 ; Début à la hauteur de couche initiale
G0 X100.000000 Y0.000000 Z0.000000 ; Déplacement initial
G1 E-1 F300 ; Rétractation
G28 ; Retour à l'origine
M104 S0 ; Arrêt de l'extrudeur
M140 S0 ; Arrêt du plateau
; Fin du fichier G-code