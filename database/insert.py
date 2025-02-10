from database.database import db, cursor

def insert_user(titulo, autor, isbn, categoria):
    cursor.execute(
        '''
        INSERT INTO lib (titulo, autor, isbn, categoria) VALUES (%s, %s, %s, %s)
        ''', (titulo, autor, isbn, categoria)
    )
    db.commit()