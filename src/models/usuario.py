from flask_login import UserMixin
from src import db
from sqlalchemy import Enum
import enum

class TipoUsuario(enum.Enum):
    comum = "Comum"
    admin = "Administrador"
    gestor = "Gestor"

class StatusTarefa(enum.Enum):
    pendente = "Pendente"
    em_andamento = "Em Andamento"
    concluida = "Concluída"
    atrasada = "Atrasada"

class PrioridadeTarefa(enum.Enum):
    baixa = "Baixa"
    media = "Média"
    alta = "Alta"

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    tipo_usuario = db.Column(db.Enum(TipoUsuario), nullable=False, default=TipoUsuario.comum)

    tarefas_criadas = db.relationship('Tarefa', backref='criador', foreign_keys='Tarefa.criador_id')
    tarefas_designadas = db.relationship('Tarefa', backref='designado', foreign_keys='Tarefa.designado_para_id')

    @property
    def tipo_usuario_display(self):
        return self.tipo_usuario.value

class Tarefa(db.Model):
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    setor = db.Column(db.String(50), nullable=True)
    cliente = db.Column(db.String(100), nullable=True)
    tipo_tarefa = db.Column(db.String(50), nullable=True)
    status = db.Column(db.Enum(StatusTarefa), nullable=False, default=StatusTarefa.pendente)
    prioridade = db.Column(db.Enum(PrioridadeTarefa), nullable=False, default=PrioridadeTarefa.baixa)
    prazo = db.Column(db.DateTime, nullable=True)
    criador_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    designado_para_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)