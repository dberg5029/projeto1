from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email, Length
from src.models.usuario import Usuario

class RegisterForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    tipo_usuario = SelectField('Tipo de Usuário', choices=[('comum', 'Comum'), ('admin', 'Administrador'), ('gestor', 'Gestor')], validators=[DataRequired()])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    lembrar = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class ResetPasswordForm(FlaskForm):
    senha = PasswordField('Nova Senha', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Redefinir Senha')

class TarefaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(min=2, max=100)])
    descricao = TextAreaField('Descrição', validators=[Length(max=500)])
    setor = StringField('Setor', validators=[Length(max=50)])
    cliente = StringField('Cliente', validators=[Length(max=100)])
    tipo_tarefa = StringField('Tipo de Tarefa', validators=[Length(max=50)])
    prioridade = SelectField('Prioridade', choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')],validators=[DataRequired()])
    prazo = DateTimeField('Prazo', format='%Y-%m-%d', validators=[DataRequired()])
    designado_para = SelectField('Designado Para', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Criar Tarefa')

    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        self.designado_para.choices = [(u.id, u.nome) for u in Usuario.query.order_by(Usuario.nome).all()]