/*
1. Constructeurs et destructeurs

EXERCICE 1 :

*/

#include <iostream>
#include "Personne.h"


using namespace std;

int main(){

    

    Personne objetParDefaut;
    char nom[] = {'K','O','U','T','A','\0'};
    char prenom[] = {'A','B','O','U','\0'};
    Personne objetParParametre(nom, prenom, 22);
    Personne objetParCopie(objetParParametre);

    cout << "- Affichage des résultats -" << endl;
    cout << endl;
    cout << "Constructeur par défault : " << endl;
    objetParDefaut.affiche();
    cout << "Constructeur avec des paramètres : " << endl;
    objetParParametre.affiche();
    cout << "Constructeur de copie : " << endl;
    objetParCopie.affiche();



    return 0;
}
