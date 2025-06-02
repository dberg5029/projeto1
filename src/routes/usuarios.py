from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from src import db, bcrypt
from src.models.usuario import Usuario
from src.forms import RegisterForm, LoginForm, ResetPasswordForm

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        usuario = Usuario(
            nome=form.nome.data,
            email=form.email.data,
            senha=hashed_password,
            tipo_usuario=form.tipo_usuario.data
        )
        db.session.add(usuario)
        db.session.commit()
        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect(url_for('usuarios.login'))
    return render_template('register.html', title='Registrar', form=form)

@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario:
            try:
                if bcrypt.check_password_hash(usuario.senha, form.senha.data):
                    login_user(usuario, remember=form.lembrar.data)
                    next_page = request.args.get('next')
                    flash('Login bem-sucedido!', 'success')
                    return redirect(next_page) if next_page else redirect(url_for('main.index'))
                else:
                    flash('Senha incorreta.', 'danger')
            except ValueError as e:
                flash(f'Erro ao verificar senha: {str(e)}. Por favor, redefina sua senha.', 'danger')
        else:
            flash('Email não encontrado.', 'danger')
    return render_template('login.html', title='Login', form=form)

@usuarios_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('main.index'))

@usuarios_bp.route('/reset_password/<int:user_id>', methods=['GET', 'POST'])
@login_required
def reset_password(user_id):
    if current_user.tipo_usuario not in ['admin', 'gestor']:
        flash('Acesso não autorizado.', 'danger')
        return redirect(url_for('main.index'))
    usuario = Usuario.query.get_or_404(user_id)
    form = ResetPasswordForm()
    if form.validate_on_submit():
        usuario.senha = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        db.session.commit()
        flash('Senha redefinida com sucesso.', 'success')
        return redirect(url_for('main.index'))
    return render_template('reset_password.html', title='Redefinir Senha', form=form, usuario=usuario)