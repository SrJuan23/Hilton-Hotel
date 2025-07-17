from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, UserMixin
from app.models.usuario_model import buscar_usuario_por_correo, insertar_usuario, buscar_usuario_por_id
from app import bcrypt, login_manager
from app.models.pais_model import obtener_paises

auth_bp = Blueprint('auth', __name__)


class Usuario(UserMixin):
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo


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
    paises = obtener_paises()

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()   
        clave = request.form['clave']
        pais_codigo = request.form['pais_codigo']

        errores = []
        if not nombre:
            errores.append("El nombre es obligatorio.")
        if not correo or "@" not in correo:
            errores.append("Correo inválido.")
        if len(clave) < 6:
            errores.append("La clave debe tener al menos 6 caracteres.")
        if not pais_codigo:
            errores.append("Seleccione un país.")

        if errores:
            for error in errores:
                flash(error, 'danger')
            return render_template('usuario/registro.html', paises=paises, datos=request.form)
        
        clave_hash = bcrypt.generate_password_hash(clave).decode('utf-8')
        insertar_usuario(nombre, correo, clave_hash, pais_codigo)

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('usuario/registro.html', paises=paises)

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
