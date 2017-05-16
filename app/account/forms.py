from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, \
    HiddenField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
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

class SetPassword(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(), \
        EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Input Again', validators=[DataRequired()])
    token = HiddenField('Token')
    submit = SubmitField('Submit')

class ForgetPassword(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Check')

class CreateUser(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Create')