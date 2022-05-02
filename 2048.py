# Projet
# Auteurs : TROADEC-SAMOUR Mariam, TAIBI Yanis, GUEHO Yohan

# Importation des modules

import tkinter as tk
import random
from turtle import right

# Constantes et variables

LARGEUR = 500
HAUTEUR = 500
color_0 = "white"

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

def start():
    return

def stop():
    return

def load():
    return

def save():
    return

def verify():
    return

# Programme principal

# Widgets

root = tk.Tk()
mainCanvas = tk.Canvas(root, bg="black", width=LARGEUR, height=HAUTEUR)
gameArea = mainCanvas.create_rectangle(LARGEUR-480, HAUTEUR-480, LARGEUR-15, HAUTEUR-15, fill="red")

start_button = tk.Button(root, text="START", height=2, width=20,command=start)
stop_button = tk.Button(root, text="STOP", height=2, width=20, command=start)
load_button = tk.Button(root, text="LOAD", height=2, width=20, command=start)
save_button = tk.Button(root, text="SAVE", height=2, width=20, command=start)

left_button = tk.Button(root, text="LEFT", height=5, width=10, command=start)
up_button = tk.Button(root, text="UP", height=2, width=20, command=start)
down_button = tk.Button(root, text="DOWN", height=2, width=20, command=start)
right_button = tk.Button(root, text="RIGHT", height=5, width=10, command=start)

# Création des cases (CASE_LIGNE_COLONNE)

#Ligne 1

CASE_1_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-475, LARGEUR-365, HAUTEUR-365, fill=color_0)
CASE_1_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-475, LARGEUR-250, HAUTEUR-365, fill=color_0)
CASE_1_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-475, LARGEUR-135, HAUTEUR-365, fill=color_0)
CASE_1_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-475, LARGEUR-20, HAUTEUR-365, fill=color_0)

#Ligne 2

CASE_2_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-360, LARGEUR-365, HAUTEUR-250, fill=color_0)
CASE_2_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-360, LARGEUR-250, HAUTEUR-250, fill=color_0)
CASE_2_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-360, LARGEUR-135, HAUTEUR-250, fill=color_0)
CASE_2_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-360, LARGEUR-20, HAUTEUR-250, fill=color_0)

#Ligne 3

CASE_3_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-245, LARGEUR-365, HAUTEUR-135, fill=color_0)
CASE_3_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-245, LARGEUR-250, HAUTEUR-135, fill=color_0)
CASE_3_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-245, LARGEUR-135, HAUTEUR-135, fill=color_0)
CASE_3_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-245, LARGEUR-20, HAUTEUR-135, fill=color_0)

#Ligne 4

CASE_4_1 = gameArea = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-130, LARGEUR-365, HAUTEUR-20, fill=color_0)
CASE_4_2 = gameArea = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-130, LARGEUR-250, HAUTEUR-20, fill=color_0)
CASE_4_3 = gameArea = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-130, LARGEUR-135, HAUTEUR-20, fill=color_0)
CASE_4_4 = gameArea = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-130, LARGEUR-20, HAUTEUR-20, fill=color_0)


mainCanvas.grid(column=0, columnspan=4, row=0)

start_button.grid(column=0, row=1, columnspan=2)
stop_button.grid(column=2, row=1, columnspan=2)
load_button.grid(column=0, row=2, columnspan=2)
save_button.grid(column=2, row=2, columnspan=2)

left_button.grid(column=0, row=3, rowspan=2)
up_button.grid(column=1, row=3, columnspan=2)
down_button.grid(column=1, row=4, columnspan=2)
right_button.grid(column=3, row=3, rowspan=2)

root.mainloop()
