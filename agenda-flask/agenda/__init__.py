import os
from flask import Flask
from decouple import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    environment = config('APPLICATION_ENV', default='Development')

    app = Flask(__name__)

    config_name = f'agenda.config.{environment}'
    app.config.from_object(config_name)

    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join(BASE_DIR, 'migrations'))

    register_blueprints(app)

    return app

def register_blueprints(app):
    from agenda.url import bp_home, bp_contact

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_contact)
