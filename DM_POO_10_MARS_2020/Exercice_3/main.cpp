/*
1. Constructeurs et destructeurs

EXERCICE 3 :

*/


#include <iostream>
#include "Pile_entier.h"

using namespace std;

int main(){

    int i;
    Pile_entier p1(3); // une pile avec 3 entiers
    cout << "P1 est-elle vide ? " << p1.vide() << endl;
    p1.empile(2);
    p1.empile(1);
    p1.empile(5);
    cout << "___On remplie P1___" << endl;
    cout << "P1 est-elle pleine ? " << p1.pleine() << endl;
    cout << "P1 est-elle vide ? " << p1.vide() << endl;
    cout << "___On depile P1___" << endl;
    Pile_entier p2(p1);
    p1.depile();
    cout << "P1 est-elle pleine ? " << p1.pleine() << endl;
    cout << "P1 est-elle vide ? " << p1.vide() << endl;
    cout << "P2 est-elle pleine ? " << p2.pleine() << endl;
    cout << "P2 est-elle vide ? " << p2.vide() << endl;

    return 0;
}

