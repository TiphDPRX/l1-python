import tkinter as tk


############################
#Fonstions

def draw_line(event):
    """Attends 2 clics de l'utilisateur"""
    canvas.create_oval(event.x, event.y)
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


##########################
#Gestion clics
canvas.bind("<button1>", draw_line)


#####################
#Lancement de la boucle principale
racine.mainloop()