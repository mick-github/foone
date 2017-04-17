import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .. import user_db, login_manager
from uuid import uuid3, NAMESPACE_DNS
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class User(user_db.Model, UserMixin):
    __tablename__ = 'users'
    id = user_db.Column(user_db.String(32), primary_key=True, unique=True)
    username = user_db.Column(user_db.String(128))
    email = user_db.Column(user_db.String(128), unique=True)
    password_hash = user_db.Column(user_db.String(128))
    confirmed = user_db.Column(user_db.Boolean, default=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        id = uuid3(NAMESPACE_DNS, username)
        id = ''.join(str(id).split('-'))
        self.id = id
        self.password = password
        self.has_confirmed = False

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
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        pass

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)