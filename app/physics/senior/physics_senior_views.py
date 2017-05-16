from flask import render_template, url_for, request, abort
from flask_login import login_required, current_user
from app.account.models import sites
from app.util.decorators import site_permitted

@login_required
def before_request():
    if not current_user.check_site(sites.PHYSICS_SENIOR):
        abort(403)

@login_required
def index():
    return "This is the senior physics homepage"