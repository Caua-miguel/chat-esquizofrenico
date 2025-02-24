from flask import Blueprint, render_template, request
from flask_login import login_required
from project.database.select import select_usuario, select_usuario_by_id, select_colecao, select_lib
from project.database.insert import insert_colecao
from project.database.update import update_user_by_id
from project.database.delete import delete_usuario, delete_colecao

lib_route = Blueprint('lib', __name__)

usuarios = select_usuario()
lib = select_lib()
lista_colecao = select_colecao()

@lib_route.route('/')
@login_required
def home():
    return render_template('lista_usuarios.html', usuarios=usuarios)

@lib_route.route('/explorar')
def explorar():
    return render_template('explorar.html', usuarios=lib)

@lib_route.route('/colecao')
def colecao():
    return render_template('colecao.html', usuarios=lista_colecao)

@lib_route.route('/<int:id>')
def usuario_id(id):
    return render_template('lista_usuarios.html', usuario=select_usuario_by_id(id))

@lib_route.route('/new')
def form_add_usuario():
    return render_template('cadastro.html')

# @lib_route.route('/cadastrar', methods=['POST'])
# def add_user():

#     data = request.form

#     nome = data["nome"]
#     email = data["email"]
#     senha = data["senha"]

#     insert_user(nome, email, senha)

#     return redirect(url_for('home.home'))

@lib_route.route('/edit/<int:id>', methods=['POST'])
def form_edit_usuario(id):

    return render_template('cadastro.html', usuario=select_usuario_by_id(id))

@lib_route.route('/editar/<int:id>', methods=['POST'])
def edit_user(id):
    data = request.form

    titulo = data["titulo"]
    autor = data["autor"]
    isbn = data["isbn"]
    categoria = data["categoria"]

    update_user_by_id(id, titulo, autor, isbn, categoria)

    lista = select_lib()
    return render_template('lista_usuarios.html', usuarios=lista)

@lib_route.route('/colecao/add/<int:id>', methods=['POST'])
def add_colecao(id):

    insert_colecao(id)

    lista = select_colecao()
    return render_template('/colecao.html', usuarios=lista)

@lib_route.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    delete_usuario(id)
    lista = select_usuario()
    return render_template('lista_usuarios.html', usuarios=lista)

@lib_route.route('/colecao/delete/<int:id>', methods=['POST'])
def delete_colecao_by_id(id):
    delete_colecao(id)
    lista = select_colecao()
    return render_template('colecao.html', usuarios=lista)
