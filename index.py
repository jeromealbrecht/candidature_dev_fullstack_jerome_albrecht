import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Liste de tours magiques
tours_magiques = [
    "Résolution de problèmes",
    "Expérience Front-End avec JavaScript, TypeScript",
    "Projet de simulation de modules IoT auto générés en PHP: [lien du projet sur GitHub](https://github.com/jeromealbrecht/IoT-app)",
    "Expérience Back-End avec Node.js, Python",
    "Réalisation d'un site référencé pour un studio d'enregistrement [lien du site](https://www.couleurdeson.fr)",
    "Expérience Full-Stack avec React, Angular, Svelte JS",
    "Communication en équipe avec Slack, Microsoft Teams, Discord",
    "Relationnel avec les clients : 4.9/5 sur Google My Business",
    "Gestion de projet avec Trello, Asana",
    "Gestion de code source avec Git, GitHub",
    "Déploiement avec Vercel, onRender, planetHoster",
    "Expérience en référencement SEO",
    "À venir : formation au cloud AWS",
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