/**
 * Programme de saisie de l'index, des noms, des poids et de l'âge d'identifieant d'aniamux d'un zoo.
 * Avec un menu.
 * @autor : Julie
 * @date : 15/01/20
 */

// Programme principal

public class Zoo {


    public static void main(String... args){

        // constante pour la taille des tableaux
        final int TAILLE = 10;

        // Initialisation des tables
        int[] tableIndex = new int[TAILLE];
        int[] tablePoids = new int[TAILLE];

/*  // Appel des fonctions indépendament du menu
        Animal.index(tableIndex);
        Animal.poids(tablePoids);
        Animal.recap(tableIndex,tablePoids);
        Animal.nomEtAge();
 */
        // Affiche le menu du programme et propose à l'utilisateur un choix d'action à effectuer
        Menu.menuAnimal(tableIndex, tablePoids);

    }
}
