#!/bin/bash
mkdir ArcheoAssembler
cd ArcheoAssembler
virtualenv -p /usr/bin/python2.7 venv
. venv/bin/activate #refaire cette ligne à chaque lancement du projet
pip install Flask numpy opencv-python networkx matplotlib layers scipy
pip install "keras<2.2.4"
pip install "tensorflow<1.13.1"

mkdir Data
# importer dans ArcheoAssembler vos datas, votre dossier images et le tableur de métadonnées ainsi que les .xml et xsd.
# mettre jstopy.py et les scripts de python dans le repertoire ArcheoAssembler
# mettre le fichier patchAssemble_ost2.h5 dans le repertoire ArcheoAssembler
mkdir templates
# créer un repertoire templates
# mettre index.html dans le repertoire ArcheoAssembler/templates
mkdir static
cd static
mkdir img
# mettre flavon.ico dans le repertoire ArcheoAssembler/static/img/
mkdir lib
# mettre les librairies jszip.js/sm.js/xls.js/xlsl.js/xmlToJSON.js  dans le repertoire ArcheoAssembler/static/lib
cd ..
# mettre index.js,index.css  dans le repertoire ArcheoAssembler/static
# créer un répertoire pour les images de résultats
mkdir preprocessed_
cd preprocessed_
mkdir test


# pour demarer le serveur :
# export FLASK_APP=jstopy.py
# export FLASK_ENV=development
# flask run

# pour acceder a l'interface : ouvrir une page d'un navigateur et aller sur http://127.0.0.1:5000/

# pour interompre le serveur : faire ctrl-c
