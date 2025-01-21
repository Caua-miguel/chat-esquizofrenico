from database.database import cursor
from database.models.user import usuario

def select_usuario():
    
    lista_usuarios = []
    
    cursor.execute(
        '''
        SELECT * FROM usuarios;
        '''
    )
    dados_usuario = cursor.fetchall()
    
    for dado in dados_usuario:
        lista_usuario = usuario(dado[0], dado[1], dado[2], dado[3])
        lista_usuarios.append(lista_usuario)
    return lista_usuarios

def select_usuario_by_id(id):

    cursor.execute(
       '''
        SELECT * FROM usuarios WHERE serial = %s;
       ''', (id,)
    )
    dados_usuario_id = cursor.fetchone()

    usuario_id = usuario(dados_usuario_id[0], dados_usuario_id[1], dados_usuario_id[2], dados_usuario_id[3])
    
    return usuario_id