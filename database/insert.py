from database.database import db, cursor

def insert_user(nome, email):
    cursor.execute(
        '''
        INSERT INTO usuarios (nome, email, status) VALUES (%s, %s, %s)
        ''', (nome, email, True)
    )
    db.commit()