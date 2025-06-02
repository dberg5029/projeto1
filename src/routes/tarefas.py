from flask import Blueprint, render_template, redirect, url_for, flash, request, Response
from flask_login import login_required, current_user
from src import db
from src.models.usuario import Tarefa, Usuario, StatusTarefa
from src.forms import TarefaForm
from io import StringIO
import csv

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/listar')
@login_required
def listar():
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status')
    prioridade = request.args.get('prioridade')
    cliente = request.args.get('cliente')
    per_page = 10

    query = Tarefa.query
    if current_user.tipo_usuario not in ['admin', 'gestor']:
        query = query.filter_by(designado_para_id=current_user.id)
    
    if status:
        query = query.filter(Tarefa.status == status)
    if prioridade:
        query = query.filter(Tarefa.prioridade == prioridade)
    if cliente:
        query = query.filter(Tarefa.cliente.ilike(f'%{cliente}%'))

    tarefas = query.order_by(Tarefa.prazo.asc()).paginate(page=page, per_page=per_page)
    return render_template('listar_tarefas.html', title='Lista de Tarefas', tarefas=tarefas)

@tarefas_bp.route('/criar', methods=['GET', 'POST'])
@login_required
def criar():
    if current_user.tipo_usuario not in ['admin', 'gestor']:
        flash('Acesso não autorizado.', 'danger')
        return redirect(url_for('tarefas.listar'))
    
    form = TarefaForm()
    if form.validate_on_submit():
        tarefa = Tarefa(
            titulo=form.titulo.data,
            descricao=form.descricao.data,
            setor=form.setor.data,
            status=StatusTarefa.pendente,
            prioridade=form.prioridade.data,
            prazo=form.prazo.data,
            criador_id=current_user.id,
            designado_para_id=form.designado_para.data,
            cliente=form.cliente.data,
            tipo_tarefa=form.tipo_tarefa.data
        )
        db.session.add(tarefa)
        db.session.commit()
        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('tarefas.listar'))
    return render_template('criar_tarefa.html', title='Criar Tarefa', form=form)

@tarefas_bp.route('/visualizar/<int:id>')
@login_required
def visualizar(id):
    tarefa = Tarefa.query.get_or_404(id)
    
    if current_user.tipo_usuario not in ['admin', 'gestor'] and tarefa.designado_para_id != current_user.id:
        flash('Acesso não autorizado.', 'danger')
        return redirect(url_for('tarefas.listar'))
    
    return render_template('visualizar_tarefa.html', tarefa=tarefa)

@tarefas_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    tarefa = Tarefa.query.get_or_404(id)
    
    if current_user.tipo_usuario not in ['admin', 'gestor'] and tarefa.designado_para_id != current_user.id:
        flash('Acesso não autorizado.', 'danger')
        return redirect(url_for('tarefas.listar'))
    
    form = TarefaForm(obj=tarefa)
    if form.validate_on_submit():
        form.populate_obj(tarefa)
        db.session.commit()
        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('tarefas.listar'))
    
    return render_template('editar_tarefa.html', form=form, tarefa=tarefa)

@tarefas_bp.route('/excluir/<int:id>', methods=['POST'])
@login_required
def excluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    
    if current_user.tipo_usuario not in ['admin', 'gestor']:
        flash('Acesso não autorizado.', 'danger')
        return redirect(url_for('tarefas.listar'))
    
    db.session.delete(tarefa)
    db.session.commit()
    flash('Tarefa excluída com sucesso!', 'success')
    return redirect(url_for('tarefas.listar'))

@tarefas_bp.route('/exportar_csv')
@login_required
def exportar_csv():
    query = Tarefa.query
    if current_user.tipo_usuario not in ['admin', 'gestor']:
        query = query.filter_by(designado_para_id=current_user.id)

    status = request.args.get('status')
    prioridade = request.args.get('prioridade')
    cliente = request.args.get('cliente')

    if status:
        query = query.filter(Tarefa.status == status)
    if prioridade:
        query = query.filter(Tarefa.prioridade == prioridade)
    if cliente:
        query = query.filter(Tarefa.cliente.ilike(f'%{cliente}%'))

    tarefas = query.order_by(Tarefa.prazo.asc()).all()

    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['ID', 'Título', 'Descrição', 'Setor', 'Prioridade', 'Prazo', 'Cliente', 'Status'])

    for tarefa in tarefas:
        writer.writerow([
            tarefa.id,
            tarefa.titulo,
            tarefa.descricao,
            tarefa.setor,
            tarefa.prioridade,
            tarefa.prazo.strftime('%Y-%m-%d') if tarefa.prazo else '',
            tarefa.cliente,
            tarefa.status
        ])

    output = si.getvalue()
    si.close()

    return Response(output, mimetype='text/csv', headers={
        'Content-Disposition': 'attachment; filename=tarefas.csv'
    })