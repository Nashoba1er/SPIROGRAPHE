; D�but du fichier G-code
G21 ; Unit�s en millim�tres
G90 ; Mode de positionnement absolu
M104 S200 ; Chauffer l'extrudeur � 200�C
M140 S60 ; Chauffer le plateau � 60�C
G28 ; Aller � l'origine
G92 E0 ; R�initialiser l'extrusion
G1 Z0.2 F300 ; D�but � la hauteur de couche initiale
G0 X100.000000 Y0.000000 Z0.000000 ; D�placement initial
G1 E-1 F300 ; R�tractation
G28 ; Retour � l'origine
M104 S0 ; Arr�t de l'extrudeur
M140 S0 ; Arr�t du plateau
; Fin du fichier G-code