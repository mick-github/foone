from flask_login import login_required

@login_required
def edit_problem(problem_id):
    return "Located in /main/maintainer_views.py/edit_problem with {" \
           "}".format(problem_id)