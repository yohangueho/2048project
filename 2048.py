# Projet
# Auteurs : TROADEC-SAMOUR Mariam, TAIBI Yanis, GUEHO Yohan

# Importation des modules

import tkinter as tk
import random

# Constantes et variables

LARGEUR = 500
HAUTEUR = 800

matrice = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
case_1_1 = random.randint(0,3)
case_1_2 = random.randint(0,3)
case_2_1 = random.randint(0,3)
case_2_2 = random.randint(0,3)
numb1 = random.randint(1,2)
numb2 = random.randint(1,2)

matrice[case_1_1][case_1_2] = numb1
matrice[case_2_1][case_2_2] = numb2

print(matrice)


# Fonctions

def verify():
    return

# Programme principal

# Widgets

root = tk.Tk()
mainCanvas = tk.Canvas(root, bg="black", width=LARGEUR, height=HAUTEUR)
gameArea = mainCanvas.create_rectangle(LARGEUR-480, HAUTEUR-780, LARGEUR-15, HAUTEUR-315, fill="red")

# Création des cases (CASE_LIGNE_COLONNE)

#Ligne 1

CASE_1_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-775, LARGEUR-365, HAUTEUR-665, fill="blue")
CASE_1_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-775, LARGEUR-250, HAUTEUR-665, fill="blue")
CASE_1_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-775, LARGEUR-135, HAUTEUR-665, fill="blue")
CASE_1_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-775, LARGEUR-20, HAUTEUR-665, fill="blue")

#Ligne 2

CASE_2_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-660, LARGEUR-365, HAUTEUR-550, fill="blue")
CASE_2_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-660, LARGEUR-250, HAUTEUR-550, fill="blue")
CASE_2_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-660, LARGEUR-135, HAUTEUR-550, fill="blue")
CASE_2_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-660, LARGEUR-20, HAUTEUR-550, fill="blue")

#Ligne 3

CASE_3_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-545, LARGEUR-365, HAUTEUR-435, fill="blue")
CASE_3_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-545, LARGEUR-250, HAUTEUR-435, fill="blue")
CASE_3_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-545, LARGEUR-135, HAUTEUR-435, fill="blue")
CASE_3_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-545, LARGEUR-20, HAUTEUR-435, fill="blue")

#Ligne 4

CASE_4_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-430, LARGEUR-365, HAUTEUR-320, fill="blue")
CASE_4_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-430, LARGEUR-250, HAUTEUR-320, fill="blue")
CASE_4_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-430, LARGEUR-135, HAUTEUR-320, fill="blue")
CASE_4_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-430, LARGEUR-20, HAUTEUR-320, fill="blue")


mainCanvas.grid()
root.mainloop()
