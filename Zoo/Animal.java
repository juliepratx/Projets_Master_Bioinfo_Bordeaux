/**
 * La classe Animal comprend :
 * @index
 * @nom
 * @poids
 * @âge
 * @moyenne des poids des animaux
 */
// Les imports
import java.io.*;


class Lapin extends Animal{
}

class Canari extends Animal{
}

public class Animal {
    int index;
    int poids;
    String nom;
    int age;

    public static void canari(){
        System.out.println("Je suis un canard qui ri !");
    }

    public static void lapin(){
        System.out.println("Je m'appelle Bujuxx !");
    }

    public static void nomEtAge(){
        for (int i = 0 ; i < 10 ; i++){
            System.out.println("Donnez le nom de l'animal n° " + (i + 1));
            String nom = saisie_chaine();
            System.out.println("Donnez l'âge (en nombre de mois) de " + nom);
            int age = saisie_entier();
            System.out.println(nom + " est âgé de " + age + " mois.");
        }
    }
    public static void index(int[] table){
        for(int i = 0 ; i < 10 ; i++){
            System.out.println("Donnez l'index de l'animal n° " + (i + 1));
            int index = saisie_entier();
            table[i] = index;
         }
    }
    public static void poids(int[] table){
        for (int i = 0 ; i < 10 ; i++){
            System.out.println("Donnez le poids de l'animal n° " + (i + 1));
            int poids = saisie_entier();
            table[i] = poids;
        }
    }
    public static float moyennePoids(int[] tablePoids){
        float moyennePoidsDesAnimaux = 0.00f;
        float sommePoids = 0.00f;
        for (int i = 0 ; i < 10 ; i++){
            sommePoids += tablePoids[i];
            moyennePoidsDesAnimaux = sommePoids / 10;
        }
        System.out.println("La moyenne des poids des anmimaux du zoo est de " + moyennePoidsDesAnimaux + " kg.");
        return moyennePoidsDesAnimaux;
    }
    public static void animalPoidsSupMoyenne(int[] tableIndex, int[] tablePoids){
        float moyennePoidsDesAnimaux = Animal.moyennePoids(tablePoids);
        System.out.println();
        for (int i = 0 ; i < tablePoids.length ; i++){
            if (tablePoids[i] > moyennePoidsDesAnimaux){
                System.out.println("L'animal n° " + tableIndex[i] + " a un poids de " + tablePoids[i] + " kg qui est supérieur à moyenne.");
            }
            else {
                System.out.println("L'animal n° " + tableIndex[i] + " a un poids inférieur à la moyenne des poids des animaux.");
            }

        }
    }

    // Récapitulatif de la saisie des données
    public static void recap(int[] tableIndex, int[] tablePoids){
        System.out.println("Récapitulatif de la saisie :");
        for (int i = 0; i < tableIndex.length; i++) {
            System.out.println("L'animal " + (i + 1) + " qui à l'index n° " + tableIndex[i] + " à un poids de " + tablePoids[i] + " kg.");
        }
    }

    // Pour que l'utilisateur puisse saisir les index, le poids et l'âge des animaux : saisie de nombre entier
    public static int saisie_entier(){
        try{
            BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
            String chaine = buff.readLine();
            int num = Integer.parseInt(chaine);
            return num;
        }
        catch (IOException e){return 0;}
    }

    // Pour que l'utilisateur puisse saisir le nom des animaux : saisie de chaine de caractères
    public static String saisie_chaine(){
        try{
            BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
            String chaine = buff.readLine();
            return chaine;
        }
        catch (IOException e){return null;}
    }

}

/*
// Pour sauvegarder la saisie de l'utilisateur
    void save (BufferedWriter buff)
        throws IOException{
        buff.write(index);
        buff.newLine();
        buff.write(nom);
        buff.newLine();
        buff.write(age);
        buff.newLine();
        buff.write(poids);
        buff.newLine();
    }
 */
