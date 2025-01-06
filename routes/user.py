from flask import Blueprint, render_template

user_route = Blueprint('user', __name__)

@user_route.route('/user')
def home():
    return render_template('cadastro.html')