from flask import Blueprint

# blueprint for junior Chinese
from app.chinese.junior import chinese_junior_views

chinese_junior = Blueprint('chinese_junior', __name__)

chinese_junior.before_request(chinese_junior_views.before_request)
chinese_junior.add_url_rule('/', 'index', view_func=chinese_junior_views.index,
                            methods=['GET', 'POST'])


# blueprint for senior Chinese
from app.chinese.senior import chinese_senior_views

chinese_senior = Blueprint('chinese_senior', __name__)

chinese_senior.before_request(chinese_senior_views.before_request)
chinese_senior.add_url_rule('/', 'index', view_func=chinese_senior_views.index,
                            methods=['GET', 'POST'])

