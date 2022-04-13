# Projet
# Auteurs : TROADEC-SAMOUR Mariam, TAIBI Yanis, GUEHO Yohan

# Importation des modules

import tkinter as tk
import random

# Constantes et variables

LARGEUR = 500
HAUTEUR = 800

# Fonctions

# Programme principal

# Widgets

root = tk.Tk()
mainCanvas = tk.Canvas(root, bg="black", width=LARGEUR, height=HAUTEUR)
gameArea = mainCanvas.create_rectangle(LARGEUR-480, HAUTEUR-780, LARGEUR-20, HAUTEUR-320, fill="red")

# Création des cases



mainCanvas.grid()
root.mainloop()
