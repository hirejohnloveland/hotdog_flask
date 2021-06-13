from flask import Flask, url_for
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    CORS(app)
    login.login_view = 'users.login'
    login.login_message = 'Please login to access the shopping cart'
    login.login_message_category = 'warning'
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
