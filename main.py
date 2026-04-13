from fastapi import FastAPI

#inicializar o app fastapi

app = FastAPI(title="Gestão Escolar")

#Metodos hhtp: GET, POST, PUT, DELETE
@app.get("/")
def tela_inicial():
    return {"Mensagem": "Sistema Gestão Escolar"}

#Banco de dados
usuarios = {
    1: {"nome": "Laura", "idade": 17},
    2: {"nome": "Kaua", "idade": 17},
    3: {"nome": "Kazuki", "idade": 17}
    
}

@app.get("/listar_alunos")
def  listar_alunos():
    return{"usuarios": usuarios}