from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import current_user
from .models import User

from . import models

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('User Name')
    submit = SubmitField('Log In')

class ChangePassword(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), \
        EqualTo('new_password2', message='Passwords must match.')])
    new_password2 = PasswordField('Input Again', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_old_password(self, field):
        if not current_user.verify_password(field.data):
            raise ValidationError('Old password does not match')