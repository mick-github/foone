from flask_login import login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from app.util.util import sites_endpoint

@login_required
def index():
    site = current_user.sites
    if site > 0 and site & (site - 1) == 0:
        site = sites_endpoint[site]
        return redirect(url_for(site))
    return "This is the main page"