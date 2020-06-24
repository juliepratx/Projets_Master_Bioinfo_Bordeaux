/*
3. Fonctions en ligne

EXERCICE 7 : Quel est la différence entre les deux "fonctions" suivantes ?

*/

#include <iostream>

using namespace std;

#define copie1(source,dest) source = dest;

inline void copie2(int source, int dest) {

    source = dest;
}


/*
Est-ce que la copie des réalisée dans les deux cas ? Essayez d'appeler les deux "fonctions" avec
des rationnels (de type double). Que se passe t-il ? Peut-on définir des fonctions récursives de 
cette façon ?
*/

int main(){

    double a = 1.01;
    double b = 5.04;

    int c = 1;
    int d = 56;

    cout << "Copie 1" << endl;
    copie1(a, b);
    copie1(c, d);

    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout << d << endl;


    cout << "\nCopie 2" << endl;
    copie2(a, b);
    copie2(c, d);

    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout << d << endl;

    return 0;
}


