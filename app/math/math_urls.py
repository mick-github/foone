from flask import Blueprint

# blueprint for junior Math
from app.math.junior import math_junior_views

math_junior = Blueprint('math_junior', __name__)

math_junior.before_request(math_junior_views.before_request)
math_junior.add_url_rule('/', 'index', view_func=math_junior_views.index,
                         methods=['GET', 'POST'])


# blueprint for senior Math
from app.math.senior import math_senior_views

math_senior = Blueprint('math_senior', __name__)

math_senior.before_request(math_senior_views.before_request)
math_senior.add_url_rule('/', 'index', view_func=math_senior_views.index,
                  methods=['GET', 'POST'])