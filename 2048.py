# Projet
# Auteurs : TROADEC-SAMOUR Mariam, TAIBI Yanis, GUEHO Yohan

# Importation des modules

import tkinter as tk
import random

# Constantes et variables

LARGEUR = 500
HAUTEUR = 800

matrice = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
case_1_1 = random.randint(1,4)
case_1_2 = random.randint(1,4)
case_2_1 = random.randint(1,4)
case_2_2 = random.randint(1,4)
numb1 = random.choice[1,2]
numb2 = random.choice[1,2]

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
gameArea = mainCanvas.create_rectangle(LARGEUR-480, HAUTEUR-780, LARGEUR-20, HAUTEUR-320, fill="red")

# Création des cases



mainCanvas.grid()
root.mainloop()
