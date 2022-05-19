
#########################
# Bibliothèques
import tkinter as tk
import random as rd


########################
# Variables

#taille de la grille
N = 12

#taille du canvas
HAUTEUR = 600
LARGEUR = 600


#variables globales
grille = []
couleur = "black"


# liste à 2D qui représente la configuration aléatoire (le tas de sable)
liste_config = []


#########################
# Fonctions

def init_configCourante():
    """Initialise la grille blanche (sans aucun grain de sable) et création de la configuration aléatoire (le tas de sable) à l'aide d'une liste à deux dimensions"""    
    global grille, liste_config

    # Cette liste "grille" à deux dimensions permet d'associer une valeur à chaque carré qui sera crée par la suite par la variable "carre",
    #  on pourra alors agir sur chaque carre de manière individuel
    for i in range(N):
        grille.append([0]*N)

    #Création des carrés
    for i in range(N):
        for j in range(N):
            carre = canvas.create_rectangle(LARGEUR//N*i, HAUTEUR//N*j,LARGEUR//N*(i+1), HAUTEUR//N*(j+1), fill = couleur, outline = "white")
            grille[i][j] = carre
  
    #Création de la liste à deux dimensions qui définit le nombre de grain de sable contenu dans un carré
    for i in range(N):
        ligne = [] #liste qui permet de créer les "lignes" de la liste à 2 dimensions
        for j in range(N):
            aleatoire = rd.randint(1, 10)
            ligne.append(aleatoire)
        liste_config.append(ligne)



def init_aleatoire():
    """Associe une couleur aux nombre de "grains de sables" de chaque case (c'est-à-dire, initialise la configuration aléatoire) :
        * blue >= 4
        * rouge = 3
        * cyan = 2
        * violet = 1
        * noir = 0
    """
    global couleur
    for i in range (N):
        for j in range(N):
            if liste_config[i][j] == 0:
                couleur = "black"
            if liste_config[i][j] == 1:
                couleur = "purple"
            if liste_config[i][j] == 2:
                couleur = "cyan"
            if liste_config[i][j] == 3:
                couleur = "red"
            if liste_config[i][j] >= 4:
                couleur = "blue"
            canvas.itemconfigure(grille[i][j], fill = couleur)

def etape():
    """Fait une étape de l'automate"""
    global liste_config
    liste_config_ = []
    for i in range (N) :
        liste_config_.append([0]*N)
    liste_config = liste_config_
    pass #il faut que je regarde ça plus tard pour l'éboulement

        




#########################
# Partie Principale

#création des widgets
racine = tk.Tk()
racine.title("Tas de Sable")
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR)
bouton_config = tk.Button(racine, text = "Générer", command = init_aleatoire)



init_configCourante()
print(liste_config)


#placement des widgets
canvas.grid()
bouton_config.grid()


#boucle principale
racine.mainloop()

