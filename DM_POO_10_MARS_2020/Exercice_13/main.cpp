/*
5. Fonctions amies

EXERCICE 13 :

*/

#include <iostream>
#include "VecteurMatrice.h"

using namespace std;


int main(){

    double t[3];
    double s[3][3];
    Matrice m1(s);
    Vecteur v1(t);
    Vecteur v2 = m1.produit(v1);

    return 0;

}