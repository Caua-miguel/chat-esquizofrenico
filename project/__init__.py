from flask import Flask
from flask_login import LoginManager
from project.database.database import db
from project.database.select import select_usuario

app = Flask(__name__)
app.secret_key = 'super'

login_manager = LoginManager()
login_manager.init_app(app)

from project.routes.home import home_route
from project.routes.lib import lib_route
from project.routes.login import login_route
from project.routes.chat import chat_route

app.register_blueprint(home_route)
app.register_blueprint(lib_route, url_prefix='/lib')
app.register_blueprint(login_route, url_prefix='/login')
app.register_blueprint(chat_route, url_prefix='/chat')

from database.models import user

db
select_usuario()