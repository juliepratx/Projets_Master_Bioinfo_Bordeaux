#ifndef PERSONNE_H_INCLUDED
#define PERSONNE_H_INCLUDED


class Personne
{
private:
    char* nom;
    char* prenom;
    int age;

public:

    //CONSTRUCTEURS
    Personne(); // constructeur par défaut
    Personne(char*, char*, int); // constructeur avec des paramètres
    Personne(const Personne&); // constructeur par copie

    // DESTRUCTEUR
   // ~Personne();

    // AFFICHE
    void affiche() const;


};

#endif 
