# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:07:36 2019

@author: Julie

Crétion d'un fichier contenant la séquence d'ADN (brin sens et brin non sens)
ainsi que les Read et leurs valeurs de qualité.

id_read : numéro du read (0, 1, 2, etc...)
read : liste des reads
valeur de qualité : valeur de chaque nucléotide de chaque read
dictionnaire : regroupe le tout

dico = {id_read:[[read],[valeur_qualité]]} où id_read est la clé et [[]] est la valeur
exemple :
dico = {0: [[ATTAGCCAT], [0.1,0.24,0.54, etc...]]
        1: [[TACCCTGAT], [1,0.54,0.21, etc... ]] 
        .....}    
"""
###############################################################################
###########################  PARTIE I #########################################
###############################################################################
import random
#                   Les listes et dictionnaires
nucleic = ["A","T","G","C"]
adaptateurs = []
#                    Pour le brin sens 5'-> 3'
readBS = [] 
valeur_q = []
valeur_qualité = [] 
dico_readsS = {}
#                   Pour le brin non sens 3' <- 5'
readBNS =[] 
valeur_qC = []
valeur_qualitéC = []
dico_readsNS = {}
###############################################################################
#                          Fonction random                                    #
###############################################################################
"""
Cette procédure prend pour argument num (nombre de caractère que l'on veut générer)
et alphabet (type de caractère que l'on veut générer).
Son but est de nous créer une séquence de nucléotides aléatoirement.
"""
print();print("1 - Séquence initiale d'ADN générée aléatoirement", "\n")
def randseq(num,alphabet):
    seq = ''
    while len(seq) < num:
        seq += nucleic[random.randint(0, len(nucleic) - 1)]
    return seq
# test
seq = randseq(80, nucleic)
print("Séquence initiale ADN :")
print("5'-", seq, "-3'", "\n")
###############################################################################
#                       Brin complémentaire                                   #
###############################################################################
"""
Cette procédure prend pour argument sequence (qui correspond à notre séquence
généré aléatoirement à la procédure précédente).
Son but est de générer le brin d'ADN complémentaire qui sera utilisé dans la
partie 2 du programme.
"""
def brincomplementaire(sequence):
    seqC = ''
    for i in sequence:
        if i == "A":
            seqC += "T"           
        if i == "T":
            seqC += "A"
        if i == "G":
            seqC += "C"
        if i == "C":
            seqC += "G"       
    return seqC

seqC = brincomplementaire(seq)
print("Séquence initiale complémentaire ADN :")
print("3'-", seqC, "-5'", "\n")
###############################################################################
#                           Reads brin sens                                   #
###############################################################################
"""
Cette procédure (pour le brin sens) prend pour argument seq (la séqeunce a 
transformer en reads) et nb_read (le nombre de read que l'on veut).
Dans cette version, les reads sont de mêmes tailles et le décalage est de 1 
nucléotide vers la droite.
"""
#print();print("2 - Reads", "\n")
def readsBS(seq,nb_read):
    for i in range (0,nb_read):
        s = seq[i:i+20]
        readBS.append(s)     
    return readBS

readsBS(seq, 10)
###############################################################################
#                Valeur de qualité des reads brin sens                        #
###############################################################################
"""
Cette procédure (pour le brin sens) prend pour argument read (la séquence 
générée précédemment) et nb_read (définit dans la procédure précédente).
"""
#print();print("3 - Valeur de qualité", "\n")
def valeurQBS(read,nb_read):
    for i in range (nb_read):
        for j in range (nb_read):
            valQ = random.randint(0,100)
            valeur_qualité.append(valQ/100) 
    for k in range(nb_read):                
        valeur_q.append(valeur_qualité[20*k:20*k+20])
    return valeur_q
     
valeurQBS(readsBS, 20)    
print("Liste des valeurs de qualité :", valeur_qualité, "\n")
###############################################################################
#                           Reads brin non sens                               #
###############################################################################
"""
Cette procédure (pour le brin non sens) prend pour argument seq (la séqeunce a 
transformer en reads) et nb_read (le nombre de read que l'on veut).
Dans cette version, les reads sont de mêmes tailles et le décalage est de 1 
nucléotide vers la droite.
"""
#print();print("2 - Reads", "\n")
def readsBNS(seq,nb_read):
    for i in range (0,nb_read):
        s = seq[i:i+20]
        readBNS.append(s) 
    return readBNS
#test
#readsBNS(seqC, 10)    
###############################################################################
#              Valeur de qualité des reads brin non sens                      #
###############################################################################
"""
Cette procédure (pour le brin non sens) prend pour argument read (la séquence
générée précédemment) et nb_read (définit dans la procédure précédente).
"""
#print();print("3 - Valeur de qualité", "\n")
def valeurQBNS(read,nb_read):
    for i in range (nb_read):
        for j in range (nb_read):
            valQ = random.randint(0,100)
            valeur_qualitéC.append(valQ/100) 
    for k in range(nb_read):                
        valeur_qC.append(valeur_qualitéC[20*k:20*k+20])
    return valeur_qC
    
#test  
#valeurQBNS(readBNS, 20)    
#print("Liste des valeurs de qualité :", valeur_qualitéC, "\n")     
###############################################################################
#                     Dico brin sens 5' -> 3'                                 #
###############################################################################
"""
Cette procédure pour le brin sens prend pour argument seq (brin sens) et
nb_read (le nombre de clé du dictionnaire).
Son but est de stocker les index, les reads et leur valeur de qualité dans un
dictionnaire.
"""
print();print("2 - Dico brin sens 5' -> 3'", "\n")
def dicoReadsS(seq,nb_read):
    r1 = readsBS (seq,nb_read)
    v1 = valeurQBS (r1,nb_read)
    id = []
    for i in range(nb_read):
        id = i
        dico_readsS[id] = [0,0,0]
    for id, i in zip(dico_readsS.keys(),range(nb_read)):
        dico_readsS[id][0] = [r1[i]]
        dico_readsS[id][1] = len(r1[i])
        dico_readsS[id][2] = v1[i]
    print("Dico brin sens 5'-> 3' :", dico_readsS, "\n") # affiche le dico des
#   reads du brin sens
     
dicoReadsS(seq, 65)
###############################################################################
#                   Dico brin non sens 3' -> 5'                               #
###############################################################################
"""
Cette procédure pour le brin non sens prend pour argument seq (brin non sens) et
nb_read (le nombre de clé du dictionnaire).
Son but est de stocker les index, les reads et leur valeur de qualité dans un
dictionnaire.
"""
print();print("2' - Dico brin non sens 3' -> 5'", "\n")
def dicoReadsNS(seq,nb_read):
    r1 = readsBNS (seqC,nb_read)
    v1 = valeurQBNS (r1,nb_read)
    id = []
    for i in range(nb_read):
        id = i
        dico_readsNS[id] = [0,0,0]
    for id, i in zip(dico_readsNS.keys(),range(nb_read)):
        dico_readsNS[id][0] = [r1[i]]
        dico_readsNS[id][1] = len(r1[i])
        dico_readsNS[id][2] = v1[i]
    print("Dico brin non sens 3' -> 5' :", dico_readsNS) # affiche le dico des 
#   reads du brin non sens
     
dicoReadsNS(seqC, 65) # seqC = séquence complémentaire
###############################################################################
#                            Adaptateur                                       #
###############################################################################
"""
Cette procédure prend pour argument nb (nombre d'adaptateur).
Son but est de générer une liste d'adaptateur qui sera utilisée dans la partie
2 du programme. 
"""
def adaptateursF(nb):
    for i in range (1, nb+1):
        ad = randseq(4, nucleic)
        adaptateurs.append(ad)
    return adaptateurs    

#adaptateursF(10)
###############################################################################
#                      Sauvegarde dans un fichier                             #
###############################################################################
"""
Ces 5 procédures ont pour même arguments file (nom du fichier de sauvegarde des
données).
Leur but est de créer des fichiers texte pour stocker les dictionnaires / listes
générés dans la partie 1 du programme.
"""
def saveDicoBS(file):
    NomDuFichier = (file)
    Fichier = open(NomDuFichier,'w') # Crée un fichier *.txt en écriture    
    Fichier.write(str(dico_readsS)) # Ecrit le dictionnaire dans le fichier
    Fichier.close() 
    
saveDicoBS("Dictionnaire_BS_OBI.txt")  

def saveDicoBNS(file):
    NomDuFichier = (file)
    Fichier = open(NomDuFichier,'w') # Crée un fichier *.txt en écriture    
    Fichier.write(str(dico_readsNS)) # Ecrit le dictionnaire dans le fichier
    Fichier.close() 

saveDicoBNS("Dictionnaire_BNS_OBI.txt")  


def saveSeqIniBS(file):
    NomDuFichier = (file)
    Fichier = open(NomDuFichier,'w')
    Fichier.write(seq)
    Fichier.close()
    
saveSeqIniBS("Séquence_ini_BS_OBI.txt")   

def saveSeqIniBNS(file):
    NomDuFichier = (file)
    Fichier = open(NomDuFichier,'w')
    Fichier.write(seqC) 
    Fichier.close()

saveSeqIniBNS("Séquence_ini_BNS_OBI.txt") 

def saveAdaptateurs(file):
    NomDuFichier = (file)
    Fichier = open(NomDuFichier,'w')
    Fichier.write(str(adaptateurs))
    Fichier.close()

saveAdaptateurs("Adaptateurs_OBI.txt") 
###############################################################################
###############################################################################