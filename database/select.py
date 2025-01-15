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