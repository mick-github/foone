from flask import Blueprint

from . import views, admin_views, typer_views, maintainer_views

# blueprint for all staff

main = Blueprint('main', __name__)

main.add_url_rule('/', 'index', views.index)


# blueprint for typer

typer = Blueprint('typer', __name__)

typer.add_url_rule('/add/', 'add_problem', view_func=typer_views.add_problem)

# blueprint for maintainer

maintainer = Blueprint('maintainer', __name__)

maintainer.add_url_rule('/edit/<problem_id>/', 'edit_problem', view_func=maintainer_views.edit_problem)

# blueprint for admin

admin = Blueprint('admin', __name__)

admin.add_url_rule('/', endpoint='admin_index', view_func=admin_views.index)