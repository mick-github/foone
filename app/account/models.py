import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .. import user_db, login_manager
from uuid import uuid3, NAMESPACE_DNS
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class Permission:
    CREATE = 0x01
    EDIT = 0x02
    DELETE = 0x04
    USER_ADMIN = 0x08

roles = {
    'Input': Permission.CREATE,
    'Editor': Permission.CREATE | Permission.EDIT,
    'Admin': Permission.USER_ADMIN,
    'Super': Permission.CREATE | Permission.EDIT | Permission.DELETE |
        Permission.USER_ADMIN
}

class sites:
    CHEMISTRY = 0x001
    CHINESE_JUNIOR = 0x002
    CHINESE_SENIOR = 0x004
    ENGLISH_JUNIOR = 0x008
    ENGLISH_SENIOR = 0x010
    MATH_JUNIOR = 0x020
    MATH_SENIOR = 0x040
    PHYSICS_JUNIOR = 0x080
    PHYSICS_SENIOR = 0x100

class User(user_db.Model, UserMixin):
    __tablename__ = 'users'
    id = user_db.Column(user_db.String(32), primary_key=True, unique=True)
    username = user_db.Column(user_db.String(128))
    email = user_db.Column(user_db.String(128), unique=True)
    password_hash = user_db.Column(user_db.String(128))
    confirmed = user_db.Column(user_db.Boolean, default=False)
    permissions = user_db.Column(user_db.Integer, default=0x00)
    sites = user_db.Column(user_db.Integer, default=0x000)

    def __init__(self, username, email, **kwargs):
        self.username = username
        self.email = email
        id = uuid3(NAMESPACE_DNS, username)
        id = ''.join(str(id).split('-'))
        self.id = id
        self.confirmed = False
        self.permissions = kwargs.get('permissions', 0x00)
        self.sites = kwargs.get('sites', 0x000)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'email': self.email})

    @staticmethod
    def verify_email(email):
        user = User.query.filter_by(email=email).first()
        if not user:
            return True
        else:
            return False

    @staticmethod
    def extract_user_from_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.filter_by(email=data.get('email', None)).first()

    def can(self, permissions):
        return self.permissions & permissions == permissions

    def check_site(self, site):
        return self.sites & site == site

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)