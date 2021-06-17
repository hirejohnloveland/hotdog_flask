from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.blueprints.users import bp as users
        app.register_blueprint(users)

        from app.blueprints.menu import bp as menu
        app.register_blueprint(menu)

        from app.blueprints.orders import bp as orders
        app.register_blueprint(orders)

        from app.blueprints.api import bp as api
        app.register_blueprint(api)

    return app
