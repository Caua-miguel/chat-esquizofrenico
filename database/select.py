from database.database import cursor
from database.models.user import usuario
from database.models.lib import lib

# Tabela usuário
def select_usuario():
    
    lista_usuarios = []
    
    cursor.execute(
        '''
        SELECT * FROM usuarios_novos;
        '''
    )
    dados_usuario = cursor.fetchall()
    
    for dado in dados_usuario:
        lista_usuario = usuario(dado[0], dado[1], dado[2], dado[3], dado[4])
        lista_usuarios.append(lista_usuario)
    return lista_usuarios

def select_usuario_by_id(id):

    cursor.execute(
       '''
        SELECT * FROM usuarios_novos WHERE id = %s;
       ''', (id,)
    )
    dados_usuario_id = cursor.fetchone()

    usuario_id = usuario(dados_usuario_id[0], dados_usuario_id[1], dados_usuario_id[2], dados_usuario_id[3], dados_usuario_id[4])
    
    return usuario_id

# Tabela lib
def select_lib():
    
    lista_usuarios = []
    
    cursor.execute(
        '''
        SELECT * FROM lib;
        '''
    )
    dados_usuario = cursor.fetchall()
    
    for dado in dados_usuario:
        lista_usuario = lib(dado[0], dado[1], dado[2], dado[3], dado[4])
        lista_usuarios.append(lista_usuario)
    return lista_usuarios

def select_lib_by_id(id):

    cursor.execute(
       '''
        SELECT * FROM lib WHERE id = %s;
       ''', (id,)
    )
    dados_usuario_id = cursor.fetchone()

    usuario_id = lib(dados_usuario_id[0], dados_usuario_id[1], dados_usuario_id[2], dados_usuario_id[3], dados_usuario_id[4])
    
    return usuario_id

# Tabela colecao
def select_colecao():
    
    lista_colecao = []
    
    cursor.execute(
        '''
        SELECT * FROM colecao;
        '''
    )
    dados_colecao = cursor.fetchall()
    
    for dado in dados_colecao:
        lista = lib(dado[0], dado[1], dado[2], dado[3], dado[4])
        lista_colecao.append(lista)
    return lista_colecao