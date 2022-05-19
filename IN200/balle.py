import tkinter as tk
import random as rd

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

# Variables
mouv = 0
x=0
y=0
rayon=0
est_fixe = False


###################
# Fonctions

def creer_balle():
    global x, y, rayon
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    global mouv, est_fixe
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    if est_fixe == False :
        canvas.move(balle[0], balle[1], balle[2])
        mouv = canvas.after(20, mouvement)
        alea = rd.randint(0, 100)
    if alea < 5 :
        canvas.after_cancel(mouv)
        est_fixe = True
        #attend_clic()
"""
def attend_clic(event):
    global est_fixe
    if x-rayon <event.x< x+rayon and y-rayon <event.y < y+rayon :
        rayon = rayon - 5
        est_fixe = False"""




    


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]

        alea = rd.randint(0, 100)
        if alea < 5 :
            canvas.after_cancel(mouv)


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()


# initialisation de la balle
balle = creer_balle()
#racine.bind('<Button1>', attend_clic)

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
