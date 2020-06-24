/*
4. Fonctions membres et surdéfinition

EXERCICE 8 : On souhaitedonner le même nom à trois fonctions : "somme". La première additionne deux
entiers (type int), la deuxième deux réels (type float) et la troisième deux tableaux de dix entiers.
Donner le prototype de ces fonctions. Que se passe-t-il lorsqu'un appel est fait, avec comme arguments,
deux short. Est-il possible de créer une fonction somme prenant 3 paramètres de même type ? Est-il possible
de définir une fonction somme ayant deux paramètres de types différents (par ex un int et un float) ?
*/

#include <iostream>
#include "main.h"

using namespace std;

int const TAILLEMAX(10);


int somme(int a, int b) {

    int somme = 0;

    somme = a + b;

    return somme;
}

float somme(float a, float b) {

    float somme = 0.0;

    somme = a + b;

    return somme;
}

int somme(int* a, int* b) {

    int sommeA = 0; int sommeB = 0;
    int somme = 0;

    cout << endl;
    // Tableau A
    for (int i = 0; i < TAILLEMAX; i++) {
        sommeA += a[i];
    }

    cout << "Somme du tableau A : " << sommeA << endl;

    // Tableau B
    for (int i = 0; i < TAILLEMAX; i++) {
        sommeB += b[i];
    }
    cout << "Somme du tableau B : " << sommeB << endl;

    somme = sommeA + sommeB;

    cout << "Total des 2 tableaux : " << somme << endl;

    return somme;
}

int somme(int a, int b, int c) {

    int somme;

    somme = a + b + c;

    return somme;
}

int somme(float a, int b) {

    int somme;

    somme = a + b;

    return somme;
}

void contenuTab(int* a) {

    for (int i = 0; i < TAILLEMAX; i++) {

        cout << "La case du tableau [" << i << "] contient la valeur " << a[i] << endl;
    }
}




int main() {

    int tab_A[] = {21, 13, 9, 76, 1, 54, 32, 200, 3, 16};
    int tab_B[] = {37, 12, 90, 4, 73, 82, 33, 29, 75, 7};

    /*
    cout << "** Test des constructeurs **" << endl;
    cout << endl;
    cout << "- Résultat somme1 -" << endl;
    somme1(12, 32);
    cout << endl;
    cout << "- Résultat somme2 -" << endl;
    somme2(21.2, 12.9);
    cout << endl;
    cout << "- Contenu tableau A -" << endl;
    contenuTab(tab_A);
    cout << endl;
    cout << "- Contenu tableau B -" << endl;
    contenuTab(tab_B);
    cout << endl;
    cout << "- Résultat somme3 -" << endl;
    somme3(tab_A, tab_B);
    cout << endl;
    */
    cout << "** Avec un seul constructeur **" << endl;
    short nb1 = 12; short nb2 = 19;
    cout << "Avec 2 short : " << nb1 << " + " << nb2 << " = " << somme(nb1, nb2) << endl;
    cout << "Avec 3 paramètres de même type : " << somme(22, 87, 1) << endl;
    float nb3 = 12.65;
    cout << "Avec 2 paramètres différents : " << somme(nb3, 2) << endl;
    
   

    return 0;
}