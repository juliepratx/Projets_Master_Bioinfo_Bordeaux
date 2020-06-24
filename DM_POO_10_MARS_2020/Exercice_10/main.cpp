/*
4. Fonctions membres et surdéfinition

EXERCICE 10 : Rajouter les fonctions suivantes à la classe Vecteur3D :
- Des fonctions permettant d'accéder au coordonnées d'un vecteur :
     - int abscisse() pour x
     - int ordonnée() pour y
     - int cote() pour z
- Des fonctions permettant de modifier les coordonnées d'un vecteur :
     - void fixer_abscisse(int nouvelle_abscisse) pour x
     - void fixer_ordonnée(int nouvelle_ordonnée) pour z
     - voit fixer_cote(int nouvelle_cote) pour z
- bool coincide(Vecteur3D v) qui renvoie true si v et l'objet courant
ont les mêmes coordonnées, sinon false.
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
    cout << "Coincide v1 et v2 : " << v1.coincide(v2) << endl;
    cout << "Coincide v2 et v3 : " << v2.coincide(v3) << endl;

    return 0;
}

