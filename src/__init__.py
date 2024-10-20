from flask import Flask
from config import Config,db
from src.service import register_services
from src.controller import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)


    with app.app_context():
        db.create_all()
        register_services(app)
        register_blueprints(app)

    return app
