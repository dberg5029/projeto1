import os
import sys
# Adiciona o diretório raiz do projeto (C:\projeto1) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import create_app, db
from src.models.usuario import Usuario, Tarefa

def init_db():
    app = create_app()
    with app.app_context():
        db.drop_all()  # Apaga todas as tabelas existentes
        db.create_all()  # Cria as tabelas com o esquema atual
        print("✅ Banco de dados criado com sucesso!")
        print(f"📁 Local do banco: {app.config['SQLALCHEMY_DATABASE_URI']}")

if __name__ == '__main__':
    init_db()