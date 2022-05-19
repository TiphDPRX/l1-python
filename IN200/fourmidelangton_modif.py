#################################
# Groupe MI TD2 (groupe de projet n°3)
# Ania AOUAOUCHE
# Tiphanie DEPREAUX
# Baptiste PARIS
# https://github.com/uvsq22102500/Fourmi-de-Langton
#################################
from tkinter import *

#-------------------------------------------------------------------------------------------------------
# constantes 
#-------------------------------------------------------------------------------------------------------
# dimensions de notre canvas
LARGEUR = 640
HAUTEUR = 640

# nombre et dimensions des carrés de notre canvas
N = 71
L = LARGEUR//N   

# couleurs possibles
BLANC = 0
NOIR = 1

ORANGE = 2
ROUGE = 3
BLEU = 4

COULEUR_FLECHE = "brown"
 
# directions possibles de la fleche
NORD = 0
SUD = 1
OUEST = 2
EST = 3

#-------------------------------------------------------------------------------------------------------
# variables globales 
#-------------------------------------------------------------------------------------------------------
# listes
grille = []
grille_canvas = []

# positions de la fourmi principale
position_i = N//2
position_j = N//2

# direction initiale de la fourmi principale
DIRECTION = NORD

# direction et positions initiales de nos 3 nouvelles fourmis
DIRECTIONS = [NORD, NORD ,NORD]
positions_i = [N//2, N//2, N//2]
positions_j = [N//2, N//2, N//2]

# variable qui nous permettra de mettre le bouton play en pause
mouv = True

# variable qui nous permettra de passer de la couleur aux noirs et blanc
couleurs = False
noir_blanc = False
trois_fourmis = False

# variables qui nous permettront de modifier la vitesse de la fourmi
normal, rapide, lent = True, True, True

# variable qui nous permettra d'activer la fonction couleur
coul_normal, coul_fast, coul_slow = False, False, False


# compteur qui nous permettra de differencier le 1er et le 2eme mouvement a gauche et a droite
cpt_D_BLANC, cpt_D_ROUGE = 1, 1
cpt_G_ORANGE, cpt_G_BLEU  = 1, 1

# compteur qui nous permettra de creer qu'une seule fois nos fleches
cpt = 0
check_fleche = 0

# -----------------------------------------------------------------------------------------------------------
# les fonctions
# -----------------------------------------------------------------------------------------------------------

# ---------------------------- fonctions initiales -----------------------------------------
def initialisation(): 
    """initialisation de la grille a 0 """
    """cette grille nous permettra plus tard de savoir de quelle couleur est notre carré """
    """pour ensuite pouvoir la modifier (en 1 ou 0 ; 1 etant le noir ; 0 etant le blanc) """
    for i in range(N):
        grille.append([0]*N)
        """cette 2eme grille nous permettra de garder les coordonnés des carrés de notre environnement"""
        grille_canvas.append([0]*N) 

def environnement():
    for i in range(N):
        for j in range(N):
            x, y = j*L , i*L 
            carre = canvas.create_rectangle( (x,y), (x + L, y + L), fill="white")
            grille[i][j] = BLANC
            grille_canvas[i][j] = carre


#---------------fonction qui permet de changer les coordonnés de la fleche ,"sa position"-----------------
def fourmi_update():
    global fleche, position_i, position_j, id_after, x1, x2, y1, y2
    """ changement des coordonnés de la fourmi en fonction de sa direction """
    if DIRECTION == NORD:
        x1 = position_j * L + L/2   
        y1 = position_i *L + L
        x2 = position_j * L + L/2
        y2 = position_i *L 
        canvas.coords ( fleche , x1, y1, x2, y2 )
    elif DIRECTION == SUD:
        x2 = position_j * L + L/2   
        y2 = position_i *L + L
        x1 = position_j * L + L/2
        y1 = position_i *L 
        canvas.coords ( fleche , x1, y1, x2, y2 )  
    elif DIRECTION == EST:
        x1 = position_j * L 
        y1 = position_i *L + L/2
        x2 = position_j * L + L 
        y2 = position_i *L + L/2
        canvas.coords ( fleche , x1, y1, x2, y2 )
    elif DIRECTION == OUEST:
        x2 = position_j * L  
        y2= position_i *L + L/2
        x1 = position_j * L + L
        y1 = position_i *L + L/2
        canvas.coords ( fleche , x1, y1, x2, y2 )

    #changement de vitesse
    """ normal se remet a True quand on appuie sur play, lent rapide et couleurs se mettent a False"""
    """ idem pour le reste ; des que un se met en True le reste se met a False """
    if normal == True :
        id_after = canvas.after(100, play)
    elif rapide == True :
        id_after = canvas.after(25, play)
    elif lent == True :
        id_after = canvas.after(500, play)
    elif coul_normal == True :
        id_after = canvas.after(100,couleur)
    elif coul_fast == True :
        id_after = canvas.after(25,couleur)
    elif coul_slow == True :
        id_after = canvas.after(500,couleur)

#--------------fonction qui permet de changer la couleur d'un carré et de changer la direction de la fleche------------
def play ():
    global fleche ,check_fleche, position_i, position_j , DIRECTION, cpt, fleche1,fleche2,fleche3
    
    """supprimer des fleches si elles existent"""
    if cpt == 1 :
        canvas.delete(fleche1)
        canvas.delete(fleche2)
        canvas.delete(fleche3)
    cpt = 0 #initialiser a zero

    """verifier si notre fleche existe deja ou pas ou est ce qu'elle a ete supprimé ou pas"""
    if check_fleche == 0 :
        x_mil = LARGEUR//2  #milieu de notre canvas en x
        y_mil = HAUTEUR//2  #milieu de notre canvas en y

        check_fleche += 1 #pour creer la fleche

        """ verifier le cas ou le nombre de carrés est pair ou impair et placer la fleche au milieu """
        if N % 2 != 0 :
            x1 = x_mil 
            y1 = y_mil+ L/2
            x2 = x_mil
            y2 = y_mil- L/2    
        else :
            x1 = x_mil + L/2
            y1 = y_mil + L
            x2 = x_mil + L/2
            y2 = y_mil 

        # creation de la fleche 
        if check_fleche == 1 :   
            fleche = canvas.create_line ( (x1, y1), (x2, y2), fill = COULEUR_FLECHE, width = 5, smooth = True, arrow = "last", arrowshape = (5,6,2) )

    """verification de la couleur de notre carre"""
    if grille[position_i][position_j] == BLANC :
        grille[position_i][position_j] = NOIR 
        canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "black")

        """changement de direction si la couleur du carré est blanc"""
        if DIRECTION == NORD:
            DIRECTION = EST
            position_j = (position_j+1)%N
        elif DIRECTION == SUD:
            DIRECTION = OUEST
            position_j = (position_j-1)%N
        elif DIRECTION == EST:
            DIRECTION = SUD
            position_i = (position_i+1)%N
        elif DIRECTION == OUEST:
            DIRECTION = NORD
            position_i = (position_i-1)%N 
    else :
        grille[position_i][position_j] = BLANC 
        canvas.itemconfigure(grille_canvas[position_i][position_j], fill = "white")

        """changement de direction si la couleur du carré est noir"""
        if DIRECTION == NORD:
            position_j = (position_j-1)%N
            DIRECTION = OUEST   
        elif DIRECTION == SUD:
            position_j = (position_j+1)%N     
            DIRECTION = EST
        elif DIRECTION == EST:
            position_i = (position_i-1)%N
            DIRECTION = NORD
        elif DIRECTION == OUEST:
            position_i = (position_i+1)%N
            DIRECTION = SUD
    
    fourmi_update()

# ----------------------fonction qui genere 4 couleurs---------------------------------------
def couleur():
    global cpt,fleche,normal,rapide,lent, coul_normal, coul_fast, coul_slow, position_i, position_j , DIRECTION,check_fleche,x1,x2,y1,y2,cpt_G_ORANGE ,cpt_D_BLANC ,cpt_G_BLEU ,cpt_D_ROUGE ,couleurs,fleche1,fleche2,fleche3
    """si on est sur du blanc ou du rouge on tourne a 90 a droite et on change la couleur en orange la 1ere fois et en bleu la 2eme fois"""
    """si on est sur du orange ou du bleu on tourne a 90 a gauche et on change la couleur en rouge la 1ere fois et en blanc la 2eme fois"""
    
    """supprimer des fleches si elles existent"""
    if cpt == 1 :
        canvas.delete(fleche1)
        canvas.delete(fleche2)
        canvas.delete(fleche3)
    cpt = 0 #initialiser a zero
    
    """verificationsi la fleche existe deja ou pas ou si elle a ete supprimé ou pas """
    if check_fleche == 0 :
        x_mil = LARGEUR//2  #milieu de notre canvas en x
        y_mil = HAUTEUR//2  #milieu de notre canvas en y

        check_fleche += 1 #pour creer la fleche

        """ verifier le cas ou le nombre de carrés est pair ou impair et placer la fleche au milieu """
        if N % 2 != 0 :
            x1 = x_mil 
            y1 = y_mil+ L/2
            x2 = x_mil
            y2 = y_mil- L/2    
        else :
            x1 = x_mil + L/2
            y1 = y_mil + L
            x2 = x_mil + L/2
            y2 = y_mil 

        # creation de la fleche 
        if check_fleche == 1 :   
            fleche = canvas.create_line ( (x1, y1), (x2, y2), fill = COULEUR_FLECHE, width = 5, smooth = True, arrow = "last", arrowshape = (5,6,2) )

    """verification de la couleur de la case et changement de couleurs"""
    if grille[position_i][position_j] == BLANC or grille[position_i][position_j] == ROUGE :

        if grille[position_i][position_j] == ROUGE :
            if cpt_D_ROUGE == 1 :
                grille[position_i][position_j] = ORANGE
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "orange")
                cpt_D_ROUGE += 1
            else :
                grille[position_i][position_j] = BLEU
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "blue")
                cpt_D_ROUGE -= 1

        elif grille[position_i][position_j] == BLANC :
            if cpt_D_BLANC == 1 : 
                grille[position_i][position_j] = ORANGE
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "orange")
                cpt_D_BLANC += 1
            else :
                grille[position_i][position_j] = BLEU
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "blue")
                cpt_D_BLANC -= 1
        #le premier a gauche de la case blanche est donc orange et le deuxieme bleu

        if DIRECTION == NORD:
            DIRECTION = EST
            position_j = (position_j+1)%N
        elif DIRECTION == SUD:
            DIRECTION = OUEST
            position_j = (position_j-1)%N
        elif DIRECTION == EST:
            DIRECTION = SUD
            position_i = (position_i+1)%N
        elif DIRECTION == OUEST:
            DIRECTION = NORD
            position_i = (position_i-1)%N        
    
    elif grille[position_i][position_j] == BLEU or grille[position_i][position_j] == ORANGE :
        if grille[position_i][position_j] == ORANGE :
            if cpt_G_ORANGE == 1 :
                grille[position_i][position_j] = ROUGE
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "red")
                cpt_G_ORANGE += 1
            else :
                grille[position_i][position_j] = BLANC
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "white")
                cpt_G_ORANGE -= 1

        elif grille[position_i][position_j] == BLEU :
            if cpt_G_BLEU == 1 :
                grille[position_i][position_j] = ROUGE
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "red")
                cpt_G_BLEU += 1
            else :
                grille[position_i][position_j] = BLANC
                canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "white")
                cpt_G_BLEU -= 1
            # le premier a gauche de la case bleu est donc rouge et le deuxieme blanc

        if DIRECTION == NORD:
            position_j = (position_j-1)%N
            DIRECTION = OUEST   
        elif DIRECTION == SUD:
            position_j = (position_j+1)%N     
            DIRECTION = EST
        elif DIRECTION == EST:
            position_i = (position_i-1)%N
            DIRECTION = NORD
        elif DIRECTION == OUEST:
            position_i = (position_i+1)%N
            DIRECTION = SUD           

    normal,rapide,lent = False,False,False    
    coul_normal = True  

    fourmi_update()

# ------------------------------ fonction qui modifie les coordonnés de nos fourmis ------------------------------------

def plusieurs_fourmis():
    global fleche1, fleche2, fleche3, fleches, DIRECTIONS , normal, positions_i , positions_j, x1,x2,y1,y2, id_after

    for i in range (3) :
        if grille[positions_i[i]][positions_j[i]] == BLANC :
            grille[positions_i[i]][positions_j[i]] = NOIR 
            canvas.itemconfigure( grille_canvas[positions_i[i]][positions_j[i]] ,  fill = "black")

            """changement de direction si la couleur du carré est blanc"""
            if DIRECTIONS[i] == NORD:
                DIRECTIONS[i] = EST
                positions_j[i] = (positions_j[i]+1)%N
            elif DIRECTIONS[i] == SUD:
                DIRECTIONS[i] = OUEST
                positions_j[i] = (positions_j[i]-1)%N
            elif DIRECTIONS[i] == EST:
                DIRECTIONS[i] = SUD
                positions_i[i] = (positions_i[i]+1)%N
            elif DIRECTIONS[i] == OUEST:
                DIRECTIONS[i] = NORD
                positions_i[i] = (positions_i[i]-1)%N 
        else :
            grille[positions_i[i]][positions_j[i]] = BLANC 
            canvas.itemconfigure(grille_canvas[positions_i[i]][positions_j[i]], fill = "white")

            if DIRECTIONS[i] == NORD:
                positions_j[i] = (positions_j[i]-1)%N
                DIRECTIONS[i] = OUEST   
            elif DIRECTIONS[i] == SUD:
                positions_j[i] = (positions_j[i]+1)%N     
                DIRECTIONS[i] = EST
            elif DIRECTIONS[i] == EST:
                positions_i[i] = (positions_i[i]-1)%N
                DIRECTIONS[i] = NORD
            elif DIRECTIONS[i] == OUEST:
                positions_i[i] = (positions_i[i]+1)%N
                DIRECTIONS[i] = SUD
        
        if DIRECTIONS[i] == NORD:
            x1 = positions_j[i] * L + L/2   
            y1 = positions_i[i] *L + L
            x2 = positions_j[i] * L + L/2
            y2 = positions_i[i] *L 
            canvas.coords ( fleches[i] , x1, y1, x2, y2 )
        elif DIRECTIONS[i] == SUD:
            x2 = positions_j[i] * L + L/2   
            y2 = positions_i[i] *L + L
            x1 = positions_j[i] * L + L/2
            y1 = positions_i[i] *L 
            canvas.coords ( fleches[i] , x1, y1, x2, y2 )  
        elif DIRECTIONS[i] == EST:
            x1 = positions_j[i] * L 
            y1 = positions_i[i] *L + L/2
            x2 = positions_j[i] * L + L 
            y2 = positions_i[i] *L + L/2
            canvas.coords ( fleches[i] , x1, y1, x2, y2 )
        elif DIRECTIONS[i] == OUEST:
            x2 = positions_j[i] * L  
            y2= positions_i[i] *L + L/2
            x1 = positions_j[i] * L + L
            y1 = positions_i[i] *L + L/2
            canvas.coords ( fleches[i] , x1, y1, x2, y2 )

    id_after=canvas.after(50 ,plusieurs_fourmis)

#--------------------------------- creation des 3 fourmis -----------------------------------
def demarrer_plusieurs_fourmis():
    global fleche1, fleche2, fleche3, fleches, DIRECTIONS ,cpt, check_fleche, fleche,position_i , position_j, x1,x2,y1,y2 
    """supprimer des fleches s'il en existe"""
    if check_fleche == 1 :
        canvas.delete(fleche)
    check_fleche = 0

    if cpt == 0 :
        cpt = cpt + 1 

        x_mil = LARGEUR//2  
        y_mil = HAUTEUR//2  

        if N % 2 != 0 :
            x1 = x_mil 
            y1 = y_mil+ L/2
            x2 = x_mil
            y2 = y_mil- L/2    
        else :
            x1 = x_mil + L/2
            y1 = y_mil + L
            x2 = x_mil + L/2
            y2 = y_mil 

        if (cpt==1):
            fleche1 = canvas.create_line ( (x1, y1), (x2, y2), fill = COULEUR_FLECHE, width = 5, smooth = True, arrow="last", arrowshape = (5,6,2) )
            fleche2 = canvas.create_line ( (x1, y1), (x2, y2), fill = COULEUR_FLECHE, width = 5, smooth = True, arrow="last", arrowshape = (5,6,2) )
            fleche3 = canvas.create_line ( (x1, y1), (x2, y2), fill = COULEUR_FLECHE, width = 5, smooth = True, arrow="last", arrowshape = (5,6,2) )
            
            fleches = [fleche1, fleche2, fleche3]
    
    plusieurs_fourmis()    

#-------------------------fonction qui remet toutes les cases en blanc------------------------------------------
def efface():
    global cpt, check_fleche, fleche1,fleche2,fleche3
    """ Remplace tous les éléments de la grille en 0 """
    """ On utilisera cette fonction quand on voudra passer de noir et blanc à 4 couleurs"""
    """ On utilisera cette fonction quand on voudra passer de 2 couleurs(noir et blanc) à 4 couleurs"""

    for i in range(N):
        for j in range(N):
            grille[i][j]=0
            canvas.itemconfigure(grille_canvas[i][j], fill ="white")

    """effacer les fleches si elles existent"""
    if cpt == 1 :
        canvas.delete(fleche1)
        canvas.delete(fleche2)
        canvas.delete(fleche3)
        cpt = 0 #une fois effacé initialiser la compteur a zero pour quelle soit recreer
    
    """effacer la fleche si elles existent"""
    if check_fleche == 1 :
        canvas.delete(fleche)
        check_fleche = 0  #une fois effacé initialiser la compteur a zero pour quelle soit recreer 

#----------------fonction qui change le bouton "play" en bouton "pause",et active la fonction play-------------
def demarrer ():    
    """ Active la fonction Play et change le texte "play" en "pause", de telle sorte que si on appuie sur pause,
    la fourmi s'arrête.
    NB :Les variables globales booléennes noir_blanc et couleurs permettent de savoir si la fonction couleur
    (resp. play) est activée pour pouvoir nettoyer le Canvas en blanc si besoin"""

    global mouv, id_after, normal,rapide,lent, noir_blanc, couleurs, trois_fourmis
    """cette fonction ne s'utilise que pour la version noir et blanc de la fourmi."""
    if mouv:
        button_play.config(text="Pause")
        normal = True
        rapide, lent = False, False
        if couleurs == True or trois_fourmis == True :
            button_color.config(text="Couleurs")
            button_troisFourmis.config(text="3 Fourmis")
            efface()

        noir_blanc = True
        couleurs = False
        trois_fourmis = False
        play()

    else:
        canvas.after_cancel(id_after)
        button_play.config(text="Play")
    mouv = not mouv


#----------fonction qui change le bouton "couleurs" en bouton "pause couleurs",et active la fonction couleur-------------
def demarrer_couleur():
    """Active la fonction Couleur et change le texte "Couleurs" en "Pause Couleurs",
    de telle sorte que si on appuie sur pause, la fourmi s'arrête.
    Cette fonction ne s'utilise que pour la version couleur de la fourmi."""

    global mouv, id_after, couleurs, noir_blanc, trois_fourmis, normal,rapide,lent, couleurs_normal
    
    if mouv:
        couleurs_normal = True
        button_color.config(text="Pause Couleurs")
        if noir_blanc == True or trois_fourmis == True :
            button_play.config(text="Play")
            button_troisFourmis.config(text="3 Fourmis")
            efface()

        trois_fourmis = False
        couleurs = True
        noir_blanc = False
        couleur()
    else:

        canvas.after_cancel(id_after)
        button_color.config(text="Couleurs")
    mouv = not mouv

#----------fonction qui change le bouton "couleurs" en bouton "pause couleurs",et active la fonction couleur-------------
def demarrer3():
    global mouv, couleurs, noir_blanc, trois_fourmis,id_after

    if mouv:
        button_troisFourmis.config(text="Stop !")
        if noir_blanc == True or couleurs == True:
            button_play.config(text="Play")
            button_color.config(text="Couleurs")
            efface()

        couleurs = False
        noir_blanc = False
        trois_fourmis = True
        demarrer_plusieurs_fourmis()
    else:
        canvas.after_cancel(id_after)
        button_troisFourmis.config(text="3 Fourmis")
    mouv = not mouv


#----------------------------fonction qui permet d'accelerer le mouvement de la fourmi--------------------
def rightKey (event):
    global normal,rapide,lent, coul_normal, coul_fast, coul_slow
    if noir_blanc == True :
        normal, lent = False, False
        rapide = True
    elif couleurs == True :
        coul_normal, coul_slow = False, False
        coul_fast = True

    fourmi_update

#--------------------------- fonction qui permet de ralentir le mouvement de la fourmi---------------------
def leftKey (event):
    global normal,rapide,lent
    normal, rapide = False, False
    lent = True
    fourmi_update  
   
# ------------------fonction qui permet de faire avancer la fourmi d'un mouvement ----------------------------
def next ():
    global mouv, id_after, normal,rapide,lent
    normal,rapide,lent = False, False , False
    play()
    
# ---------- fonction qui permet de revenir en arriere d'un mouvement -----------------------------------
def retour ():
    global DIRECTION, position_i, position_j, normal,rapide,lent

    normal,rapide,lent = False, False , False

    """verification de la direction de la fourmi"""
    if DIRECTION == NORD :
        """verification de la couleur de la case ou elle etait la fourmi"""
        if grille[position_i+1][position_j] == BLANC :
            grille[position_i+1][position_j] = NOIR
            canvas.itemconfigure( grille_canvas[position_i+1][position_j] ,  fill = "black")
            position_i = (position_i+1)%N
            DIRECTION = EST
        else :
            grille[position_i+1][position_j] = BLANC
            canvas.itemconfigure( grille_canvas[position_i+1][position_j] ,  fill = "white")
            position_i = (position_i+1)%N
            DIRECTION = OUEST

    elif DIRECTION == SUD :
        if grille[position_i-1][position_j] == BLANC :
            grille[position_i-1][position_j] = NOIR
            canvas.itemconfigure( grille_canvas[position_i-1][position_j] ,  fill = "black")
            position_i = (position_i-1)%N
            DIRECTION = OUEST
        else :
            grille[position_i-1][position_j] = BLANC
            canvas.itemconfigure( grille_canvas[position_i-1][position_j] ,  fill = "white")
            position_i = (position_i-1)%N
            DIRECTION = EST
            
    elif DIRECTION == EST :
        if grille[position_i][position_j-1] == BLANC :
            grille[position_i][position_j-1] = NOIR
            canvas.itemconfigure( grille_canvas[position_i][position_j-1] ,  fill = "black")
            position_j = (position_j-1)%N
            DIRECTION = SUD
        else :
            grille[position_i][position_j-1] = BLANC
            canvas.itemconfigure( grille_canvas[position_i][position_j-1] ,  fill = "white")
            position_j = (position_j-1)%N
            DIRECTION = NORD

    elif DIRECTION == OUEST :
        if grille[position_i][position_j+1] == BLANC :
            grille[position_i][position_j+1] = NOIR
            canvas.itemconfigure( grille_canvas[position_i][position_j+1] ,  fill = "black")
            position_j = (position_j+1)%N
            DIRECTION = NORD
        else :
            grille[position_i][position_j+1] = BLANC
            canvas.itemconfigure( grille_canvas[position_i][position_j+1] ,  fill = "white")
            position_j = (position_j+1)%N
            DIRECTION = SUD
    
    fourmi_update()


#---------------------  fonction enregistrer une sequence -------------------------------------
def enregistre():
    """Ecrit la taille de la grille et les valeurs de la liste grille dans le fichier enregistrement.txt"""
    fic = open("enregistrement.txt", "w")
    fic.write(str(N) + "\n")
    fic.write(str(position_i)+ "\n")
    fic.write(str(position_j)+ "\n")
    fic.write(str(DIRECTION)+ "\n")
    fic.write(str(x1) + "\n")
    fic.write(str(y1) + "\n")
    fic.write(str(x2) + "\n")
    fic.write(str(y2) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(grille[i][j])+ "\n")
    fic.close()

#------------------ fonction qui permet de lire le fichier et affiche dans le canvas la grille lu ----------------
def charge_grille():
    global N, position_i, position_j, mouv, DIRECTION, x1, x2, y1, y2, fleche
    """Lit le fichier enregistrement.txt, affiche dans le canvas la grille lu dans le fichier,
    replace la fourmi à l'état dans lequel elle se trouvait lors de l'enregistrement"""

    fic = open("enregistrement.txt", "r")

    # Récupérer le nombre de lignes et de colonnes de la grille
    taille = fic.readline()
    # Récuperer la position ,l'orientation et les coordonnés de la fleche
    position1 = fic.readline()
    position2 = fic.readline()
    orientation = fic.readline()
    coords1 = fic.readline()
    coords2 = fic.readline()
    coords3 =fic.readline()
    coords4 = fic.readline()
    
    # on recupère ensuite toutes les valeurs enregistrer dans les variables correspondantes
    N = int(taille)
    position_i = int(position1)
    position_j = int(position2)
    DIRECTION = int(orientation)
    x1 = coords1
    y1 = coords2
    x2 = coords3
    y2 = coords4

    canvas.delete() # on veut créer une nouvelle grille donc, on détruit la première
    # on initialise un nouveau canevas
    environnement()
    i, j = 0, 0
    # on met à jour la liste grille qui contient la couleur de chaque carré de l'enregistrement
    for ligne in fic:
        grille[i][j] = int(ligne)
        j += 1
        if j == N:
            j = 0
            i += 1
    # on associe les données de "grille" aux carrés en les modifiants avec la couleur correspondantes (noir ou blanc)       
    for i in range(N):
        for j in range(N):
            if grille[i][j] == 0:
                canvas.itemconfigure(grille_canvas[i][j], fill = "white")
            elif grille[i][j] ==1:  
                canvas.itemconfigure(grille_canvas[i][j], fill = "black")
    # on recrée un fleche avec les coordonnées sauvegardés             
    fleche = canvas.create_line ( (x1, y1), (x2, y2), fill = COULEUR_FLECHE, width = 5, smooth = True, arrow="last", arrowshape = (5,6,2) )
    mouv = not mouv # pour avoir le choix de redémarrer ou non l'automate avec les boutons play ou next
    demarrer()
    fic.close()

#---------------------------------------------------------------------------------------------------------
# ------------------ creation de la fenetre principale -----------------------
#---------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry("1000x700")
window.title("Fourmi de Langton")
window.configure(background='white')

#creation d'un canvas pour generer notre terrain
canvas = Canvas( window , height = HAUTEUR , width = LARGEUR, background='white' )

#creation de notre fleche
fleche = Canvas (window)

#creation des 3 autre fleches
fleche1 = Canvas (window)
fleche2 = Canvas (window)
fleche3 = Canvas (window)

#creation d'une boite ou on mettra nos boutons 
right_frame = Frame (window, height = 320 , width = 100)
left_frame = Frame (window, height = 320 , width = 100)

#implementer une image 
canvas_image = Canvas (window, height = 320 , width = 360)
image = PhotoImage(file='clavier.gif')
label= Label (canvas_image,image = image)

# les boutons 
button_play = Button (left_frame , text = ' Play  ', command = demarrer ) 
button_play.pack(padx= 10 , pady=10, fill = X )
Button (left_frame , text = ' Prochain ', command = next).pack(padx= 10 , pady=10, fill = X )
Button (left_frame , text = 'Retour', command = retour).pack(padx= 10 , pady=10, fill = X )
button_color = Button(left_frame, text="Couleurs", command=demarrer_couleur)
button_color.pack(padx= 10 , pady=10, fill = X )
button_troisFourmis = Button(left_frame, text="3 Fourmis", command=demarrer3)
button_troisFourmis.pack(padx= 10, pady=10, fill = X)

Button(right_frame, text="Enregistrer", command=enregistre).pack(padx= 10 , pady=10, fill = X )
Button(right_frame, text="Charger grille", command=charge_grille).pack(padx= 10 , pady=10, fill = X )

window.bind ('<Right>', rightKey)
window.bind ('<Left>', leftKey)

# affichage
canvas.pack (side = RIGHT)
left_frame.place (x = 80 , y = 50)
right_frame.place(x = 200, y = 120)
canvas_image.place(x = 30 , y= 350)
label.pack()

initialisation()
environnement()

window.mainloop()