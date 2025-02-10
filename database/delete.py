from database.database import db, cursor

def delete_usuario(id):
    cursor.execute(
        '''
        DELETE FROM lib WHERE id = %s
        ''', (id,)
    )
    db.commit()

def delete_colecao(id):
    cursor.execute(
        '''
        DELETE FROM colecao WHERE id = %s
        ''', (id,)
    )
    db.commit()