#ifndef LISTEORD.H
#define LISTEORD.H


class ListeOrd {

public:

	ListeOrd();
	~ListeOrd();
	void InsertInPlace(int data);//insère data à la place
	void popFirst(Element* element);//retire le premier élément
	bool Is_empty(Element* L);//vérifie si la liste est vide
	void display();//affiche le contenu de la liste



};

#endif