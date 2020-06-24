/*
2. Mot-clés const et static

EXERCICE 5 : 
- Ecrire une fonction affichant un entier : void affiche(const int& n). Que signifie le const 
dans le prototype de la fonction affiche ? Que se passe t-il s'il ont tente de modifier l'entier
n à l'intérieur de la fonction affiche ?

*/

#include <iostream>
#include "main.h"

using namespace std;

int main()
{
    affiche(4);
}

void affiche(const int& n) {


  //  int n = 4;
    cout << n << endl;
}