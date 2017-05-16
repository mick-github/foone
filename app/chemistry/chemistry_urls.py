from flask import Blueprint

from . import chemistry_views

chemistry = Blueprint('chemistry', __name__)

chemistry.before_request(chemistry_views.before_request)
chemistry.add_url_rule('/', 'index', view_func=chemistry_views.index,
                       methods=['GET', 'POST'])
