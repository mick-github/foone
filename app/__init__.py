import os

from flask import Flask
from flask_login import LoginManager
# from flask_principal import Principal
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import config

user_db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'accounts.login'

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__,
                template_folder=config[config_name].TEMPLATE_PATH,
                static_folder=config[config_name].STATIC_PATH
                )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    user_db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # register the blueprints
    from .accounts.urls import accounts as accounts_blueprint
    app.register_blueprint(accounts_blueprint, url_prefix='/accounts')

    from .main.urls import main as main_blueprint, typer as typer_blueprint, \
        maintainer as maintainer_blueprint, admin as admin_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(typer_blueprint, url_prefix='/typer')
    app.register_blueprint(maintainer_blueprint, url_prefix='/maintainer')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app