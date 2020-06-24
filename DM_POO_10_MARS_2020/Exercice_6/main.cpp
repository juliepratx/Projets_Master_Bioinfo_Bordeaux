/*
2. Mot-clés const et static

EXERCICE 6 :

*/

#include <iostream>

using namespace std;

int main(){

    int s = 1;
    const int t = 1;

    int *p = &s;
    const int *q = &s; 
    int* const r = &s; 

    int *p = &t;
    const int *q = &t;
    int* const r = &t;

    p = new int;
    q = new int; 
    r = new int; 

    int** tableau = new int* [10];
    for (int i = 0; i < 10; i++) { tableau[i] = new int; }
    cout << tableau << endl;
    for (int i = 0; i < 10; i++) { delete tableau[i]; }
    cout << tableau << endl;

    return 0;
}
