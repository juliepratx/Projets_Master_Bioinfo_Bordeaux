#include <iostream>
#include <string.h>
#include "Personne.h"

using namespace std;

void Personne::affiche() const {
   // this->age = 0;
    cout << "Nom : " << nom << endl;;
    cout << "Prenom : " << prenom << endl;
    cout << "Age : " << age << " ans" << endl;
}
Personne::Personne() {
    // allocation dynamique de la memoire
    nom = new char[1];
    prenom = new char[1];

    nom[0] = '\0'; // \0 correspond au caractère de fin de chaine de caractères
    prenom[0] = '\0';
    age = -1; // -1 est un chiffre choisi pour désigner un age qui correspond au caractère de fin de chaine pour le type char.
}
Personne::Personne(char* unNom, char* unPrenom, int unAge) {
    //allocation dynamique de la mémoire
    nom = new char[strlen(unNom)];
    prenom = new char[strlen(unPrenom)];
    age = unAge;

    strncpy(nom, unNom, strlen(unNom));
    strncpy(prenom, unPrenom, strlen(unPrenom));
}
Personne::Personne(const Personne& unePersonne)
{
    //allocation dynamique de la mémoire
    nom = new char[strlen(unePersonne.nom)];
    prenom = new char[strlen(unePersonne.prenom)];
    age = unePersonne.age;

    strncpy(nom, unePersonne.nom, strlen(unePersonne.nom));
    strncpy(prenom, unePersonne.prenom, strlen(unePersonne.prenom));
}