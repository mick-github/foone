from flask import Blueprint

from . import views

accounts = Blueprint('accounts', __name__)

accounts.add_url_rule('/login/', 'login', views.login, methods=['GET', 'POST'])
accounts.add_url_rule('/logout/', 'logout', views.logout)
accounts.add_url_rule('/change_password', 'change_password',
                      views.change_password, methods=['GET', 'POST'])
accounts.add_url_rule('/reset', 'reset_password',
                      view_func=views.reset_password, methods=['GET', 'POST'])
accounts.add_url_rule('/add', 'add_user', view_func=views.add_user, \
                      methods=['GET', 'POST'])
accounts.add_url_rule('/forget', 'forget_password', \
                      view_func=views.forget_password, methods=['GET', 'POST'])
accounts.add_url_rule('/index', 'index', view_func=views.index, \
                      methods=['GET', 'POST'])
accounts.add_url_rule('/create/', 'create_user', \
                      view_func=views.create_new_user, methods=['GET', 'POST'])
