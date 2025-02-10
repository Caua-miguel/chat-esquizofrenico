from database.database import db, cursor

def insert_user(titulo, autor, isbn, categoria):
    cursor.execute(
        '''
        INSERT INTO lib (titulo, autor, isbn, categoria) VALUES (%s, %s, %s, %s)
        ''', (titulo, autor, isbn, categoria)
    )
    db.commit()

def insert_colecao(id):
    cursor.execute(
        '''
        SELECT titulo, autor, isbn, categoria FROM lib WHERE id = %s
        ''', (id,)
    )
    result = cursor.fetchone()

    if result:
        titulo, autor, isbn, categoria = result
        cursor.execute(
            '''
            INSERT INTO colecao (titulo, autor, isbn, categoria) 
            VALUES (%s, %s, %s, %s)
            ''', (titulo, autor, isbn, categoria)
        )
        db.commit()
    else:
        print("Erro: Nenhum dado encontrado para o ID especificado.")
