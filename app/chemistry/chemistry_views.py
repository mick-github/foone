from flask import render_template, url_for, request, redirect, flash, abort
from flask_login import current_user, login_required
from ..account.models import sites

@login_required
def before_request():
    if not current_user.check_site(sites.CHEMISTRY):
        abort(403)

@login_required
def index():
    return "This is the chemistry homepage"