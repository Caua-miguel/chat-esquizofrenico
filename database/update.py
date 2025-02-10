from database.database import db, cursor

def update_user_by_id(id, titulo, autor, isbn, categoria):
    cursor.execute(
        '''
        UPDATE lib SET titulo = %s, autor, isbn = %s, categoria = %s = %s WHERE id = %s
        ''', (titulo, autor, isbn, categoria, id)
    )
    db.commit()