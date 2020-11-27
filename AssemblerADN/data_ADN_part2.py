# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:47:51 2019

@author: Julie

On récupère les données enregistré dans le fichier.
Puis, on doit appliquer des adaptateurs sur chaque read et couper le read si
l'adaptateur s'adapte au read.
Puis, on doit définir un filtre pour éliminer certaine valeur de qualité des
reads.
Ainsi qu'un autre filtre pour la qualité moyenne (moyenne des valeur de qualité
de chaque read).
Ensuite, on doit déterminer quels reads se chevauchent le mieux.
Et enfin, on doit reconstituer la séquence à l'aide des chevauchement.

"""
###############################################################################
############################ PARTIE II ########################################
###############################################################################
#                        Les imports
import ast
import numpy as np
#                Listes et dico des brins sens et non sens
seq_ini = [] # liste temporaire
adaptateurs = [] # liste des adaptateurs
#                   Pour le brin sens 5'-> 3'
BS = [] # Brin Sens (BS) liste temporaire
dico_BS = {} # dictionnaire des reads brin sens
seq = [] # séquence initiale d'ADN
#                   Pour le brin non sens 3' <- 5'
BNS = [] #Brin Non Sens (BNS) liste temporaire
seqC = [] # sequence initiale Complémentaire
dico_BNS = {} # dictionnaire des reads brin non sens
###############################################################################
#print("                Chargement de la sauvegarde :", "\n")  
# Les 2 dictionnaires contenant les reads et les val qualité des 2 brins d'ADN
"""
Ici, on charge tous les fichiers textes qui contiennent les données générées 
dans la partie 1 du programme.
Ces données vont être traitées à l'aide de différents filtres. 
"""
Fichier = open('Dictionnaire_BS_OBI.txt','r')
for sortie1 in Fichier:
    BS = sortie1  
Fichier.close()
Fichier = open('Dictionnaire_BNS_OBI.txt','r')
for sortie1 in Fichier:
    BNS = sortie1  
Fichier.close()

# Le double brin d'ADN
Fichier = open('Séquence_ini_BS_OBI.txt','r')
for sortie2 in Fichier:
    seq_ini = sortie2
    seq.append(seq_ini)
#    print("Séquence initiale brin sens :", "\n")
#    print("5'-", seq, "-3'", "\n")
Fichier.close()
Fichier = open('Séquence_ini_BNS_OBI.txt','r')
for sortie2 in Fichier:
    seq_ini = sortie2
    seqC.append(seq_ini)
#    print("Séquence initiale brin non sens :", "\n")
#    print("3'-", seqC, "-5'", "\n")
Fichier.close()

# Adaptateurs
Fichier = open('Adaptateurs_OBI.txt','r')
for sortie3 in Fichier:
    ADP = sortie3  
Fichier.close()
###############################################################################
#                          Mise en forme                                      #
###############################################################################
"""
Dans cette partie, on transforme le type de sortie (string) en (dict) ou en 
(list) pour pouvoir les traiter dans les procédures suivantes.
"""
# Retour dans le dico
dico_BS = ast.literal_eval(BS)      
#print("Dictionnaire brin sens :", dico_BS, "\n")
dico_BNS = ast.literal_eval(BNS)      
#print("Dictionnaire brin non sens :", dico_BNS, "\n")
# Retour dans une liste
adaptateurs = ast.literal_eval(ADP)
#print("Liste d'adaptateurs :", adaptateurs, "\n")
###############################################################################
#                   Liste Reads + valeurs qualité                             #
###############################################################################
"""
Cette procédure sert à afficher les différentes clés et valeurs contenus dans
les dictionnaires. 
On a donc :
    - le dico_BS qui contient les reads et valeurs de qualité des Brins Sens
    (5' -> 3')
    - le dico_BNS qui contient les reads et valeurs de qualité des Brins Non 
    Sens (3' <- 5')
"""
def LoadReadSet(file):
    for cle, valeur in dico_BS.items():       
      #print("Reads + longueur + val qualité brin sens :", cle, valeur, "\n")
      return dico_BS    
    for cle, valeur in dico_BNS.items():
      #print("Reads + longueur + val qualité brin non sens :", cle, valeur, "\n")
      return dico_BNS    
        
LoadReadSet(dico_BS) # pour les brins sens
print()
LoadReadSet(dico_BNS) # pour les brins non sens
print()
###############################################################################
#                            Adaptateur                                       #
###############################################################################
"""
Cette procédure prends pour arguement ReadSet (à remplacer par le dictionnaire
à traiter) et Adaptateurs (à remplacer par une séquence de nucléotides).

Elle sert à trouver des nucléotides complémentaires au différents reads que 
compose le dictionnaire sélectionné en argument et à les éliminer. 
"""
def FiltreAdapateurs(ReadSet, Adaptateurs):
    for cle in ReadSet.keys():
        if Adaptateurs == ReadSet[cle][0][0][0:4]:
            # retourne le read emputé de ces 4 premiers nucleotides
            ReadSet[cle][0][0] = ReadSet[cle][0][0][4:] 
            #  longueur du read après le passage du filtre
            ReadSet[cle][1] = ReadSet[cle][1] - 4 
            # nouvelles valeurs de qualité 
            ReadSet[cle][2] = ReadSet[cle][2][4:]  
        if Adaptateurs == ReadSet[cle][0][0][16:20]:
            # retourne le read emputé de ces 4 derniers nucléotides
            ReadSet[cle][0][0] = ReadSet[cle][0][0][:-4]
            #  longueur du read après le passage du filtre
            ReadSet[cle][1] = ReadSet[cle][1] - 4
            # nouvelles valeurs de qualité 
            ReadSet[cle][2] = ReadSet[cle][2][:-4]
    return ReadSet
    
#print("Dico BS :", FiltreAdapateurs(dico_BS, 'ATGA'), "\n")
#print("Dico BNS :", FiltreAdapateurs(dico_BNS, 'TACT'), "\n")
###############################################################################
#                      Filtre qualité minimale                                #
###############################################################################
"""
Cette procédure prend pour argument ReadSet (vu dans la procédure précédente)
et SeuilQualité (élimine les nucléotides et leur valeur de qualité associée
si le seuil de qualité n'est pas atteint).
"""
def FiltreExtremites(ReadSet, SeuilQualite):
    for cle in ReadSet.keys():
        # retourne le read entier
        R = ReadSet[cle][0][0]
        valsuppr = []; new = []
        for i in range (len(R)):
            # toutes les valeurs qualité
            if ReadSet[cle][2][i] < SeuilQualite: 
                valsuppr.append(i) 
            else:
                new.append(ReadSet[cle][2][i])
        # nouvelle liste de nucléotides
        ReadSet[cle][0][0] = ''.join(R[j] for j in range(len(R)) if j not in valsuppr)
        # longeur de la chaine de nucleotide
        ReadSet[cle][1] = len(ReadSet[cle][0][0])
        # nouvelle liste de valeur qualité
        ReadSet[cle][2] = new 
    return ReadSet
        
print("Filtre sur valuers de qualités minimales :"
      , FiltreExtremites(dico_BS, 0.3), "\n")
###############################################################################
#                       Filtre qualité moyenne                                #
###############################################################################
"""
Cette procédure prend pour argument ReadSet (vu dans les procédures précédentes)
et SeuilQualité. Cette fois-ci, le seuil de qualité rentré en argument va 
éliminer les reads entiers ainsi que leur valeur de qualité si la moyenne de
ces valeurs (nldr de qualité) ont une moyenne strictement inférieure au seuil 
définit par l'utilisateur.
"""
def Filtre(ReadSet, SeuilQualite):
    faible = []
    for cle in ReadSet.keys():
        moyenne = np.average(ReadSet[cle][2])
        if moyenne < SeuilQualite:
            faible.append(cle)
    for i in faible:
        ReadSet.pop(i)
    return ReadSet

print("Filtre sur les qualités moyennes :", Filtre(dico_BS, 0.6), "\n")
###############################################################################
#              ID du meilleur chevauchements entre les reads                  #
###############################################################################
"""
Cette procédure prend pour argument Read (séquence de nucléotide à tester) et 
ReadSet (vu dans les procédures précédentes).
Son but est de nous indiquer l'ID du Read qui se chevauche le mieux avec le
Read que l'on a entré en paramètre.
"""
def BestReadChevauchant(Read, ReadSet):
    maximum = max_chev = 0; best_id = None
    # contrôle de chaque Read du dictionnaire
    for cle in ReadSet.keys(): 
        # longueur du Read le plus court avec le chevauchement maximal
        c = lmin = min(len(Read),len(ReadSet[cle][0][0]))
        # test à partir du chevauchement maximal
        while c > 0 and c <= lmin: 
            if ReadSet[cle][0][0][:c] == Read[-c:] or ReadSet[cle][0][0][-c:] == Read[0:c]:
                max_chev = c
                break
            else:
                c -= 1        
        if maximum < max_chev:
            maximum = max_chev
            best_id = cle        
    return best_id

Read = 'GGTCATACATAGTC'
print("L'ID du read qui correspond le mieux avec la séquence suiavnte", Read, 
      "est le read n°" , BestReadChevauchant (Read, dico_BS), "\n")
###############################################################################
#                            Assemblage                                       #
###############################################################################
"""
Cette procédure permet re reassembler les reads après les différentes étapes de
filtrage et de recomposer au mieux la séquence de départ.
"""     



###############################################################################
######################### FIN DU PROGRAMME ####################################
###############################################################################