# from flask import Blueprint, render_template, request, redirect, url_for
# from database.select import select_usuario_by_email, select_usuario
# from flask_login import login_user, login_required
# from main import login_manager

# login_usuario = Blueprint('login', __name__)

# usuarios = select_usuario()

# @login_manager.user_loader
# def user_loader(email):
#     usuario_logado = select_usuario_by_email(email)
    
#     if usuario_logado is None:
#         return None

#     return usuario_logado

# @login_manager.request_loader
# def request_loader(request):
    
#     data = request.form

#     email = data["email"]

#     usuario_logado = select_usuario_by_email(email)

#     if usuario_logado is None:
#         return None
    
#     return usuario_logado

# @login_usuario.route('/', method = ['GET'])
# def home():

#     if request.method == 'GET':

#         return render_template('teste_index.html')
    
#     email = request.form['email']
#     if email in usuarios and request.form['senha'] == usuarios[email]['senha']:
#         usuario_logado = select_usuario_by_email(email)
#         login_user(usuario_logado)

#         return redirect(url_for('protected'))
    
#     return 'Bad login'

# @login_usuario.route('/protected')
# @login_required
# def protected():
#     return 'Logged in your accont!'