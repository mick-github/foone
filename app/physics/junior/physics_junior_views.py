from flask import render_template, url_for, request, abort
from app.account.models import sites
from flask_login import login_required, current_user

@login_required
def before_request():
    if not current_user.check_site(sites.PHYSICS_JUNIOR):
        abort(403)

@login_required
def index():
    return "This is the junior physics homepage"
