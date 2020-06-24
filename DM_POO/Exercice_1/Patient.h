#ifndef PATIENT_H
#define PATIENT_H

#include <iostream>
#include <string>
#include "Personne.h"

using namespace std;


class Patient :
	public Personne
{
public :

	void affiche();

private :

	int etatGrave = 3;
	int etatInt = 2;
	int etatLeg = 1;

};

#endif
