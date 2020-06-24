/*
Programme principal
*/

#include <iostream>
#include "Forme.h"

using namespace std;

int main()
{
    Forme F(2.1, 3.2);
    Cercle C(4.2, 5.3, 5.0);
    Sphere* PSphere;
    Cercle* PCercle;
    PCercle = &C;
    PSphere = PCercle;
    PSphere->affiche();

    return 0;
}

