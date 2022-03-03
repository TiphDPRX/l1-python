import tkinter as tk


############################
#Fonstions

def attendre_clics(event):
    """Attends 2 clics de l'utilisateur"""
    pass



###########################
#Création des widgets
racine = tk.Tk()
racine.title("Exercice 2")
canvas = tk.Canvas(racine, width = 500, height = 500)
bouton = tk.Button(racine, text = "Pause")



############################
#Positionnement des widgets
canvas.grid()
bouton.grid()
racine.mainloop()

##########################
#Gestion clics
racine.bind("<button1>", attendre_clics)