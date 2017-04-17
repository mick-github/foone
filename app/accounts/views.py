from flask import render_template, redirect, request, flash, url_for, \
current_app, session, abort
from flask_login import login_user, logout_user, login_required, current_user
from . import forms
from .models import User
from .. import user_db

def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash("Invalid email or password.")
    return render_template('accounts/login.html', form=form)


@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('accounts.login'))


@login_required
def change_password():
    form = forms.ChangePassword()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        user.password = form.new_password.data
        user_db.session.add(user)
        user_db.session.commit()
        flash("password changed successfully")
        return redirect(url_for('main.index'))
    return render_template('accounts/change_password.html', form=form)


@login_required
def add_user():
    pass


def reset_password():
    pass


def forget_password():
    pass


@login_required
def index():
    pass


@login_required
def create_new_user():
    pass