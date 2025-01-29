from database.database import db, cursor

def update_user_by_id(id, nome, email):
    cursor.execute(
        '''
        UPDATE usuarios SET nome = %s, email = %s WHERE id = %s
        ''', (nome, email, id)
    )
    db.commit()