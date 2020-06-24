/*
5. Fonctions amies

EXERCICE 12 :
*/

#include <iostream>
#include "Vecteur3D.h"

using namespace std;

int main(){


    Vecteur3D v1;
    Vecteur3D v2(4.2, 5, 6.1);
    v1.affiche();
    v2.affiche("test");
    v2.fixer_abscisse(5);
    v2.fixer_ordonnee(7);
    v2.fixer_cote(1);
    cout << "Abscisse v2 : " << v2.abscisse() << endl;
    cout << "Ordonnee v2 : " << v2.ordonnee() << endl;
    cout << "Cote v2 : " << v2.cote() << endl;
    Vecteur3D v3(5, 7, 1);
    cout << "Coincide v1 et v2 : " << coincide(v1, v2) << endl;
    cout << "Coincide v2 et v3 : " << coincide(v2, v3) << endl;

    cout << "Produit scalaire v2 et v3 : " << v2.produit_scalaire(v3) << endl;
    Vecteur3D vaffiche = v2.somme(v3);
    vaffiche.affiche();


    return 0;
   
}

