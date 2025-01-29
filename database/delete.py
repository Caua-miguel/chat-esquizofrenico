from database.database import db, cursor

def delete_usuario(id):
    cursor.execute(
        '''
        DELETE FROM usuarios WHERE id = %s
        ''', (id,)
    )
    db.commit()