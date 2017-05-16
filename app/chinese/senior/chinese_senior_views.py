from flask import url_for, request, redirect, flash, abort
from flask_login import login_required, current_user
from app.account.models import sites
from app.util.decorators import site_permitted

@login_required
def before_request():
    if not current_user.check_site(sites.CHINESE_SENIOR):
        abort(403)

@login_required
#@site_permitted(sites.CHINESE_SENIOR)
def index():
    return "This is the senior chinese homepage"