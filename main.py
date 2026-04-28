from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Aluno, Curso

#import a bibloteca: 
#pip install jinja2 python-multipart 

#python -m uvicorn main:app --reload

# inicializar o app fastapi
app = FastAPI(title="Gestão Escolar")

#Aponta para pasta onde ficam os html
templates = Jinja2Templates(directory="templates")

# Metodos http: GET - POST - PUT - DELETE

#Rota inicial

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
     request,
     "index.html",
     {"request": request}
)

#Para exibir um html na rota - Exibe o formulário
@app.get("/cursos/cadastro", response_class=HTMLResponse)
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(request, "cadastro_curso.html", {"request": request})


#Cadastrar curso
@app.post("/cursos")
def criar_curso(
    nome: str = Form(...),
    carga_horaria: int =Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    #Criar um objeto
    novo_curso = Curso(nome=nome, carga_horaria=carga_horaria, descricao=descricao)
    db.add(novo_curso)
    db.commit()

    return RedirectResponse(url="/listar_cursos", status_code=303)


#Listar cursos
@app.get("/listar_cursos")
def exibir_cursos(
    request: Request,
    db: Session = Depends(get_db)
    ):
    cursos = db.query(Curso).all()
    return templates.TemplateResponse(
        request,
        "cursos.html",
        {"request": request, "cursos": cursos}
    )

#Deletar um curso
@app.post("/cursos/{id}/deletar")
def deletar_cursos(
    id: int, 
    db: Session = Depends(get_db)
):
    curso = db.query(Curso).get(id)
    if curso: 
        db.delete(curso)
        db.commit()

    return RedirectResponse(url="/listar_cursos", status_code=303)
