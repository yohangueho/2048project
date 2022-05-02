# Projet 2048
# Auteurs : TROADEC-SAMOUR Mariam, TAIBI Yanis, GUEHO Yohan

# Importation des modules

import tkinter as tk
import random

# Constantes et variables

LARGEUR = 500
HAUTEUR = 500

matrice = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

numbers = [0,2,4,8,16,32,64,128,256,512,1024,2048]
numbers_text = ["","2","4","8","16","32","64","128","256","512","1024","2048"]
colors = ["white","yellow","green","brown","purple","pink","grey","orange","blue","skyblue2","skyblue3","cyan"]


# Fonctions

def start():

    case_1_1 = random.randint(0,3)
    case_1_2 = random.randint(0,3)
    case_2_1 = random.randint(0,3)
    case_2_2 = random.randint(0,3)

    while case_1_1 == case_2_1 and case_1_2 == case_2_2:
        case_2_1 = random.randint(0,3)
        case_2_2 = random.randint(0,3)

    numb1 = random.choice([2,4])
    numb2 = random.choice([2,4])

    matrice[case_1_1][case_1_2] = numb1
    matrice[case_2_1][case_2_2] = numb2

    print(matrice)
    affichage()
    return matrice

def stop():
    return

def load():
    return

def save():
    return

def left():
    return  

def up():
    return

def down():
    return

def right():
    return

# Programme principal

def coup():
    affichage()
    return

def affichage():
    color = []
    number = []
    for i in range (0,4):
        for j in range (0,4):
            color.append(colors[numbers.index(matrice[i][j])])
            number.append(numbers_text[numbers.index(matrice[i][j])])

    mainCanvas.itemconfig(CASE_1_1, fill=color[0])
    mainCanvas.itemconfig(CASE_1_2, fill=color[1])
    mainCanvas.itemconfig(CASE_1_3, fill=color[2])
    mainCanvas.itemconfig(CASE_1_4, fill=color[3])
    mainCanvas.itemconfig(CASE_2_1, fill=color[4])
    mainCanvas.itemconfig(CASE_2_2, fill=color[5])
    mainCanvas.itemconfig(CASE_2_3, fill=color[6])
    mainCanvas.itemconfig(CASE_2_4, fill=color[7])
    mainCanvas.itemconfig(CASE_3_1, fill=color[8])
    mainCanvas.itemconfig(CASE_3_2, fill=color[9])
    mainCanvas.itemconfig(CASE_3_3, fill=color[10])
    mainCanvas.itemconfig(CASE_3_4, fill=color[11])
    mainCanvas.itemconfig(CASE_4_1, fill=color[12])
    mainCanvas.itemconfig(CASE_4_2, fill=color[13])
    mainCanvas.itemconfig(CASE_4_3, fill=color[14])
    mainCanvas.itemconfig(CASE_4_4, fill=color[15])

    mainCanvas.itemconfig(LABEL_1_1, text=number[0])
    mainCanvas.itemconfig(LABEL_1_2, text=number[1])
    mainCanvas.itemconfig(LABEL_1_3, text=number[2])
    mainCanvas.itemconfig(LABEL_1_4, text=number[3])
    mainCanvas.itemconfig(LABEL_2_1, text=number[4])
    mainCanvas.itemconfig(LABEL_2_2, text=number[5])
    mainCanvas.itemconfig(LABEL_2_3, text=number[6])
    mainCanvas.itemconfig(LABEL_2_4, text=number[7])
    mainCanvas.itemconfig(LABEL_3_1, text=number[8])
    mainCanvas.itemconfig(LABEL_3_2, text=number[9])
    mainCanvas.itemconfig(LABEL_3_3, text=number[10])
    mainCanvas.itemconfig(LABEL_3_4, text=number[11])
    mainCanvas.itemconfig(LABEL_4_1, text=number[12])
    mainCanvas.itemconfig(LABEL_4_2, text=number[13])
    mainCanvas.itemconfig(LABEL_4_3, text=number[14])
    mainCanvas.itemconfig(LABEL_4_4, text=number[15])

    print(number, color)
    return number, color

# Widgets

root = tk.Tk()
mainCanvas = tk.Canvas(root, bg="black", width=LARGEUR, height=HAUTEUR)
gameArea = mainCanvas.create_rectangle(LARGEUR-480, HAUTEUR-480, LARGEUR-15, HAUTEUR-15, fill="red")

start_button = tk.Button(root, text="START", height=2, width=20,command=start)
stop_button = tk.Button(root, text="STOP", height=2, width=20, command=stop)
load_button = tk.Button(root, text="LOAD", height=2, width=20, command=load)
save_button = tk.Button(root, text="SAVE", height=2, width=20, command=save)

left_button = tk.Button(root, text="LEFT", height=5, width=10, command=left)
up_button = tk.Button(root, text="UP", height=2, width=20, command=up)
down_button = tk.Button(root, text="DOWN", height=2, width=20, command=down)
right_button = tk.Button(root, text="RIGHT", height=5, width=10, command=right)

# Création des cases (CASE_LIGNE_COLONNE)

#Ligne 1

CASE_1_1 =  mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-475, LARGEUR-365, HAUTEUR-365, fill=colors[0])
LABEL_1_1 = mainCanvas.create_text((80, 80),text="", fill="black")

CASE_1_2 = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-475, LARGEUR-250, HAUTEUR-365, fill=colors[0])
LABEL_1_2 = mainCanvas.create_text((195, 80),text="", fill="black")

CASE_1_3 = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-475, LARGEUR-135, HAUTEUR-365, fill=colors[0])
LABEL_1_3 = mainCanvas.create_text((310, 80),text="", fill="black")

CASE_1_4 = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-475, LARGEUR-20, HAUTEUR-365, fill=colors[0])
LABEL_1_4 = mainCanvas.create_text((425, 80),text="", fill="black")

#Ligne 2

CASE_2_1 = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-360, LARGEUR-365, HAUTEUR-250, fill=colors[0])
LABEL_2_1 = mainCanvas.create_text((80, 195),text="", fill="black")

CASE_2_2 = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-360, LARGEUR-250, HAUTEUR-250, fill=colors[0])
LABEL_2_2 = mainCanvas.create_text((195, 195),text="", fill="black")

CASE_2_3 = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-360, LARGEUR-135, HAUTEUR-250, fill=colors[0])
LABEL_2_3 = mainCanvas.create_text((310, 195),text="", fill="black")

CASE_2_4 = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-360, LARGEUR-20, HAUTEUR-250, fill=colors[0])
LABEL_2_4 = mainCanvas.create_text((425, 195),text="", fill="black")

#Ligne 3

CASE_3_1 = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-245, LARGEUR-365, HAUTEUR-135, fill=colors[0])
LABEL_3_1 = mainCanvas.create_text((80, 310),text="", fill="black")

CASE_3_2 = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-245, LARGEUR-250, HAUTEUR-135, fill=colors[0])
LABEL_3_2 = mainCanvas.create_text((195, 310),text="", fill="black")

CASE_3_3 = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-245, LARGEUR-135, HAUTEUR-135, fill=colors[0])
LABEL_3_3 = mainCanvas.create_text((310, 310),text="", fill="black")

CASE_3_4 = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-245, LARGEUR-20, HAUTEUR-135, fill=colors[0])
LABEL_3_4 = mainCanvas.create_text((425, 310),text="", fill="black")

#Ligne 4

CASE_4_1 = mainCanvas.create_rectangle(LARGEUR-475, HAUTEUR-130, LARGEUR-365, HAUTEUR-20, fill=colors[0])
LABEL_4_1 = mainCanvas.create_text((80, 425),text="", fill="black")

CASE_4_2 = mainCanvas.create_rectangle(LARGEUR-360, HAUTEUR-130, LARGEUR-250, HAUTEUR-20, fill=colors[0])
LABEL_4_2 = mainCanvas.create_text((195, 425),text="", fill="black")

CASE_4_3 = mainCanvas.create_rectangle(LARGEUR-245, HAUTEUR-130, LARGEUR-135, HAUTEUR-20, fill=colors[0])
LABEL_4_3 = mainCanvas.create_text((310, 425),text="", fill="black")

CASE_4_4 = mainCanvas.create_rectangle(LARGEUR-130, HAUTEUR-130, LARGEUR-20, HAUTEUR-20, fill=colors[0])
LABEL_4_4 = mainCanvas.create_text((425, 425),text="", fill="black")


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
