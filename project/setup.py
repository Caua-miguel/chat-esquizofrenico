# from routes.home import home_route
# from routes.lib import lib_route
# from routes.chat import chat_route
# # from routes.login import login_usuario
# from database.database import db
# from database.select import select_usuario

# def setup_app(app):
#     configure_routes(app)
#     configure_db()

# def configure_routes(app):
    
#     app.register_blueprint(home_route)
#     app.register_blueprint(lib_route, url_prefix='/user')
#     # app.register_blueprint(login_usuario, url_prefix='/login')
#     app.register_blueprint(chat_route, url_prefix='/chat')

# def configure_db():
#     db
#     select_usuario()
#     # db.commit()
#     # cursor.close()
#     # db.close()