
# Librairies
import tkinter as tk
import random as rd

# Constantes
WIDTH = 600
HEIGHT = 400

# Variables

est_arrete = True

# Fonctions

def creer_ball():
    """Crée la balle et renvoi une liste contenant l'identifiant de celle-ci, suivi de deux entiers choisi au hazard entre 1 et 7"""
    x_milieu = WIDTH/2
    y_milieu = HEIGHT/2
    x1 = x_milieu - 20
    y1 = y_milieu - 20
    x2 = x_milieu + 20
    y2 = y_milieu + 20
    identifiant_balle = canvas.create_oval((x1, y1), (x2, y2), fill = "blue")
    return [identifiant_balle, rd.randint(1, 7), rd.randint(1, 7)]

    

def mouvement():
    global id_after
    """Déplace la balle dans le canevas"""
    canvas.move(balle[0], balle[1], balle[2])
    id_after = canvas.after(20, mouvement)


def démarrer():
    global est_arrete, id_after
    """la balle se déplace lorsque l'on clic sur démarrer"""
    if est_arrete :
        mouvement()
        bouton.config(text = "Arrêter")
    else :
        canvas.after_cancel(id_after)
        bouton.config(text = "Démarrer")
    



    


# Création des Widgets

racine = tk.Tk()
canvas = tk.Canvas(racine, width = WIDTH, height = HEIGHT, bg = "black")
bouton = tk.Button(racine, text = "Démarrer", command = démarrer)
balle = creer_ball()



# Positionnement des Widgtes

canvas.grid()
bouton.grid(row =1)



# Boucle principale

racine.mainloop()
