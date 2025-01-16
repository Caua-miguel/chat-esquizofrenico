from database.database import cursor

def delete_usuario(id):
    cursor.execute(
        '''
        DELETE FROM usuarios WHERE serial = %s
        ''', (id)
    )