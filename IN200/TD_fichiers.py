# exercice 1

from fileinput import close


fic = open("notes.txt", "r")
ficmyn = open("moyenne.txt","w")

for ligne in fic :
    list = ligne.split()
    print(list)
    moyenne = (int(list[1]) + int(list[2]) + int(list [3])) / 3
    print(moyenne)
    l = ligne.rstrip("\n") + " " + str(moyenne) + "\n" # .rstrip() => supprime ce qu'on met en argument
    print(l)
    ficmyn.write(l)

ficmyn.close()  
fic.close()

# Correction Exercice 1


"""
import random
def exercice_1():
    list_notes = []
    # On ouvre le fichier
    notes = open("notes.txt", "r")
    while(True):
        # On lit les lignes
        new_line = notes.readline()
        # Si on lit une ligne vide, o arrette
        if(new_line == ""):
            break
        # on split la ligne dans une liste
        splitted_line = new_line.split()
        sum_notes = 0
        # on fait la somme
        for i in range(1, len(splitted_line)):
            sum_notes += int((splitted_line[i]))
        # on fait la moyenne
        mean_notes = sum_notes / (i)
        # on ajoute la moyenne à la fin de notre ligne
        splitted_line.append(mean_notes)
        # on ajoute cette liste à notre liste de listes
        list_notes.append(splitted_line)
    # On pense bien à fermer le fichier
    notes.close()
    # On ré-écrit nos notes dans le fichier
    ecrire_notes = open("moyennes.txt", "w")
    for listes in list_notes:
        for elem in listes:
            # On re-écrit les éléements de notre liste
            ecrire_notes.write(f"{elem} ")
        # On oublie pas le retour à la ligne
        ecrire_notes.write("\n")
    ecrire_notes.close()
"""

#########################################
# Exercice 2.1

"""
def nb_lignes(nom_fichier):
    nb = 0
    fic = open(nom_fichier, "r")
    for ligne in fic :
        nb += 1

    fic.close()
    return(nb)

nb = nb_lignes("words.txt")
"""

# Correction 2.1

def nb_lignes(nom_fichier):
    fic = open(nom_fichier, "r")
    lignes = fic.readlines() #readlines avec un "s", different de readline
    return len(lignes)

nb = nb_lignes("words.txt")
print(nb)

# Correction 2.2

def ecrit_liste_mot(n):
    f1 = open("words.txt", "r")
    f2 = open("words.txt", "w")
    while(True) :
        ligne = f1.readline()
        if ligne == " ":
            break
        if len(ligne==n+1): # n+1 à cause du retour à la ligne
            f2.write(ligne)
    f1.close()
    f2.close()

# Correction 2.3

import random
def melange_mots(nom_fichier):
    f1 = open(f"{nom_fichier}.txt", "r")
    f2 = open(f"{nom_fichier}.mel", "w")
    lignes = f1.readlines
    random.shuffle(lignes)
    for mot in lignes :
        f2.write(mot)
    f1.close()
    f2.close()


# autres corrections : cf github
#   https://github.com/JosephDqs/CorrectionTD2IN200



