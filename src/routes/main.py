from flask import Blueprint, render_template
from flask_login import login_required, current_user
from src.models.usuario import Tarefa

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', title='Página Inicial')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    tarefas = []
    if current_user.tipo_usuario in ['admin', 'gestor']:
        tarefas = Tarefa.query.order_by(Tarefa.prazo.asc()).all()
    else:
        tarefas = Tarefa.query.filter_by(designado_para_id=current_user.id).order_by(Tarefa.prazo.asc()).all()
    
    stats = {
        'total': len(tarefas),
        'concluidas': sum(1 for t in tarefas if t.status.name == 'concluida'),
        'pendentes': sum(1 for t in tarefas if t.status.name == 'pendente'),
        'em_andamento': sum(1 for t in tarefas if t.status.name == 'em_andamento'),
        'atrasadas': sum(1 for t in tarefas if t.status.name == 'atrasada')
    }
    
    return render_template('dashboard.html', title='Painel de Tarefas', tarefas=tarefas, stats=stats)