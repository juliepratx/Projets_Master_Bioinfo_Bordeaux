# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:57:52 2019

@author: Julie
"""
###############################################################################
#                                  Import & co                                #
###############################################################################
import sys
import random
Salles = {}
pieges = {}
###############################################################################
#                                   MENU                                      #  
###############################################################################
def afficheMenu():
    global rep
    print("                Chasse le Wumpus !", "\n")
    dessin_wp()
    print()
    print("               1 - Commencer le jeu")
    print("               2 - Règles du jeu")
    print("               3 - Histoire du jeu")
    print("               4 - Crédits", "\n")
    print("               0 - Quitter le jeu", "\n") 
    rep = int(input())
###############################################################################
#                           Initialisation                                    #
###############################################################################
def initialisation(Salles):
    for position in range(12):
        position += 1
        Salles[position] = {}
        Salles[position]["salle possible"] = []
    for position in Salles.keys():
        if position == 1:
            Salles[position]["salle possible"].append(2)
            Salles[position]["salle possible"].append(3)
            Salles[position]["salle possible"].append(5)          
        if position == 2:
            Salles[position]["salle possible"].append(1)
            Salles[position]["salle possible"].append(4)
            Salles[position]["salle possible"].append(8)
        if position == 3:
            Salles[position]["salle possible"].append(1)
            Salles[position]["salle possible"].append(4)
            Salles[position]["salle possible"].append(6)
        if position == 4:
            Salles[position]["salle possible"].append(2)
            Salles[position]["salle possible"].append(3)
            Salles[position]["salle possible"].append(7)
        if position == 5:
            Salles[position]["salle possible"].append(1)
            Salles[position]["salle possible"].append(6)
            Salles[position]["salle possible"].append(11)
        if position == 6:
            Salles[position]["salle possible"].append(3)
            Salles[position]["salle possible"].append(5)
            Salles[position]["salle possible"].append(9)
        if position == 7:
            Salles[position]["salle possible"].append(4)
            Salles[position]["salle possible"].append(8)
            Salles[position]["salle possible"].append(10)
        if position == 8:
            Salles[position]["salle possible"].append(2)
            Salles[position]["salle possible"].append(7)
            Salles[position]["salle possible"].append(12)
        if position == 9:
            Salles[position]["salle possible"].append(6)
            Salles[position]["salle possible"].append(10)
            Salles[position]["salle possible"].append(11)
        if position == 10:
            Salles[position]["salle possible"].append(7)
            Salles[position]["salle possible"].append(9)
            Salles[position]["salle possible"].append(12)
        if position == 11:
            Salles[position]["salle possible"].append(5)
            Salles[position]["salle possible"].append(9)
            Salles[position]["salle possible"].append(12)
        if position == 12:
            Salles[position]["salle possible"].append(8)
            Salles[position]["salle possible"].append(10)
            Salles[position]["salle possible"].append(11)
###############################################################################
#                  Positionnement aléatoire des pièges                        #
###############################################################################
def choisir_numero_salles(pieges):
    nom_salle = random.randint(1,12)
    while nom_salle in pieges.values():
        nom_salle = random.randint(1,12)
        if nom_salle not in pieges.values():
            return nom_salle
    return nom_salle
###############################################################################
#                             Start                                           #
###############################################################################
def depart(Salles, nbFleches, pieges):
    pieges["C1"] = choisir_numero_salles(pieges)
    pieges["C2"] = choisir_numero_salles(pieges)
    pieges["P1"] = choisir_numero_salles(pieges)
    pieges["P2"] = choisir_numero_salles(pieges)
    pieges["W"] = choisir_numero_salles(pieges)
    initialisation(Salles)
    case_actuelle = random.randint(1,12)
    while case_actuelle in pieges.values():
        case_actuelle = random.randint(1,12)
    print ("Vous débutez votre aventure dans la salle", case_actuelle, "\n")
    afficheCarte(case_actuelle)
    nbFleches = avertissement(Salles,case_actuelle, nbFleches)
    mouvement(Salles,case_actuelle, nbFleches)
###############################################################################
#                        Messages d'avertissement                             #
###############################################################################    
def avertissement(Salles,case_actuelle, nbFleches):
#    print();print("POSITION P1 = "+str(pieges['P1']))
#    print("POSITION P2 = "+str(pieges['P2']))
#    print("POSITION C1 = "+str(pieges['C1']))
#    print("POSITION C2 = "+str(pieges['C2']))
#    print("POSITION W = "+str(pieges['W']))
    print()
    if case_actuelle == pieges["C1"] or case_actuelle == pieges["C2"]:
        case_actuelle = random.randint(1,12)
        print("Vous rencontrez une chauve-souris ^o^ ! Elle vous a transporté dans la salle", case_actuelle)
        dessin_cs()
        afficheCarte(case_actuelle)
        nbFleches = avertissement(Salles,case_actuelle, nbFleches)
    if case_actuelle == pieges["P1"] or case_actuelle == pieges["P2"]:
        print("Ahhhhhhhhhhhhhh !!!!! Splash !")
        print("Vous êtes mort écrasé au fond du puits !", "\n") 
        dessin_puits()
        rejouer()
    if case_actuelle == pieges["W"]:
        print("Grrrrrouuahhhhh !")
        print("Vous avez servi d'amuse-bouche au Wumpus !", "\n")
        dessin_wpf()
        rejouer()
    else:
        if pieges["C1"] in Salles[case_actuelle]["salle possible"] or pieges["C2"] in Salles[case_actuelle]["salle possible"]:
            print("Un battement d'aile se fait entendre !")
            print("Une chauve-souris se situe dans une case adjacente à la vôtre.", "\n")
            dessin_cs()
        if pieges["P1"] in Salles[case_actuelle]["salle possible"] or pieges["P2"] in Salles[case_actuelle]["salle possible"]:
            print("Brrrrr... Vous  sentez un courant d'air.")
            print("Attention à ne pas tomber dans un puits !", "\n")
        if pieges["W"] in Salles[case_actuelle]["salle possible"] :
            print("ZzzzZZZzzz")
            print("Vous approchez du Wumpus !", "\n")
            nbFleches = choix_crucial(Salles,case_actuelle,pieges,nbFleches)
        mouvement(Salles,case_actuelle, nbFleches)
    return nbFleches
###############################################################################
#                          Déplacement du joueur                              #
###############################################################################    
def mouvement(Salles,case_actuelle, nbFleches):
    print("Vous pouvez aller dans les salles suivantes:",Salles[case_actuelle]["salle possible"])
    print("Dans quelle salle voulez-vous aller ?")
    choix_joueur = int(input())
    if choix_joueur in Salles[case_actuelle]["salle possible"]:
        case_actuelle = choix_joueur
        print("Vous êtes à present dans la salle",case_actuelle, "\n")
        afficheCarte(choix_joueur)
        nbFleches = avertissement(Salles,case_actuelle,nbFleches)
    else:
        print("Cette salle n'est pas accessible depuis votre position ou n'existe pas")
        mouvement(Salles,case_actuelle, nbFleches)
###############################################################################
#                               Choix crucial                                 #
###############################################################################    
def choix_crucial(Salles, case_actuelle,pieges, nbFleches):
    print("Vous avez la possibilité de :", "\n")
    print("1 - Tirer une flêche >-->")
    print("2 - Continuer à vous déplacer. ")
    choix_joueur = int(input())
    if choix_joueur == 1:
        print("Vous pouvez viser les salles suivantes", Salles[case_actuelle]["salle possible"])
        print("Quel est votre choix ?")
        fleche = int(input())
        nbFleches -= 1
        print("Il vous reste :", nbFleches, "flèche(s)", "\n")
        if fleche in Salles[case_actuelle]["salle possible"]:
            if fleche == pieges["W"] :
                print("Bravo ! Vous avez eliminé le Wumpus", "\n")
                rejouer()
            else :
                print("Oups, raté")
                print("Le sifflement de la flèche a reveillé le Wumpus")
                position = 0
                while position not in Salles[pieges["W"]]["salle possible"]:
                    position = choisir_numero_salles(pieges)
                pieges["W"] = position
        #       print("Nouvelle position du W :", position)
                print("Le Wumpus s'est déplacé")
                if nbFleches == 0:
                    print("Vous n'avez plus de flèches !")
                    rejouer()
                if case_actuelle == pieges["W"]:
                    print("Grrrrr")
                    print("Vous avez servi d'amuse bouche au Wumpus !")
                    dessin_wpf()
                    rejouer()
                avertissement(Salles,case_actuelle, nbFleches)
        else:
            print("Cette salle n'est pas accessible depuis votre position ou elle n'existe pas")
            nbFleches = choix_crucial(Salles,case_actuelle,pieges,nbFleches)
    return nbFleches
###############################################################################
#                                  Rejouer                                    #
###############################################################################
def rejouer():
    print("Voulez-vous rejouer ? Oui / Non")
    choix_joueur = gestionSaisie(["oui","Oui","non","Non"])
    if choix_joueur == "oui" or choix_joueur == "Oui":
        depart(Salles, 3, pieges)
        choisir_numero_salles(pieges)
    else:
        sys.exit()
###############################################################################
#                           Gestion de la saisie                              #
###############################################################################        
def gestionSaisie(list):
    choix = input()
    if choix not in list:
        print("ERREUR: Veuillez recommencer votre saisie : ")
        choix = input()
    else:
        return choix
###############################################################################
#                               Dessins                                       #
###############################################################################            
def dessin_cs():
    print()
    print("_______          _______")
    print("\_     \  ^ ^  /     _/")
    print("  \_    \ (..) /    _/")
    print("     \_ /  \/  \ _/")
    print()
    print("eheheheheehehehehehhehehehe", "\n")
    
def dessin_wp():
    print("  __      __                     ____            ____  ")
    print(" / /  /\  \ \ __   __           |  __ \ __   __/   __| ")
    print(" \ \ /  \ / /|  |_| | '_ ` _ \  | /__)/|  |_| |\___  \ ")
    print("  \_/    /_/  \___,_|_| |_| |_| | |     \___,_||____ / ", "\n")  
    
def dessin_wpf():
    print()
    print("                  __________     Miam miam ! Excellent repas !!  ")
    print("           ______/ _     _  \______                                      ")
    print("          |      '' '' '' ''       |                                     ")
    print("      ___/      /|_|\_|\_|\_|\      \___                                 ")
    print("     |          \| |_/|_/|_/|/          |                                ")
    print("      \    /\_____________________/\    /                                ")
    print("      /___/                         \___\                                ", "\n")    

def dessin_puits():
    print()
    print("                   __   ______   __                                          ")
    print("                   \ \ /_    _\ / /    Aaaaaaaahhhhhh! Plouf !!!    ")
    print("                    \ \---''---/ /                                           ")
    print("           ____________|_______|___________                                  ")
    print("            |___                      ___|                                   ")
    print("                 |    |         |     |                                      ")
    print("                 |    |         |     |                                      ")
    print("                 |     | ..... |      |                                      ")
    print("                 | )    |'___'|     ( |                                      ")
    print("                  \)________________(/                                       ", "\n")
    
###############################################################################    
#                 Carte du jeu avec position du joueur                        #
###############################################################################    
def afficheCarte(choix_joueur):
    L1 =   ("             Carte du jeu             ")
    L11 =  ("                                      ")
    L2 =   ("             1 -------- 2             ")
    L21 =  ("            (1)-------- 2             ")
    L22 =  ("             1 --------(2)            ")
    L3 =   ("            / \        /  \           ")
    L4 =   ("           /   3 ---- 4    \          ")
    L43 =  ("           /  (3)---- 4    \          ")
    L44 =  ("           /   3 ----(4)   \          ")
    L5 =   ("          /    /       \    \         ")
    L6 =   ("         5----6        7----8         ")
    L65 =  ("        (5)---6        7----8         ")
    L66 =  ("         5---(6)       7----8         ")
    L67 =  ("         5----6       (7)---8         ")
    L68 =  ("         5----6        7---(8)        ")
    L7 =   ("          \    \       /    /         ")
    L8 =   ("           \    9 --- 10   /          ")
    L89 =  ("           \   (9)--- 10   /          ")
    L810 = ("           \    9 ---(10)  /          ")  
    L9 =   ("            \  /        \ /           ")
    L10 =  ("             11 -------- 12           ") 
    L1011 =("            (11)-------- 12           ") 
    L1012 =("             11 --------(12)          ") 
    
    carte = [[L1,L11,L2,L3,L4,L5,L6,L7,L8,L9,L10],#0
    [L1,L11,L21,L3,L4,L5,L6,L7,L8,L9,L10],#1 
    [L1,L11,L22,L3,L4,L5,L6,L7,L8,L9,L10],#2 
    [L1,L11,L2,L3,L43,L5,L6,L7,L8,L9,L10],#3
    [L1,L11,L2,L3,L44,L5,L6,L7,L8,L9,L10],#4
    [L1,L11,L2,L3,L4,L5,L65,L7,L8,L9,L10],#5
    [L1,L11,L2,L3,L4,L5,L66,L7,L8,L9,L10],#6
    [L1,L11,L2,L3,L4,L5,L67,L7,L8,L9,L10],#7
    [L1,L11,L2,L3,L4,L5,L68,L7,L8,L9,L10],#8
    [L1,L11,L2,L3,L4,L5,L6,L7,L89,L9,L10],#9
    [L1,L11,L2,L3,L4,L5,L6,L7,L810,L9,L10],#10
    [L1,L11,L2,L3,L4,L5,L6,L7,L8,L9,L1011],#11
    [L1,L11,L2,L3,L4,L5,L6,L7,L8,L9,L1012]]#12
    for i in range(11) :   
        print(carte[choix_joueur][i])   
############################################################################### 
#                               Règes du jeu                                  #
###############################################################################        
def regles_du_jeu():
    print("          Règles du jeu.", "\n")
    print("Vous débutez le jeu dans une salle aléatoire.")
    print("Vous ne pouvez vous déplacer que d'une seule salle à la fois.")
    print("Seules les cases adjacentes à la vôtre sont possibles.")
    print("Ce labyrinthe contient des pièges répartis aléatoirement.")
    print("A chaque début de partie, leur position change.")
    print("Si vous entrez dans une salle où se trouve une chauve-souris,")
    print("celle-ci vous transportera dans une autre salle au hasard.")
    print("La chauve-souris retournera dans sa salle initiale jusqu'à")
    print("la fin de la partie.")
    print("Si vous avez le malheur de tomber dans un puits, ça sera fini")
    print("pour vous ! Mais vous aurez la possibilité de rejouer.")
    print("Lorsque vous aprocherez de la salle où se cache le Wumpus,")
    print("vous aurez la possibilité de tirer une flèche.")
    print("Mais attention ! Si vous ratez le Wumpus, celui-ci se déplacera")
    print("pour venir dans une autre salle du labyrinthe et y compris")
    print("celle où vous êtes. Il vous dévorra tout cru !")
    print("Vous avez 3 flèches en votre possession. Faites-en bon usage !")
    print("Bonne chasse !", "\n")
    return
###############################################################################
#                                  Crédits                                    #
###############################################################################      
def crédits():
    print("              Crédits", "\n")
    print("Le jeu a été réalisé par :")
    print("Lola Denet, Uyen Vu Thao et Julie Pratx")
    print("Dans le cadre d'un projet de programmation en python.")
    print("Le 22 novembre 2019", "\n")
    return
###############################################################################
#                                Histoire du jeu                              #
###############################################################################    
def histoire_jeu():
    print("                   Histoire du jeu.", "\n")
    print("Il existe un labyrinthe dont nul n'est revenu vivant...")
    print("Le Wumpus est le plus féroce et démoniaque de ses habitants !")
    print("Vous décidez alors d'entreprendre une chasse pour l'éliminer !")
    print("Attention ! Votre aventure sera semée d'embuches...")
    print("Vous pourrez entendre le battement d'ailes de chauve-souris proches de vous.")
    print("Vous sentirez le froid vous glacer le sang lorsque vous approcherez d'un puits.")
    print("Lorsque vous entendrez le ronflement du Wumpus il faudra faire un choix crucial...")
    print("Essayez de le tuer mais si vous échouez, priez pour qu'il ne se déplace pas vers vous !","\n")
    return
###############################################################################
###############################################################################     
########################### Programme principal  ##############################    
###############################################################################
###############################################################################    
while(True):
    afficheMenu()
    rep = int(rep)
    if rep == 0:
        sys.exit(0)
    if rep == 1:
        depart(Salles, 3, pieges)
    if rep == 2:
        regles_du_jeu()
    if rep == 3:
        histoire_jeu()
    if rep == 4:
        crédits()
###############################################################################
############################ FIN DU PROGRAMME #################################
###############################################################################        