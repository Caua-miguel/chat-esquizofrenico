from flask import Flask
from project.routes.home import home_route
from project.routes.lib import lib_route
from project.routes.chat import chat_route
from project.database.database import db
from project.database.select import select_usuario

app = Flask(__name__)
# app.secret_key = 'super'

app.register_blueprint(home_route)
app.register_blueprint(lib_route, url_prefix='/user')
# app.register_blueprint(login_usuario, url_prefix='/login')
app.register_blueprint(chat_route, url_prefix='/chat')

# login_manager = flask_login.LoginManager()

# login_manager.init_app(app)

db
select_usuario()