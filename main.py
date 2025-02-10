from flask import Flask
# import flask_login
from setup import setup_app


app = Flask(__name__)
# app.secret_key = 'super'

setup_app(app)

# login_manager = flask_login.LoginManager()

# login_manager.init_app(app)

app.run(debug=True)