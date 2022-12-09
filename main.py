from fastapi import FastAPI
from secrets import token_hex
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import CONN, Pessoa, Tokens

app = FastAPI()

def conectaBD(): # FUNÇÃO PARA CONECTAR AO BD
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post("/cadastro")
def cadastro(nome: str, user: str, senha: str):
    session = conectaBD() # FUNÇÃO PARA CONECTAR AO BD
    filtra_usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all() # USUARIO = BD/ USER = API
    if len(filtra_usuario) == 0: # SE NÃO HOUVER USUÁRIO IGUAL CADASTRADO
        cadastra_novo_usuario = Pessoa(nome=nome, usuario=user, senha=senha) # CADASTRA NOVO USUÁRIO
        session.add(cadastra_novo_usuario)
        session.commit()
        return {'status': 'Usuário cadastrado com sucesso!'}
    elif len(filtra_usuario) > 0:
        return {'status': 'Usuário já cadastrado!'}

@app.post('/login')
def login(usuario: str, senha: str):
    session = conectaBD()
    filtra_usuario = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all() # SE USUARIO API == USUARIO BD / SENHA API == SENHA BD
    if len(filtra_usuario) == 0:
        return {'status': 'O usuário não existe!'}

    while True:
        token = token_hex(50) # CRIA TOKEN COM 100 CARACTERES
        filtra_token = session.query(Tokens).filter_by(token=token).all() # PROCURA SE EXISTE ALGUM TOKEN IGUAL AO GERADO ACIMA
        if len(filtra_token) == 0: # SE NÃO EXISTIR NENHUM TOKEN
            filtra_usuario_token = session.query(Tokens).filter_by(id_pessoa=filtra_usuario[0].id).all() # PROCURA SE O USUARIO TEM UM TOKEN
            if len(filtra_usuario_token) == 0: # SE O USUARIO NÃO TIVER TOKEN
                novo_token = Tokens(id_pessoa=filtra_usuario[0].id, token=token) # ADICIONA O TOKEN GERADO NO INICIO AO USUARIO
                session.add(novo_token)
            elif len(filtra_usuario_token) == 1: # SE O USUÁRIO TIVER UM TOKEN, ATUALIZA O TOKEN
                filtra_usuario_token[0].token = token
            session.commit()
            break
    return token
