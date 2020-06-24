/*
Programe principal
*/

#include <iostream>
#include "Personne.h"
#include "Patient.h"


using namespace std;

int main()
{

    Personne P1; // création d'un objet Personne
    P1.getNom();
    P1.getPrenom();
    P1.getDate_Naissance();
    P1.getNum_INSEE();
    P1.affiche();
    Patient Pa1; // création d'un objet Patient
    Pa1.getNom();
    Pa1.getPrenom();
    Pa1.getDate_Naissance();
    Pa1.getNum_INSEE();
    Pa1.affiche();

}