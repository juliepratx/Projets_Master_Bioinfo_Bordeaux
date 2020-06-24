#include <iostream>
#include "Personne.h"


using namespace std;

void Personne::affiche() const {
    cout << "Nom : " << nom << endl;;
    cout << "Prenom : " << prenom << endl;
    cout << "Age : " << age << " ans" << endl;
}
Personne::Personne() {
    nom[0] = '\0'; // \0 correspond au caractère de fin de chaine de caractères
    prenom[0] = '\0';
    age = -1; // -1 est un chiffre choisi pour désigner un age qui correspond au caractère de fin de chaine pour le type char.
}
Personne::Personne(char unNom[], char unPrenom[], int unAge) {
    age = unAge;
    int i = 0;
    while (unNom[i] != '\0' && i < sizeof(nom) - 1)
    {
        nom[i] = unNom[i];
        i++;
    }
    nom[i] = '\0';
    i = 0;
    while (unPrenom[i] != '\0' && i < sizeof(prenom) - 1) {
        prenom[i] = unPrenom[i];
        i++;
    }
    prenom[i] = '\0';
}
Personne::Personne(const Personne& unePersonne)
{
    age = unePersonne.age;
    int i = 0;
    while (unePersonne.nom[i] != '\0' && i < sizeof(nom) - 1) {

        nom[i] = unePersonne.nom[i];
        i++;
    }
    nom[i] = '\0';
    i = 0;
    while (unePersonne.prenom[i] != '\0' && i < sizeof(prenom) - 1) {

        prenom[i] = unePersonne.prenom[i];
        i++;
    }
    nom[i] = '\0';
}

Personne::~Personne() {;}




