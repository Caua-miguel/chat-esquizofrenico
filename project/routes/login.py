from flask import Blueprint, request, render_template, redirect, url_for
from database.models.user import users, User
from flask_login import login_user, login_required, current_user, logout_user

login_route = Blueprint('login', __name__, template_folder='templates')

@login_route.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('cadastro.html')
    
    login = request.form['username']
    if login in users and request.form['password'] == users [login]['password']:
        user = User()
        user.id = login
        login_user(user)
        return redirect(url_for('login.protected'))
    return 'Bad login'

@login_route.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

@login_route.route('/logout')
def logout():
    logout_user()
    return 'Logged out'