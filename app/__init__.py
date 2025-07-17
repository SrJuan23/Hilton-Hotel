from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
from .extensions import mysql

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    mysql.init_app(app)

    
    from app.controllers.auth_controller import auth_bp
    from app.controllers.hotel_controller import hotel_bp
    from app.controllers.categoria_controller import categoria_bp
    from app.controllers.habitacion_controller import habitacion_bp
    from app.controllers.tipo_habitacion_controller import tipo_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(habitacion_bp)
    app.register_blueprint(tipo_bp)

    return app
