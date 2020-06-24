/*
4. Fonctions membres et surdéfinition

EXERCICE 9 : Ecrivez une classe Vector3D comprenant :
- trois données membre de type double x, y et z (privées)
- deux fonctions membres d'affichage :
    - void affiche() affichant le vecteur
    - void affiche(const char* string) affichant le string avant l'affichage du vecteur
- deux constructeurs :
    - l'un sans argument, initialisant chaque composante à 0
    - l'autre, avec trois arguments correspondant aux coordonnées du vecteur.
Modifiez ensuite le code pour que les constructeurs soit des fonction en ligne (inline).
*/

#include <iostream>
#include "Vecteur3D.h"

using namespace std;

int main(){
    

    cout << "- Affichage des résultats - " << endl;
    cout << "Affiche V1 :" << endl;
    Vecteur3D V1;
    V1.affiche();
    Vecteur3D V2(23, 76, 11);
    V2.affiche("Affiche moi V2 :");

    return 0;
}

