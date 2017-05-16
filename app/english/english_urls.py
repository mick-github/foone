from flask import Blueprint

from app.english.junior import english_junior_views

english_junior = Blueprint('english_junior', __name__)

english_junior.before_request(english_junior_views.before_request)
english_junior.add_url_rule('/', 'index', view_func=english_junior_views.index,
                            methods=['GET', 'POST'])


# blueprint for senior English
from app.english.senior import english_senior_views

english_senior = Blueprint('english_senior', __name__)

english_senior.before_request(english_senior_views.before_request)
english_senior.add_url_rule('/', 'index', view_func=english_senior_views.index,
                     methods=['GET', 'POST'])