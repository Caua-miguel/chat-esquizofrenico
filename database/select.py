from database.database import cursor

def select_usuario():
    cursor.execute(
        '''
        SELECT * FROM usuarios;
        '''
    )