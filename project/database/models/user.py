# from flask_login import UserMixin

class usuario:
    def __init__(self, id, nome, email, status, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.status = status
        self.senha = senha