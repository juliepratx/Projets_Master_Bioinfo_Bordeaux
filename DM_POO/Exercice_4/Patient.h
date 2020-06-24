#ifndef PATIENT_H
#define PATIENT_H

#include <iostream>
#include <string>
#include "Personne.h"

using namespace std;


class Patient :
	public Personne
{
public:

	void etatPatient(int etatP1, string P1, int etatP2, string P2) {
	        // compare les chaines de caractères
		if (etatP1 == etatP2) {
			cout << "L'état des patients " << P1 << " et " << P2 << " sont identiques." << endl;
		}
		if (etatP1 < etatP2) {
			cout << "Le patient " << P2 << " est dans un état plus grave que le patient " << P1 << endl;
		}
	}
	void affiche();

private:

	int etatGrave = 3;
	int etatInt = 2;
	int etatLeg = 1;

};

#endif
