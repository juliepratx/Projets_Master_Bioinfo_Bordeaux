/**
 * La classe menu sert à :
 * @afficher le menu
 * @choix de l'utilisateur
 * @RQ : si le choix de l'utilisateur n'est pas valable, renvoi d'une erreur
 * AJOUT : un menu intermédiaire qui permet à l'utilisateur de choisir le type d'animal à enregistrer (canari ou lapin)
 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Menu {
/*
    public static void afficheMenu(int[] tableIndex, int[] tablePoids) {

        System.out.println("      Menu d'enregistrement des données !");
        System.out.println();
        System.out.println("1 - Entrer l'index de l'animal.");
        System.out.println("2 - Entrer le nom et l'âge de l'animal.");
        System.out.println("3 - Entrer le poids de l'animal");
        System.out.println("4 - Afficher le récapitulatif de la saisie.");
        System.out.println("5 - Calculer la moyenne des poids des animaux.");
        System.out.println("6 - Afficher les animaux qui ont un poids > à la moyenne.");
        System.out.println("7 - Sauvegarder les données dans un fichier.txt.");
        System.out.println("8 - Charger la dernière sauvegarde de données.");
        System.out.println("9 - Choix du type d'animal.");
        System.out.println("0 - Quitter le programme.");

        int rep = saisieReponse();

        while (true) {
*/
          /*  switch (rep) {
                case '1':
                    Animal.index(tableIndex);
                    afficheMenu(tableIndex, tablePoids);
                    break;
                case '2':
                    Animal.nomEtAge();
                    afficheMenu(tableIndex, tablePoids);
                    break;
                case '3':
                    Animal.poids(tablePoids);
                    afficheMenu(tableIndex, tablePoids);
                    break;
                case '4':
                    Animal.recap(tableIndex, tablePoids);
                    afficheMenu(tableIndex, tablePoids);
                    break;
                case '5':
                    afficheMenu(tableIndex, tablePoids);
                    break;
                case '6':

                    break;
                case '0':
                    System.exit(0);
                default:
                    System.out.println("Erreur de saisie.");
                    afficheMenu(tableIndex, tablePoids);
            }

           */
/*

            if (rep == 1){
                Animal.index(tableIndex);
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 2){
                Animal.nomEtAge();
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 3){
                Animal.poids(tablePoids);
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 4){
                Animal.recap(tableIndex, tablePoids);
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 5){
                Animal.moyennePoids(tablePoids);
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 6){
                Animal.animalPoidsSupMoyenne(tableIndex, tablePoids);
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 7){
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 8){
                afficheMenu(tableIndex, tablePoids);
            }
            if (rep == 9){
                menuAnimal(tableIndex,tablePoids);
            }
            if (rep == 0){
                System.exit(0);
            }
            if (rep >= 10){
                System.out.println("Erreur de saisie.");
                afficheMenu(tableIndex, tablePoids);
            }

        }
    }
    */

    public static int saisieReponse() {
        try {
            BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
            String chaine = buff.readLine();
            int reponse = Integer.parseInt(chaine);
            return reponse;
        } catch (IOException e) {
            return 0;
        }
    }

    public static void menuAnimal(int[] tableIndex, int[] tablePoids){

        System.out.println();
        System.out.println("               Menu principal");
        System.out.println("   Quel type d'animal voulez-vous enregistrer ?");
        System.out.println();
        System.out.println("1 - Canari");
        System.out.println("2 - Lapin");
        System.out.println("0 - Quitter le programme");

        int rep = saisieReponse();

        while(true){

            if (rep == 1){
                Canari.canari();
                System.out.println();
                menuCanari(tableIndex,tablePoids);
            }
            if (rep == 2){
                Lapin.lapin();
                System.out.println();
                menuLapin(tableIndex,tablePoids);
            }
            if (rep == 0){
                System.exit(0);
            }
            if (rep >= 3){
                System.out.println("Erreur de saisie.");
                menuAnimal(tableIndex, tablePoids);
            }

        }

    }

    public static void menuCanari(int[] tableIndex, int[] tablePoids){

        System.out.println("                      CANARI");
        System.out.println();
        System.out.println("      Menu d'enregistrement des données !");
        System.out.println();
        System.out.println("    1 - Entrer l'index de l'animal.");
        System.out.println("    2 - Entrer le nom et l'âge de l'animal.");
        System.out.println("    3 - Entrer le poids de l'animal");
        System.out.println("    4 - Afficher le récapitulatif de la saisie.");
        System.out.println("    5 - Calculer la moyenne des poids des animaux.");
        System.out.println("    6 - Afficher les animaux qui ont un poids > à la moyenne.");
        System.out.println("    7 - Sauvegarder les données dans un fichier.txt.");
        System.out.println("    8 - Charger la dernière sauvegarde de données.");
        System.out.println("    9 - Choix du type d'animal.");
        System.out.println("    0 - Quitter le programme.");

        int rep = saisieReponse();

        while (true) {

            if (rep == 1){
                Canari.index(tableIndex);
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 2){
                Canari.nomEtAge();
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 3){
                Canari.poids(tablePoids);
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 4){
                Canari.recap(tableIndex, tablePoids);
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 5){
                Canari.moyennePoids(tablePoids);
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 6){
                Canari.animalPoidsSupMoyenne(tableIndex, tablePoids);
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 7){
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 8){
                menuCanari(tableIndex, tablePoids);
            }
            if (rep == 9){
                menuAnimal(tableIndex,tablePoids);
            }
            if (rep == 0){
                System.exit(0);
            }
            if (rep >= 10){
                System.out.println("Erreur de saisie.");
                menuCanari(tableIndex, tablePoids);
            }
        }

    }

    public static void menuLapin(int[] tableIndex, int[] tablePoids){

        System.out.println("                       LAPIN");
        System.out.println();
        System.out.println("      Menu d'enregistrement des données !");
        System.out.println();
        System.out.println("    1 - Entrer l'index de l'animal.");
        System.out.println("    2 - Entrer le nom et l'âge de l'animal.");
        System.out.println("    3 - Entrer le poids de l'animal");
        System.out.println("    4 - Afficher le récapitulatif de la saisie.");
        System.out.println("    5 - Calculer la moyenne des poids des animaux.");
        System.out.println("    6 - Afficher les animaux qui ont un poids > à la moyenne.");
        System.out.println("    7 - Sauvegarder les données dans un fichier.txt.");
        System.out.println("    8 - Charger la dernière sauvegarde de données.");
        System.out.println("    9 - Choix du type d'animal.");
        System.out.println("    0 - Quitter le programme.");

        int rep = saisieReponse();

        while (true) {

            if (rep == 1){
                Lapin.index(tableIndex);
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 2){
                Lapin.nomEtAge();
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 3){
                Lapin.poids(tablePoids);
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 4){
                Lapin.recap(tableIndex, tablePoids);
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 5){
                Lapin.moyennePoids(tablePoids);
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 6){
                Lapin.animalPoidsSupMoyenne(tableIndex, tablePoids);
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 7){
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 8){
                menuLapin(tableIndex, tablePoids);
            }
            if (rep == 9){
                menuAnimal(tableIndex,tablePoids);
            }
            if (rep == 0){
                System.exit(0);
            }
            if (rep >= 10){
                System.out.println("Erreur de saisie.");
                menuLapin(tableIndex, tablePoids);
            }

        }

    }
}










