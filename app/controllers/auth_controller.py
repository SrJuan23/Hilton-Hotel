from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, UserMixin
from app.models.usuario_model import buscar_usuario_por_correo, insertar_usuario, buscar_usuario_por_id
from app import bcrypt, login_manager

auth_bp = Blueprint('auth', __name__)

# Clase de usuario para Flask-Login
class Usuario(UserMixin):
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo

# Carga del usuario por ID (obligatorio para Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    user = buscar_usuario_por_id(user_id)
    if user:
        return Usuario(id=user[0], nombre=user[1], correo=user[2])
    return None

@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        clave = request.form['clave']
        user = buscar_usuario_por_correo(correo)

        if user and bcrypt.check_password_hash(user[3], clave):
            user_obj = Usuario(id=user[0], nombre=user[1], correo=user[2])
            login_user(user_obj)
            flash('Sesión iniciada correctamente.', 'success')
            return redirect(url_for('auth.dashboard'))
        flash('Credenciales inválidas.', 'danger')
    return render_template('usuario/login.html')

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        pais_codigo = request.form['pais_codigo']

        clave_hash = bcrypt.generate_password_hash(clave).decode('utf-8')
        insertar_usuario(nombre, correo, clave_hash, pais_codigo)

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('usuario/registro.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('usuario/dashboard.html')
