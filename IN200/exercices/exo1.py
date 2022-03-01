import tkinter as tk

#######################
#constantes

#taille du canevas
WIDTH = 500
HEIGHT = 500

#variable qui choisit la couleur du rectangle
couleur = 0

#dit si la couleur est fixe: 
est_fixe = False


#coordonées des sommets du rectangle
x1, y1 = 150, 150
x2, y2 = 350, 350

######################
#fonctions

def gestion_du_clic(event):
    """Gère le clic sur le canevas"""
    global couleur, est_fixe
    if est_fixe == True :
        return
    liste_couleurs = ["red", "blue"] 
    if x1 < event.x < x2 and y1 < event.y < y2 :
        couleur = 1 - couleur
        canvas.itemconfigure(rectangle, fill = liste_couleurs[couleur])
    else :
        est_fixe = True 

def restart():
    """Mets le rectangle à rouge et autorise à modifier la couleur"""
    global est_fixe, couleur
    est_fixe = False
    couleur = 0
    canvas.itemconfigure(rectangle, fill = "red")





######################
#création des widgets

racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "black", width = WIDTH, height = HEIGHT)
bouton = tk.Button(racine, text = "recommencer", command = restart)


####################
#positionnement des widgets
canvas.grid()
bouton.grid()

#gestion du clic
canvas.bind("<Button-1>", gestion_du_clic)

#dessine un rectangle rouge
rectangle = canvas.create_rectangle((x1, y1), (x2, y2), fill = "red")

racine.mainloop()

