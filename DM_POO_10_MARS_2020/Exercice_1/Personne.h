#ifndef PERSONNE_H_INCLUDED
#define PERSONNE_H_INCLUDED


class Personne{


private:

    char nom[20]; // nom est un tableau de 20 caractères
    char prenom[20];
    int age;

public:

    //CONSTRUCTEURS
    Personne(); // constructeur par défaut
    Personne(char[], char[], int); // constructeur avec des paramètres
    Personne(const Personne&); // constructeur par copie

    // DESTRUCTEURS
    ~Personne(); 

    // FONCTION
    void affiche() const;

};

#endif
