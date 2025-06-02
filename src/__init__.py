from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
migrate = Migrate()
def create_app():
    # ... outras configurações ...
    migrate.init_app(app, db)
    # ...
load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "usuarios.login"
login_manager.login_message_category = "info"

def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from src.routes.main import main_bp
    from src.routes.usuarios import usuarios_bp
    from src.routes.tarefas import tarefas_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
    app.register_blueprint(tarefas_bp, url_prefix="/tarefas")

    from src.models.usuario import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    return app