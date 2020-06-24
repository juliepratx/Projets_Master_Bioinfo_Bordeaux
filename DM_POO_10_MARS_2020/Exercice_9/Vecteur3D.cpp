#include "Vecteur3D.h"
#include <iostream>

using namespace std;

Vecteur3D::~Vecteur3D() { ; }

void Vecteur3D::affiche(){

	cout << "x : " << x << endl;
	cout << "y : " << y << endl;
	cout << "z : " << z << endl;

}

void Vecteur3D::affiche(const char* string){

	cout << string << endl;
	Vecteur3D::affiche();

}



