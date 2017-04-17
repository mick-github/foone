from flask_login import login_required

@login_required
def add_problem():
    return "located in /main/typer_views.py/add_problem"