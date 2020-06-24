#ifndef VECTEUR3D_H_INCLUDED
#define VECTEUR3D_H_INCLUDED


class Vecteur3D{

private:
    double x, y, z;

public:
    //Constructeurs et destructeur
    inline Vecteur3D();
    inline Vecteur3D(double, double, double);
    ~Vecteur3D();

    //Fonctions affiche
    void affiche();
    void affiche(const char* string);

    //Getters
    int abscisse();
    int ordonnee();
    int cote();

    //Setters
    void fixer_abscisse(int);
    void fixer_ordonnee(int);
    void fixer_cote(int);

    friend int coincide(const Vecteur3D& v1, const Vecteur3D& v2) {
        return (v1.x == v2.x && v1.y == v2.y && v1.z == v2.z);
    }

    double produit_scalaire(Vecteur3D);
    Vecteur3D somme(Vecteur3D);
};

inline Vecteur3D::Vecteur3D() {
    x = 0;
    y = 0;
    z = 0;
}

inline Vecteur3D::Vecteur3D(double _x, double _y, double _z) {
    x = _x;
    y = _y;
    z = _z;
}

#endif 
