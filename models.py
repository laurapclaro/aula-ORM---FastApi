# models é o arquivo onde fica as classes (tabelas)
# instalar = pip install sqlalchemy
# instalar = pip install alembic
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#Tabelas Curso e aluno (1:N)
class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    descricao = Column(String(150))

    alunos = relationship("Aluno", back_populates="cursos")

    def __repr__(self):
        return f"Curso = id: {self.id} - nome: {self.nome} - Carga Hóraria: {self.carga_horaria}"

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    curso_id = Column(Integer, ForeignKey("cursos.id"))

    cursos = relationship("Curso", back_populates="alunos")

    def __repr__(self):
        return f"Aluno = id: {self.id} - nome: {self.nome} - Email: {self.email}"
