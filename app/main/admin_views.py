from flask_login import login_required

@login_required
def index():
    return "Located in /main/admin_views.py/index"