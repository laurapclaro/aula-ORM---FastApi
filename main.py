from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
#import a biblioteca
#pip install jinja2 

#inicializar o app fastapi

app = FastAPI(title="Gestão Escolar")

templates = Jinja2Templates(directory="templates")

#Metodos hhtp: GET, POST, PUT, DELETE

#Rota Inicial

#Para exibir um html na rota - Exibe o formulario
@app.get("/cursos/cadastro", response_class=HTMLResponse)
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(request, "cadastro_curso.html", {"request": request})
