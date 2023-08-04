from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    from . import main

    app.register_blueprint(main.bp)

    return app