from flask import Blueprint, render_template

user_route = Blueprint('user', __name__)

@user_route.route('/')
def home():
    # Listar os usuários
    return render_template('cadastro.html')

@user_route.route('/new')
def new_user():
    return render_template('cadastro.html')