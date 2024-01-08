import random
from flask import Flask, render_template, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)
basic_auth = BasicAuth(app)

# Utilisateur et mot de passe pour l'authentification de base
app.config['BASIC_AUTH_USERNAME'] = 'LettreJerome'
app.config['BASIC_AUTH_PASSWORD'] = 'Lj$8dPc7ùR'

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
@basic_auth.required  # Décorateur pour exiger l'authentification sur cette route
def index():
    return render_template('index.html')

@app.route('/api/generer_tour_magique', methods=['GET'])
@basic_auth.required  # Décorateur pour exiger l'authentification sur cette route
def generer_tour_magique():
    tour_magique = random.choice(tours_magiques)
    return jsonify({'tour_magique': tour_magique})

if __name__ == '__main__':
    app.run(debug=True)
