from flask import Blueprint, render_template
from database.select import select_usuario, select_usuario_by_id
from database.delete import delete_usuario

user_route = Blueprint('user', __name__)
usuarios = select_usuario()

@user_route.route('/')
def home():
    return render_template('lista_usuarios.html', usuarios=usuarios)

@user_route.route('/new')
def new_user():
    return render_template('cadastro.html')

@user_route.route('/<int:id>')
def usuario_id(id):
    return render_template('lista_usuarios.html', usuario=select_usuario_by_id(id))
