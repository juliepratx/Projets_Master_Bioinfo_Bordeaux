#ifndef VECTEUR3D_H_INCLUDED
#define VECTEUR3D_H_INCLUDED


class Vecteur3D{

private:

	double x, y, z;

public :
	inline Vecteur3D();
	inline Vecteur3D(double x, double y, double z);
	~Vecteur3D();

	void affiche();
	void affiche(const char* string);

	
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


