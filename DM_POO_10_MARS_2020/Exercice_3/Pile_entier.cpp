#include <iostream>
#include "Pile_entier.h"


Pile_entier::Pile_entier(int n) {
    taille = n;
    entiers = new int[taille];
    nbElements = 0;
}

Pile_entier::Pile_entier() {
    taille = 20;
    entiers = new int[taille];
    nbElements = 0;
}
Pile_entier::Pile_entier(const Pile_entier& pile) {
    entiers = new int[taille = pile.taille];
    nbElements = pile.nbElements;
    for (int i = 0; i < nbElements; i++) {
        entiers[i] = pile.entiers[i];
    }
}

Pile_entier::~Pile_entier() {
    delete entiers;
}

void Pile_entier::empile(int p) {
    if (nbElements < taille) {
        entiers[++nbElements] = p;
    }
}

int Pile_entier::depile() {
    if (nbElements > 0) {
        return entiers[--nbElements];
    }
}

int Pile_entier::pleine() {
    return (nbElements == taille);
}

int Pile_entier::vide() {
    return (nbElements == 0);
}