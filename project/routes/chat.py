from flask import Blueprint, render_template

chat_route = Blueprint('chat', __name__)

@chat_route.route('/')
def home():
    return render_template('chat.html')