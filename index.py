import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Liste de tours magiques
tours_magiques = [
    "Expérience Front-End avec JavaScript, TypeScript",
    "Expérience Back-End avec Node.js, Python",
    "Expérience Full-Stack avec React, Angular, Svelte JS",
    "Communication en équipe avec Slack, Microsoft Teams",
    "Relationnel avec les clients",
    "Gestion de projet avec Trello, Asana",
    "Gestion de code source avec Git, GitHub",
    "Déploiement avec Vercel, onRender, planet Hoster",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generer_tour_magique', methods=['GET'])
def generer_tour_magique():
    tour_magique = random.choice(tours_magiques)
    return jsonify({'tour_magique': tour_magique})

if __name__ == '__main__':
    # Utilisons Gunicorn pour le déploiement en production
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
        'workers': 4
    }

    GunicornApp(app, options).run()