from flask import Blueprint, render_template
from database.select import select_usuario
from database.delete import delete_usuario

user_route = Blueprint('user', __name__)
usuarios = select_usuario()

@user_route.route('/')
def home():
    return render_template('lista_usuarios.html', usuarios=usuarios)

@user_route.route('/new')
def new_user():
    return render_template('cadastro.html')

@user_route.route('/int:usuario.id/delete', methods=['DELETE'])
def deletar_usuario(id):
    delete_usuario(id)
