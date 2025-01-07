from pygame import *
import sys

# Initialisation de 
init()

# taille de l'écran
info = display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Définir les dimensions de la fenêtre
screen_width = int(screen_width)
screen_height = int(screen_height * 0.90)

# Créer la fenêtre
screen = display.set_mode((screen_width, screen_height))
display.set_caption("Fenêtre Pygame - Fond bleu")

# Couleur bleue
blue_color = (0, 0, 255)

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

screen.fill(blue_color)


# Boucle principale
running = True
while running:
    for pyEvent in event.get():
        if pyEvent.type == QUIT:  # Quitter le programme
            running = False

    # Remplir l'écran avec la couleur bleue
    ecriture("prout oe oe oe",(0,255,0),360,(screen_width/2,screen_height/2))

    # Mettre à jour l'écran
    display.flip()

# Quitter Pygame
quit()
sys.exit()
