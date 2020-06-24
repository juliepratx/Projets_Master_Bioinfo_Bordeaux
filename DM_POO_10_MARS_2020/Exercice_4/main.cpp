/*
2. Mot-clés const et static

EXERCICE 4 : Quelles différences il y a t-il entre les deux constantes MAX1 et MAX2 définies de la façon suivante ?
*/

#include <iostream>

using namespace std;

#define MAX1 100
static const int MAX2 = 100;

int main(){

    int *p1 = &MAX1;
    int *p2 = &MAX2;

}


