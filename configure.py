from routes.home import home_route
from routes.user import user_route
from routes.chat import chat_route
from database.database import db, cursor
from database.select import select_usuario

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    
    app.register_blueprint(home_route)
    app.register_blueprint(user_route, url_prefix='/user')
    app.register_blueprint(chat_route, url_prefix='/chat')

def configure_db():
    db
    select_usuario()
    # db.commit()
    # cursor.close()
    # db.close()