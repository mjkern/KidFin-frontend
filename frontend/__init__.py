from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from frontend.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "common.login"

    from frontend.users.routes import users
    from frontend.dashboard.routes import dash
    from frontend.common.routes import common
    from frontend.normal.routes import normal
    from frontend.master.routes import master
    from frontend.admin.routes import admin
    app.register_blueprint(users)
    app.register_blueprint(dash)
    app.register_blueprint(common)
    app.register_blueprint(normal)
    app.register_blueprint(master)
    app.register_blueprint(admin)

    db.create_all(app=app)

    return app
