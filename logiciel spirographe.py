from pygame import init, draw, font, K_BACKSPACE, key, K_RETURN, K_DOWN, K_UP, KEYDOWN, K_LEFT, K_RIGHT, KEYUP, time
from pygame import K_TAB, K_LSHIFT, K_RSHIFT, display, event, QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP, K_ESCAPE
from numpy import linspace, cos, sin

# couleurs

BLACK = (0, 0, 0)
GRAY = (150, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0) 
CYAN = (0, 255, 255) #Bleu très clair
MAGENTA = (255, 0, 255) #Violet pétant

PINK = (255,0,128) #Rose
PINK2 = (255, 20, 147) #Rose fluo
PINK3 = (255, 192, 203)

C1_GREEN = (204, 255, 204) #Vert très clair
C1_BLUE = (153, 204, 255) #Bleu ciel -> couleur de l'écran
bgColor = (127,127,255) #Bleu sympa

VERT = (0,200,0)
JAUNE = YELLOW
ORANGE = (255,130,0)
ROUGE = RED
MARRON = (110,42,42)
NOIR = BLACK

CYAN = CYAN
ROSE_CLAIR = (255,182,193)
ROSE_FONCE = PINK
VIOLET_FONCE = (148,0,211)
BLEU = BLUE
BLEU_FONCE = (0,0,150)
GRIS_CLAIR = (200,200,200)
VERT_CLAIR = (150,255,150)

SAUGE_LOANN = (146,166,157)
ROSE_POUDREE = (204,153,159)
BLEU_JOLI = (169,184,204)

init() #on initialise tout

# fonctions d'affichage

def ecriture(phrase,couleur,taille,position):
    '''
    entrée :
        phrase : le texte
        couleur : la couleur du texte
        taille : la taille de la police
        position = (x,y) : la position du centre du texte
    effet : 
        ecrit ce qu'il faut où il faut    
    '''
    police = font.SysFont("Courier New", taille) #donner une forme à la police d'écriture
    string_rendu = police.render(phrase, True,couleur)     # Rendu du texte avec la police choisie
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
        ecriture("Rayon trop grand",RED,int(police_taille*1.3),(3*window_width/4,window_height/2))
    elif r2 > r1 :
        ecriture("Petit rayon plus grand",RED,int(police_taille),(3*window_width/4,3*window_height/8))
        ecriture("que le grand rayon",RED,int(police_taille),(3*window_width/4,5*window_height/8))
    elif p > r2 :
        ecriture("Point en dehors",RED,int(police_taille*1.3),(3*window_width/4,3*window_height/8))
        ecriture("du petit cercle",RED,int(police_taille*1.3),(3*window_width/4,5*window_height/8))
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
        ecriture("Rayon trop grand",RED,int(police_taille*2.6),(window_width/2,window_height/2))
    elif r2 > r1 :
        ecriture("Petit rayon plus grand",RED,int(police_taille*2.6),(window_width/2,3*window_height/8))
        ecriture("que le grand rayon",RED,int(police_taille*2.6),(window_width/2,5*window_height/8))
    elif p > r2 :
        ecriture("Point en dehors",RED,int(police_taille*2.6),(window_width/2,3*window_height/8))
        ecriture("du petit cercle",RED,int(police_taille*2.6),(window_width/2,5*window_height/8))
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
    draw.rect(screen,WHITE,[current_line_x,(num_champ)*espace+current_line1_y,width,height])
    draw.rect(screen,BLACK,[current_line_x,(num_champ)*espace+current_line1_y,width,height],2)

def ecritures():
    '''
    effet : afficher les écritures de la page du spinographe en 2D
    '''
    ecriture("Saisie des paramètres",BLACK,police_taille,(window_width/4,window_height/8))
    ecriture("Rayon du grand cercle",BLACK,int(3/5*police_taille),(window_width/4,window_height/4))
    ecriture("Rayon du petit cercle",BLACK,int(3/5*police_taille),(window_width/4,window_height/2))
    ecriture("Distance au centre   ",BLACK,int(3/5*police_taille),(window_width/4,3*window_height/4))
    ecriture("R max = 100",BLACK,int(3/5*police_taille),(window_width/4,window_height/4+5*window_height/32))
    ecriture(" r max = R ",BLACK,int(3/5*police_taille),(window_width/4,window_height/2+5*window_height/32))
    ecriture(" d max = r ",BLACK,int(3/5*police_taille),(window_width/4,3*window_height/4+5*window_height/32))

def bouton_gcode(pos):
    '''
    entrée :
        pos = (x,y) : la position du curseur
    effet :
        affiche le bouton G CODE 
            en blanc si le curseur n'est pas dessus
            en vert à l'inverse
    '''
    res = False
    (cursor_x, cursor_y) = pos
    width = police_taille*3/5*7
    height = police_taille
    pos_x = window_width/2
    pos_y = 9*window_height/10
    draw.rect(screen,BLACK,[pos_x-(width/2),pos_y-(height/2),width,height],0,20)
    if cursor_x < pos_x+(width/2) and cursor_x > pos_x-(width/2) and cursor_y < pos_y+(height/2) and cursor_y > pos_y-(height/2):
        draw.rect(screen,GREEN,[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture("G CODE",GREEN,police_taille,(pos_x,pos_y))
        res = True

    else :
        draw.rect(screen,WHITE,[pos_x-(width/2),pos_y-(height/2),width,height],2,20)
        ecriture("G CODE",WHITE,police_taille,(pos_x,pos_y))
    return True

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
        affiche le rendu
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
    ecritures()
    modifie_rayons(lines)
    # ecrit_init :
    for i in range(3):
        ecrit(i)
        if i != current_line:
            draw.rect(screen,WHITE,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
    ecrit(current_line)
    curseurs_init(lines)
    return_arrow((0,0))

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
    
def menu_choix():
    global run_zoom_rendu,couleur_g_cercle,couleur_p_cercle,couleur_fond
    screen.fill(couleur_fond)
    r1 = 50*(window_height/2)/100
    r2 = 31.25*(window_height/2)/100
    p = 25*(window_height/2)/100
    centre_x, centre_y = window_width/2,window_height/2
    if not (r1 > window_height/2 or r2 >= r1 or p > r2) : 
        screen.fill(couleur_fond)
        #draw.circle(screen,BLUE,(3*window_width/4,3*window_height/4),r1,1)
        point_x, point_y = points(6000.0, 10000, r1, r2, p)
        for i in range(10000):
            draw.circle(screen,couleur_rendu,(centre_x+point_x[i],centre_y+point_y[i]),2)
    else :
        run_zoom_rendu = False
    
def curseurs_init(lines):
    for num_champ in range(3):
        curseur(num_champ)    

def curseur(num_champ):
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
        draw.circle(screen,BLACK,coord,5)
        draw.circle(screen,couleur_curseur,coord,3)

    else : 
        draw.rect(screen,couleur_curseur,[pos_x - width/2,pos_y,width,2],0)

def draw_arrow(surface, color, start_pos, width, height):
    '''
    dessine une flèche de la couleur color, de centre start_pos, de longueur width, de hauteur height (body) et de hauteur de triangle 3*height/2
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
        color_arrow = GREEN
        res = True
    else : 
        color_arrow = GRIS_CLAIR 
    draw.rect(screen,BLACK,[x-width/2,y-height/2,width,height],0,int((height+width)/10))
    draw.rect(screen,color_arrow,[x-width/2,y-height/2,width,height],2,int((height+width)/10))
    draw_arrow(screen,color_arrow,coord,width/2,height/3)
    return res

def bouge_curseur(coord,dragging):
    '''
    entrée : les coordonnées de la souris, dragging = le numéro du champ dont le curseur est associé
    effet : met à jour la position du curseur et met à jour le champ
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
    
    lines[num_curseur] = str(param)
    cursor_position = len(lines[current_line])
    modifie_rayons(lines)
    ecrit(num_curseur)
    curseur(num_curseur)
    

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
        met à jour la position du curseur et le contenu du champ
    '''
    global current_line, lines, cursor_position, key_press_times, run_visu_2D
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
            draw.rect(screen,WHITE,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line += 1
            cursor_position = len(lines[current_line])
        else :
            draw.rect(screen,WHITE,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line = 0
            cursor_position = len(lines[current_line])
    elif event.key == K_ESCAPE:
        run_visu_2D = False
    elif event.key == K_TAB and (keys[K_LSHIFT] or keys[K_RSHIFT]):
        if current_line > 0:
            draw.rect(screen,WHITE,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
            current_line -=1
            cursor_position = len(lines[current_line])
    elif event.key == K_TAB:
        #si on appuie sur la touche du bas, on passe à la ligne suivante :
        if current_line < 2:
            draw.rect(screen,WHITE,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
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

def ecrit(num_champ):
    '''
    entrée :
        num_champ : numéro du champ
    effet :
        affiche le contenu du champ numéro "current_line"
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
    txt_surf = police.render(lines[num_champ], True, BLACK)
    screen.blit(txt_surf, (indent_x, indent_y + num_champ*espace))
    draw.rect(screen,BLACK,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,0.7*window_height/15],0)
    curseur(num_champ)
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
            normalise les valeurs selon la taille de l'écran
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
            met la variable run_visu_2D à false

        (si le clic est sur le bouton G CODE :)
        (    ouvre le menu G CODE )
        (    n'ouvre pas le zoom_rendu)
    '''
    global current_line, cursor_position, run_zoom_rendu, run_visu_2D, run_zoom_schema, dragging
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
            draw.rect(screen,WHITE,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,taille_curseur],0)
            current_line = i
            cursor_position = len(lines[current_line])
            for carac in range(len(lines[current_line])):
                if (coord_x < current_line_x + (len(lines[current_line])-carac)*taille_carac) :
                    cursor_position = len(lines[current_line])-carac - 1
            draw.rect(screen,BLACK,[window_width/8 + cursor_position * taille_carac + taille_carac/4,(current_line)*window_height/4+9*window_height/32 + 0.15*window_height/15,2,taille_curseur],0)
        
        # Vérifie si le clic est sur un curseur
        if coord_y > (i)*espace+current_line1_y + 2 * window_height/32 and coord_y < (i)*espace+current_line1_y + 4 * window_height/32 :
            # je suis à hauteur du curseur
            if coord_x > current_line_x and coord_x < current_line_x  + width :
                dragging = i  # On commence à déplacer l'objet
                print("prout",i)
    #clic sur le shéma
    if (coord_x > window_width/2 and coord_y < window_height/2):
        run_zoom_schema = True 
    #clic sur le rendu
    if (coord_x > window_width/2 and coord_y > window_height/2):
        run_zoom_rendu = True
    #clic sur la flèche retour
    if return_arrow(coord):
        run_visu_2D = False

    if bouton_gcode(coord):
        print("clic sur le bouton G CODE")

    display.flip()


#fonctions pour le menu principal :



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
screen.fill(BLEU_JOLI) #pour choisir la couleur du fond de la fenêtre


# Variables globales
police_taille = int(window_height/17)
police = font.SysFont("Courier New", police_taille)  # Police par défaut, taille 36
character_limit = 7  # Limite de caractères par ligne
lines = ['75','40','20']  # Liste des lignes de texte
current_line = 0  # Index de la ligne courante
cursor_position = 2
couleur_g_cercle = ROUGE
couleur_p_cercle = BLEU_FONCE
couleur_rendu = WHITE
couleur_fond = C1_BLUE
couleur_param = BLEU_JOLI
dragging = -1

run = True
run_visu_2D = False
run_zoom_schema = False
run_zoom_rendu = False

while run :
    menu_choix()
    for pyEvent in event.get():
        if pyEvent.type == QUIT:
            run = False
        if pyEvent.type == KEYDOWN :
            if pyEvent.key == K_RETURN:
                menu_cercle_dans_cercle_init(lines)
                run_visu_2D = True
                while run_visu_2D : 
                    for pyEvent in event.get():
                        if pyEvent.type == QUIT:
                            run_visu_2D = False
                            run = False
                        if pyEvent.type == MOUSEBUTTONDOWN:
                            clic(pyEvent.pos)
                            while run_zoom_schema :
                                zoom_schema(lines)
                                for pyEvent in event.get():
                                    if pyEvent.type == QUIT :
                                        run_visu_2D = False
                                        run_zoom_schema = False
                                    if pyEvent.type == MOUSEBUTTONDOWN :
                                        run_zoom_schema = False
                                        menu_cercle_dans_cercle_init(lines)
                                display.flip() #mettre à jour l'affichage
                            while run_zoom_rendu :
                                zoom_rendu(lines)
                                for pyEvent in event.get():
                                    if pyEvent.type == QUIT :
                                        run_visu_2D = False
                                        run_zoom_rendu = False 
                                        run = False
                                    if pyEvent.type == MOUSEBUTTONDOWN :
                                        run_zoom_rendu = False
                                        menu_cercle_dans_cercle_init(lines)
                                        ecrit(current_line)
                                display.flip() #mettre à jour l'affichage
                            display.flip() #mettre à jour l'affichage
                        
                        if pyEvent.type == KEYDOWN:
                            input_to_text(pyEvent)  # Appel à la fonction pour gérer l'input
                            ecrit(current_line)
                        if pyEvent.type == MOUSEMOTION:
                            bouton_gcode(pyEvent.pos)
                            return_arrow(pyEvent.pos)
                        # Relâchement du clic
                        if pyEvent.type == MOUSEBUTTONUP:
                            dragging = -1  # On arrête de déplacer l'objet
                        if pyEvent.type == MOUSEMOTION and dragging >= 0:
                            bouge_curseur(pyEvent.pos,dragging)
                        display.flip() #mettre à jour l'affichage
    display.flip() #mettre à jour l'affichage


quit()
