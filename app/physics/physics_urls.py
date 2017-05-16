from flask import Blueprint

from app.physics.junior import physics_junior_views
from app.physics.senior import physics_senior_views

physics_senior = Blueprint('physics_senior', __name__)

physics_senior.before_request(physics_senior_views.before_request)

physics_senior.add_url_rule('/', 'index', view_func=physics_senior_views.index,
                     methods=['GET', 'POST'])

physics_junior = Blueprint('physics_junior', __name__)

physics_junior.before_request(physics_junior_views.before_request)

physics_junior.add_url_rule('/', 'index', view_func=physics_junior_views.index,
                            methods=['GET', 'POST'])