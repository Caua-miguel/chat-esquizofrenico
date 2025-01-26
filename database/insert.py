from database.database import db, cursor

def insert_user(nome, email, status):
    cursor.execute(
        '''
        INSERT INTO usuarios (nome, email, status) VALUES (%s, %s, %s)
        ''', (nome, email, status)
    )
    db.commit()