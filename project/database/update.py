from project.database.database import db, cursor

def update_user_by_id(id, titulo, autor, isbn, categoria):
    cursor.execute(
        '''
        UPDATE lib SET titulo = %s, autor = %s, isbn = %s, categoria = %s WHERE id = %s
        ''', (titulo, autor, isbn, categoria, id)
    )
    db.commit()