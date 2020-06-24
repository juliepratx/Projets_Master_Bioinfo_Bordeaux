#include <iostream>
//#include "ListeOrd.h"

using namespace std;

struct Element
{
	int data;
	Element* suivant;
};

Element* liste = NULL; // initialisation de la liste en liste vide

void InsertInPlace(int data)
{
	Element* element = new Element; // on fixe la valeur de l'élément
	element->data = data; // on place le nouvel élément en début de liste
	element->suivant = liste; // déplacement du pointeur vers la tête de la liste
	liste = element;
}

Element* Rechercher(int data)
{
	Element* element = liste;
	// On se place en première position tant qu'il y a des éléments suivant
	// jusqu'à ce qu'on trouve un élément de la liste qui correspond à 
	// notre recherche
	while (element != NULL && element->data != data)
		element = element->suivant;
	// et on renvoi l'élément s'il existe
	// sinon, NULL s'affichera à l'écran
	return element;
}

void popFirst(Element* element)
{
	Element* precedent = liste;
	// si l'élément à supprimer est le premier sur la liste
	if (element == liste) {
		liste = NULL;
		delete element;
		return;
	}
	// dans le cas contraire, il faut détourner le pointeur pour
	// qu'il pointe vers l'élément suivant
	while (precedent != NULL && precedent->suivant != element)
		precedent = precedent->suivant;

	if (precedent == NULL) return;
	precedent->suivant = element->suivant;
	delete element;
}

void display()
{
	Element* element = liste; // affiche chaque élément de la liste
	while (element != NULL) {
		cout << element->data << "\t"; // \t sert à la mise en forme de la liste au lancement du programme
		element = element->suivant;
	}
	cout << endl;
}

int main(void)
{
	Element* e;

	InsertInPlace(10);
	InsertInPlace(5);
	InsertInPlace(13);

	display();

	e = Rechercher(5);
	popFirst(e);
	//e = Rechercher(13); // ne fonctionne pas si je veux supprimer 2 éléments à la suite
	//popFirst(e);

	display();

	return 0;
}
