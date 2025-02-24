from project import login_manager
import flask_login

users = {'admin': {'password': 'admin'}}

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(login):
    if login not in users:
        return
    
    user = User()
    user.id = login
    return user

@login_manager.request_loader
def request_loader(request):
    login = request.form.get('username')
    if login not in users:
        return
    
    user = User()
    user.id = login
    return user