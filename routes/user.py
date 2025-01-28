from flask import Blueprint, render_template, request
from database.select import select_usuario, select_usuario_by_id
from database.insert import insert_user
# from database.update import update_user_by_id
from database.delete import delete_usuario

user_route = Blueprint('user', __name__)
usuarios = select_usuario()

@user_route.route('/')
def home():
    return render_template('lista_usuarios.html', usuarios=usuarios)

@user_route.route('/<int:id>')
def usuario_id(id):
    return render_template('lista_usuarios.html', usuario=select_usuario_by_id(id))

@user_route.route('/new')
def form_usuario():
    return render_template('cadastro.html')

@user_route.route('/cadastrar', methods=['POST'])
def add_user():

    data = request.form

    nome = data['nome']
    email = data['email']

    novo_usuario = insert_user(nome, email)

    return render_template('item_usuario.html', usuario=novo_usuario)

@user_route.route('editar/<int:id>', methods=['POST'])
def edit_user(id):
    # data = request.get_json()

    # nome = data["nome"]
    # email = data["email"]
    # status = data["status"]

    # update_user_by_id(id, nome, email, status)

    return render_template('cadastro.html', usuario=select_usuario_by_id(id))

@user_route.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    delete_usuario(id)
    lista = select_usuario()
    return render_template('lista_usuarios.html', usuarios=lista)
