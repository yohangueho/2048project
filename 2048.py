# Projet 2048
# Auteurs : TROADEC-SAMOUR Mariam, TAIBI Yanis, GUEHO Yohan

# Importation des modules

import tkinter as tk
import random
from tkinter.messagebox import showinfo

# Constantes et variables

LARGEUR = 500
HAUTEUR = 500

matrice = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

k = 0

numbers = [0,2,4,8,16,32,64,128,256,512,1024,2048, 4096]
numbers_text = ["","2","4","8","16","32","64","128","256","512","1024","2048", "4096"]
colors = ["white","yellow","green","brown","purple","pink","grey","orange","blue","skyblue2","skyblue3","cyan","orange"]

# Fonctions

def new_case():
    new1 = random.choice([2,4])
    new_case_1_1 = random.randint(0,3)
    new_case_1_2 = random.randint(0,3)

    while matrice[new_case_1_1][new_case_1_2] != 0:
        new_case_1_1 = random.randint(0,3)
        new_case_1_2 = random.randint(0,3)

    matrice[new_case_1_1][new_case_1_2] = new1

def start():

    for i in range (0,4):
        for j in range (0,4):
            matrice[i][j] = 0

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

def deplacement():

    global k

    res = 0
    for i in range (0,4):
        if (matrice[i][0] == 0 and matrice[i][1] == 0 and matrice[i][2] == 0 and matrice[i][3] == 0) or \
            (matrice[i][0] != 0 and matrice[i][1] == 0 and matrice[i][2] == 0 and matrice[i][3] == 0) or \
            (matrice[i][0] != 0 and matrice[i][1] != 0 and matrice[i][0] != matrice[i][1] and matrice[i][2] == 0 and matrice[i][3] == 0) or \
            (matrice[i][0] != 0 and matrice[i][1] != 0 and matrice[i][2] != 0 and matrice[i][0] != matrice[i][1] and matrice[i][1] != matrice[i][2] and matrice[i][3] == 0) or \
            (matrice[i][0] != 0 and matrice[i][1] != 0 and matrice[i][2] != 0 and matrice[i][3] != 0 and matrice[i][0] != matrice[i][1] and matrice[i][1] != matrice[i][2] and matrice[i][2] != matrice[i][3]) :
            res += 1
        else:
            pass

    print(res)

    for i in range (0,4):
        if matrice[i][0] == 0: # Si la case 1 est vide...
            if matrice[i][1] == 0: # ...et que la case 2 est vide...
                if matrice[i][2] == 0: # ...et que la case 3 est vide...
                    if matrice[i][3] == 0: # ...et que la case 4 est vide :
                        pass # ne rien faire
                    else: # ...et que la case 4 n'est pas vide :
                        matrice[i][0] = matrice[i][3] # déplacer sa valeur à la case 1
                        matrice[i][3] = 0 # puis mettre la case 4 à 0
                else: # ...et que la case 3 n'est pas vide :
                    if matrice[i][3] == 0: # Si la case 4 est vide :
                        matrice[i][0] = matrice[i][2] # déplacer sa valeur à la case 1
                        matrice[i][2] = 0 # puis mettre la case 3 à 0
                    else: # Si la case 4 n'est pas vide :
                        if matrice[i][2] == matrice[i][3]: # Si les cases 3 et 4 sont les mêmes :
                            matrice[i][0] = matrice[i][2] + matrice[i][3] # Ajoutez leur valeur et la mettre à la case 1
                            matrice[i][2] = 0 # Puis mettre la case 3 à 0
                            matrice[i][3] = 0 # Et la case 4 à 0 églement
                        else: # Si les cases 3 et 4 ne sont pas les mêmes :
                            matrice[i][0] = matrice[i][2] # Déplacer la valeur de la case 3 à la case 1
                            matrice[i][1] = matrice[i][3] # Déplacer la valeur de la case 4 à la case 2
                            matrice[i][2] = 0 # Puis mettre la case 3 à 0
                            matrice[i][3] = 0 # Et la case 4 à 0 également
            else: # ...et que la case 2 n'est pas vide :
                if matrice[i][2] == 0: # Si la case 3 est vide...
                    if matrice[i][3] == 0: #...et si la case 4 est vide :
                        matrice[i][0] = matrice[i][1] # Déplacer sa valeur à la case 1
                        matrice[i][1] = 0 # Puis mettre la case 1 à 0
                    else: # ...et que la case 4 n'est pas vide :
                        if matrice[i][1] == matrice[i][3]: # Si les cases 2 et 4 sont les mêmes
                            matrice[i][0] = matrice[i][1] + matrice[i][3] # Ajoutez leur valeur et la mettre à la case 1
                            matrice[i][1] = 0 # Puis mettre la case 2 à 0
                            matrice[i][3] = 0 # Et la case 4 à 0 églement
                        else: # Si les cases 2 et 4 ne sont pas les mêmes :
                            matrice[i][0] = matrice[i][1] # Déplacer la valeur de la case 2 à la case 1
                            matrice[i][1] = matrice[i][3] # Déplacer la valeur de la case 4 à la case 2
                            matrice[i][3] = 0 # Puis mettre la case 4 à 0
                else: # Si la case 3 n'est pas vide
                    if matrice[i][3] == 0: #...et si la case 4 est vide :
                        if matrice[i][1] == matrice[i][2]: # Si les cases 2 et 3 sont les mêmes
                            matrice[i][0] = matrice[i][1] + matrice[i][2] # Ajoutez leur valeur et la mettre à la case 1
                            matrice[i][1] = 0 # Puis mettre la case 2 à 0
                            matrice[i][2] = 0 # Et la case 3 à 0 églement
                        else: # Si les cases 2 et 3 ne sont pas les mêmes :
                            matrice[i][0] = matrice[i][1] # Déplacer la valeur de la case 2 à la case 1
                            matrice[i][1] = matrice[i][2] # Déplacer la valeur de la case 4 à la case 2
                            matrice[i][2] = 0 # Puis mettre la case 4 à 0
                    else: # ...et que la case 4 n'est pas vide :
                        if matrice[i][1] == matrice[i][2]: # Si les cases 2 et 3 sont les mêmes
                            matrice[i][0] = matrice[i][1] + matrice[i][2] # Ajoutez leur valeur et la mettre à la case 1
                            matrice[i][1] = matrice[i][3] # Puis déplacer la valeur de la case 4 à la case 2
                            matrice[i][2] = 0 # Et mettre la case 3 à 0
                            matrice[i][3] = 0 # Ainsi que la case 4
                        else: # Si les cases 2 et 3 ne sont pas les mêmes
                            if matrice[i][2] == matrice[i][3]: # Si les cases 3 et 4 sont les mêmes
                                matrice[i][0] = matrice[i][1] # Puis déplacer la valeur de la case 4 à la case 2
                                matrice[i][1] = matrice[i][2] + matrice[i][3] # Ajoutez leur valeur et la mettre à la case 1
                                matrice[i][2] = 0 # Et mettre la case 3 à 0
                                matrice[i][3] = 0 # Ainsi que la case 4
                            else: # Si aucune case n'est pareille
                                matrice[i][0] = matrice[i][1]
                                matrice[i][1] = matrice[i][2]
                                matrice[i][2] = matrice[i][3]
                                matrice[i][3] = 0
        else: # Si la case 1 n'est pas vide...
            if matrice[i][1] == 0: #... et que la case 2 est vide...
                if matrice[i][2] == 0: #... et que la case 3 est vide...
                    if matrice[i][3] == 0: #... et que la case 4 est vide...
                        pass # ne rien faire
                    else: # ...et que la case 4 n'est pas vide :
                        if matrice[i][0] == matrice[i][3]: # Si les cases 1 et 4 sont les mêmes :
                            matrice[i][0] = matrice[i][0] + matrice[i][3] # Mettre la valeur de la case 1 au double
                            matrice[i][3] = 0 # Puis mettre la case 4 à 0
                        else: # Si les cases 1 et 4 ne sont pas les mêmes :
                            matrice[i][1] = matrice[i][3] # Déplacer la case 4 à la case 2
                            matrice[i][3] = 0 # Mettre la case 4 à 0
                else: # ...et que la case 3 n'est pas vide :
                    if matrice[i][3] == 0: # Si la case 4 est vide :
                        if matrice[i][0] == matrice[i][2]: # Si les case 1 et 3 sont les mêmes
                            matrice[i][0] = matrice[i][0] + matrice[i][2]
                            matrice[i][2] = 0
                        else: # Si les cases 1 et 3 ne sont pas les mêmes :
                            matrice[i][1] = matrice[i][2] # Déplacer la case 3 à la case 2
                            matrice[i][2] = 0 # Mettre la case 3 à 0
                    else: # Si la case 4 n'est pas vide
                        if matrice[i][0] == matrice[i][2]: # Si les case 1 et 3 sont les mêmes
                            matrice[i][0] = matrice[i][0] + matrice[i][2] # Mettre la case 1 au double
                            matrice[i][1] = matrice[i][3] # Déplacer la valeur de la case 4 à la case 2
                            matrice[i][2] = 0 # Mettre la case 3 à 0
                            matrice[i][3] = 0 # Mettre la case 4 à 0
                        else: # Si les cases 1 et 3 ne sont pas les mêmes
                            if matrice[i][2] == matrice[i][3]: # Si les case 3 et 4 sont les mêmes
                                matrice[i][1] = matrice[i][2] + matrice[i][3] # Mettre la somme des deux à la case 1
                                matrice[i][2] = 0 # Mettre la case 3 à 0
                                matrice[i][3] = 0 # Mettre la case 4 à 0
                            else: # Si aucune case consécutive n'est pareille
                                matrice[i][1] = matrice[i][2] # Déplacer la valeur de la case 3 à la case 2
                                matrice[i][2] = matrice[i][3] # Déplacer la valeur de la case 4 à la case 3
                                matrice[i][3] = 0 # Mettre la case 4 à 0
            else: # ...et que la case 2 n'est pas vide :
                if matrice[i][2] == 0: # Si la case 3 est vide :
                    if matrice[i][3] == 0: # Si la case 4 est vide :
                        if matrice[i][0] == matrice[i][1]: # Si les cases 1 et 2 sont les mêmes
                            matrice[i][0] = matrice[i][0] + matrice[i][1] # Mettre au double la valeur de la case 1
                            matrice[i][1] = 0 # Mettre la case 2 à 0
                        else: # Si les cases 1 et 2 ne sont pas les mêmes
                            pass # Ne rien faire
                    else: # Si la case 4 n'est pas vide
                        if matrice[i][0] == matrice[i][1]: # Si les cases 1 et 2 sont les mêmes
                            matrice[i][0] = matrice[i][0] + matrice[i][1]
                            matrice[i][1] = matrice[i][3]
                            matrice[i][3] = 0
                        else: # Si les cases 1 et 2 ne sont pas les mêmes
                            if matrice[i][1] == matrice[i][3]: # Si les cases 1 et 4 sont les mêmes
                                matrice[i][1] = matrice[i][1] + matrice[i][3]
                                matrice[i][3] = 0
                            else: # Si les cases 1 et 4 ne sont pas les mêmes
                                matrice[i][2] = matrice[i][3]
                                matrice[i][3] = 0
                else: # Si la case 3 n'est pas vide
                    if matrice[i][3] == 0: # Si la case 4 est vide
                        if matrice[i][0] == matrice[i][1]: # Si les cases 1 et 2 sont les mêmes
                            matrice[i][0] = matrice[i][0] + matrice[i][1]
                            matrice[i][1] = matrice[i][2]
                            matrice[i][2] = 0
                        else: # Si les cases 1 et 2 ne sont pas les mêmes
                            if matrice[i][1] == matrice[i][2]:
                                matrice[i][1] = matrice[i][1] + matrice[i][2]
                                matrice[i][2] = 0
                    else: # Si la case 4 n'est pas vide
                        if matrice[i][2] == 0: # Si la case 3 est vide :
                            if matrice[i][0] == matrice[i][1]: # Si les cases 1 et 2 sont les mêmes
                                matrice[i][0] = matrice[i][0] + matrice[i][1]
                                matrice[i][1] = matrice[i][3]
                                matrice[i][3] = 0
                            else: # Si les cases 1 et 2 ne sont pas les mêmes
                                if matrice[i][1] == matrice[i][3]: # Si les cases 1 et 4 sont les mêmes
                                    matrice[i][1] = matrice[i][1] + matrice[i][3]
                                    matrice[i][3] = 0
                                else: # Si les cases 1 et 4 ne sont pas les mêmes
                                    matrice[i][2] = matrice[i][3]
                        else: # Si la case 3 n'est pas vide
                            if matrice[i][0] == matrice[i][1]: # Si les cases 1 et 2 sont les mêmes
                                if matrice[i][2] == matrice[i][3]: # Si les cases 1 et 4 sont les mêmes
                                    matrice[i][0] = matrice[i][0] + matrice[i][1]
                                    matrice[i][1] = matrice[i][2] + matrice[i][3]
                                    matrice[i][2] = 0
                                    matrice[i][3] = 0
                                else: # Si les cases 1 et 4 ne sont pas les mêmes
                                    matrice[i][0] = matrice[i][0] + matrice[i][1]
                                    matrice[i][1] = matrice[i][2]
                                    matrice[i][2] = matrice[i][3]
                                    matrice[i][3] = 0
                            else: # Si les cases 1 et 2 ne sont pas les mêmes
                                if matrice[i][2] == matrice[i][3]: # Si les cases 3 et 4 sont les mêmes
                                    matrice[i][2] = matrice[i][2] + matrice[i][3]
                                    matrice[i][3] = 0
                                else: # Si les cases 3 et 4 ne sont pas les mêmes
                                    if matrice[i][1] == matrice[i][2]: # Si les cases 2 et 3 sont les mêmes
                                        matrice[i][1] = matrice[i][1] + matrice[i][2]
                                        matrice[i][2] = matrice[i][3]
                                        matrice[i][3] = 0
                                    else: # Si les cases 2 et 3 ne sont pas les mêmes
                                        pass
    
    if res != 4:
        new_case()
    else:
        pass

def left():

    deplacement()
    affichage()
    end()
    return matrice


def up():
    MU = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range (0,4):
        for j in range (0,4):
            MU[i][j] = matrice[j][3-i]
    for i in range (0,4):
        for j in range (0,4):
            matrice[i][j] = MU[i][j]

    deplacement()

    for i in range (0,4):
        for j in range (0,4):
            MU[i][j] = matrice[3-j][i]
    for i in range (0,4):
        for j in range (0,4):
            matrice[i][j] = MU[i][j]

    affichage()
    end()
    return matrice

def down():
    MU = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range (0,4):
        for j in range (0,4):
            MU[i][j] = matrice[3-j][i]
    for i in range (0,4):
        for j in range (0,4):
            matrice[i][j] = MU[i][j]

    deplacement()

    for i in range (0,4):
        for j in range (0,4):
            MU[i][j] = matrice[j][3-i]
    for i in range (0,4):
        for j in range (0,4):
            matrice[i][j] = MU[i][j]

    affichage()
    end()
    return matrice

def right():
    MU = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range (0,4):
        for j in range (0,4):
            MU[i][j] = matrice[3-i][3-j]
    for i in range (0,4):
        for j in range (0,4):
            matrice[i][j] = MU[i][j]

    deplacement()

    for i in range (0,4):
        for j in range (0,4):
            MU[i][j] = matrice[3-i][3-j]
    for i in range (0,4):
        for j in range (0,4):
            matrice[i][j] = MU[i][j]

    affichage()
    end()
    return matrice

def end():
    end = 0
    total = 0
    for i in range (0,4):
        if (matrice[i][0] != matrice[i][1] and matrice[i][0] != 0 and matrice[i][1] != 0) and \
            (matrice[i][1] != matrice[i][2] and matrice[i][1] != 0 and matrice[i][2] != 0) and \
            (matrice[i][2] != matrice[i][3] and matrice[i][2] != 0 and matrice[i][3] != 0):
            end += 1
        else:
            pass
    for j in range (0,4):
        if (matrice[0][j] != matrice[1][j] and matrice[0][j] != 0 and matrice[1][j] != 0) and \
            (matrice[1][j] != matrice[2][j] and matrice[1][j] != 0 and matrice[2][j] != 0) and \
            (matrice[2][j] != matrice[3][j] and matrice[2][j] != 0 and matrice[3][j] != 0):
            end += 1
        else:
            pass

    for i in range (0,4):
        for j in range (0,4):
            total += matrice[i][j] # LE TOTAL DE POINTS DANS CETTE VARIABLE
    
    if end == 8:
        END = 0
        higher = 0
        for i in range (0,4):
            for j in range (0,4):
                if matrice[i][j] < 2048:
                    pass
                else:
                    END += 1
                    if matrice[i][j] > higher:
                        higher = matrice[i][j]
                    else:
                        pass

        if END == 0:
            showinfo("The end", "Jeu terminé ! Dommage... Mais vous avez obtenu"+" "+str(total)+" "+"points !")
        else:
            showinfo("The end", "Jeu terminé ! Bravo ! Vous avez atteint"+" "+str(higher)+" "+"et obtenu"+" "+str(total)+" "+"points !")

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

# Création des cases (CASE_LIGNE_COLONNE) et des chiffres qui vont avec (de bases aucun texte puisqu'il n'y a pas de cases)

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

affichage()
root.mainloop()