from flask import Blueprint

from . import views

account = Blueprint('account', __name__)

account.add_url_rule('/login/', 'login', views.login, methods=['GET', 'POST'])
account.add_url_rule('/logout/', 'logout', views.logout)
account.add_url_rule('/change_password', 'change_password',
                      views.change_password, methods=['GET', 'POST'])
account.add_url_rule('/forget', 'forget_password', \
                      view_func=views.forget_password, methods=['GET', 'POST'])
account.add_url_rule('/index', 'index', view_func=views.index, \
                      methods=['GET', 'POST'])
account.add_url_rule('/', 'index', view_func=views.index, \
                      methods=['GET', 'POST'])
account.add_url_rule('/create/', 'create_user', \
                      view_func=views.create_user, methods=['GET', 'POST'])
account.add_url_rule('/permission/', 'change_permission', \
                      view_func=views.change_permission, \
                      methods=['GET', 'POST'])
account.add_url_rule('/all_users/', 'show_all_users', \
                      view_func=views.show_all_users, \
                      methods=['GET'])
account.add_url_rule('/set/<string:token>', 'set_password', \
                      view_func=views.set_password, \
                      methods=['GET', 'POST'])

