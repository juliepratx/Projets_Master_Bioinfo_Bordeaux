#ifndef PILE_ENTIER_H_INCLUDED
#define PILE_ENTIER_H_INCLUDED

class Pile_entier{

private:
    int taille; // taille de la pile
    int* entiers; // emplacement des entiers
    int nbElements; // nombre d'entiers empilés

public:
    Pile_entier(int n);
    Pile_entier();
    Pile_entier(const Pile_entier& p);
    ~Pile_entier();

    void empile(int p);
    int depile();
    int pleine();
    int vide();
};

#endif 
