#ifndef PERSONNE_H
#define PERSONNE_H

#include <iostream>
#include <string>

using namespace std;

class Personne {

protected: 

	string Nom;
	string Prenom;
	string Num_INSEE;
	string Date_Naissance;

public:

	Personne();
	Personne(string, string, string, string);
	string getNom();
	string getPrenom();
	string getNum_INSEE();
	string getDate_Naissance();
	void affiche();
};
#endif
