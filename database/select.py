from database.database import cursor

def select_usuario():
    
    lista_usuarios = []
    
    cursor.execute(
        '''
        SELECT * FROM usuarios;
        '''
    )
    dados_usuario = cursor.fetchall()

    for usuario in dados_usuario:
        lista_usuario = {
            'id': usuario[0],
            'nome': usuario[1],
            'email': usuario[2],
            'status': usuario[3],
        }
        lista_usuarios.append(lista_usuario)
    
    return lista_usuarios

def select_usuario_by_id(id):

    cursor.execute(
       '''
        SELECT * FROM usuarios WHERE serial = %s;
       ''', (id,)
    )
    dados_usuario_id = cursor.fetchone()

    usuario_id = {
            'id': dados_usuario_id[0],
            'nome': dados_usuario_id[1],
            'email': dados_usuario_id[2],
            'status': dados_usuario_id[3],
        }
    
    return usuario_id