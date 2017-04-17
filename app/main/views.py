from flask_login import login_required

@login_required
def index():
    return "This is the function located in /main/views.py/index()"