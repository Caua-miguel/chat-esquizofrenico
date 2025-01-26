from database.database import db, cursor

def update_user_by_id(id, nome, email, status):
    cursor.execute(
        '''
        UPDATE usuarios SET nome = %s, email = %s, status = %s WHERE serial = %s
        ''', (nome, email, status, id)
    )
    db.commit()