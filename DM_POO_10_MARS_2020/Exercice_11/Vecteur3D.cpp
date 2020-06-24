#include "Vecteur3D.h"
#include <iostream>

using namespace std;


Vecteur3D::~Vecteur3D() { ; }

void Vecteur3D::affiche() {
    cout << "x = " << x << " y = " << y << " z = " << z << endl;
}
void Vecteur3D::affiche(const char* string) {
    cout << "String = " << string << endl;
    cout << "x = " << x << " y = " << y << " z = " << z << endl;
}
int Vecteur3D::abscisse() {
    return x;
}
int Vecteur3D::ordonnee() {
    return y;
}
int Vecteur3D::cote() {
    return z;
}
void Vecteur3D::fixer_abscisse(int _x) {
    x = _x;
}
void Vecteur3D::fixer_ordonnee(int _y) {
    y = _y;
}
void Vecteur3D::fixer_cote(int _z) {
    z = _z;
}
bool Vecteur3D::coincide(const Vecteur3D& v) {
    return (v.x == x && v.y == y && v.z == z);
}
double Vecteur3D::produit_scalaire(Vecteur3D v) {
    return (x * v.x) + (y * v.y) + (z * v.z);
}
Vecteur3D Vecteur3D::somme(Vecteur3D v) {
    Vecteur3D vret(x + v.x, y + v.y, z + v.z);
    return vret;
}