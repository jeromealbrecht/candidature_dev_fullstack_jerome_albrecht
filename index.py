from flask import Flask, render_template, jsonify
from waitress import serve
from index import app

import random

app = Flask(__name__)

# Liste de tours magiques
tours_magiques = [
    "Gestion du workflow documentaire.",
    "Amélioration de la navigation dans la Drive.",
    "Amélioration du partage dans l’organisation💻",
    "Enrichissement automatique des données.",
    "Solution orientée IA : IA générative.",
    "Recherche unifiée Google et applications tiers",
    "Identification des personnes selon leurs champs de compétences et d’expertises"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generer_tour_magique', methods=['GET'])
def generer_tour_magique():
    tour_magique = random.choice(tours_magiques)
    return jsonify({'tour_magique': tour_magique})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)