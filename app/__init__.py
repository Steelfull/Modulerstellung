from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Erstellen einer SQLAlchemy-Instanz
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Datenbankkonfiguration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modulbeschreibungen.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SQLAlchemy mit der Flask-App verbinden
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app


