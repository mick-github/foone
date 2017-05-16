import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_mongoengine import MongoEngine

from config import config

user_db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'

bootstrap = Bootstrap()
mail = Mail()
problem_db = MongoEngine()

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
    mail.init_app(app)
    problem_db.init_app(app)

    app.url_map.default_subdomain = 'www'

    # register the blueprints
    from .main.urls import main
    app.register_blueprint(main, subdomain='www')

    from .chemistry.chemistry_urls import chemistry
    app.register_blueprint(chemistry, subdomain='chemistry')

    from .chinese.chinese_urls import chinese_junior, chinese_senior
    app.register_blueprint(chinese_junior, subdomain='chinese',
                           url_prefix='/junior')
    app.register_blueprint(chinese_senior, subdomain='chinese',
                           url_prefix='/senior')

    from .english.english_urls import english_junior, english_senior
    app.register_blueprint(english_junior, subdomain='english',
                           url_prefix='/junior')
    app.register_blueprint(english_senior, subdomain='english',
                           url_prefix='/senior')

    from .math.math_urls import math_junior, math_senior
    app.register_blueprint(math_junior, subdomain='math', url_prefix='/junior')
    app.register_blueprint(math_senior, subdomain='math', url_prefix='/senior')

    from .physics.physics_urls import physics_junior, physics_senior
    app.register_blueprint(physics_junior, subdomain='physics',
                           url_prefix='/junior')
    app.register_blueprint(physics_senior, subdomain='physics',
                           url_prefix='/senior')

    from .account.urls import account
    app.register_blueprint(account, subdomain='account')

    return app