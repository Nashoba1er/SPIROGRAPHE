from pygame import init, draw, font, K_BACKSPACE, key, K_RETURN, K_DOWN, K_UP, KEYDOWN, K_LEFT, K_RIGHT, KEYUP, time, image
from pygame import K_TAB, K_LSHIFT, K_RSHIFT, display, event, QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP, K_ESCAPE, transform, surfarray
from numpy import linspace, cos, sin, sqrt, all
from tkinter import filedialog, Tk
from os import path, startfile
from webbrowser import open as webopen
from json import dump, load

script_dir = path.dirname(__file__)  # Dossier où se trouve le script
img_path_github = path.join(script_dir, "img", "github.png")  # Sous-dossier "img"
# Charger et redimensionner l'image
logo_github = image.load(img_path_github)  # Charger l'image

# couleurs

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

init() #on initialise tout

# fonctions d'affichage

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
     
def cercles(r1,r2,p,couleur_g_cercle,couleur_p_cercle,couleur_rendu,couleur_fond):
    '''
    entrée :
        r1 : rayon du grand cercle
        r2 : rayon du petit cercle
        p : distance entre le centre du petit cercle et le point P
        couleur_... : les couleurs des 3 éléments
    effet :
        affiche le schéma spinographe
        affiche les variables 
    '''
    draw.rect(screen,couleur_fond,[window_width/2,0,window_width/2,window_height],0)
    if r1 > window_height/4 :
        ecriture("Rayon trop grand",couleur("RED"),int(police_taille*1.3),(3*window_width/4,window_height/2))
    elif r2 > r1 :
        ecriture("Petit rayon plus grand",couleur("RED"),int(police_taille),(3*window_width/4,3*window_height/8))
        ecriture("que le grand rayon",couleur("RED"),int(police_taille),(3*window_width/4,5*window_height/8))
    elif p > r2 :
        ecriture("Point en dehors",couleur("RED"),int(police_taille*1.3),(3*window_width/4,3*window_height/8))
        ecriture("du petit cercle",couleur("RED"),int(police_taille*1.3),(3*window_width/4,5*window_height/8))
    else :
        centre_g_x = 3*window_width/4
        centre_g_y = window_height/4
        centre_p_x = (r1-r2)+centre_g_x
        centre_p_y = centre_g_y
        centre_d_x,centre_d_y = (centre_g_x + (r1-r2)-p,centre_g_y)

        pos_r1 = (centre_g_x - (r1/2),centre_g_y - (r1/4))
        pos_r2 = (centre_p_x + (r2/2),centre_p_y - (r2/4))
        pos_p = (centre_d_x,centre_d_y+r2/4)

        # grand cercle
        draw.circle(screen,couleur_g_cercle,(centre_g_x,centre_g_y),r1,1)
        draw.rect(screen,couleur_g_cercle,[centre_g_x-r1,centre_g_y-1,r1,2],1)
        #draw.circle(screen,couleur_g_cercle,(centre_g_x,centre_g_y),3,0)

        # point P
        draw.rect(screen,couleur_rendu,[centre_d_x,centre_d_y-1,p,1],1)
        draw.circle(screen,couleur_rendu,(centre_d_x,centre_d_y),5,0)


        # petit cercle
        draw.circle(screen,couleur_p_cercle,(centre_p_x,centre_p_y),r2,1)
        draw.rect(screen,couleur_p_cercle,[centre_p_x,centre_p_y-1,r2,1],1)
        #draw.circle(screen,couleur_p_cercle,(centre_p_x,centre_p_y),2,0)

        # écritures
        ecriture("R",couleur_g_cercle,int(police_taille*r1/100),pos_r1)
        ecriture("r",couleur_p_cercle,int(police_taille*r2/100),pos_r2)
        ecriture("d",couleur_rendu,int(police_taille*r2/100),pos_p)

def zoom_cercles(r1,r2,p,couleur_g_cercle,couleur_p_cercle,couleur_rendu,couleur_fond):
    '''
    entrée :
        r1 : rayon du grand cercle
        r2 : rayon du petit cercle
        p : distance entre le centre du petit cercle et le point P
        couleur_... : les couleurs des 3 éléments et du fond
    effet :
        affiche le schéma spinographe sur toute la page
        affiche les variables 
    '''
    screen.fill(couleur_fond)
    if r1 > window_height :
        ecriture("Rayon trop grand",couleur("RED"),int(police_taille*2.6),(window_width/2,window_height/2))
    elif r2 > r1 :
        ecriture("Petit rayon plus grand",couleur("RED"),int(police_taille*2.6),(window_width/2,3*window_height/8))
        ecriture("que le grand rayon",couleur("RED"),int(police_taille*2.6),(window_width/2,5*window_height/8))
    elif p > r2 :
        ecriture("Point en dehors",couleur("RED"),int(police_taille*2.6),(window_width/2,3*window_height/8))
        ecriture("du petit cercle",couleur("RED"),int(police_taille*2.6),(window_width/2,5*window_height/8))
    else :
        centre_g_x = window_width/2
        centre_g_y = window_height/2
        centre_p_x = (r1-r2)+centre_g_x
        centre_p_y = centre_g_y
        centre_d_x,centre_d_y = (centre_g_x + (r1-r2)-p,centre_g_y)

        pos_r1 = (centre_g_x - (r1/2),centre_g_y - (r1/4))
        pos_r2 = (centre_p_x + (r2/2),centre_p_y - (r2/4))
        pos_p = (centre_d_x,centre_d_y-r2/4)

        # grand cercle
        draw.circle(screen,couleur_g_cercle,(centre_g_x,centre_g_y),r1,1)
        draw.rect(screen,couleur_g_cercle,[centre_g_x-r1,centre_g_y-1,r1,2],1)
        #draw.circle(screen,couleur_g_cercle,(centre_g_x,centre_g_y),3,0)

        # point P
        draw.rect(screen,couleur_rendu,[centre_d_x,centre_d_y-1,p,1],1)
        draw.circle(screen,couleur_rendu,(centre_d_x,centre_d_y),5,0)


        # petit cercle
        draw.circle(screen,couleur_p_cercle,(centre_p_x,centre_p_y),r2,1)
        draw.rect(screen,couleur_p_cercle,[centre_p_x,centre_p_y-1,r2,1],1)
        #draw.circle(screen,couleur_p_cercle,(centre_p_x,centre_p_y),2,0)

        # écritures
        ecriture("R",couleur_g_cercle,int(police_taille*r1/100),pos_r1)
        ecriture("r",couleur_p_cercle,int(police_taille*r2/100),pos_r2)
        ecriture("d",couleur_rendu,int(police_taille*r2/100),pos_p)

def champ(num_champ):
    '''
    entrée : 
        num_champ : numéro du champ
    effet : 
        colorie en blanc le champ numéro "num_champ" (efface son contenu)
    '''
    espace = window_height/4
    current_line1_y = 9*window_height/32
    current_line_x = window_width/8
    height = window_height/15
    width = window_width/4
    draw.rect(screen,couleur("WHITE"),[current_line_x,(num_champ)*espace+current_line1_y,width,height])
    draw.rect(screen,couleur("BLACK"),[current_line_x,(num_champ)*espace+current_line1_y,width,height],2)

def ecritures_param():
    '''
    effet : afficher les écritures de la page du spinographe en 2D
    '''
    ecriture("Saisie des paramètres",couleur("BLACK"),police_taille,(window_width/4,window_height/8))
    ecriture("Rayon du grand cercle",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/4))
    ecriture("Rayon du petit cercle",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/2))
    ecriture("Distance au centre   ",couleur("BLACK"),int(3/5*police_taille),(window_width/4,3*window_height/4))
    ecriture("R max = 100",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/4+5*window_height/32))
    ecriture(" r max = R ",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/2+5*window_height/32))
    ecriture(" d max = r ",couleur("BLACK"),int(3/5*police_taille),(window_width/4,3*window_height/4+5*window_height/32))

def bouton_gcode(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton G CODE :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "G CODE"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = window_width/2
    pos_y = 9*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def points (theta_max, N, petit_r, grand_r, p) :
    '''
    entrée :
        theta_max : la valeur de théta max
        N : le nombre de points calculés
        petit_r : rayon du petit cercle
        grand_r : rayon du grand cercle
        p : distance entre le centre du petit cercle et le point P
    effet : 
        calcule les N points du rendu
    Sortie : renvoie les N points du rendu
    '''
    theta = linspace(0.0, theta_max, N)
    diff_r = grand_r - petit_r
    q = 1.0 - (grand_r/petit_r) #arrangez vous pour que ce rapport soit différent de 1/2
    x = []
    y = []
    for i in range ( N ) :
        new_x = diff_r*cos(theta[i]) + p * cos(q*theta[i])
        new_y = diff_r*sin(theta[i]) + p * sin(q*theta[i])
        x.append(new_x)
        y.append(new_y)

    return x, y

def rendu(r1,r2,p,couleur_rendu):
    '''
    entrée :
        r1 : rayon du grand cercle
        r2 : rayon du petit cercle
        p : distance entre le centre du petit cercle et le point P
        couleur_rendu : la couleur du rendu
    effet :
        affiche le rendu et le bouton_gcode
    '''
    centre_x, centre_y = 3*window_width/4,3*window_height/4
    if not (r1 > window_height/4 or r2 >= r1 or p > r2) : 
        #draw.circle(screen,BLUE,(3*window_width/4,3*window_height/4),r1,1)
        point_x, point_y = points(6000.0, 10000, r1, r2, p)
        for i in range(10000):
            draw.circle(screen,couleur_rendu,(centre_x+point_x[i],centre_y+point_y[i]),1)
    bouton_gcode((0,0))

def menu_cercle_dans_cercle_init(lines):
    '''
    entrée :
        le contenu des champs
    effet :
        initialise le menu de visualisation du rendu cercle_dans_cercle
    '''
    global couleur_fond,window_height,window_width,cursor_position,police_taille,current_line
    taille_carac = 3/5*police_taille
    screen.fill(couleur_fond)
    draw.rect(screen,couleur_param,[0,0,window_width/2,window_height],0)
    ecritures_param()
    modifie_rayons(lines)
    # ecrit_init :
    for i in range(3):
        ecrit(i)
        if i != current_line:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
    ecrit(current_line)
    curseurs_init()
    return_arrow((0,0))
    bouton_gcode((0,0))
    bouton_d_equal_r((0,0))

def zoom_schema(lines):
    '''
    entrée :
        les valeurs des champs
    effet :
        affiche le schéma sur tout l'écran
    '''
    global run_zoom_schema,couleur_g_cercle,couleur_p_cercle,couleur_fond
    if is_float(lines[0]) and is_float(lines[1]) and is_float(lines[2]):
        r1 = float(lines[0])*(window_height/2)/100
        r2 = float(lines[1])*(window_height/2)/100
        p = float(lines[2])*(window_height/2)/100
        zoom_cercles(r1,r2,p,couleur_g_cercle,couleur_p_cercle,couleur_rendu,couleur_fond)
    else :
        run_zoom_schema = False

def zoom_rendu(lines):
    '''
    entrée :
        r1 : rayon du grand cercle
        r2 : rayon du petit cercle
        p : distance entre le centre du petit cercle et le point P
        couleur_rendu : la couleur du rendu
    effet :
        affiche le rendu
    '''
    global run_zoom_rendu,couleur_g_cercle,couleur_p_cercle,couleur_fond
    if is_float(lines[0]) and is_float(lines[1]) and is_float(lines[2]):
        r1 = float(lines[0])*(window_height/2)/100
        r2 = float(lines[1])*(window_height/2)/100
        p = float(lines[2])*(window_height/2)/100
    centre_x, centre_y = window_width/2,window_height/2
    if not (r1 > window_height/2 or r2 >= r1 or p > r2) : 
        screen.fill(couleur_fond)
        #draw.circle(screen,BLUE,(3*window_width/4,3*window_height/4),r1,1)
        point_x, point_y = points(12000.0, 75000, r1, r2, p)
        for i in range(75000):
            draw.circle(screen,couleur_rendu,(centre_x+point_x[i],centre_y+point_y[i]),1)
    else :
        run_zoom_rendu = False

def curseurs_init():
    '''
    effet : affiche les 3 curseurs
    '''
    for num_champ in range(3):
        curseur(num_champ)    

def curseur(num_champ):
    '''
    entrée : num_champ = le numéro du curseur
    effet : affiche le curseur numéro "num_champ" en fonction de la valeur du champ
    '''
    global couleur_g_cercle,couleur_p_cercle, couleur_rendu, lines
    espace = window_height/4
    current_line1_y = 9*window_height/32
    pos_y = (num_champ)*espace+current_line1_y + 3 * window_height/32
    pos_x = window_width / 4
    width_champ = window_width / 4
    width = width_champ * (2/3)

    if num_champ == 0 :
        couleur_curseur = couleur_g_cercle
    elif num_champ == 1:
        couleur_curseur = couleur_p_cercle
    else :
        couleur_curseur = couleur_rendu

    if is_float(lines[num_champ]):
        param = float(lines[num_champ])
        coord = (pos_x-width/2 + param/100*width,pos_y+1)
        draw.rect(screen,couleur_param,[pos_x - width/2 - 5,pos_y-6,width + 10,12],0)
        draw.rect(screen,couleur_curseur,[pos_x - width/2,pos_y,width,2],0)
        draw.circle(screen,couleur("BLACK"),coord,5)
        draw.circle(screen,couleur_curseur,coord,3)

    else : 
        draw.rect(screen,couleur_curseur,[pos_x - width/2,pos_y,width,2],0)

def draw_arrow(surface, color, start_pos, width, height):
    '''
    entrée :
        surface : l'écran
        color : la couleur de la flèche
        start_pos : les coordonées du centre de la flèche
        width : la longueur de la flèche
        height : la hauteu de la flèche
    effet : 
        dessine une flèche de la couleur color, 
        de centre start_pos, 
        de longueur width, 
        de hauteur height (body) et 
        de hauteur de triangle 3*height/2
    '''
    # Points pour créer une flèche pointant vers la droite
    (x,y) = start_pos
    arrow_points = [
        (x + width/2,y-height/2),  # Point haut droit
        (x+width/2, y+height/2),  # Point bas droit
        (x -width/4 , y + height/2),  # Base du triangle bas
        (x -width/4 , y + 3*height/4),  # Pointe basse
        (x- width/2, y),  # Pointe de la flèche
        (x -width/4 , y - 3*height/4),  # Pointe haute
        (x -width/4 , y - height/2),  # Base du triangle haut

    ]

    draw.polygon(surface, color, arrow_points)

def return_arrow(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche la flèche retour
            en gris si le curseur n'est pas dessus
            en vert à l'inverse
    '''
    res = False
    width = window_width/16
    height = window_height/16
    coord = x,y = (window_width/20,window_height/20)
    if pos[0] < x + width/2 and pos[0] > x - width/2 and pos[1] < y + height/2 and pos[1] > y - height/2:
        color_arrow = couleur("GREEN")
        res = True
    else : 
        color_arrow = couleur("GRIS_CLAIR") 
    draw.rect(screen,couleur("BLACK"),[x-width/2,y-height/2,width,height],0,int((height+width)/10))
    draw.rect(screen,color_arrow,[x-width/2,y-height/2,width,height],2,int((height+width)/10))
    draw_arrow(screen,color_arrow,coord,width/2,height/3)
    return res

def bouge_curseur(coord,dragging):
    '''
    entrée : 
        les coordonnées de la souris, 
        dragging = le numéro du champ dont le curseur est associé
    effet : 
        met à jour la position du curseur et met à jour le champ
        met à jour 2 curseurs si d = r est enclenché
    '''

    # set les variables dont j'ai besoin
    global lines, cursor_position
    num_curseur = dragging # numéro du curseur qu'on change
    espace = window_height/4 # espace vertical entre les curseurs
    coord_x, _ = coord # coordonnées du clic
    pos_x = window_width/4 # centre du curseur
    width_champ = window_width / 4 # taille du champ
    width = width_champ * (2/3) # taille du curseur

    if coord_x < pos_x - width/2:
        pos_curseur_x = pos_x - width/2
    elif coord_x > pos_x + width/2 :
        pos_curseur_x = pos_x + width/2
    else :
        pos_curseur_x = coord_x

    # mise à jour de la valeur du champ : 
    param = int(((pos_curseur_x-pos_x+width/2))/width * 100)
    if param > 100 :
        param = 100
    if param < 0:
        param = 0
    lines[num_curseur] = str(param)

    if d_equal_r and num_curseur == 1:
        lines[2] = lines[1]
        ecrit(2)
        curseur(2)
    if d_equal_r and num_curseur == 2:
        lines[1] = lines[2]
        ecrit(1)
        curseur(1)

    cursor_position = len(lines[current_line])
    modifie_rayons(lines)

    ecrit(num_curseur)
    curseur(num_curseur)

def bouton_d_equal_r(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton r= d :
            en blanc si le curseur n'est pas dessus et qu'il n'est pas sélectionné
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    global d_equal_r
    res = False
    message = " d = r "
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1) / 2
    height = police_taille *3 / 4
    pos_x = window_width/12
    pos_y = window_height/2 + 9*window_height/32 + window_height/30
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    # Si je suis sur le bouton : 
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        res = True
    # Si je suis sur le bouton et qu'il n'est pas sélectionné : je met en vert
    if res and not d_equal_r:
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille//2,(pos_x,pos_y))
    # Si je ne suis pas sur le bouton mais qu'il est sélectionné : je met en vert
    elif not res and d_equal_r :
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille//2,(pos_x,pos_y))
    # Sinon je met en blanc
    else : 
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille//2,(pos_x,pos_y))

    return res

# fonctions d'écriture :

# Fonction pour gérer l'entrée de texte
def input_to_text(event):
    '''
    entrée :
        evènement PYGAME :
            - BACKSPACE
            - RETURN
            - UP | DOWN | LEFT | RIGHT
            - TAB
            - ESCAPE
            - any letter
    effet : 
        Tout ceci n'est pas affiché, la fonction ecrit se charge de l'affichage
        - BACKSPACE : efface le caractère à gauche du curseur
        - RETURN : place le curseur à la fin du champ suivant (le 0 quand on est sur le 2)
        - UP : augmente de 1 la valeur du champ
        - DOWN : diminue de 1 la valeur du champ
        - LEFT : déplace le curseur sur la gauche
        - RIGHT : déplace le curseur sur la droite
        - TAB : passe au champs suivant ou au champ précédent
        - ESCAPE : revient au menu précédent (met run_cdc à False)
        - any letter : écrit la touche qu'on vient de taper
    '''
    global current_line, lines, cursor_position, key_press_times, run_cdc
    taille_carac = 3/5 * police_taille
    keys = key.get_pressed()
    longueur_current_line = len(lines[current_line]) 

    if event.key == K_BACKSPACE:
        # Si Retour arrière est appuyé
        if longueur_current_line > 0 and cursor_position > 0:
            if cursor_position == 1 :
                lines[current_line] = lines[current_line][1:]
            elif cursor_position == (longueur_current_line) :
                lines[current_line] = lines[current_line][:-1]
            else :
                lines[current_line] = lines[current_line][:(cursor_position-1)] + lines[current_line][(cursor_position):]  # Supprime le dernier caractère
            cursor_position -= 1
    elif event.key == K_RETURN:
        # Si 'Entrée' est appuyé,
        if current_line < 2:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line += 1
            cursor_position = len(lines[current_line])
        else :
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line = 0
            cursor_position = len(lines[current_line])
    elif event.key == K_ESCAPE:
        run_cdc = False
    elif event.key == K_TAB and (keys[K_LSHIFT] or keys[K_RSHIFT]):
        if current_line > 0:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line -=1
            cursor_position = len(lines[current_line])
    elif event.key == K_TAB:
        #si on appuie sur la touche du bas, on passe à la ligne suivante :
        if current_line < 2:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line += 1
            cursor_position = len(lines[current_line])
    elif event.key == K_UP :
        if is_float(lines[current_line]):
            lines[current_line] = str(int(float(lines[current_line])) + 1)
        cursor_position = len(lines[current_line])
        modifie_rayons(lines)
    elif event.key == K_DOWN :
        if is_float(lines[current_line]):
            lines[current_line] = str(int(float(lines[current_line])) - 1)
        cursor_position = len(lines[current_line])
        modifie_rayons(lines)
    elif event.key == K_RIGHT:
        #si on appuie sur la flèche de droite, le curseur se déplace d'une lettre
        if cursor_position < (longueur_current_line):
            cursor_position += 1
    elif event.key == K_LEFT:
        #si on appuie sur la flèche de gauche, le curseur se déplace d'une lettre
        if cursor_position > 0:
            cursor_position -=1
    else:
        # Autres touches
        if longueur_current_line <= character_limit:
        # Ajouter le caractère à la ligne actuelle
            letter = event.unicode
            if letter:  # Si la touche produit un caractère (ignore Shift, Ctrl, etc.)
                if cursor_position == 0:
                    lines[current_line] = letter + lines[current_line]
                elif cursor_position < (longueur_current_line):
                    lines[current_line] = lines[current_line][:(cursor_position)] + letter + lines[current_line][(cursor_position):]
                else: 
                    lines[current_line] += letter
                cursor_position += 1
                modifie_rayons(lines)
    if (current_line == 1) and d_equal_r :
        lines[current_line+1] = lines[current_line]
        modifie_rayons(lines)
    if (current_line == 2) and d_equal_r :
        lines[current_line-1] = lines[current_line]
        modifie_rayons(lines)

def ecrit(num_champ):
    '''
    entrée :
        num_champ : numéro du champ
    effet :
        met à jour le contenu du champ numéro "current_line"
    '''
    global cursor_position
    espace = window_height/4 # Espace entre chaque current_line en pixels
    current_line1_y = 9*window_height/32
    current_line_x = window_width/8
    spacing = 1/5*police_taille #marge gauche
    taille_carac = 3/5 * police_taille
    indent_x,indent_y = current_line_x + spacing,current_line1_y # position
    champ(num_champ)
    # Rendre et afficher chaque ligne de texte
    txt_surf = police.render(lines[num_champ], True, couleur("BLACK"))
    screen.blit(txt_surf, (indent_x, indent_y + num_champ*espace))
    draw.rect(screen,couleur("BLACK"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
    curseur(num_champ)
    ecriture("%",couleur("BLACK"),police_taille,(indent_x + 11.5*taille_carac, (num_champ)*espace+current_line1_y+window_height/30))
    display.update()

def is_float(value):
    '''
    entrée :
        value : variable quelconque
    effet :
        vérifie que cette valeur est un float
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False

def modifie_rayons(lines):
    '''
    entrée :
        le contenu des champs
    effet :
        vérifie que le contenu des champs est suffisant pour faire un rendu
        si c'est le cas :
            normalise les valeurs sur 100 selon la taille de l'écran
            affiche le rendu et le schéma
    '''
    if is_float(lines[0]) and is_float(lines[1]) and is_float(lines[2]):
        r1 = float(lines[0])*(window_height/4)/100
        r2 = float(lines[1])*(window_height/4)/100
        p = float(lines[2])*(window_height/4)/100
        cercles(r1,r2,p,couleur_g_cercle,couleur_p_cercle,couleur_rendu,couleur_fond)
        rendu(r1,r2,p,couleur_rendu)

def clic(coord):
    '''
    entrée :
        coord = (x,y) : l'endroit du clic
    effet :
        si le clic est sur un champ :
            change le curseur de champ
            place le curseur dans l'inter-caractère le plus proche
        si le clic est sur le rendu : 
            met la variable run_zoom_rendu à true
        si le clic est sur le schéma : 
            met la variable run_zoom_schema à true
        si le clic est sur un curseur :
            met la variable dragging au numéro du curseur sélectionné (-1 par défaut)
        
        si le clic est sur le bouton flèche retour :
            met la variable run_cdc à false

        si le clic est sur le bouton d = r :
            met la variable d_equal_r true si elle était à false et inversement

        si le clic est sur le bouton G CODE :
            ouvre le menu G CODE 
            n'ouvre pas le zoom_rendu
    '''
    global current_line, cursor_position, run_zoom_rendu, run_cdc, run_zoom_schema, dragging, d_equal_r, run_g_code
    coord_x, coord_y = coord
    espace = window_height/4
    current_line1_y = 9*window_height/32
    current_line_x = window_width/8
    height = window_height/15
    width = window_width/4
    taille_carac = 3/5 * police_taille
    taille_curseur = 0.7*window_height/15
    
    for i in range(3):
        if (coord_x > current_line_x and coord_x < current_line_x  + width and coord_y > (i*espace)+current_line1_y and coord_y < (i*espace)+current_line1_y+height) :
            # je suis dans le champ i
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,taille_curseur],0)
            current_line = i
            cursor_position = len(lines[current_line])
            for carac in range(len(lines[current_line])):
                if (coord_x < current_line_x + (len(lines[current_line])-carac)*taille_carac) :
                    cursor_position = len(lines[current_line])-carac - 1
            draw.rect(screen,couleur("BLACK"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,taille_curseur],0)
        
        # Vérifie si le clic est sur un curseur
        if coord_y > (i)*espace+current_line1_y + 2 * window_height/32 and coord_y < (i)*espace+current_line1_y + 4 * window_height/32 :
            # je suis à hauteur du curseur
            if coord_x > current_line_x and coord_x < current_line_x  + width :
                dragging = i  # On commence à déplacer l'objet
    #clic sur le shéma
    if (coord_x > window_width/2 and coord_y < window_height/2):
        run_zoom_schema = True 
    #clic sur le rendu
    if (coord_x > window_width/2 and coord_y > window_height/2):
        run_zoom_rendu = True
    #clic sur la flèche retour
    if return_arrow(coord):
        run_cdc = False
    #clic sur le bouton d = r
    if bouton_d_equal_r(coord):
        d_equal_r = not d_equal_r
        if d_equal_r :
            lines[2] = lines[1]
            ecrit(2)
            modifie_rayons(lines)

    #clic sur le bouton g_code
    if bouton_gcode(coord):
        run_g_code = True
        run_zoom_rendu = False

    display.flip()

#fonctions pour le menu principal :

def menu_choix():
    '''
    effet : affiche le menu de choix du format du mandala
    '''
    global screen,couleur_g_cercle,couleur_p_cercle,couleur_fond,couleur_rendu,police_taille
    screen.fill(couleur_fond)
    r1 = 50*(window_height/2)/100
    r2 = 31.25*(window_height/2)/100
    p = 25*(window_height/2)/100
    centre_x, centre_y = window_width/2,window_height/2
    screen.fill(couleur_fond)
    point_x, point_y = points(6000.0, 10000, r1, r2, p)
    for i in range(10000):
        draw.circle(screen,couleur_rendu,(centre_x+point_x[i],centre_y+point_y[i]),2)

    ecriture("SPIROGRAPHE",couleur_rendu,police_taille*2, (window_width/2,window_height/8))
    #affiche les boutons sans les considérer commme sélectionné
    bouton_cdc((0,0))
    bouton_cdc3D((0,0))
    #bouton_couleur((0,0))
    bouton_param_et_info((0,0))

def bouton_cdc(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton Cercle dans Cercle :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "Spiro 2D"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 8*window_width/10
    pos_y = 4*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def bouton_cdc3D(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton Cercle dans Cercle :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "Spiro 3D"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 2*window_width/10
    pos_y = 4*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def bouton_couleur(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton Couleur :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "Couleurs"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 7*window_width/10
    pos_y = 8*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def bouton_ede(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton Ellipse dans Ellipse :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "Ellipse"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 3*window_width/10
    pos_y = 8*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def bouton_param_et_info(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton Param & Infos :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "Param & Infos"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = window_width/2
    pos_y = 8.5*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def clic_menu(pos):
    '''
    entrée :
        coord = (x,y) : l'endroit du clic
    effet :
        si on clique :
            sur le bouton cercle dans cercle : met run_cdc à True
    '''
    global run_cdc, run_couleur, run_cdc3D, run_param_et_info

    if bouton_cdc(pos):
        run_cdc = True

    if bouton_couleur(pos):
        run_couleur = True

    if bouton_cdc3D(pos):
        run_cdc3D = True

    if bouton_param_et_info(pos):
        run_param_et_info = True


#fonctions pour le menu couleur :

def menu_couleur():
    '''
    effet :
        - affiche des boutons pour changer les couleurs de fond
        - affiche des boutons indiquant les couleurs pour le rendu
    '''
    global couleur_rendu,couleur_fond
    screen.fill(couleur_param)
    return_arrow((0,0))

    ecriture("fond",couleur("WHITE"),police_taille,(window_width/5,window_height/5))
    ecriture("paramètres",couleur("WHITE"),police_taille,(window_width/2,window_height/5))
    ecriture("rendu",couleur("WHITE"),police_taille,(4*window_width/5,window_height/5))
    
    taille = window_width/16

    draw.rect(screen,couleur_fond,[window_width/5-taille/2,window_height/5+taille,taille,taille],0)
    draw.rect(screen,couleur("WHITE"),[window_width/2-taille/2,window_height/5+taille,taille+1,taille+1],2)
    draw.rect(screen,couleur_rendu,[4*window_width/5-taille/2,window_height/5+taille,taille,taille],0)


    # couleurs au choix fond:
    boutons_choix_couleur((0,0))
    

def boutons_choix_couleur(coord):
    '''
    entrée : les coordonnées de la souris
    effet : entoure en vert les boutons de couleur que le curseur survole
    '''

    taille = window_width/16
    x_0 = window_width/5-5*taille/4
    y_0 = 2*window_height/5+taille
    incrément = 1.5*taille
    couleur_1 = couleur_fond
    couleur_2 = couleur_param
    couleur_3 = couleur_rendu

    # couleurs au choix fond:

    couleurs = [["C1_BLUE","BLEU_JOLI","PINK3","GRIS_CLAIR","SAUGE_LOANN","ROSE_CLAIR"],
               ["C1_BLUE","BLEU_JOLI","PINK3","GRIS_CLAIR","SAUGE_LOANN","ROSE_CLAIR"],
               ["C1_BLUE","BLEU_JOLI","PINK3","GRIS_CLAIR","SAUGE_LOANN","ROSE_CLAIR"]]
    
    for i in range(6):
        if bouton_choix_couleur(x_0+(i%2)*incrément,y_0+i//2*incrément,taille,couleur(couleurs[0][i]),coord):
            couleur_1 = couleur(couleurs[0][i])
    
    x_0 = window_width/2 - 5*taille/4

    for i in range(6):
        if bouton_choix_couleur(x_0+(i%2)*incrément,y_0+i//2*incrément,taille,couleur(couleurs[1][i]),coord):
            couleur_2 = couleur(couleurs[0][i])

    x_0 = 4*window_width/5-5*taille/4

    for i in range(6):
        if bouton_choix_couleur(x_0+(i%2)*incrément,y_0+i//2*incrément,taille,couleur(couleurs[2][i]),coord):
            couleur_3 = couleur(couleurs[0][i])

    return (couleur_1,couleur_2,couleur_3)

def bouton_choix_couleur(x,y,taille,color,coord):
    pos_x, pos_y = coord
    draw.rect(screen,color,[x,y,taille,taille],0)
    if pos_x > x and pos_x < x + taille and pos_y > y and pos_y < y + taille :
        draw.rect(screen,couleur("GREEN"),[x,y,taille,taille],2)
        return True
    draw.rect(screen,couleur("WHITE"),[x,y,taille,taille],2)
    return False 

def clic_couleur(coord):
    '''
    entrée : les coordonnées du clic
    effet : change la couleur selon le clic
    '''
    global run_couleur,couleur_fond,couleur_param,couleur_rendu
    (couleur_fond,couleur_param,couleur_rendu) = boutons_choix_couleur(coord)

    if return_arrow(coord):
        run_couleur = False
    menu_couleur()
    display.flip()
    

#fonctions pour le menu demi-sphère :

def menu_cdc3D(numéro):
    '''
    effet :
        - affiche des boutons pour changer les couleurs de fond
        - affiche des boutons indiquant les couleurs pour le rendu
    '''
    global couleur_fond,window_height,window_width,cursor_position,police_taille,current_line
    taille_carac = 3/5*police_taille
    screen.fill(couleur_fond)

    draw.rect(screen,couleur_param,[0,0,window_width/2,window_height],0)
    draw.rect(screen,couleur_param,[0,window_height/5+window_height/40-window_height/50,window_width/2, police_taille*1.3])
    S_max = float(lines2[1]) - float(lines2[2]) + float(lines2[3]) 
    ecriture("Rayon de la sphère :",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/5 + window_height/40))
    ecriture("(S max = "+str(S_max)+")",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/5+window_height/40 + window_height/30))
    ecriture("Saisie des paramètres",couleur("BLACK"),police_taille,(window_width/4,window_height/8))
    ecriture("Rayon du grand cercle",couleur("BLACK"),int(3/5*police_taille),(window_width/4,2*window_height/5+ window_height/40))
    ecriture("(R max = 100)",couleur("BLACK"),int(3/5*police_taille),(window_width/4,2*window_height/5+window_height/40 + window_height/30))
    ecriture("Rayon du petit cercle",couleur("BLACK"),int(3/5*police_taille),(window_width/4,3*window_height/5+ window_height/32))
    ecriture(" (r max = R) ",couleur("BLACK"),int(3/5*police_taille),(window_width/4,3*window_height/5+window_height/40 + window_height/30))
    ecriture("Distance au centre   ",couleur("BLACK"),int(3/5*police_taille),(window_width/4,4*window_height/5+ window_height/32))
    ecriture(" (d max = r) ",couleur("BLACK"),int(3/5*police_taille),(window_width/4,4*window_height/5+window_height/40 + window_height/30))
    
    modifie_rayons3D(lines2,numéro)

    for i in range(4):
        ecrit3D(i)
        if i != current_line:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5-9*window_height/32,2,0.7*window_height/15],0)
    ecrit3D(current_line)
    curseurs_init3D()

    script_dir = path.dirname(__file__)  # Dossier où se trouve le script
    img_path = path.join(script_dir, "img", "sphere.png")  # Sous-dossier "img"
    # Charger et redimensionner l'image
    img = image.load(img_path)  # Charger l'image
    img = transform.scale(img, (window_width // 18, window_width // 18))  # Redimensionner

    
    screen.blit(img, (5.4*window_width/6, window_height/20))
    #screen.blit(img, (5.4*window_width/6+1, window_height/11))
    #screen.blit(img, (5.4*window_width/6, window_height/11+1))
    #screen.blit(img, (5.4*window_width/6+1, window_height/11+1))

    bouton_xy((0,0))
    bouton_xz((0,0))
    return_arrow((0,0))

def clic_cdc3D(coord, numéro):
    '''
    entrée : les coordonnées du clic
    effet : change la couleur selon le clic
    '''
    global run_cdc3D
    
    global current_line, cursor_position, run_zoom_rendu, run_cdc, run_zoom_schema, dragging
    coord_x, coord_y = coord
    espace = window_height/5
    current_line1_y = 9*window_height/32
    current_line_x = window_width/8
    height = window_height/15
    width = window_width/4
    taille_carac = 3/5 * police_taille
    taille_curseur = 0.7*window_height/15
    
    for i in range(4):
        if (coord_x > current_line_x and coord_x < current_line_x  + width and coord_y > (i*espace)+current_line1_y and coord_y < (i*espace)+current_line1_y+height) :
            # je suis dans le champ i
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5+9*window_height/32 + 0.15*window_height/15,2,taille_curseur],0)
            current_line = i
            cursor_position = len(lines2[current_line])
            for carac in range(len(lines2[current_line])):
                if (coord_x < current_line_x + (len(lines2[current_line])-carac)*taille_carac) :
                    cursor_position = len(lines2[current_line])-carac - 1
            draw.rect(screen,couleur("BLACK"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5+9*window_height/32 + 0.15*window_height/15,2,taille_curseur],0)
        
        # Vérifie si le clic est sur un curseur
        if coord_y > (i)*espace+current_line1_y + 2 * window_height/32 and coord_y < (i)*espace+current_line1_y + 4 * window_height/32 :
            # je suis à hauteur du curseur
            if coord_x > current_line_x and coord_x < current_line_x  + width :
                dragging = i  # On commence à déplacer l'objet
    #clic sur le shéma
    if (coord_x > window_width/2 and coord_y < window_height/2):
        run_zoom_schema = True 
    #clic sur le rendu
    if (coord_x > window_width/2 and coord_y > window_height/2):
        run_zoom_rendu = True
    #clic sur la flèche retour
    if return_arrow(coord):
        run_cdc3D = False

    #clic sur la sélection du plan
    if (bouton_xy(coord)) :
        numéro = 1
    if (bouton_xz(coord)):
        numéro = 2

    if bouton_gcode(coord):
        print("clic sur le bouton G CODE")

    display.flip()

    return numéro

def input_to_text3D(event,numéro):
    '''
    entrée :
        evènement PYGAME :
            - BACKSPACE
            - RETURN
            - UP | DOWN | LEFT | RIGHT
            - TAB
            - ESCAPE
            - any letter
    effet : 
        Tout ceci n'est pas affiché, la fonction ecrit se charge de l'affichage
        - BACKSPACE : efface le caractère à gauche du curseur
        - RETURN : place le curseur à la fin du champ suivant (le 0 quand on est sur le 2)
        - UP : augmente de 1 la valeur du champ
        - DOWN : diminue de 1 la valeur du champ
        - LEFT : déplace le curseur sur la gauche
        - RIGHT : déplace le curseur sur la droite
        - TAB : passe au champs suivant ou au champ précédent
        - ESCAPE : revient au menu précédent (met run_cdc à False)
        - any letter : écrit la touche qu'on vient de taper
    '''
    global current_line, lines2, cursor_position, key_press_times, run_cdc
    taille_carac = 3/5 * police_taille
    keys = key.get_pressed()
    longueur_current_line = len(lines2[current_line]) 

    if event.key == K_BACKSPACE:
        # Si Retour arrière est appuyé
        if longueur_current_line > 0 and cursor_position > 0:
            if cursor_position == 1 :
                lines2[current_line] = lines2[current_line][1:]
            elif cursor_position == (longueur_current_line) :
                lines2[current_line] = lines2[current_line][:-1]
            else :
                lines2[current_line] = lines2[current_line][:(cursor_position-1)] + lines2[current_line][(cursor_position):]  # Supprime le dernier caractère
            cursor_position -= 1
    elif event.key == K_RETURN:
        # Si 'Entrée' est appuyé,
        if current_line < 2:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line += 1
            cursor_position = len(lines2[current_line])
        else :
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line = 0
            cursor_position = len(lines2[current_line])
    elif event.key == K_ESCAPE:
        run_cdc = False
    elif event.key == K_TAB and (keys[K_LSHIFT] or keys[K_RSHIFT]):
        if current_line > 0:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line -=1
            cursor_position = len(lines2[current_line])
    elif event.key == K_TAB:
        #si on appuie sur la touche du bas, on passe à la ligne suivante :
        if current_line < 2:
            draw.rect(screen,couleur("WHITE"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line += 1
            cursor_position = len(lines2[current_line])
    elif event.key == K_UP :
        if is_float(lines2[current_line]):
            lines2[current_line] = str(int(float(lines2[current_line])) + 1)
        cursor_position = len(lines2[current_line])
        modifie_rayons3D(lines2,numéro)
    elif event.key == K_DOWN :
        if is_float(lines2[current_line]):
            lines2[current_line] = str(int(float(lines2[current_line])) - 1)
        cursor_position = len(lines2[current_line])
        modifie_rayons3D(lines2,numéro)
    elif event.key == K_RIGHT:
        #si on appuie sur la flèche de droite, le curseur se déplace d'une lettre
        if cursor_position < (longueur_current_line):
            cursor_position += 1
    elif event.key == K_LEFT:
        #si on appuie sur la flèche de gauche, le curseur se déplace d'une lettre
        if cursor_position > 0:
            cursor_position -=1
    else:
        # Autres touches
        if longueur_current_line <= character_limit:
        # Ajouter le caractère à la ligne actuelle
            letter = event.unicode
            if letter:  # Si la touche produit un caractère (ignore Shift, Ctrl, etc.)
                if cursor_position == 0:
                    lines2[current_line] = letter + lines2[current_line]
                elif cursor_position < (longueur_current_line):
                    lines2[current_line] = lines2[current_line][:(cursor_position)] + letter + lines2[current_line][(cursor_position):]
                else: 
                    lines2[current_line] += letter
                cursor_position += 1
                modifie_rayons3D(lines2,numéro)

def modifie_rayons3D(lines2,numéro):
    '''
    entrée :
        le contenu des champs
    effet :
        vérifie que le contenu des champs est suffisant pour faire un rendu
        si c'est le cas :
            normalise les valeurs sur 100 selon la taille de l'écran
            affiche le rendu et le schéma
    '''
    draw.rect(screen,couleur_fond,[window_width/2, 3*window_height/20, window_width/2, 17*window_height/20],0)
    if is_float(lines2[0]) and is_float(lines2[1]) and is_float(lines2[2]) and is_float(lines2[3]):
        Rsph = float(lines2[0])*(window_height/4)/100
        r1 = float(lines2[1])*(window_height/4)/100
        r2 = float(lines2[2])*(window_height/4)/100
        p = float(lines2[3])*(window_height/4)/100

        rendu3D(r1,r2,p,couleur_rendu,numéro,Rsph)
    draw.rect(screen,couleur_param,[0,window_height/5+window_height/40-window_height/50,window_width/2, police_taille*1.3])
    S_max = float(lines2[1]) - float(lines2[2]) + float(lines2[3]) 
    ecriture("Rayon de la sphère :",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/5 + window_height/40))
    ecriture("(S max = "+str(S_max)+")",couleur("BLACK"),int(3/5*police_taille),(window_width/4,window_height/5+window_height/40 + window_height/30))

def bouton_xy(pos):
    #Ajout pour les boutons
    res = False
    message = "Plan de haut"
    (cursor_x, cursor_y) = pos
    police_taille2 = police_taille-8
    width = police_taille2*3/5*(len(message)+1)
    height = police_taille2
    pos_x = 15*window_width/20
    pos_y = window_height/20
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille2,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille2,(pos_x,pos_y))
    return res

def bouton_xz(pos):

    #Ajout pour les boutons
    res = False
    message = "Plan en coupe"
    (cursor_x, cursor_y) = pos
    police_taille2 = police_taille-8
    width = police_taille2*3/5*(len(message)+1)
    height = police_taille2
    pos_x = 15*window_width/20
    pos_y = window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille2,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille2,(pos_x,pos_y))
    return res

def ecrit3D(num_champ):
    '''
    entrée :
        num_champ : numéro du champ
    effet :
        met à jour le contenu du champ numéro "current_line"
    '''
    global cursor_position
    espace = window_height/5 # Espace entre chaque current_line en pixels
    current_line1_y = 9*window_height/32
    current_line_x = window_width/8
    spacing = 1/5*police_taille #marge gauche
    taille_carac = 3/5 * police_taille
    indent_x,indent_y = current_line_x + spacing,current_line1_y # position
    champ3D(num_champ)
    # Rendre et afficher chaque ligne de texte
    txt_surf = police.render(lines2[num_champ], True, couleur("BLACK"))
    screen.blit(txt_surf, (indent_x, indent_y + num_champ*espace))
    draw.rect(screen,couleur("BLACK"),[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/5-9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
    curseur3D(num_champ)
    ecriture("%",couleur("BLACK"),police_taille,(indent_x + 11.5*taille_carac, (num_champ)*espace+current_line1_y+window_height/30))
    display.update()

def champ3D(num_champ):
    '''
    entrée : 
        num_champ : numéro du champ
    effet : 
        colorie en blanc le champ numéro "num_champ" (efface son contenu)
    '''
    espace = window_height/5
    current_line1_y = 9*window_height/32
    current_line_x = window_width/8
    height = window_height/15
    width = window_width/4
    draw.rect(screen,couleur("WHITE"),[current_line_x,(num_champ)*espace+current_line1_y,width,height])
    draw.rect(screen,couleur("BLACK"),[current_line_x,(num_champ)*espace+current_line1_y,width,height],2)

def curseurs_init3D():
    '''
    effet : affiche les 4 curseurs
    '''
    for num_champ in range(4):
        curseur3D(num_champ)    

def curseur3D(num_champ):
    '''
    entrée : num_champ = le numéro du curseur
    effet : affiche le curseur numéro "num_champ" en fonction de la valeur du champ
    '''
    global couleur_g_cercle,couleur_p_cercle, couleur_rendu, lines2
    espace = window_height/5
    current_line1_y = 9*window_height/32
    pos_y = (num_champ)*espace+current_line1_y + 3 * window_height/32
    pos_x = window_width / 4
    width_champ = window_width / 4
    width = width_champ * (2/3)

    if num_champ == 0 :
        couleur_curseur = couleur_g_cercle
    elif num_champ == 1:
        couleur_curseur = couleur_p_cercle
    else :
        couleur_curseur = couleur_rendu

    if is_float(lines2[num_champ]):
        param = float(lines2[num_champ])
        coord = (pos_x-width/2 + param/100*width,pos_y+1)
        draw.rect(screen,couleur_param,[pos_x - width/2 - 5,pos_y-6,width + 10,12],0)
        draw.rect(screen,couleur_curseur,[pos_x - width/2,pos_y,width,2],0)
        draw.circle(screen,couleur("BLACK"),coord,5)
        draw.circle(screen,couleur_curseur,coord,3)

    else : 
        draw.rect(screen,couleur_curseur,[pos_x - width/2,pos_y,width,2],0)

def rendu3D(r1,r2,p,couleur_rendu,numéro, Rsphere):
    '''
    entrée :
        r1 : rayon du grand cercle
        r2 : rayon du petit cercle
        p : distance entre le centre du petit cercle et le point P
        couleur_rendu : la couleur du rendu
    effet :
        affiche le rendu et le bouton_gcode
    '''
    centre_x, centre_y = 3*window_width/4,window_height/2
    if not (r1 > window_height/4 or r2 >= r1 or p > r2) : 
        #draw.circle(screen,BLUE,(3*window_width/4,3*window_height/4),r1,1)
        point_x, point_y, point_z = points3D(6000.0, 10000, r1, r2, p, Rsphere)
        if numéro == 1:
            for i in range(10000):
                draw.circle(screen,couleur_rendu,(centre_x+1.7*point_x[i],centre_y + window_height/10+1.7*point_y[i]),1)
            draw.line(screen, couleur("RED"), (centre_x - window_width/5, centre_y+window_height/10), (centre_x + window_width/5, centre_y+window_height/10), 2)
            flèche_x = centre_x + window_width / 5
            flèche_y = centre_y + window_height / 10
            draw.polygon(screen, couleur("RED"),[(flèche_x + 10, flèche_y),(flèche_x, flèche_y - 5),(flèche_x, flèche_y + 5)])
            draw.line(screen, couleur("RED"), (centre_x, centre_y+window_height/2.4), (centre_x , centre_y-window_height/4), 2)
            flèche_x = centre_x
            flèche_y = centre_y - window_height / 4  # Extrémité supérieure de l'axe
            draw.polygon(screen, couleur("RED"),[(flèche_x, flèche_y - 10),(flèche_x - 5, flèche_y),(flèche_x + 5, flèche_y)])
            ecriture("x",couleur("RED"),police_taille,(centre_x + window_width / 5, centre_y + window_height / 7))
            ecriture("y",couleur("RED"),police_taille,(centre_x + window_width/20, centre_y - window_height / 4))
        if numéro == 2:
            for i in range(10000):
                draw.circle(screen,couleur_rendu,(centre_x+1.7*point_x[i],centre_y + window_height/5 +1.7*point_z[i]),1)
            draw.line(screen, couleur("RED"), (centre_x - window_width/5, centre_y+window_height/10), (centre_x + window_width/5, centre_y+window_height/10), 2)
            flèche_x = centre_x + window_width / 5
            flèche_y = centre_y + window_height / 10
            draw.polygon(screen, couleur("RED"),[(flèche_x + 10, flèche_y),(flèche_x, flèche_y - 5),(flèche_x, flèche_y + 5)])
            draw.line(screen, couleur("RED"), (centre_x, centre_y+window_height/2.4), (centre_x , centre_y-window_height/4), 2)
            flèche_x = centre_x
            flèche_y = centre_y - window_height / 4  # Extrémité supérieure de l'axe
            draw.polygon(screen, couleur("RED"),[(flèche_x, flèche_y - 10),(flèche_x - 5, flèche_y),(flèche_x + 5, flèche_y)])
            ecriture("x",couleur("RED"),police_taille,(centre_x + window_width / 5, centre_y + window_height / 7))
            ecriture("z",couleur("RED"),police_taille,(centre_x + window_width/20, centre_y - window_height / 4))
    bouton_gcode((0,0))

def zoom_rendu3D(lines2, numéro):
    '''
    entrée :
        r1 : rayon du grand cercle
        r2 : rayon du petit cercle
        p : distance entre le centre du petit cercle et le point P
        couleur_rendu : la couleur du rendu
    effet :
        affiche le rendu
    '''
    global run_zoom_rendu,couleur_g_cercle,couleur_p_cercle,couleur_fond
    if is_float(lines2[0]) and is_float(lines2[1]) and is_float(lines2[2]) and is_float(lines2[3]):
        Rsphere = float(lines2[0])*(window_height/2)/100
        r1 = float(lines2[1])*(window_height/2)/100
        r2 = float(lines2[2])*(window_height/2)/100
        p = float(lines2[3])*(window_height/2)/100
    centre_x, centre_y = window_width/2,window_height/2
    if not (r1 > window_height/2 or r2 >= r1 or p > r2) : 
        screen.fill(couleur_fond)
        #draw.circle(screen,BLUE,(3*window_width/4,3*window_height/4),r1,1)
        point_x, point_y, point_z = points3D(12000.0, 75000, r1, r2, p, Rsphere)
        if numéro == 1:
            for i in range(75000):
                draw.circle(screen,couleur_rendu,(centre_x+point_x[i],centre_y+point_y[i]),1)
        if numéro == 2:
            for i in range(75000):
                draw.circle(screen,couleur_rendu,(centre_x+point_x[i],centre_y+point_z[i]),1)
    else :
        run_zoom_rendu = False

def points3D(theta_max, N, petit_r, grand_r, p,Rsphere) :
    theta = linspace(0.0, theta_max, N)
    diff_r = grand_r - petit_r
    q = 1.0 - (grand_r/petit_r) #arrangez vous pour que ce rapport soit différent de 1/2
    x = []
    y = []
    z = []
    print (Rsphere)
    for i in range ( N ) :
        new_x = diff_r*cos(theta[i]) + p * cos(q*theta[i])
        new_y = diff_r*sin(theta[i]) + p * sin(q*theta[i])
        if (grand_r - petit_r + p < float(Rsphere)):
            new_z = - sqrt(float(Rsphere)**2 - new_x**2 - new_y**2)
        #else:
            
        x.append(new_x)
        y.append(new_y)
        z.append(new_z)
    
    return x, y, z

#fonctions pour le menu Infos et Paramètres

def menu_param_et_info():
    '''
    effet :
        - affiche des boutons pour changer les couleurs de fond
        - affiche des boutons indiquant les couleurs pour le rendu
    '''
    screen.fill(couleur_param)
    ecriture("Paramètres & Informations",couleur("WHITE"),police_taille*3//2,(window_width/2,3*window_height/20))
    
    ecriture("Le but de ce projet est de générer un fichier G CODE",couleur("BLACK"),police_taille*2//3,(window_width/2,5*window_height/20))
    ecriture("utilisable par une imprimante 3D",couleur("BLACK"),police_taille*2//3,(window_width/2,6*window_height/20))
    ecriture("En se basant sur le fonctionnement d'un spirographe",couleur("BLACK"),police_taille*2//3,(window_width/2,7*window_height/20))

    ecriture("Contributeurs :",couleur("WHITE"),police_taille,(window_width/2,9*window_height/20))
    ecriture("Antoine Dumont (Dev)",couleur("BLACK"),police_taille*2//3,(window_width/2,11*window_height/20))
    ecriture("Julien Chantail (Dev)",couleur("BLACK"),police_taille*2//3,(window_width/2,12*window_height/20))
    ecriture("Papis Diop (Dev)",couleur("BLACK"),police_taille*2//3,(window_width/2,13*window_height/20))
    ecriture("Ulysse Gaumet (Tuteur)",couleur("BLACK"),police_taille*2//3,(window_width/2,14*window_height/20))

    bouton_github((0,0))
    return_arrow((0,0))
    bouton_couleur((0,0))
    bouton_ede((0,0))
    bouton_compte_rendu((0,0))

def clic_param_et_info(coord):
    '''
    entrée : les coordonnées du clic
    effet : change la couleur selon le clic
    '''
    global run_param_et_info, run_couleur, run_ede
    if return_arrow(coord):
        run_param_et_info = False
    if bouton_github(coord):
        url = "https://github.com/Nashoba1er/SPIROGRAPHE"
        webopen(url)
    if bouton_compte_rendu(coord):
        script_dir = path.dirname(__file__)  # Dossier où se trouve le script
        presentation_path = path.join(script_dir, "img", "project_tech__spirographe-4.pdf")  # Sous-dossier "img"
        startfile(presentation_path)
    if bouton_couleur(coord):
        run_couleur = True
    if bouton_ede(coord):
        run_ede = True

def bouton_github(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton Github :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "  Github    "
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 2*window_width/10
    pos_y = 6*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))

    #affiche_github_logo : 
    affiche_logo_github(res,logo_github)
    return res

def bouton_compte_rendu(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton Github :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie : 
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "Compte rendu"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 8*window_width/10
    pos_y = 6*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def affiche_logo_github(res,image):
    pos_x = 2*window_width/10
    pos_y = 6*window_height/10

    image = image.convert_alpha()
    image = transform.scale(image, (police_taille*0.8, police_taille*0.8))
    # Modifier les couleurs en utilisant pygame.surfarray.array3d()
    image_array = surfarray.array3d(image)

    inverted_array = 255 - image_array  # Inversion des couleurs

    image_array = inverted_array

    # Trouver et remplacer les pixels noir (l'image est noire)
    mask = all(image_array == couleur("WHITE"), axis=-1)  # Crée un masque des pixels blancs
    if res:
        image_array[mask] = couleur("GREEN")  # Remplace les pixels blancs par vert
    else : 
        image_array[mask] = couleur("WHITE")  # Remplace les pixels blancs par vert

    # Convertir le tableau modifié en une surface Pygame
    modified_image = surfarray.make_surface(image_array)

    screen.blit(modified_image, (pos_x+3.5*police_taille*3/5,pos_y-police_taille/2+4))


#fonctions pour le menu G CODE :

def points_3d (theta_max, N, petit_r, grand_r, p, Rsphere, nb_couches, ep_couches) :
    '''
    retourne la liste des points en 3D de coordonée z qui varie selon le rayon Rsphere si (grand_r-petit_r+p)<=Rpshere
    retourne la liste des points en 3D de coordonée z fixe égale à 0 si Rsphere = 0
    '''
  
    theta = linspace(0.0, theta_max, N)
    diff_r = grand_r - petit_r
    q = 1.0 - (grand_r/petit_r) #arrangez vous pour que ce rapport soit différent de 1/2
    max_dist = diff_r + p
    res = []
    for j in range (nb_couches) :
        if (Rsphere == 0) :
            for i in range (N) :
                new_x = diff_r*cos(theta[i]) + p * cos(q*theta[i])
                new_y = diff_r*sin(theta[i]) + p * sin(q*theta[i])
                z = j*ep_couches
                res.append((new_x, new_y, z))
        elif (max_dist<=Rsphere) :
            for i in range (N) :
                new_x = diff_r*cos(theta[i]) + p * cos(q*theta[i])
                new_y = diff_r*sin(theta[i]) + p * sin(q*theta[i])
                z = sqrt(Rsphere*Rsphere - new_x*new_x - new_y*new_y) - sqrt (Rsphere*Rsphere - max_dist*max_dist) + j*ep_couches
                res.append((new_x, new_y, z))
        else:
            print("Rsphere trop petit")
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
                        (points[i][2] - points[i - 1][2]) ** 2) ** 0.5
            extrusion += distance * extrusion_rate
            gcode.append(f"G1 X{x:.6f} Y{y:.6f} Z{z:.6f} E{extrusion:.4f}")
    gcode.append("G1 E-1 F300 ; Rétractation")
    gcode.append("G28 ; Retour à l'origine")
    gcode.append("M104 S0 ; Arrêt de l'extrudeur")
    gcode.append("M140 S0 ; Arrêt du plateau")
    gcode.append("; Fin du fichier G-code")
    return "\n".join(gcode)

def write_gcode (theta_max, N, petit_r, grand_r, p, Rsphere, nb_couches, ep_couches) :
  points = points_3d (theta_max, N, petit_r, grand_r, p, Rsphere, nb_couches, ep_couches)
  gcode = generate_gcode_points (points)
  if (Rsphere>=(grand_r - petit_r + p)) :
    gcode_name = f"{theta_max:.0f}_{N}_{petit_r:.0f}_{grand_r:.0f}_{p:.0f}_{Rsphere:.0f}_{nb_couches}_{1000*ep_couches:.0f}.gcode"
  elif (Rsphere==0) :
    gcode_name = f"{theta_max:.0f}_{N}_{petit_r:.0f}_{grand_r:.0f}_{p:.0f}_a_plat_{nb_couches}_{1000*ep_couches:.0f}.gcode"
  return gcode_name, gcode

def sauvegarde_fichier_gcode(name, content):
    root = Tk()
    root.withdraw()  # Cacher la fenêtre principale Tkinter
    fichier = filedialog.asksaveasfilename(
        title="Enregistrer sous",
        initialfile=name,
        filetypes=[("Fichiers GCODE", "*.gcode"), ("Tous les fichiers", "*.*")]
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

def menu_g_code(theta_max, N, petit_r, grand_r, p, Rsphere):
    screen.fill((0, 0, 0))  # Fond noir
    i = 1
    ecriture("Vous vous appretez à sauvegarder un fichier gcode" , (255,255,255), 25, (window_width/2, i*window_height/12))
    ecriture("généré selon les paramètres suivants" , (255,255,255), 25, (window_width/2, (2*i+1)*window_height/24))
    i = i+1.5
    i = 2*i+1
    ecriture(f"theta_max = {theta_max}", (255,255,255),25,(window_width/2, i*window_height/24))
    i = i+1.5
    ecriture(f"N = {N}",(255,255,255), 25,(window_width/2, i*window_height/24))
    i = i+1.5
    ecriture( f"grand_r = {grand_r}", (255,255,255),25,(window_width/2, i*window_height/24))
    i = i+1.5
    ecriture( f"petit_r = {petit_r}", (255,255,255),25,(window_width/2, i*window_height/24))
    i = i+1
    ecriture( f"p = {p}", (255,255,255),25,(window_width/2, i*window_height/24))
    i = i+1
    if Rsphere == 0 :
        ecriture( "à plat", (255,255,255),25,(window_width/2, i*window_height/24))
    elif Rsphere >= (grand_r+p-petit_r) :
        ecriture(f"Rsphere = {Rsphere}", (255,255,255),25,(window_width/2, i*window_height/24))
    i = i+1
    ecriture("appuyez sur Entrée pour poursuivre", (255,255,255), 25 ,(window_width/2, i*window_height/12))
    i = i+1
    ecriture("sinon, fermez la fenêtre", (255,255,255), 25, (window_width/2, i*window_height/12))
    return_arrow((0,0))
    bouton_save_g_code((0,0))

    display.flip()

def sauvegarde_g_code(lines):
    global window_height,window_width
    grand_r = float(lines[0])*(window_height/4)/100
    petit_r = float(lines[1])*(window_height/4)/100
    p = float(lines[2])*(window_height/4)/100
    gcode_name, gcode = write_gcode(12000.0, 100000, petit_r, grand_r, p, 0)
    chemin_fichier = sauvegarde_fichier_gcode(gcode_name, gcode)
    if chemin_fichier:
        print(f"Fichier enregistré à : {chemin_fichier}")

def bouton_save_g_code(pos):
    #Ajout pour les boutons
    res = False
    message = "Sauvegarder G CODE"
    (cursor_x, cursor_y) = pos
    police_taille2 = police_taille-8
    width = police_taille2*3/5*(len(message)+1)*2
    height = police_taille2*2
    pos_x = window_width/2
    pos_y = 8*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("GREEN"),police_taille2*2,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture(message,couleur("WHITE"),police_taille2*2,(pos_x,pos_y))
    return res

def clic_g_code(pos):
    global run_g_code, cursor_position, current_line,police_taille_valeurs_champs,lines, numéro
    coord_x, coord_y = pos
    current_line_y = 25*window_height/32
    current_line_x = window_width/2 - 2.5*1.1*window_width/8
    height = 1.1*police_taille_valeurs_champs
    width = window_width/8
    taille_carac = 3*police_taille_valeurs_champs/5
    if bouton_sauvegarde(pos):
        gcode_name, gcode = write_gcode (theta_max, N, petit_r, grand_r, p, Rsphere, nb_couches, ep_couches)
        run_g_code = False
        chemin_fichier = sauvegarde_fichier_gcode(gcode_name, gcode)
        if chemin_fichier:
            print(f"Fichier enregistré à : {chemin_fichier}")
        run_g_code = False
        if run_cdc : 
            menu_cercle_dans_cercle_init(lines)
        if run_cdc3D :
            menu_cdc3D(numéro)
    elif bouton_annulation(pos):
        run_g_code = False
        if run_cdc : 
            menu_cercle_dans_cercle_init(lines)
        if run_cdc3D :
            menu_cdc3D(numéro)
    elif return_arrow(pos):
        run_g_code = False
        if run_cdc : 
            menu_cercle_dans_cercle_init(lines)
        if run_cdc3D :
            menu_cdc3D(numéro)
    for i in range(5):
        if (coord_y > current_line_y and coord_y < current_line_y  + height and coord_x > (i*1.1*window_width/8)+current_line_x and coord_x < (i*1.1*window_width/8)+current_line_x+width) :
            # je suis dans le champ i
            current_line = i
            cursor_position = len(lines3[current_line])
            for carac in range(len(lines3[current_line])):
                if (coord_x < current_line_x + (len(lines3[current_line])-carac)*taille_carac) :
                    cursor_position = len(lines3[current_line])-carac - 1

def champ_gcode(num_champ):
    '''
    entrée :
        num_champ : numéro du champ
    effet :
        colorie en blanc le champ numéro "num_champ" (efface son contenu)
    '''

    height = 1.1 * police_taille_valeurs_champs
    width = window_width/8
    width_2 = 1.1 * width
    x_champ = window_width/2 + (num_champ-2.5)*width_2
    x_texte = x_champ + width/2
    y_champ = 25*window_height/32
    y_texte = 49*window_height/64
    if num_champ == 0 :
        ecriture ("theta_max (rad)", couleur("WHITE"), int(police_taille_valeurs_champs/3), (x_texte, y_texte))
    if num_champ == 1 :
        ecriture ("nb_points", couleur("WHITE"), int(police_taille_valeurs_champs/3), (x_texte, y_texte))
    if num_champ == 2 :
        ecriture ("theta_max (rad)", couleur("WHITE"), int(police_taille_valeurs_champs/3), (x_texte, y_texte))
    if num_champ == 3 :
        ecriture ("nb_points", couleur("WHITE"), int(police_taille_valeurs_champs/3), (x_texte, y_texte))
    if num_champ == 4 :
        ecriture ("theta_max (rad)", couleur("WHITE"), int(police_taille_valeurs_champs/3), (x_texte, y_texte))
    draw.rect(screen,couleur("WHITE"),[x_champ,y_champ,width,height])
    draw.rect(screen,couleur("BLACK"),[x_champ,y_champ,width,height],6)
    draw.rect(screen,couleur("WHITE"),[x_champ,y_champ,width,height],2)

def input_to_text_g_code(event):
    global current_line, lines3, cursor_position, key_press_times, run_cdc
    taille_carac = 3/5 * police_taille
    keys = key.get_pressed()
    longueur_current_line = len(lines3[current_line])

    if event.key == K_BACKSPACE:
        # Si Retour arrière est appuyé
        if longueur_current_line > 1 and cursor_position > 0:
            if cursor_position == 1 :
                lines3[current_line] = lines3[current_line][1:]
            elif cursor_position == (longueur_current_line) :
                lines3[current_line] = lines3[current_line][:-1]
            else :
                lines3[current_line] = lines3[current_line][:(cursor_position-1)] + lines3[current_line][(cursor_position):]  # Supprime le dernier caractère
            cursor_position -= 1
        modifie_valeurs(lines3)
    elif event.key == K_UP :
        if int(lines3[current_line]) < (10**character_limit_gcode - 1) :
            lines3[current_line] = str(int(float(lines3[current_line])) + 1)
        cursor_position = len(lines3[current_line])
        modifie_valeurs(lines3)
    elif event.key == K_DOWN :
        if int(lines3[current_line]) > 0 :
            lines3[current_line] = str(int(float(lines3[current_line])) - 1)
        modifie_valeurs(lines3)
    elif event.key == K_RIGHT:
        #si on appuie sur la flèche de droite, le curseur se déplace d'une lettre
        if cursor_position < (longueur_current_line):
            cursor_position += 1
    elif event.key == K_LEFT:
        #si on appuie sur la flèche de gauche, le curseur se déplace d'une lettre
        if cursor_position > 0:
            cursor_position -=1
    else:
        # Autres touches
        if longueur_current_line < character_limit_gcode:
        # Ajouter le caractère à la ligne actuelle
            letter = event.unicode
            if letter and letter.isdigit():  # Si la touche produit un caractère (ignore Shift, Ctrl, etc.)
                if cursor_position == 0:
                    lines3[current_line] = letter + lines3[current_line]
                elif cursor_position < (longueur_current_line):
                    lines3[current_line] = lines3[current_line][:(cursor_position)] + letter + lines3[current_line][(cursor_position):]
                else:
                    lines3[current_line] += letter
                cursor_position += 1
                modifie_valeurs(lines3)

def ecrit_champ_gcode(num_champ):
    '''
    entrée :
        num_champ : numéro du champ
    effet :
        met à jour le contenu du champ numéro "current_line"
    '''
    global police_taille_valeurs_champs
    current_line_y = 25*window_height/32
    current_line_x = window_width/2 + (num_champ - 2.5)*1.1*window_width/8
    spacing = 1/5*police_taille_valeurs_champs #marge gauche
    taille_carac = 3/5 * police_taille_valeurs_champs
    indent_x,indent_y = current_line_x+spacing,current_line_y # position
    champ_gcode(num_champ)
    # Rendre et afficher chaque ligne de texte
    police = font.SysFont("Courier New", police_taille_valeurs_champs)
    txt_surf = police.render(lines3[num_champ], True, couleur("BLACK"))
    screen.blit(txt_surf, (indent_x, indent_y))
    display.update()

def modifie_valeurs(lines3):
    global theta_max, N, grand_r, petit_r, Rsphere, nb_couches, ep_couches, p
    theta_max = float(lines3[0])
    N = int(lines3[1])
    nb_couches = int(lines3[2])
    ep_couches = float(lines3[3])/1000
    grand_r = float(lines3[4])
    petit_r = float(int(round((rapport_petit_r*grand_r), 0)))
    p = float(int(round((rapport_p*grand_r), 0)))
    Rsphere = float(int(round((rapport_rsphere*grand_r), 0)))

def bouton_sauvegarde(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton SAUVEGARDER LE G CODE :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie :
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "SAUVEGARDER LE G CODE"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 2*window_width/5
    pos_y = 9*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def bouton_annulation(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton ANNULER :
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    sortie :
        renvoie True si le curseur est sur le bouton, False sinon
    '''
    res = False
    message = "ANNULER"
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*(len(message)+1)
    height = police_taille
    pos_x = 23*window_width/32
    pos_y = 9*window_height/10
    draw.rect(screen,couleur("BLACK"),[pos_x-(width/2),pos_y-(height/2),width,height],0)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,couleur("GREEN"),[pos_x-(width/2),pos_y-(height/2),width,height],2)
        ecriture(message,couleur("GREEN"),police_taille,(pos_x,pos_y))
        res = True
    else :
        draw.rect(screen,couleur("WHITE"),[pos_x-(width/2),pos_y-(height/2),width,height],2)
        ecriture(message,couleur("WHITE"),police_taille,(pos_x,pos_y))
    return res

def menu_g_code_init(lines3):
    screen.fill((0, 0, 0))  # Fond noir
    i = 1
    ecriture("Vous vous appretez à sauvegarder un fichier gcode" , (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    ecriture("généré selon les paramètres suivants" , (255,255,255), police_taille_infos, (window_width/2, (2*i+1)*window_height/24))
    i = i+1.5
    ecriture("angle de rotation variant de 0 à " + str(int(theta_max)) + " rad", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    i = i+1
    if N<=1 :
        ecriture("Motif de " + str(N) + " point", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    elif N>1 :
        ecriture("Motif de " + str(N) + " points", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    i = i+1
    if nb_couches == 1 :
        ecriture("une couche d'epaisseur " + str(ep_couches) + " mm", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    elif (nb_couches >= 2) :
        ecriture(str(nb_couches) + " couches d'epaisseur " + str(ep_couches) + " mm", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    i = i+1
    ecriture("rayon du grand cercle égal à " + str(float(grand_r)/10) + " cm", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    i = i+1
    ecriture("rayon du petit cercle égal à " + str(float(petit_r)/10) + " cm", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    i = i+1
    ecriture("stylo posé à " + str(float(p)/10) + " cm du centre du petit cercle", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    i = i+1
    if Rsphere == 0 :
        ecriture("à plat", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))
    elif (Rsphere >= (grand_r-petit_r+p)) :
        ecriture("motif posé sur une sphere de rayon " + str(float(Rsphere)/10) + " cm", (255,255,255), police_taille_infos, (window_width/2, i*window_height/12))

    bouton_sauvegarde ((0, 0))
    bouton_annulation ((0, 0))
    return_arrow((0,0))
    ecrit_champ_gcode (0)
    ecrit_champ_gcode (1)
    ecrit_champ_gcode (2)
    ecrit_champ_gcode (3)
    ecrit_champ_gcode (4)
    display.flip()


# fonctoins pour le menu Ellipse dans Ellipse :

def menu_ede():
    screen.fill(couleur_fond)

    return_arrow((0,0))

def clic_ede(coord):
    global run_ede
    if return_arrow(coord):
        run_ede = False


## affichage

# définition de l'écran

# taille de l'écran
info = display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Dimensions ajustées à 90% de l'écran
window_width = int(screen_width)
window_height = int(screen_height * 0.90)

if window_height > 9/16*window_width :
    window_height = 9/16*window_width
else : 
    window_width = 16/9*window_height

# paramètres de la fenêtre
size = window_width, window_height #pour choisir la taille de la fenêtre
screen = display.set_mode(size) # pour créer une fenêtre de la taille souhaitée
display.set_caption('génération de gcode pour un spirographe') #donner un nom affiché à cette fenêtre.
display.update() #mettre à jour les données de l'affichage
screen.fill(couleur("BLEU_JOLI")) #pour choisir la couleur du fond de la fenêtre


# Variables globales
police_taille = int(window_height/17)
police = font.SysFont("Courier New", police_taille)  # Police par défaut, taille 36
character_limit = 7  # Limite de caractères par ligne
lines = ['75','40','20']  # Liste des lignes de texte
lines2 = ['80', '60', '40', '20'] # Liste des lignes de texte pour 3D
police_taille_valeurs_champs = int(window_height/22)
police_taille_infos = int(window_height/36)

# variables globales G CODE
theta_max = 6000.0
N = 100000
petit_r = 39
grand_r = 100
p = 35
Rsphere = 175
nb_couches = 4
ep_couches = 1
lines3 = [str(int(theta_max)), str(N), str(nb_couches), str(1000*ep_couches), str(grand_r)]
rapport_rsphere = float(Rsphere)/float(grand_r)
rapport_petit_r = float(petit_r)/float(grand_r)
rapport_p = float(p)/float(grand_r)
character_limit_gcode = 7


current_line = 0  # Index de la ligne courante
cursor_position = 2
couleur_g_cercle = couleur("RED")
couleur_p_cercle = couleur("BLEU_FONCE")

couleur_rendu = couleur("WHITE")
couleur_fond = couleur("C1_BLUE")
couleur_param = couleur("BLEU_JOLI")

try:
    with open("data_prout.json", "r") as file:
        data = load(file)
        couleur_fond_str = data.get("couleur_fond", str(couleur("C1_BLUE")))  # Valeur par défaut 0 si "x" n'existe pas

        color_tuple = eval(couleur_fond_str)
except FileNotFoundError:
    couleur_fond = couleur("C1_BLUE")
    couleur_param = couleur("BLEU_JOLI")
    couleur_rendu = couleur("WHITE")


dragging = -1
d_equal_r = False

run = True
run_cdc = False
run_zoom_schema = False
run_zoom_rendu = False
run_couleur = False
run_cdc3D = False
run_param_et_info = False
numéro = 2
run_g_code = False
run_ede = False

menu_choix()

while run :
    for pyEvent in event.get():
        if pyEvent.type == QUIT:
            run = False
        if pyEvent.type == MOUSEMOTION :
            bouton_cdc(pyEvent.pos)
            bouton_cdc3D(pyEvent.pos)
            bouton_param_et_info(pyEvent.pos)
        if pyEvent.type == MOUSEBUTTONDOWN :
            clic_menu(pyEvent.pos)
            if run_cdc : 
                menu_cercle_dans_cercle_init(lines)
                
            while run_cdc : 
                for pyEvent in event.get():
                    if pyEvent.type == QUIT:
                        run_cdc = False
                        run = False
                    if pyEvent.type == MOUSEBUTTONDOWN:
                        clic(pyEvent.pos)
                        if run_zoom_schema:
                            zoom_schema(lines)
                        while run_zoom_schema :
                            for pyEvent in event.get():
                                if pyEvent.type == QUIT :
                                    run = False
                                    run_cdc = False
                                    run_zoom_schema = False
                                if pyEvent.type == MOUSEBUTTONDOWN :
                                    run_zoom_schema = False
                                    menu_cercle_dans_cercle_init(lines)
                                    ecrit(current_line)
                            display.flip() #mettre à jour l'affichage
                        if run_zoom_rendu:
                            zoom_rendu(lines)
                        while run_zoom_rendu :
                            for pyEvent in event.get():
                                if pyEvent.type == QUIT :
                                    run_cdc = False
                                    run_zoom_rendu = False 
                                    run = False
                                if pyEvent.type == MOUSEBUTTONDOWN :
                                    run_zoom_rendu = False
                                    menu_cercle_dans_cercle_init(lines)
                                    ecrit(current_line)
                                if pyEvent.type == MOUSEMOTION :
                                    return_arrow(pyEvent.pos)
                            display.flip() #mettre à jour l'affichage
                        if run_g_code: 
                            lines3 = [str(int(theta_max)), str(N), str(nb_couches), str(1000*ep_couches), str(lines[0])]
                            rapport_rsphere = 0 # float(Rsphere)/float(grand_r)
                            rapport_petit_r = float(lines[1])/float(lines[0])
                            rapport_p = float(lines[2])/float(lines[0])
                            menu_g_code_init(lines3)
                        # Boucle g_code
                        while run_g_code:
                            for Pyevent in event.get():
                                if Pyevent.type == QUIT:
                                    run_g_code = False
                                    run_cdc = False
                                    run = False
                                if Pyevent.type == MOUSEMOTION :
                                    bouton_sauvegarde(Pyevent.pos)
                                    bouton_annulation(Pyevent.pos)
                                    return_arrow(Pyevent.pos)
                                    display.flip()
                                if Pyevent.type == MOUSEBUTTONDOWN :
                                    clic_g_code(Pyevent.pos)
                                if Pyevent.type == KEYDOWN:
                                    input_to_text_g_code(Pyevent)
                                    menu_g_code_init(lines3)
                            display.flip()

                    if pyEvent.type == KEYDOWN:
                        input_to_text(pyEvent)  # Appel à la fonction pour gérer l'input
                        if d_equal_r:
                            ecrit(2)
                        ecrit(current_line)
                    if pyEvent.type == MOUSEMOTION:
                        bouton_gcode(pyEvent.pos)
                        return_arrow(pyEvent.pos)
                        bouton_d_equal_r(pyEvent.pos)
                    # Relâchement du clic
                    if pyEvent.type == MOUSEBUTTONUP:
                        dragging = -1  # On arrête de déplacer l'objet
                    if pyEvent.type == MOUSEMOTION and dragging >= 0:
                        bouge_curseur(pyEvent.pos,dragging)
                    display.flip() #mettre à jour l'affichage
            if run_cdc3D :
                menu_cdc3D(numéro)
            while run_cdc3D :
                for pyEvent in event.get():
                    if pyEvent.type == QUIT:
                        run = False
                        run_cdc3D = False
                    if pyEvent.type == MOUSEMOTION :
                        return_arrow(pyEvent.pos)
                        bouton_xy(pyEvent.pos)
                        bouton_xz(pyEvent.pos)
                    if pyEvent.type == MOUSEBUTTONDOWN :
                        numéro = clic_cdc3D(pyEvent.pos,numéro)
                        modifie_rayons3D(lines2,numéro)
                        display.flip()
                        while run_zoom_rendu :
                            zoom_rendu3D(lines2, numéro)
                            for pyEvent in event.get():
                                if pyEvent.type == QUIT :
                                    run_cdc = False
                                    run_zoom_rendu = False 
                                    run = False
                                if pyEvent.type == MOUSEBUTTONDOWN :
                                    run_zoom_rendu = False
                                    menu_cdc3D(numéro)
                                    ecrit3D(current_line)
                                if pyEvent.type == MOUSEMOTION :
                                    return_arrow(pyEvent.pos)
                            display.flip() #mettre à jour l'affichage
                    if pyEvent.type == KEYDOWN:
                        input_to_text3D(pyEvent,numéro)  # Appel à la fonction pour gérer l'input
                        ecrit3D(current_line)
                display.flip()
                    
            if run_param_et_info :
                menu_param_et_info()
            while run_param_et_info :
                for pyEvent in event.get():
                    if pyEvent.type == QUIT:
                        run = False
                        run_param_et_info = False
                    if pyEvent.type == MOUSEMOTION :
                        return_arrow(pyEvent.pos)
                        bouton_couleur(pyEvent.pos)
                        bouton_ede(pyEvent.pos)
                        bouton_github(pyEvent.pos)
                        bouton_compte_rendu(pyEvent.pos)
                    if pyEvent.type == MOUSEBUTTONDOWN :
                        clic_param_et_info(pyEvent.pos)
                        if run_couleur :
                            menu_couleur()
                        while run_couleur :
                            for pyEvent in event.get():
                                if pyEvent.type == QUIT:
                                    run = False
                                    run_param_et_info = False
                                    run_couleur = False
                                if pyEvent.type == MOUSEMOTION :
                                    boutons_choix_couleur(pyEvent.pos)
                                    return_arrow(pyEvent.pos)
                                if pyEvent.type == MOUSEBUTTONDOWN :
                                    clic_couleur(pyEvent.pos)
                            display.flip()
                        if run_ede :
                            menu_ede()
                        while run_ede:
                            for pyEvent in event.get():
                                if pyEvent.type == QUIT:
                                    run = False
                                    run_param_et_info = False
                                    run_couleur = False
                                if pyEvent.type == MOUSEMOTION :
                                    return_arrow(pyEvent.pos)
                                if pyEvent.type == MOUSEBUTTONDOWN :
                                    clic_ede(pyEvent.pos)
                            display.flip()
                        menu_param_et_info()
                display.flip()
            menu_choix()

    display.flip() #mettre à jour l'affichage

print(str(couleur_fond))

# Sauvegarder plusieurs valeurs
data = {
    "couleur_fond" : str(couleur_fond),
    "couleur_param": str(couleur_param),
    "couleur_rendu": str(couleur_rendu)}

with open("data.json", "w") as file:
    dump(data, file)


quit()



# commande pour convertir le fichier python en fichier .exe :

        # pyinstaller --onefile \
        #     --add-data "documents/mon_fichier.pdf;documents" \
        #     --add-data "images/image1.png;images" \
        #     --add-data "images/image2.jpg;images" \
        #     "C:/Users/antoi/Documents_local/dossier_mines_st_etienne/cours/protech/code/logiciel spirographe.py"
