import random
from flask import Flask, render_template, jsonify

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
    # Utilisez Gunicorn pour le déploiement en production
    from gunicorn.app.base import BaseApplication

    class GunicornApp(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:8080',
        'workers': 4  # Ajustez le nombre de travailleurs en fonction de vos besoins
    }

    GunicornApp(app, options).run()
