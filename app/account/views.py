from flask import render_template, redirect, request, flash, url_for, \
    current_app, abort
from flask_login import login_user, logout_user, login_required, current_user

from app.util.decorators import permission_required
from . import forms
from .email import send_email
from .models import User, Permission
from .. import user_db
from flask import session
from app.util.util import sites_endpoint, redirect_sites


def login():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('account.index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            old_user_email = session.get('user_email', None)
            if old_user_email and old_user_email != user.email:
                flash('Another account has logged in')
                redirect(url_for('account.index'))

            if user.confirmed and user.verify_password(form.password.data):
                login_user(user)
                session['user_email'] = user.email
                site = redirect_sites(user)
                return redirect(url_for(site))
            else:
                flash("Invalid password or password not set.")
        else:
            flash("Invalid email")
    return render_template('account/login.html', form=form)


@login_required
def logout():
    del session['user_email']
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('account.login'))


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
    return render_template('account/change_password.html', form=form)


# This function deals with the situation if the user forget the password. It
# is the page showing the place for user to input email.
def forget_password():
    form = forms.ForgetPassword()
    if form.validate_on_submit():
        user = None
        try:
            user = User.query.filter_by(email=form.email.data).first()
        except:
            flash('User not found')

        if user is not None:
            send_email(user.email, '[Foone] Confirm Email',
                       'account/email/confirm',
                       user=user,
                       token=user.generate_confirmation_token())
            user.confirmed = False
            user_db.session.add(user)
            user_db.session.commit()
            flash('An email has sent to your box. Please check that.')
            return redirect(url_for('account.login'))
    return render_template('account/forget_password.html', form=form)


@login_required
def index():
    user = current_user
    return render_template('account/index.html', user=user)


@login_required
@permission_required(Permission.USER_ADMIN)
def create_user():
    form = forms.CreateUser()
    if form.validate_on_submit():
        if User.verify_email(form.email.data):
            # create a user
            user = User(username=form.username.data, email=form.email.data)
            user_db.session.add(user)
            user_db.session.commit()
            send_email(user.email, '[Foone] Confirm Email',
                       'account/email/confirm',
                       user=user, token=user.generate_confirmation_token())
            flash('User added successfully')
            return redirect(url_for('account.create_user'))
        else:
            flash('This email has been used.')
    return render_template('account/create_user.html', form=form)


# This view function does not have a page. It just receives request and make
# corresponding response and redirect to other places, like logout
@login_required
@permission_required(Permission.USER_ADMIN)
def change_permission():
    pass


@login_required
@permission_required(Permission.USER_ADMIN)
def show_all_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.order_by(User.username.asc()).paginate(
        page, current_app.config.get('PER_PAGE', 20), error_out=False
    )
    users = pagination.items
    return render_template('account/all_users.html', users=users,
                           pagination=pagination)


# This function is used for the following step of forget_password. In this
# page, the user should input two identical passwords as his new password,
# and the page will redirect to the login page. This page should be
# redirected from link shown in the email.
def set_password(token):
    # extract the email from the link
    user = User.extract_user_from_token(token=token)
    if not user:
        flash('No user can be found.')
        abort(404)
    elif user.confirmed:
        flash('You have already set your password. Please log in.')
        return redirect(url_for('account.login'))

    # if user exists and not set password
    form = forms.SetPassword()
    if form.validate_on_submit():
        user.password = form.password.data
        user.confirmed = True
        user_db.session.add(user)
        user_db.session.commit()
        flash('You have successfully reset your password! Please log in')
        return redirect(url_for('account.login'))
    return render_template('account/set_password.html', form=form, token=token)
