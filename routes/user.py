from flask import Blueprint, render_template
from database.select import select_usuario

user_route = Blueprint('user', __name__)

@user_route.route('/')
def home():
    usuarios = select_usuario()
    return render_template('lista_usuarios.html', usuarios=usuarios)

@user_route.route('/new')
def new_user():
    return render_template('cadastro.html')