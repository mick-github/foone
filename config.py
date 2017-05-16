# missing database settings
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fooneShanghai2009!')

    TEMPLATE_PATH = os.path.join(basedir, 'app/templates')
    STATIC_PATH = os.path.join(basedir, 'app/static')
    EXPORT_PATH = os.path.join(basedir, 'app/exports')

    if not os.path.exists(EXPORT_PATH):
        os.makedirs(EXPORT_PATH)

    MAIL_SUBJECT_PREFIX = '[Foone]'
    MAIL_SENDER = 'mick4u_flask@163.com'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SERVER_NAME = 'example.local:5000'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://flask:qly200509741@localhost/develop_db'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 994
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'mick4u_flask@163.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'qly200509741')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER',
                                         'mick4u_flask@163.com')

    MONGODB_DB = 'ENG_DEVELOP_DB'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 20510

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql://flask:qly200509741@localhost/test_db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://flask:qly200509741@localhost/product_db'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}