from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        myjson = json.loads(request.data) # decode le json de la requete (json > dict)
        print(myjson["panier"]) # liste des noms des images selectionnees
        import makePatches
        print('ok')
        makePatches.imgToPatch(myjson["panier"]) # creer la liste des patches et save dans un fichier tfrecord
        import graphAssembly
        print('ok2')
        return jsonify(myjson) # encode en json (dict > json)
    return render_template("index.html") # affiche la page de l'interface

if __name__ == '__main__':
    app.run(debug=True)
