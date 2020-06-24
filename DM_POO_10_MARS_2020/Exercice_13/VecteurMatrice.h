
#ifndef VECTEURMATRICE_H_INCLUDED
#define VECTEURMATRICE_H_INCLUDED


#define TAILLE 3

#include <iostream>

using namespace std;

class Vecteur{

private:
    double vect[TAILLE];

public:
    Vecteur(double t[TAILLE]) {
        int i;
        for (i = 0; i < TAILLE; i++) {
            vect[i] = t[i];
        }
    }
    Vecteur getVect() {
        return vect;
    }
};

class Matrice{

private:
    double mat[TAILLE][TAILLE];

public:
    Matrice(double t[TAILLE][TAILLE]) {
        int i, j;
        for (i = 0; i < TAILLE; i++) {
            for (j = 0; j < TAILLE; j++) {
                mat[i][j] = t[i][j];
            }
        }
    }

    Matrice getMat() {
        return mat;
    }

    Vecteur produit(Vecteur vect) {
        Vecteur v1 = vect.getVect();
        return vect;
    }
};

//Vecteur produit(Matrice mat,Vecteur vect){
//    Matrice m1 = mat.getMat();
//    Vecteur v1 = vect.getVect();
//    return vect;
//};

#endif
